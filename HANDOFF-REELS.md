# Handoff — Reels Dokumenter "Setetes Bensin" (lanjut Bab 6)

Tanggal handoff: 2026-10-19. Bab 1–5 live-draw follow-cam reels (9:16)
**selesai dan terverifikasi**. Sesi berikutnya lanjut **Bab 6 "Kelangkaan"**.

## Status

- **Bab 1** (25,96 s), **Bab 2** (41,04 s), **Bab 3** (52,73 s, 5 slide,
  74 cue, 51 SFX), **Bab 4** (44,90 s, 4 slide, 66 cue, 42 SFX) dan
  **Bab 5** (44,45 s, 5 slide, 88 cue, 46 SFX, 4 jeda) selesai +
  terverifikasi: lint 0 error, `center_check.py` + `ink_regions2.py` lolos
  (snapshot `/sdcard/Download/cek-babN`).
- `dokumenter-bensin-reels/index.html`: host bab1–bab5 terpasang;
  root duration = **209,08 s**. Bab berikutnya mulai `data-start="209.08"`.
- Host bab: bab1 0/25.96 · bab2 25.96/41.04 · bab3 67/52.73 · bab4 119.73/44.9 · bab5 164.63/44.45.
- Bab 5: `word_timing_bab5.py` (66 kata, 13 segmen, rate 5,41 suku/dt),
  `align_bab5.py` (35,45 → 44,45 s, SISIP {12, 30, 40, 49}, GROUPS 13 grup),
  `gen_livedraw_bab5.py` (5 gambar: mesin bakar → reaksi oksigen + asap
  knalpot → panas & gerakan → aturan alam (kekekalan energi) → tak bisa
  kembali; SW=8800, X1..X5=1600..8000; helper `flame()` + `cloud()` baru).
- `TEKNIK-LIVE-DRAW.md` bag. 9 sudah diperbarui dengan catatan Bab 2–5.

## Pipeline per bab (urutan persis)

> **Update 2026-10-19**: pipeline ini sekarang sudah dibungkus jadi framework
> **`~/video/pensil`** (CLI: `pensil timing|align|gen|index|verify|run`,
> lihat `pensil/README.md`). Bab 5 didemonulasikan ulang lewat framework di
> `~/video/pensil-demo` — hasil identik (44,448 s, verify LOLOS). Bab 6–8
> bisa dikerjakan pakai `pensil new scenes/babN.py` + salin pola scene
> `pensil-demo/scenes/bab5.py`; langkah manual di bawah tetap acuan kalau
> framework tidak dipakai.
>
> **Update hook**: proyek reels sekarang punya `project.json` + `scenes/babN.py`
> (framework). Tiap bab dibuka **kartu hook** = pertanyaan besar + subjudul
> `BAB NN · JUDUL` (`SCENE["hook"]`); daftar 8 bab di
> `dokumenter-bensin-reels/hooks.md`. `index.html` & `compositions/babN.html`
> di-generate via `pensil index` / `pensil gen` — jangan diedit tangan.
> Backup index era lama: `/usr/tmp/opencode/index.bab5-era.bak`.

1. **`word_timing_babN.py`** — salin dari `word_timing_bab4.py`.
   Isi `SEG` dari `beats.json` key `"N"` (buang tail silence).
   Verifikasi Σ kata per segmen = jumlah kata naskah (`naskah/babN.txt`).
   `bobot()` (heuristik kelompok vokal) untuk distribusi waktu.
   Output: `dokumenter-bensin/assets/vo/words-babN.json`.
   Catatan bab4: 13 potongan −38dB/0,12 cocok dengan 13 segmen beats
   (tanpa tail); rate 5,19 suku/dt.
2. **`align_babN.py`** — salin dari `align_bab4.py`. Ganti path
   `SRC/OUTA/OUTJ`, isi `GROUPS` (rentang indeks kata per potongan ucapan
   asli, cocokkan silencedetect), `SISIP` (jeda 1,8 s — **semua kata sisip
   wajib kata pertama sebuah potongan** supaya jatuh di senyap alami;
   script meng-assert), `LEAD=1.8`.
   Bab4: SISIP {20, 40, 52}; 37,70 → 44,90 s.
   "Simpangan terbesar 7200 ms" = bug cetak (nilainya = total geseran); jangan diperbaiki.
3. **`gen_livedraw_babN.py`** — salin dari `gen_livedraw_bab4.py`.
   Gambar besar 1600 px per slide, SW = 1600×N + 0 (X=1600…),
   CY=2000, FY=1400, FH=1200, FW=840. Aturan:
   - jeda + preshow (frame + no saja; ground/hatch masuk cue reguler) di tiap batas slide;
   - **cue window dijalan dalam window kamera slidenya** (akhir cue ≤ awal pan berikutnya);
   - koordinat art relatif center-X kamera; id elemen unik per gambar (vN…);
   - helper `derrick()` (menara bor), `drop()`, `wave()`, `zig()`, `hatch()`,
     `flame()` (lidah api), `cloud()` (awan asap) tersedia;
   - `caps_js` wajib `",\n".join` — **typo `"\n".join` membuat array CAPS tanpa
     koma → SyntaxError runtime → timeline gagal terekam → semua frame membeku**
     (bug Bab 4; gejalanya: ink konstan ~1,05 % semua frame).
   - f-string art yang lupa ditutup `'''` menimbulkan SyntaxError menyesatkan
     di baris berikutnya — tutup tiap fungsi gambar dengan `'''` inline.
4. **gen_sfx**: `gen_livedraw_babN.py` → `gen_sfx.py` → `gen_livedraw_babN.py`.
   Output: `compositions/babN.html` + `assets/audio/sfx-babN.mp3`.
5. **index.html**: tambah host babN (`data-start` = akumulasi, `data-duration`
   = durasi align), update `data-duration` `#root`.
6. **Verifikasi** (wajib):
   - lint `HYPERFRAMES_BROWSER_PATH=$PREFIX/bin/chromium-browser hyperframes lint dokumenter-bensin-reels`
   - snapshot `--range <start>,<end> --frames 22` → `/sdcard/Download/cek-babN`
   - `center_check.py` + `ink_regions2.py /sdcard/Download/cek-babN`
   - **cek JS runtime** kalau semua frame membeku: `node cekjs4.mjs`
     (CDP Remote Debugging; sesuaikan nama file/host — salin dari sesi ini)
     atau bandingkan bagian akhir `<script>` dengan bab sebelumnya.

## Jebakan yang sudah diketahui

- **`/tmp` write diblokir** — pakai `/data/data/com.termux/files/usr/tmp/opencode` atau `/sdcard/Download`.
- Model sesi ini tidak bisa membuka PNG — andalkan `center_check.py` + `ink_regions2.py`.
- Lint `duplicate_audio_track` (track 8/9) & `composition_file_too_large` = false positive.
- Ink per-region saat menyeberang bisa ~0,65 %; ambang 0,8 % dihitung pada total frame.
- Frame tepat di batas akhir root bisa kosong — sampling artefak, cek ±0,3 s.
- `compositions/babN.html` jangan diedit tangan; VO asli + `words-babN.json` non-`-r` jangan diubah.
- centroid bisa >200 px pada frame gambar-baru-sebagian (elemen kiri dulu digambar) — bias dini, bukan salahpusat.
- **F-string art dengan `{` hilang** (mis. `38*s} 10*s}`) → SyntaxError di
  baris itu sendiri; py_compile dulu sebelum jalankan generator (bug Bab 5).
- **Artefak preview di index.html**: hyperframes preview pernah menyisipkan
  duplikat bab1 (`id="bab1r_2"`, `class="clip"`) di slot bab berikutnya dan
  menaikkan root duration (164,63 → 190,59). Selalu cek index.html setelah
  preview jalan; versi bersih ada di `.hyperframes/backup/`.

## File kunci

| Path | Peran |
|---|---|
| `…/usr/tmp/opencode/word_timing_bab5.py` | template timing kata terbaru |
| `…/usr/tmp/opencode/align_bab5.py` | template selaraskan + sisip jeda + LEAD |
| `…/usr/tmp/opencode/gen_livedraw_bab5.py` | template generator komposisi terbaru |
| `…/usr/tmp/opencode/cekjs4.mjs` | cek error JS runtime via CDP |
| `…/usr/tmp/opencode/gen_sfx.py` | sintesis SFX + campur bed (generik) |
| `…/usr/tmp/opencode/center_check.py` / `ink_regions2.py` | verifikasi snapshot |
| `dokumenter-bensin/assets/vo/beats.json` | segmen + total durasi semua bab |
| `dokumenter-bensin/assets/vo/naskah/bab6.txt` | naskah bab6 |
| `dokumenter-bensin-reels/TEKNIK-LIVE-DRAW.md` | dokumen teknik otoritatif |
| `dokumenter-bensin-reels/index.html` | root reels — akumulasi data-start/duration |

## Daftar bab tersisa

| Bab | File VO | Durasi | Kata |
|---|---|---|---|
| 6 | `bab6-kelangkaan.mp3` | 34,75 s | cek naskah |
| 7 | `bab7-solusi.mp3` | 49,18 s | cek naskah |
| 8 | lihat beats.json | — | — |
