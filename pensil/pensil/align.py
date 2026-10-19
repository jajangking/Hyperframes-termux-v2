"""Selaraskan waktu kata ke suara asli + sisipkan jeda antar-slide.

`pensil align scenes/x.py`:
  words-<id>.json + vo mentah
    → vo (stem)-r.mp3   (LEAD senyap di depan + jeda 1,8s di tiap batas slide)
    → words-<id>-r.json (waktu kata versi reels)

Jeda disisipkan tepat di senyap alami (deteksi silencedetect), sehingga
tidak memotong kata. Semua kata sisip wajib menjadi kata PERTAMA sebuah
potongan ucapan — script meng-assert.
"""

import json
import os
import subprocess

from pensil import timing as T
from pensil.config import jeda_map


def align(project, scene):
    sc = scene.SCENE
    sid = sc["id"]
    vo_raw = sc.get("vo_raw")
    if not vo_raw:
        raise SystemExit(f"scene {sid}: SCENE['vo_raw'] wajib (VO mentah) untuk align")
    words_path = project.path("work", f"words-{sid}.json")
    src = project.path("vo", vo_raw)
    out_a = project.path("work", os.path.splitext(vo_raw)[0] + "-r.mp3")
    out_j = project.path("work", f"words-{sid}-r.json")

    spec = json.load(open(words_path, encoding="utf-8"))
    words = spec["words"]
    wlist = [w["w"] for w in words]
    sy = [T.bobot(w) for w in wlist]

    d = T.dur_of(src)
    sr = T.sr_of(src)
    sil = T.silences(src)
    ch = T.chunks_of(sil, d)

    # pemetaan kata -> potongan ucapan. Prioritas:
    #   1. GROUPS buatan tangan di scene (untuk words file pipeline lama)
    #   2. counts tersimpan di words json (hasil `pensil timing`)
    #   3. alokasi ulang otomatis
    groups = getattr(scene, "GROUPS", None)
    syl_tab = getattr(scene, "SYL", None)
    if groups:
        assert len(groups) == len(ch), \
            f"{len(groups)} grup != {len(ch)} potongan ucapan — deteksi senyap berubah?"
        counts = [j - i + 1 for i, j in groups]
        assert sum(counts) == len(words), "jumlah kata di GROUPS != daftar kata"
        chunk_of = [0] * len(words)
        for c, (i, j) in enumerate(groups):
            for k in range(i, j + 1):
                chunk_of[k] = c
    else:
        counts = spec.get("counts") or T.allocate(wlist, sy, ch)
        assert sum(counts) == len(words), "jumlah kata alokasi != daftar kata"
        chunk_of = None
    if syl_tab:
        assert len(syl_tab) == len(words), "SYL tidak sepanjang daftar kata"
        sy = list(syl_tab)

    # onset tiap kata di potongan ucapan asli
    onset = T.onsets_from_chunks(wlist, ch, counts, sy)
    if chunk_of is None:
        chunk_of = T.chunk_of_onsets(onset, ch)

    # jeda per batas slide — semua harus jatuh di senyap alami
    titik = []
    for w, J in sorted(jeda_map(scene).items()):
        c = chunk_of[w]
        assert c > 0, f"kata {w} ('{words[w]['w']}') tidak punya senyap sebelumnya"
        s, e = sil[c]
        assert s <= onset[w] <= e + 1e-6, \
            (f"kata {w} ('{words[w]['w']}') tidak di dalam senyap {s:.2f}-{e:.2f} — "
             f"geser batas slide ke awal potongan ucapan")
        titik.append((s, J))

    lead = float(sc.get("lead", 0.0))
    tail = float(sc.get("tail", 0.0))    # senyap ekor: animasi akhir muat semua
    geser = [lead + sum(J for p, J in titik if p <= t + 1e-9) for t in onset]
    baru = [round(onset[k] + geser[k], 3) for k in range(len(words))]
    dur_baru = round(lead + d + sum(J for _, J in titik) + tail, 3)

    _render(src, out_a, sr, titik, lead, tail)

    for k, W in enumerate(words):
        W["t"] = baru[k]
    json.dump({"words": words, "dur": dur_baru,
               "jeda": {str(k): v for k, v in sorted(
                   jeda_map(scene).items())},
               "lead": lead, "tail": tail},
              open(out_j, "w", encoding="utf-8"), ensure_ascii=False)

    return {"src": src, "out": out_a, "dur": dur_baru, "jeda": titik, "lead": lead}


def _render(src, out_a, sr, titik, lead, tail):
    """Potong VO di senyap tiap titik sisip, sisipkan silence, rakit ulang."""
    d = T.dur_of(src)
    n = len(titik)
    batas = [p for p, _ in titik]
    seg = ([(0.0, batas[0])] if n else []) + \
          [(batas[i], batas[i + 1]) for i in range(n - 1)] + [(batas[-1], d)]
    f = [f"[0:a]aformat=sample_fmts=fltp:channel_layouts=mono:sample_rates={sr},"
         f"asplit={n + 1}" + "".join(f"[s{i}]" for i in range(n + 1))]
    for i, (a, b) in enumerate(seg):
        f.append(f"[s{i}]atrim=start={a}:end={b},asetpts=N/SR/TB[p{i}]")
    f.append(f"[1:a]aformat=sample_fmts=fltp:channel_layouts=mono:sample_rates={sr},"
             f"asplit={n + 1}" + "".join(f"[q{i}]" for i in range(n + 1)))
    if lead > 0:
        f.append(f"[q{n}]atrim=0:{lead},asetpts=N/SR/TB[gL]")
    for i, (_, J) in enumerate(titik):
        f.append(f"[q{i}]atrim=0:{J},asetpts=N/SR/TB[g{i}]")
    urut = ("[gL]" if lead > 0 else "") + \
        "".join(f"[p{i}]" + (f"[g{i}]" if i < n else "") for i in range(n + 1))
    nseg = 2 * n + (1 if lead > 0 else 0) + 1
    if tail > 0:
        f.append(f"{urut}concat=n={nseg}:v=0:a=1[cat]")
        f.append(f"[cat]apad=pad_dur={tail}[out]")
    else:
        f.append(f"{urut}concat=n={nseg}:v=0:a=1[out]")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", src,
                    "-f", "lavfi", "-i", f"anullsrc=r={sr}:cl=mono",
                    "-filter_complex", ";".join(f), "-map", "[out]",
                    "-c:a", "libmp3lame", "-q:a", "4", out_a], check=True)
