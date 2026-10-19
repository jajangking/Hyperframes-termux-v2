"""Antarmuka baris perintah pensil.

  python3 -m pensil init <dir> [--name N]       buat proyek baru
  python3 -m pensil new <scene.py> --id X       skrip scene baru (TODO)
  python3 -m pensil timing <scene.py>           naskah + VO → words-<id>.json
  python3 -m pensil align <scene.py>            sisip jeda → words-<id>-r.json + vo -r
  python3 -m pensil gen <scene.py>              → compositions/<id>.html + sfx bed
  python3 -m pensil index                       → index.html root dari project.json
  python3 -m pensil lint                        hyperframes lint
  python3 -m pensil verify <scene.py>           lint + snapshot + analisa tinta/kamera
  python3 -m pensil run <scene.py>              timing+align+gen+index+lint+verify
"""

import argparse
import json
import os
import sys

from pensil import align as A
from pensil import compose as C
from pensil import index as I
from pensil import timing as T
from pensil import verify as V
from pensil.config import load_project, load_scene

PROJECT_JSON = {
    "name": "proyek-baru",
    "canvas": {"w": 1080, "h": 1920},
    "paths": {
        "vo": "assets/vo",
        "audio": "assets/audio",
        "work": "assets/vo",
        "compositions": "compositions",
        "work_prefix": "../assets/vo",
        "audio_prefix": "../assets/audio",
    },
    "scenes": [],
}

SCENE_TEMPLATE = '''"""Scene: {sid} — {judul}.

Isi bagian bertanda TODO. Alur:
  python3 -m pensil timing scenes/{base}.py
  python3 -m pensil align  scenes/{base}.py     (jeda jatuh di senyap alami)
  python3 -m pensil gen    scenes/{base}.py
  python3 -m pensil verify scenes/{base}.py
"""

SCENE = {{
    "id": "{sid}",
    "hud_left": ("{hud1}", "{hud2}"),     # kiri atas; None = tanpa HUD
    "hud_right": "",                      # kanan atas (HTML boleh); "" = kosong
    "naskah": "{base}.txt",               # di path vo
    "vo_raw": "{base}.mp3",               # VO mentah di path vo
    "lead": 1.8,                          # senyap awal (kartu pembuka)
    "jeda": 1.8,                          # jeda per batas slide
    "spacing": 1600,                      # jarak antar gambar (px)
}}

# TODO: rentang kata per slide (indeks kata di words-*.json, inklusif).
# Batas slide otomatis jadi titik jeda + pergeseran kamera.
SLIDES = [
    {{"words": (0, 9)}},
    {{"words": (10, -1), "preshow": "v2"}},   # v2 = pra-gambar frame+no slide 2
]

# TODO: isyarat gambar (kata, selector, durasi, "d"=gores "t"=teks "f"=sekali jadi)
CUES = [
    (0, "#v1Frame", 1.0, "d"),
    (0, "#v1No", 0.6, "t"),
]

# TODO: caption (kata_awal, kata_akhir, teks); kata_akhir -1 = sampai akhir
CAPTIONS = [
    (0, -1, "TEKS CAPTION PERTAMA"),
]

# TODO: peta suara: kata → [(nama_suara, gain_dB, offset_detik)]
# suara tersedia: paper tick whoosh coin pump rev rumble deep zap puff sting chime boom
SFXMAP = {{
    0: [("paper", -8, 0.0)],
}}


def g1(X, A):
    """GAMBAR 1 — TODO ganti dengan gambar slide 1 (koordinat relatif X)."""
    return f\'\'\'        {{A.frame("v1Frame", X)}}
        {{A.txt("v1No", X - A.FW // 2 + 22, A.FY + 52, "01", 30, A.accent, weight="700")}}
        {{A.txt("v1Title", X, A.FY + 95, "JUDUL GAMBAR", 44, A.text2, anchor="middle", weight="700")}}
        <line id="v1Ground" class="d" x1="{{X - 400}}" y1="2330" x2="{{X + 400}}" y2="2330"
              stroke="{{A.ink}}" stroke-width="12"/>\'\'\'


# TODO: tambah g2, g3, ... lalu daftarkan di sini (urut = urut slide)
DRAW = [g1]
'''


def cmd_init(args):
    d = os.path.abspath(args.dir)
    os.makedirs(os.path.join(d, "assets", "vo"), exist_ok=True)
    os.makedirs(os.path.join(d, "assets", "audio"), exist_ok=True)
    os.makedirs(os.path.join(d, "compositions"), exist_ok=True)
    os.makedirs(os.path.join(d, "scenes"), exist_ok=True)
    cfg = dict(PROJECT_JSON)
    cfg["name"] = args.name or os.path.basename(d)
    f = os.path.join(d, "project.json")
    if os.path.isfile(f) and not args.force:
        raise SystemExit(f"{f} sudah ada (pakai --force untuk timpa)")
    json.dump(cfg, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("proyek dibuat:", f)


def cmd_new(args):
    sid = args.id or os.path.basename(args.file).replace(".py", "")
    base = sid.replace("-r", "")
    txt = SCENE_TEMPLATE.format(sid=sid, base=base, hud1=sid.upper(),
                                hud2=args.judul or "JUDUL", judul=args.judul or "scene")
    os.makedirs(os.path.dirname(os.path.abspath(args.file)), exist_ok=True)
    if os.path.isfile(args.file) and not args.force:
        raise SystemExit(f"{args.file} sudah ada (pakai --force untuk timpa)")
    open(args.file, "w", encoding="utf-8").write(txt)
    print("scene dibuat:", args.file)
    print("lalu: tambahkan ke \"scenes\" di project.json, isi naskah + VO, "
          "lalu `python3 -m pensil run " + args.file + "`")


def cmd_timing(args):
    project = load_project(args.project)
    scene = load_scene(project, args.scene)
    sc = scene.SCENE
    naskah = project.path("vo", sc["naskah"])
    vo = project.path("vo", sc["vo_raw"])
    out = project.path("work", f"words-{sc['id']}.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    res = T.timing(naskah, vo, out, counts_override=sc.get("counts"))
    print(f"{out}: {res['n_words']} kata, {res['n_chunks']} potongan, "
          f"{res['dur']:.2f}s, alokasi {res['counts']}")


def cmd_align(args):
    project = load_project(args.project)
    scene = load_scene(project, args.scene)
    res = A.align(project, scene)
    print(f"{res['out']}: dur={res['dur']} lead={res['lead']} "
          f"jeda={[(round(a, 2), b) for a, b in res['jeda']]}")


def cmd_gen(args):
    project = load_project(args.project)
    scene = load_scene(project, args.scene)
    if args.no_sfx:
        scene.SCENE["sfx"] = False
    res = C.compose(project, scene)
    print(f"{res['out']}: dur={res['dur']} cue={res['cues']} "
          f"kamera={res['cam']} sfx={res['sfx']}")


def cmd_index(args):
    project = load_project(args.project)
    res = I.build_index(project)
    print(f"{res['out']}: {res['scenes']} scene, total {res['total']}s")


def cmd_lint(args):
    project = load_project(args.project)
    errors, _ = V.lint(project, quiet=False)
    print(f"lint: {errors} error")
    return 1 if errors else 0


def cmd_verify(args):
    project = load_project(args.project)
    scene = load_scene(project, args.scene)
    sid = scene.SCENE["id"]
    errors = 0
    if not args.skip_lint:
        errors, _ = V.lint(project, quiet=True)
        print(f"lint: {errors} error")
    start = args.start
    if start is None:
        start = 0.0
        for sf in project.scenes:
            if os.path.basename(sf).replace(".py", "") == sid or \
               I.scene_id_of(project, sf) == sid:
                break
            start = round(start + I.comp_duration(project, I.scene_id_of(project, sf)), 3)
        else:
            raise SystemExit(f"scene {sid} tidak terdaftar di project.json")
    dur = I.comp_duration(project, sid)
    outdir = args.out or os.path.join("/sdcard/Download", f"cek-{sid}")
    if not args.skip_snapshot:
        V.snapshot(project, start, round(start + dur, 3), args.frames, outdir)
    rc, _ = V.analyze(project, scene, outdir)
    return 1 if (errors or rc) else 0


def cmd_run(args):
    for fn, a in ((cmd_timing, args), (cmd_align, args), (cmd_gen, args),
                  (cmd_index, args)):
        fn(a)
    args.skip_lint = False
    args.skip_snapshot = False
    if not args.no_verify:
        return cmd_verify(args)
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(prog="pensil",
                                 description="Toolkit video whiteboard live-draw follow-cam")
    ap.add_argument("--project", default=None, help="folder proyek (default: cari project.json ke atas)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("init", help="buat proyek baru")
    p.add_argument("dir")
    p.add_argument("--name")
    p.add_argument("--force", action="store_true")
    p.set_defaults(fn=cmd_init)

    p = sub.add_parser("new", help="skrip scene baru")
    p.add_argument("file")
    p.add_argument("--id", default=None)
    p.add_argument("--judul", default=None)
    p.add_argument("--force", action="store_true")
    p.set_defaults(fn=cmd_new)

    for name, fn, extra in (("timing", cmd_timing, ""), ("align", cmd_align, ""),
                            ("gen", cmd_gen, "")):
        p = sub.add_parser(name)
        p.add_argument("scene")
        if name == "gen":
            p.add_argument("--no-sfx", action="store_true")
        p.set_defaults(fn=fn)

    p = sub.add_parser("index", help="bangun index.html root")
    p.set_defaults(fn=cmd_index)

    p = sub.add_parser("lint")
    p.set_defaults(fn=cmd_lint)

    p = sub.add_parser("verify", help="lint + snapshot + analisa")
    p.add_argument("scene")
    p.add_argument("--frames", type=int, default=22)
    p.add_argument("--out", default=None)
    p.add_argument("--start", type=float, default=None, help="posisi scene di root (default: hitung otomatis)")
    p.add_argument("--skip-lint", action="store_true")
    p.add_argument("--skip-snapshot", action="store_true")
    p.set_defaults(fn=cmd_verify)

    p = sub.add_parser("run", help="timing+align+gen+index+lint+verify")
    p.add_argument("scene")
    p.add_argument("--frames", type=int, default=22)
    p.add_argument("--out", default=None)
    p.add_argument("--start", type=float, default=None)
    p.add_argument("--no-sfx", action="store_true")
    p.add_argument("--no-verify", action="store_true")
    p.set_defaults(fn=cmd_run)

    args = ap.parse_args(argv)
    rc = args.fn(args)
    sys.exit(rc or 0)


if __name__ == "__main__":
    main()
