# Cara mem-port `gen_livedraw_babN.py` (lama) → `scenes/babN.py` (framework pensil)

Framework: `/data/data/com.termux/files/home/video/pensil/` (dipakai via
`PYTHONPATH=/data/data/com.termux/files/home/video/pensil python3 -m pensil ...`).
Contoh scene format rujukan: `/data/data/com.termux/files/home/video/pensil-demo/scenes/bab5.py`.

Proyek target: `/data/data/com.termux/files/home/video/dokumenter-bensin-reels/`
Generator lama: `/data/data/com.termux/files/usr/tmp/opencode/gen_livedraw_babN.py`
Align lama (sumber LEAD/SISIP): `/data/data/com.termux/files/usr/tmp/opencode/align_babN.py`
Words file (SUMBER KEBENARAN waktu, JANGAN diubah):
`/data/data/com.termux/files/home/video/dokumenter-bensin/assets/vo/words-babN-r.json`

## Wajib

1. **SCENE**
   - `"id": "babN"` — TANPA akhiran `r` (penting: framework mencari
     `words-babN-r.json`; kalau id `bab1r` jadi `words-bab1r-r.json` = salah).
   - `"hook"`: teks pertanyaan pembuka (diberikan per-bab di instruksi agent).
   - `hud_left` / `hud_right` / `opening`: ambil **persis** dari bagian HUD HTML
     generator lama (`.bab`, `.ttl`, `.trblk`, `#opening`).
   - `naskah` & `vo_raw`: dari bagian `VO =` / `IN =` generator lama
     (vo_raw = nama file VO mentah, mis. `bab1-pembuka.mp3`).
   - `lead`: nilai LEAD dari align lama (atau 0).
   - `jeda`: nilai SISIP dari align lama (biasanya 1.8).
   - `spacing`: selisih X antar gambar (X2−X1; biasanya 1600).
   - `conn_y`: nilai y garis CONN lama (biasanya 2300). Kalau CONN lama beda
     pola/tak bisa direproduksi auto → `"connectors": False` + `SCENE["extra_svg"]`
     berupa fungsi `(A) -> string` yang mengembalikan SVG CONN lama apa adanya.
   - `layout`: HANYA jika konstanta generator lama beda dari default tema
     (cy=2000, sh=4060, frame w=840 y=1400 h=1200). Contoh: `"layout": {"cy": 2000}`.

2. **SLIDES** — tiap entri CAM generator lama = awal satu slide:
   - slide 0: `(CAM[0].kata, CAM[1].kata − 1)`; slide k: `(CAM[k].kata, CAM[k+1].kata − 1)`;
     slide terakhir: `(awal, jumlah_kata − 1)` (jumlah kata dari words-babN-r.json).
   - `"preshow": "vK+1"` hanya untuk slide yang di generator lama punya pasangan
     PRESHOW frame+nomor (`#vNFrame` + `#vNNo`); kalau tidak ada → tanpa kunci preshow.
   - **Validasi wajib**: semua kata pembuka slide ke-2 dst. HARUS ada di kunci
     `jeda` pada words-babN-r.json. Kalau tidak cocok, samakan dengan SISIP align
     lama (yang meng-assert senyap alami). Jangan menebak.

3. **CUES** — salin **VERBATIM** dari generator lama (urut, selector, dur, kind).

4. **CAPTIONS** — salin dari daftar CAPR generator lama, bentuk `(i, j, teks)`.
   Framework menghitung waktu caption dengan aturan yang sama seperti bab5 lama.

5. **SFXMAP** — salin **VERBATIM** (kata → [(suara, gain, offset)]).

6. **DRAW** — tiap fungsi `gN(X)` lama → `gN(X, A)`:
   - baris pertama tiap fungsi:
     ```python
     txt, frame, drop, wave, zig, hatch, derrick, flame, cloud = (
         A.txt, A.frame, A.drop, A.wave, A.zig, A.hatch, A.derrick, A.flame, A.cloud)
     FW, FY, FH = A.FW, A.FY, A.FH
     ```
     (pakai alias yang memang dipakai fungsi itu saja; hapus yang tidak dipakai).
   - isi fungsi **VERBATIM** (warna hex literal boleh tetap).
   - helper lokal `def` di generator lama ikut pindah ke scene; ubah signature-nya
     supaya menerima `A` (atau FW/FY) sebagai argumen, isi tidak berubah.
   - `DRAW = [g1, g2, ...]` urut, **jumlahnya = jumlah SLIDES** (1:1). SVG tambahan
     (CONN dsb.) jangan dimasukkan ke DRAW — pakai connectors/extra_svg.

7. **SFX auto** — framework menambahkan otomatis: `whoosh` gain −10 offset +0.05
   di awal tiap pergeseran kamera + `paper` gain −11 di pra-gambar frame —
   **persis** generator lama bab5. Kalau generator lama babN TIDAK punya pola
   auto ini, set `SCENE["sfx_auto"] = False` dan masukkan event setara ke SFXMAP.

8. **Verifikasi wajib** (dari folder dokumenter-bensin-reels):
   ```sh
   python3 -m py_compile scenes/babN.py
   PYTHONPATH=/data/data/com.termux/files/home/video/pensil python3 -m pensil gen scenes/babN.py
   ```
   Hitung `len(CUES)` dan `len(SFXMAP)` generator lama via python, bandingkan
   dengan jumlah `cue=` dan `sfx=` yang dicetak `pensil gen`.

## DILARANG

- Mengubah generator lama, align lama, words file, VO, naskah, index.html,
  atau komposisi bab lain.
- Menjalankan `pensil lint`, `pensil verify`, atau snapshot (pusat yang menjalankan).
- Mengubah `project.json` atau menambah scene selain babN yang diminta.
- Menebak waktu/urutan — semua ada di generator/align/words lama; kalau ada
  pertentangan, laporkan di ringkasan (jangan diam-diam memilih).
