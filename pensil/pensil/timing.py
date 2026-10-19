"""Deteksi senyap + alokasi kata per potongan ucapan + penyelarasan waktu.

Dipakai `pensil timing` (kata mentah → words-<id>.json) dan
`pensil align` (words → words-<id>-r.json + VO berjeda).
"""

import itertools
import json
import os
import re
import subprocess

VOKAL = "aiueoAIUEO"
NOISE = "-38dB"
MINDUR = 0.12


def bobot(w):
    """perkiraan jumlah suku kata (heuristik kelompok vokal)"""
    clean = re.sub(r"[^A-Za-z]", "", w)
    if not clean:
        return 1
    g, prev = 0, False
    for ch in clean:
        v = ch in VOKAL
        if v and not prev:
            g += 1
        prev = v
    return max(1, g)


def dur_of(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", p], capture_output=True, text=True)
    return float(r.stdout.strip())


def sr_of(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "a:0",
                        "-show_entries", "stream=sample_rate", "-of", "csv=p=0", p],
                       capture_output=True, text=True)
    return int(r.stdout.strip() or 24000)


def silences(p, noise=NOISE, mindur=MINDUR):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", p, "-af",
                        f"silencedetect=noise={noise}:d={mindur}", "-f", "null", "-"],
                       capture_output=True, text=True)
    out, st = [], None
    for ln in r.stderr.splitlines():
        m = re.search(r"silence_start:\s*([0-9.]+)", ln)
        if m:
            st = float(m.group(1))
        m = re.search(r"silence_end:\s*([0-9.]+)", ln)
        if m and st is not None:
            out.append((st, float(m.group(1))))
            st = None
    return out


def chunks_of(sil, d, gap=0.05):
    """potongan ucapan = rentang antar-senyap; sisip senyap < gap diabaikan"""
    out, cur = [], 0.0
    for s, e in sil:
        if s - cur > gap:
            out.append((cur, s))
        cur = max(cur, e)
    if d - cur > gap:
        out.append((cur, d))
    return out


def allocate(words, sy, chunks):
    """Alokasi jumlah kata tiap potongan: isi tiap potongan sampai target
    laju suku kata kumulatif (pemetaan frasa jatuh di senyap alami)."""
    speech = [b - a for a, b in chunks]
    cum = list(itertools.accumulate(speech))
    rate = sum(sy) / max(sum(speech), 1e-9)
    counts, wi, placed = [0] * len(chunks), 0, 0.0
    for i, target in enumerate(rate * c for c in cum):
        while wi < len(words):
            if placed + sy[wi] - target > target - placed:
                break
            placed += sy[wi]
            counts[i] += 1
            wi += 1
    if wi < len(words):
        counts[-1] += len(words) - wi
    assert sum(counts) == len(words)
    return counts


def distribute(words, sy, chunks, counts):
    """Sebar waktu kata dalam tiap potongan proporsional bobot suku kata."""
    out, i = [], 0
    for (a, b), cnt in zip(chunks, counts):
        grp = words[i:i + cnt]
        i += cnt
        ws = sy[i - cnt:i]
        tot = sum(ws) or 1
        cur = a
        for w, wt in zip(grp, ws):
            d = (b - a) * wt / tot
            out.append({"w": w, "t": round(cur, 3), "e": round(cur + d, 3)})
            cur += d
    return out


def onsets_from_chunks(words, chunks, counts, sy):
    """Onset tiap kata rata-rata ke potongan ucapan asli (dipakai align)."""
    onset = [0.0] * len(words)
    i = 0
    for (a, b), cnt in zip(chunks, counts):
        idx = range(i, i + cnt)
        tot = sum(sy[k] for k in idx) or 1
        acc = 0
        for k in idx:
            onset[k] = a + acc / tot * (b - a)
            acc += sy[k]
        i += cnt
    return onset


def chunk_of_onsets(onset, chunks):
    """Nomor potongan ucapan tiap kata (kata ke-i bicara di potongan ke-?)."""
    out = []
    for t in onset:
        ci = 0
        for i, (a, _b) in enumerate(chunks):
            if t >= a - 1e-6:
                ci = i
        out.append(ci)
    return out


def timing(naskah_path, vo_path, out_path, counts_override=None):
    """naskah + VO mentah → words-<id>.json (waktu kasar per kata)."""
    teks = open(naskah_path, encoding="utf-8").read().strip()
    words = teks.split()
    sy = [bobot(w) for w in words]
    d = dur_of(vo_path)
    sil = silences(vo_path)
    ch = chunks_of(sil, d)
    counts = counts_override or allocate(words, sy, ch)
    if sum(counts) != len(words):
        raise SystemExit(f"alokasi kata gagal: {sum(counts)} != {len(words)}")
    out = distribute(words, sy, ch, counts)
    json.dump({"total": round(d, 3), "words": out,
               "counts": counts, "chunks": [list(c) for c in ch]},
              open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return {"n_words": len(words), "n_chunks": len(ch), "chunks": ch,
            "counts": counts, "dur": d}
