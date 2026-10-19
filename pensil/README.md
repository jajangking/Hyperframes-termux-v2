# pensil

Framework Python untuk video **whiteboard live-draw follow-cam**:
satu *take* panjang, kamera diam saat gambar digambar, lalu bergeser
pelan ke gambar berikutnya — gaya yang dipakai dokumenter **"Setetes Bensin"**
(Bab 1–5, 9:16, terverifikasi).

Dirancang untuk Termux + Chromium + ffmpeg, dengan [hyperframes] dibungkus
sebagai adapter (lint / snapshot / preview). Tanpa dependensi Python di luar
bawaan — semua SFX disintesis sendiri.

## Instalasi

```sh
cd ~/video/pensil
# pakai langsung:
export PYTHONPATH=$PWD
alias pensil="python3 -m pensil"
# atau pasang:
pip install .
```

Syarat: `ffmpeg`, `hyperframes`, `$PREFIX/bin/chromium-browser`, `node`
(opsional, untuk `cekjs.mjs`).

## Alur kerja

```sh
pensil init myproject --name myproject   # 1. scaffold proyek
cp naskah.txt vo/ ; cp narasi.mp3 vo/    # 2. isi naskah + VO mentah
pensil new scenes/bab1.py --id bab1 --judul "JUDUL"   # 3. scene baru (TODO)
#     ... isi SLIDES / CUES / CAPTIONS / SFXMAP / fungsi gambar ...
echo '"scenes": ["scenes/bab1.py"]' >> project.json    # 4. daftarkan
pensil run scenes/bab1.py                # 5. timing→align→gen→index→lint→verify
```

Perintah:

| Perintah | Fungsi |
|---|---|
| `pensil init <dir>` | scaffold proyek (project.json, assets/, scenes/) |
| `pensil new <file.py> --id X` | skrip scene berisi TODO |
| `pensil timing <scene.py>` | naskah + VO → `words-<id>.json` (kata per potongan ucapan, heuristik suku kata) |
| `pensil align <scene.py>` | sisip `jeda` di senyap alami + `lead` kartu pembuka → `words-<id>-r.json` + VO `-r.mp3` |
| `pensil gen <scene.py>` | → `compositions/<id>.html` (GSAP) + bed SFX `sfx-<id>.mp3` |
| `pensil index` | bangun `index.html` root dari daftar scene (akumulasi `data-start`) |
| `pensil lint` | `hyperframes lint` |
| `pensil verify <scene.py>` | lint + snapshot 22 frame + analisa tinta/centroid |
| `pensil run <scene.py>` | semua tahap di atas |

## Struktur scene

Satu file Python per video (`scenes/x.py`):

```python
SCENE = {"id": "bab1r", "hud_left": ("BAB 01", "JUDUL"), "vo_raw": "bab1.mp3",
         "naskah": "naskah/bab1.txt", "lead": 1.8, "jeda": 1.8, "spacing": 1600,
         "hook": "Pertanyaan pembuka yang dijawab bab ini?"}
SLIDES = [{"words": (0, 19)}, {"words": (20, 39), "preshow": "v2"}]  # batas = jeda + kamera
CUES = [(0, "#v1Frame", 1.0, "d"), (0, "#v1Title", 0.8, "t")]        # kata, selector, dur, jenis
CAPTIONS = [(0, 19, "TEKS CAPTION")]
SFXMAP = {0: [("paper", -8, 0.0)]}                                    # kata → suara

def g1(X, A):        # satu fungsi per gambar; A = pustaka gambar (pensil.art.Art)
    return f'''      {A.frame("v1Frame", X)}
        {A.txt("v1Title", X, 1500, "JUDUL", 44, A.text2, anchor="middle")}
        <line id="v1Ground" class="d" x1="{X-400}" y1="2330" x2="{X+400}" y2="2330"
              stroke="{A.ink}" stroke-width="12"/>'''
DRAW = [g1]
```

Aturan mesin (otomatis, tidak perlu diatur manual):

- **Jeda + kamera**: tiap batas `SLIDES` menyisipkan `jeda` detik senyap di
  VO (tepat di senyap hasil deteksi — `align` menolak kalau bukan) dan
  menggeser kamera ke X slide berikutnya selama jeda itu. `lead` = senyap
  awal untuk kartu pembuka.
- **Pra-gambar**: slide dengan `"preshow": "vN"` menggambar `#vNFrame` +
  `#vNNo` di awal jeda (sebelum narasi slide itu mulai).
- **Caption** dipatok ke rentang kata — ikut bergeser otomatis kalau jeda
  berubah.
- **SFX**: peta `SFXMAP` + `whoosh` otomatis tiap pergeseran kamera +
  `paper` tiap pra-gambar. Pustaka suara: paper tick whoosh coin pump rev
  rumble deep zap puff sting chime boom (disintesis Python murni).
- **Elemen SVG**: `class="d"` = digambar (dash), `class="t"` = teks muncul,
  `class="f"` = sekali jadi (panah, silang). Id elemen dipakai di `CUES`.

Kunci `SCENE` opsional lain:

- `hook` — pertanyaan pembuka; mengubah kartu pembuka jadi pertanyaan besar +
  subjudul `BAB NN · JUDUL` (lihat `hooks.md` di proyek Setetes Bensin).
- `layout` — override tema per scene, mis. `{"cy": 2000, "frame": {...}}`
  untuk lembar dengan tata letak beda.
- `connectors: False` + `extra_svg` — matikan garis penghubung auto, isi
  manual (fungsi `(A) -> str` atau string SVG).
- `sfx_auto: False` — matikan whoosh/paper otomatis (semua suara dari `SFXMAP`).
- `opening` — pasangan `(baris1, baris2)` kartu pembuka bila beda dari HUD.

## Tema & rasio

`project.json → theme` mengatur warna latar/lembar/tinta/caption, ukuran
caption, tinggi progress bar; `canvas` mengatur rasio (1080×1920 = 9:16,
1920×1080 = 16:9, 1080×1080 = 1:1). Tata letak lembar (CY, tinggi lembar,
ukuran bingkai) juga di `theme`.

## Verifikasi (wajib tiap scene)

`pensil verify` menembak 22 frame + memeriksa:

- tidak ada frame kosong di tengah-tayang;
- tinta saat kamera bergeser ≥ `verify.ink_min` % (default 0,8);
- centroid gambar ≤ `verify.centroid_max` px dari pusat frame
  (di luar momen pergeseran).

Kalau semua frame membeku (ink konstan) → ada error JS runtime; cek dengan:

```sh
node pensil/resources/cekjs.mjs $PWD/compositions/bab1r.html bab1r 20
```

## Catatan Termux

- `/tmp` diblokir di Termux — semua keluaran ada di dalam proyek / sdcard.
- Snapshot contact sheet selalu "gagal" (modul sharp tidak tersedia di
  arm64) — PNG individu tetap tersedia; abaikan.
- Lint `duplicate_audio_track` untuk track 8/9 adalah **false positive**
  (waktu audio relatif host, sudah diakumulasi `data-start`).
- Jangan mengedit `compositions/*.html` dan `index.html` hasil generate —
  ubah scene / project.json lalu `pensil gen` / `pensil index` lagi.

## Contoh

`pensil-demo/` di folder yang sama — Bab 5 "Terbakar" dokumenter
Setetes Bensin dijalankan ulang lewat framework (VO asli baca-saja),
hasil: `dur=44.448 s, 88 cue, 5 kamera, 46 SFX, lint 0 error, verify LOLOS`.

[hyperframes]: https://github.com/pecktd/hyperframes
