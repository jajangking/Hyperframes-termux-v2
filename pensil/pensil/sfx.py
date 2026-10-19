"""Sintesis pustaka SFX (Python murni, tanpa dependensi) + campur bed per scene.

Semua suara disintesis sendiri, lalu dicampur ke satu berkas bed pada
waktu-waktu dari peta SFX scene (kata → suara, gain dB, offset detik).
"""

import json
import math
import os
import random
import struct
import subprocess
import wave

SR = 44100

# primitif -------------------------------------------------------------------
def white(n, seed=1):
    r = random.Random(seed)
    return [r.uniform(-1.0, 1.0) for _ in range(n)]


def brown(n, seed=1):
    r = random.Random(seed)
    out, v = [], 0.0
    for _ in range(n):
        v = 0.985 * v + 0.015 * r.uniform(-1.0, 1.0)
        out.append(v)
    return out


def lp1(x, fc):
    a = math.exp(-2.0 * math.pi * fc / SR)
    y, p = [0.0] * len(x), 0.0
    for i, v in enumerate(x):
        p = (1.0 - a) * v + a * p
        y[i] = p
    return y


def hp1(x, fc):
    l = lp1(x, fc)
    return [x[i] - l[i] for i in range(len(x))]


def band(x, lo, hi):
    return lp1(hp1(x, lo), hi)


def sine(f, n, ph=0.0):
    w = 2.0 * math.pi * f / SR
    return [math.sin(w * i + ph) for i in range(n)]


def sweep(f0, f1, n):
    out, ph = [], 0.0
    for i in range(n):
        f = f0 + (f1 - f0) * (i / max(n - 1, 1))
        ph += 2.0 * math.pi * f / SR
        out.append(math.sin(ph))
    return out


def env(n, a, r, hold=1.0):
    A, R = max(1, int(a * SR)), max(1, int(r * SR))
    out = [hold] * n
    for i in range(min(A, n)):
        out[i] = hold * i / A
    for i in range(min(R, n)):
        j = n - 1 - i
        out[j] = min(out[j], hold * i / R)
    return out


def expd(n, k):
    return [math.exp(-k * i / SR) for i in range(n)]


def mul(a, b):
    return [a[i] * b[i] for i in range(len(a))]


def add(*xs):
    n = max(len(x) for x in xs)
    out = [0.0] * n
    for x in xs:
        for i, v in enumerate(x):
            out[i] += v
    return out


def scale(x, g):
    return [v * g for v in x]


def norm(x, peak=0.9):
    m = max(abs(v) for v in x) or 1.0
    return [v * peak / m for v in x]


def n_of(d):
    return int(d * SR)


# pustaka suara --------------------------------------------------------------
def s_paper():                     # kertas / bingkai
    n = n_of(0.34)
    x = band(white(n, 23), 1600, 8000)
    return norm(mul(x, env(n, 0.02, 0.18)), 0.4)


def s_tick():                      # teks muncul
    n = n_of(0.09)
    a = mul(sine(1500, n), expd(n, 70))
    b = mul(band(white(n, 31), 2200, 7000), expd(n, 110))
    return norm(add(a, scale(b, 0.5)), 0.55)


def s_whoosh():                    # kamera geser
    n = n_of(1.0)
    x = band(brown(n, 41), 180, 1100)
    return norm(mul(x, env(n, 0.32, 0.52)), 0.62)


def s_coin():                      # koin / bayar
    n = n_of(0.75)
    d = expd(n, 7.0)
    return norm(add(mul(sine(2350, n), d),
                    scale(mul(sine(3310, n, 0.4), d), 0.6),
                    scale(mul(sine(4720, n, 1.1), expd(n, 12)), 0.35)), 0.55)


def s_pump():                      # pom mengisi
    n = n_of(1.5)
    pulse = [abs(math.sin(2 * math.pi * 8.6 * i / SR)) ** 6 for i in range(n)]
    body = add(scale(sine(286, n), 1.0), scale(sine(572, n), 0.35))
    air = band(white(n, 53), 700, 3000)
    return norm(mul(add(mul(body, pulse), scale(air, 0.25)), env(n, 0.05, 0.25)), 0.55)


def s_rev():                       # mesin menggerung
    n = n_of(1.7)
    a = sweep(70, 300, n)
    b = sweep(140, 600, n)
    c = sweep(210, 900, n)
    x = add(a, scale(b, 0.5), scale(c, 0.25), scale(lp1(white(n, 71), 500), 0.3))
    return norm(mul(x, env(n, 0.18, 0.55)), 0.6)


def s_rumble():                    # perut bumi
    n = n_of(2.1)
    x = add(scale(lp1(brown(n, 83), 150), 1.0), scale(sine(42, n), 0.5))
    return norm(mul(x, env(n, 0.35, 0.75)), 0.6)


def s_deep():                      # minyak mentah
    n = n_of(1.5)
    x = add(scale(sweep(132, 58, n), 1.0),
            scale(band(brown(n, 97), 40, 400), 0.55))
    return norm(mul(x, env(n, 0.12, 0.55)), 0.6)


def s_zap():                       # percikan busi
    n = n_of(0.32)
    x = add(scale(band(white(n, 103), 2400, 9000), 1.0),
            scale(mul(sine(1800, n), expd(n, 40)), 0.4))
    return norm(mul(x, expd(n, 22)), 0.55)


def s_puff():                      # asap knalpot
    n = n_of(0.65)
    x = band(brown(n, 113), 70, 900)
    return norm(mul(x, env(n, 0.012, 0.42)), 0.5)


def s_sting():                     # tanda tanya
    n = n_of(1.25)
    vib = [1.0 + 0.012 * math.sin(2 * math.pi * 6.0 * i / SR) for i in range(n)]
    x = add(scale(sweep(392, 880, n), 1.0), scale(sweep(588, 1320, n), 0.35))
    x = [x[i] * vib[i] for i in range(n)]
    return norm(mul(x, env(n, 0.09, 0.60)), 0.5)


def s_chime():                     # bel SPBU
    n = n_of(0.95)
    x = add(mul(sine(1180, n), expd(n, 5.5)),
            scale(mul(sine(1770, n, 0.3), expd(n, 7.0)), 0.6),
            scale(mul(sine(2360, n, 0.9), expd(n, 9.0)), 0.3))
    return norm(x, 0.5)


def s_boom():                      # aksen berat
    n = n_of(0.7)
    x = add(scale(mul(sine(92, n), expd(n, 11)), 1.0),
            scale(mul(lp1(white(n, 127), 260), expd(n, 16)), 0.45))
    return norm(x, 0.6)


SOUNDS = {
    "paper": s_paper, "tick": s_tick, "whoosh": s_whoosh,
    "coin": s_coin, "pump": s_pump, "rev": s_rev,
    "rumble": s_rumble, "deep": s_deep, "zap": s_zap, "puff": s_puff,
    "sting": s_sting, "chime": s_chime, "boom": s_boom,
}


# tulis berkas ---------------------------------------------------------------
def write_wav(path, x):
    data = bytearray()
    for v in x:
        s = int(max(-1.0, min(1.0, v)) * 32767)
        data += struct.pack("<h", s)
    with wave.open(path, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(bytes(data))


def build_lib(project):
    lib = project.path("audio", "sfx")
    os.makedirs(lib, exist_ok=True)
    for name, fn in SOUNDS.items():
        write_wav(os.path.join(lib, name + ".wav"), fn())
    return lib


def render_bed(events, dur, out_wav):
    n = n_of(dur) + SR // 2
    buf = [0.0] * n
    cache = {}
    for ev in events:
        name = ev["s"]
        if name not in SOUNDS:
            print("  ! suara tak dikenal:", name)
            continue
        if name not in cache:
            cache[name] = SOUNDS[name]()
        snd = cache[name]
        g = 10.0 ** (ev.get("g", 0) / 20.0)
        off = max(0, int(ev["t"] * SR))
        for i, v in enumerate(snd):
            j = off + i
            if j >= n:
                break
            buf[j] += v * g
    peak = max(abs(v) for v in buf) or 1.0
    if peak > 0.92:                        # limiter sederhana
        buf = [v * 0.92 / peak for v in buf]
    write_wav(out_wav, buf)
    return out_wav


def to_mp3(wav_path):
    mp3 = wav_path[:-4] + ".mp3"
    r = subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", wav_path,
                        "-codec:a", "libmp3lame", "-q:a", "5", mp3],
                       capture_output=True)
    if r.returncode == 0 and os.path.exists(mp3):
        os.remove(wav_path)
        return mp3
    print("  ! libmp3lame tidak ada, pakai wav")
    return wav_path


def build_bed(project, events, dur, sid):
    """Campur bed SFX scene → audio/sfx-<id>.mp3 (atau .wav)."""
    out = project.path("audio", f"sfx-{sid}.wav")
    render_bed(events, dur, out)
    return to_mp3(out)


def load_events(path):
    return json.load(open(path, encoding="utf-8"))
