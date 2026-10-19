"""Verifikasi hasil render: lint hyperframes + snapshot + analisa tinta/kamera.

Aturan lulus (dari praktik Bab 1-5 dokumenter-bensin):
  - tidak ada frame kosong (kecuali tepat di batas awal/akhir = artefak sampling);
  - tinta selama pergeseran kamera >= ink_min % (default 0.8);
  - jarak centroid gambar ke pusat frame <= centroid_max px (default 200)
    di luar pergeseran kamera (saat menyeberang centroid bebas).
"""

import glob
import math
import os
import re
import subprocess

from pensil.config import jeda_map


def _env(project):
    env = dict(os.environ)
    env["HYPERFRAMES_BROWSER_PATH"] = project.browser
    return env


def lint(project, quiet=False):
    r = subprocess.run(["hyperframes", "lint", project.root],
                       capture_output=True, text=True, env=_env(project))
    out = r.stdout + r.stderr
    if not quiet:
        print(out)
    m = re.search(r"(\d+)\s*error\(s\),\s*(\d+)\s*warning\(s\)", out)
    errors = int(m.group(1)) if m else (1 if r.returncode != 0 else 0)
    return errors, out


def snapshot(project, start, end, frames, outdir):
    cmd = ["hyperframes", "snapshot", project.root,
           "--range", f"{start},{end}", "--frames", str(frames),
           "--output", outdir, "--no-end"]
    r = subprocess.run(cmd, capture_output=True, text=True, env=_env(project))
    print((r.stdout + r.stderr).splitlines()[-1] if (r.stdout + r.stderr) else "")
    if r.returncode != 0:
        raise SystemExit("snapshot gagal:\n" + r.stdout + r.stderr)
    return outdir


def pan_windows(project, scene):
    """[(mulai, akhir)] pergeseran kamera per slide (kata → jeda)."""
    sid = scene.SCENE["id"]
    import json
    p = project.path("work", f"words-{sid}-r.json")
    if not os.path.isfile(p):
        return []
    spec = json.load(open(p, encoding="utf-8"))
    words, jm = spec["words"], {int(k): v for k, v in spec.get("jeda", {}).items()}
    return [(words[w]["t"] - J, words[w]["t"]) for w, J in jm.items()]


def _load_raw(p, W, H):
    return subprocess.run(
        ["ffmpeg", "-v", "error", "-i", p, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
        capture_output=True).stdout


def analyze(project, scene, snapdir, verbose=True):
    W, H = project.canvas["w"], project.canvas["h"]
    vcfg = project.verify_cfg
    pans = pan_windows(project, scene)
    files = sorted(glob.glob(os.path.join(snapdir, "*.png")))
    if not files:
        raise SystemExit(f"tidak ada PNG di {snapdir}")
    rows, fails = [], []
    if verbose:
        print(f"{'t':>7} {'npx':>8} {'cx':>6} {'cy':>6} {'jarak':>6} {'isi%':>6}  jenis")
    for f in files:
        m = re.search(r"at-([\d.]+)s", f)
        t = float(m.group(1))
        raw = _load_raw(f, W, H)
        sx = sy = n = 0
        y0, y1 = int(H * 140 / 1920), int(H * 1770 / 1920)
        for y in range(y0, y1):
            row = y * W * 3
            for x in range(W):
                i = row + x * 3
                if raw[i] > 110 or raw[i + 1] > 110 or raw[i + 2] > 110:
                    sx += x
                    sy += y
                    n += 1
        isi = 100.0 * n / (W * (y1 - y0))
        is_pan = any(a < t < b for a, b in pans)
        if n == 0:
            rows.append((t, 0, 0, 0, 0, 0.0, "?"))
            continue
        cx, cy = sx / n, sy / n
        d = math.hypot(cx - W / 2, cy - H / 2)
        jenis = "geser" if is_pan else "gambar"
        rows.append((t, n, cx, cy, d, isi, jenis))
        if isi < vcfg["ink_min"]:
            fails.append(f"t={t:.1f} tinta {isi:.2f}% < {vcfg['ink_min']}%")
        if not is_pan and d > vcfg["centroid_max"]:
            fails.append(f"t={t:.1f} centroid {d:.0f}px > {vcfg['centroid_max']}px")
        if verbose:
            print(f"{t:7.1f} {n:8d} {cx:6.0f} {cy:6.0f} {d:6.0f} {isi:6.2f}  {jenis}")
    # frame kosong di awal/akhir = sampling artefak; di tengah = gagal
    blanks = [r[0] for r in rows if r[1] == 0]
    tmax = rows[-1][0] if rows else 0
    for t in blanks:
        if t - rows[0][0] > 0.5 and tmax - t > 0.5:
            fails.append(f"t={t:.1f} frame kosong")
    if fails:
        print("GAGAL:")
        for x in fails:
            print("  -", x)
        return 1, fails
    print(f"LOLOS: {len(rows)} frame, "
          f"tinta min {min(r[5] for r in rows if r[1]):.2f}%, "
          f"centroid maks (luar geser) "
          f"{max((r[4] for r in rows if r[6] == 'gambar'), default=0):.0f}px")
    return 0, []
