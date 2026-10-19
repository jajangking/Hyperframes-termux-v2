#!/data/data/com.termux/files/usr/bin/python3
"""Deteksi jeda kalimat di VO tiap bab (silencedetect) -> segment kalimat."""
import os, re, subprocess, json, glob

ROOT = "/data/data/com.termux/files/home/video/dokumenter-bensin/assets/vo"

def seg(p):
    p = subprocess.run(
        ["ffmpeg", "-hide_banner", "-i", p, "-af",
         "silencedetect=n=-32dB:d=0.35", "-f", "null", "-"],
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.decode(errors="ignore")
    durs = [float(m) for m in re.findall(r"silence_duration: ([0-9.]+)", p)]
    starts = [float(m) for m in re.findall(r"silence_start: ([0-9.]+)", p)]
    ends = [float(m) for m in re.findall(r"silence_end: ([0-9.]+)", p)]
    total = float(re.search(r"Duration: (\d+):(\d+):(\d+\.\d+)",
        p).group(3)) if re.search(r"Duration: \d+:\d+:\d+\.\d+", p) else 0.0
    h, m, s = 0, 0, 0.0
    hm = re.search(r"Duration: (\d+):(\d+):(\d+\.\d+)", p)
    if hm:
        h, m, s = int(hm.group(1)), int(hm.group(2)), float(hm.group(3))
        total = h * 3600 + m * 60 + s
    # bangun segment bicara dari jeda
    segs, cur = [], 0.0
    for st in starts:
        segs.append((cur, st))
        cur = st
    segs.append((cur, total))
    segs = [(a, b) for a, b in segs if b - a > 0.3]
    return total, segs, list(zip(starts, ends, durs))

hasil = {}
for f in sorted(glob.glob(os.path.join(ROOT, "bab*.mp3"))):
    num = int(re.search(r"bab(\d+)", os.path.basename(f)).group(1))
    total, segs, pauses = seg(f)
    hasil[num] = {"file": os.path.basename(f), "total": round(total, 3),
                  "segs": [[round(a, 2), round(b, 2)] for a, b in segs]}
    print(f"bab{num}  total={total:6.2f}s  jeda={len(pauses)}")
    for i, (a, b) in enumerate(segs, 1):
        print(f"    seg{i}: {a:6.2f} -> {b:6.2f}  ({b-a:5.2f}s)")

out = os.path.join(ROOT, "beats.json")
json.dump(hasil, open(out, "w"), indent=2)
print("\ntersimpan:", out)
