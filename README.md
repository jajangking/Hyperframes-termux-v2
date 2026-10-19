# Hyperframes Termux v2 — `pensil`

Pipeline video **whiteboard live-draw follow-cam** yang jalan penuh dari HP
Android lewat Termux. Semua digenerate otomatis: VO TTS → waktu kata →
komposisi HTML+GSAP (gambar mengikuti narasi) → SFX otomatis → verifikasi
visual → rakit jadi satu video utuh.

Framework intinya bernama **`pensil`** — CLI Python murni (stdlib, tanpa
dependensi pip) yang membungkus `hyperframes` untuk lint/snapshot dan
`ffmpeg` untuk audio.

## Isi repo

| Folder | Isi |
|---|---|
| `pensil/` | **Framework CLI** — `timing`, `align`, `gen`, `index`, `lint`, `verify`, `run` |
| `dokumenter-bensin-reels/` | Proyek reels 9:16 "Setetes Bensin" (bab 1–5, port framework) |
| `dokumenter-bensin/` | Proyek induk 16:9 + VO mentah, naskah, words |
| `pensil-demo/` | Contoh scene minimal buat belajar format scene |
| `gen-vo.py`, `vo.sh`, `edge-tts-test-all.sh`, `beats.py` | Skrip legacy TTS/VO |
| `HANDOFF-REELS.md`, `brief-dokumenter-bensin.md`, `log-tanya-jawab.md`, `tts-gratis.md` | Dokumentasi pipeline & keputusan |

## Instalasi di device lain

Prasyarat: Python ≥ 3.9, `ffmpeg`, Node.js, `hyperframes`, Chromium.

```bash
# Linux (apt) / macOS (brew) / Termux (pkg)
pkg/apt/brew install python ffmpeg nodejs chromium
npm i -g hyperframes@0.8.168

# clone + pasang framework
git clone https://github.com/jajangking/Hyperframes-termux-v2.git
cd Hyperframes-termux-v2/pensil && pip install .
# (alternatif tanpa install: export PYTHONPATH=$PWD/../pensil)

# kalau Chromium gak ketemu otomatis:
export HYPERFRAMES_BROWSER_PATH=/path/ke/chromium
```

## Quickstart

```bash
cd dokumenter-bensin-reels
export PYTHONPATH=../pensil          # atau lewati kalau sudah pip install

python3 -m pensil timing scenes/bab1.py    # naskah + VO mentah → words.json
python3 -m pensil align  scenes/bab1.py    # jeda jatuh di senyap alami → VO reels
python3 -m pensil gen    scenes/bab1.py    # → compositions/bab1.html (GSAP)
python3 -m pensil verify scenes/bab1.py    # lint + snapshot + analisa tinta/kamera
python3 -m pensil index                   # rakit index.html semua bab
hyperframes preview .                     # preview http://localhost:3003
```

`pensil verify` mengambil 22 snapshot otomatis, lalu mengecek dua aturan emas:

- **tinta minimum 0,8 %** per frame — tiap momen pasti ada yang sedang digambar;
- **centroid di luar jendela kamera < 200 px** saat tidak sedang geser —
  gambar selalu nyangkut di tengah.

## Format scene

Satu scene = satu file Python (`scenes/babN.py`) berisi:

```python
SCENE    = {...}      # id, judul, VO, lead/jeda, hook kartu pembuka, ...
SLIDES   = [...]      # rentang kata per slide + pra-gambar
CUES     = [...]      # verbatim: (kata, selector, durasi, jenis) — kapan tiap
                      # elemen SVG digambar, mengikuti waktu kata
CAPTIONS = [...]      # potongan teks narasi
SFXMAP   = {...}      # penanda suara per kata (digabung jadi mp3 otomatis)
DRAW     = [g1..gN]   # fungsi pembuat SVG tiap slide (pustaka A: frame/txt/...)

# opsional: PRESHOW, GROUPS, SYL (override presisi pipeline lama)
```

Kamera, kartu pembuka, caption, whoosh-otomatis, dan jeda semuanya
**diturunkan otomatis** dari batas slide — penulis scene cuma fokus ke
naskah, gambar, dan cue.

## Aturan emas

- **Jangan edit hasil generate** (`compositions/*.html`, `words-*-r.json`,
  `index.html`, `assets/audio/sfx-*.mp3`) — selalu regenerate lewat CLI.
- **VO mentah & naskah** adalah sumber kebenaran; ubah di sana lalu
  `timing` + `align` ulang.
- Jeda antar-slide wajib jatuh di senyap alami; setiap kata sisip wajib
  jadi kata pertama potongan ucapan (di-assert otomatis oleh `align`).
- Cue yang selesai melewati durasi video bikin `gen` memunculkan
  **PERINGATAN** — perpanjang `SCENE["tail"]` atau pendekkan cue-nya.

## Dokumentasi detail

- `pensil/README.md` — perintah & API scene lengkap
- `pensil/PORTING.md` — cara mem-port generator lama ke format scene
- `HANDOFF-REELS.md` — status proyek & antrian bab
- `dokumenter-bensin-reels/TEKNIK-LIVE-DRAW.md` — teknik pipeline

MIT License.
