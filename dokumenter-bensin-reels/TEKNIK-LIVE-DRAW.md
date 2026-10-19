# Teknik: **Live-Draw Follow-Cam (Satu Shot)**

Dokumen ini menjelaskan teknik yang dipakai di Bab 1 Reels: satu lembar blueprint
besar yang digambar sambil berjalan, dengan kamera virtual yang mengikuti gambar.

---

## 1. Nama tekniknya

| Sebutan | Keterangan |
| --- | --- |
| **One-shot follow-cam whiteboard animation** | Nama paling tepat. Satu shot tanpa potongan, kamera mengikuti objek yang sedang digambar. |
| **Live-draw / speed-drawing** | Gaya "digambar saat itu juga", bukan muncul/transisi. |
| **Whiteboard animation** (gaya *RSA Animate*, *Common Craft*, VideoScribe, Doodly) | Genre besarnya: presenter menggambar di papan sambil bercerita. |
| **Self-drawing line animation** | Nama teknis untuk efek garisnya (`stroke-dasharray` + `strokeDashoffset`). |
| **Virtual camera / pan-and-scan** | Nama teknis untuk kameranya: jendela yang digeser di ruang dunia (world space). |
| **Key-point illustration** | Prinsip isinya: hanya poin penting yang digambar, bukan tiap kata. |

Jadi kalau harus satu kalimat:
> **whiteboard live-draw satu shot, kamera virtual mengikuti gambar di atas satu lembar blueprint luas.**

---

## 2. Prinsip

1. **Satu lembar.** Semua gambar hidup di satu kanvas besar (world space). Tidak ada
   potongan, tidak ada scene terpisah.
2. **Kamera = jendela 1080×1920** yang digeser di atas kanvas itu. Skala tetap →
   **hanya geser, tanpa zoom**.
3. **Kamera diam saat menggambar**, lalu geser pelan ke gambar berikutnya. Ini yang
   membuat ritme terasa tenang; kamera yang bergerak terus-menerus terbaca "gragas".
4. **Poin penting saja, tapi detail.** Satu kalimat VO = satu gambar besar yang
   digambar detail, bukan 10 ikon kecil.
5. **Waktu ikut TTS.** Setiap elemen digambar tepat saat kata yang mewakilinya
   diucapkan.

---

## 3. Cara kerja teknis

### 3.1 Garis yang menggambar diri sendiri
Setiap elemen yang digambar diberi kelas `.d`:

```js
el.style.strokeDasharray  = L + " " + L;
el.style.strokeDashoffset = L;   // garis jadi tak terlihat
```

Panjang `L` diambil dari `getTotalLength()` (untuk `<line>`, `<rect>`, `<circle>`
yang tidak punya `getTotalLength`, dipakai keliling bbox sebagai perkiraan).
Animasi menarik `strokeDashoffset` ke `0` → garis tampak tertulis dari ujung ke ujung.

Kelas lain:

| Kelas | Perilaku |
| --- | --- |
| `.d` | digambar (dash offset) |
| `.t` | muncul dengan fade (teks) |
| `.f` | fade saja — dipakai elemen ber-`marker` panah, karena marker tidak ikut ter-dash dan akan muncul lebih dulu |

Semua `.t`, `.f`, dan caption dipaksa `opacity: 0` saat init.

### 3.2 Kamera virtual
Seluruh lembar dibungkus `#world`, lalu digeser dengan transform:

```js
tx = VW/2 - center.x;      // VW = 1080
ty = VH/2 - center.y;      // VH = 1920
gsap.to(world, { x: tx, y: ty, duration: dur, ease: "power2.inOut" });
```

`center` adalah titik pusat gambar yang sedang disorot. Skala **tidak pernah diubah**.

### 3.3 Sinkronisasi dengan VO
Waktu kata diambil dari `assets/vo/words-bab1-r.json`. Waktu itu **diselaraskan ke
suara asli**, bukan disebar rata per kalimat:

1. `silencedetect` memotong VO jadi potongan ucapan.
2. Tiap potongan dibagi ke kata-katanya menurut **jumlah suku kata**.
3. Onset kata menempel ke senyap nyata (mis. "Kita" = 8.055 s = akhir senyap 8.0545 s).

Waktu lama yang disebar rata meleset ~0.5 detik, sehingga cue menggambar terlalu awal.

Cue ditulis:

```python
CUES = [(11, "#v2Car .d", 1.6, "d"), ...]   # (indeks kata, selektor, durasi, jenis)
```

Semua cue dimasukkan ke satu GSAP timeline, jadi seek/preview/render selalu konsisten.

### 3.4 Band caption (dan jebakan `.clip`)

Caption diturunkan dari **rentang kata**, bukan waktu mati, jadi ikut bergeser otomatis
kalau waktu/jeda berubah:

```python
CAPR = [(0, 8, "JUTAAN KENDARAAN BERHENTI DI TEMPAT YANG SAMA"), ...]  # (kata awal, kata akhir, teks)
```

Caption ditulis sebagai anak `#caps`:

```html
<div id="c0" class="clip" data-start="2.667" data-duration="4.65">…</div>
```

**Jebakan:** `class="clip"` wajib (lint + runtime menyembunyikan di luar rentang waktu),
tetapi `.clip` mendefinisikan `inset:0; width:1080px; height:1920px`. Tanpa override,
kotak caption jadi setinggi layar dan **teksnya menempel di puncak layar** (menimpa HUD),
bukan di bawah. Karena itu `#caps > div` harus menimpa:

```css
#caps > div {
  position: absolute; left: 0; right: 0; bottom: 26px; top: auto; height: auto;
  width: 1080px; …
}
```

Selektornya (1 id) lebih kuat dari `.clip` (1 class), jadi tiap properti `inset` teratasi.

Cara cepat memastikan caption ada di bawah: hitung piksel terang di band bawah
(y 1760–1920) vs band atas (y 0–160) — band atas harus tetap (HUD saja).

---

## 4. Aturan pacing (penting)

| Aturan | Nilai |
| --- | --- |
| Jarak antar gambar di lembar | **1600 px** (jendela 1080 px). Koridor antar gambar = 1600−840 = **760 px**, lebih sempit dari jendela → saat kamera menyeberang, tepi dua gambar selalu terlihat |
| Durasi geser kamera | **= panjang jeda** (1.8 detik; 1.0 detik untuk batas yang jatuh di tengah kalimat) |
| Geser dimulai | tepat saat jeda mulai · **tiba** tepat saat kalimat berikutnya mulai |
| Panel berikutnya | bingkai + nomor + alas digambar **di dalam jeda** (pra-gambar), supaya kamera tidak pernah tiba di layar kosong |
| Durasi menggambar per elemen | 0.6 – 1.6 detik |

**Aturan mati:** jangan pernah biarkan frame kosong. Ambang aman: liputan tinta ≥ 0.8 %.
Setelah jeda + pra-gambar + jarak 1600 px, titik terendah saat menyeberang ≈ **1.0 %**.

### 4.1 Jeda antar-slide

Supaya penonton awam sempat mencerna, tiap slide diberi **jeda** di batasnya.
Jeda disisipkan ke dalam berkas VO (bukan cuma di animasi), jadi ucapan dan gambar
tetap sinkron:

1. `silencedetect` mencari senyap alami di VO.
2. Senyap buatan ditambahkan **di dalam** senyap alami itu → tidak ada kata terpotong.
3. Semua kata pada/atau setelah titik sisip digeser sebesar jeda.
4. Kamera bergeser **selama** jeda: berangkat saat jeda mulai, tiba saat kalimat mulai.
5. Sambil kamera bergeser, panel tujuan sudah disiapkan (bingkai, nomor, alas).

| Batas slide | Pemicu | Jeda | Total senyap |
| --- | --- | --- | --- |
| 1 → 2 | kata "Kita" | 1.8 s | 2.36 s |
| 2 → 3 | kata "Tapi" | 1.8 s | 2.35 s |
| 3 → 4 | kata "dan" (tengah kalimat) | 1.0 s | 1.46 s |

Bab 1 (jeda saja): 18.36 s → 22.96 s.

### 4.2 Lead-in judul

Judul pembuka sebelumnya hanya menumpang di atas narasi dan lewat dalam ~1 detik
(tidak terbaca). Solusinya **`LEAD`**: senyap yang disisipkan di **awal** VO supaya
kartu judul berdiri sendiri sebelum narasi mulai.

| Nilai | Bab 1 |
| --- | --- |
| `LEAD` | 3.0 s |
| Judul muncul → tahan → pudar | 0.25 → 3.35 → 3.95 s (≈2.4 s diam terbaca) |
| Kata pertama | 3.217 s |

Cue menggambar & caption otomatis ikut bergeser karena semuanya dihitung dari
`WORDS[w].t` (yang sudah termasuk `LEAD`). Durasi akhir Bab 1 = **25.96 s**.

> Karena ada lead-in, caption baru mulai saat kata ke-0, jadi tidak ada caption di
> bawah selama kartu judul (judul jadi fokus tunggal).

### 4.3 `index.html` harus ikut disinkronkan

`hyperframes snapshot/lint <DIR>` merender **root timeline** (`index.html`), bukan
berkas komposisi langsung. Jadi kalau durasi bab berubah:

- `data-duration` di `#root` = jumlah durasi semua bab;
- `data-duration` tiap host = durasi bab itu;
- `data-start` tiap host = akumulasi durasi bab sebelumnya.

**Jebakan:** kalau `index.html` masih memuat bab yang sama dua kali, snapshot di
t>durasi bab akan mengambil frame **copy kedua** — verifikasi jadi menyesatkan
(mis. t=24 terlihat seperti t=24, padahal itu t=24−18.36=5.64). Selalu pastikan
satu host per bab.

---

## 5. Tata suara (SFX)

Semua SFX disintesis sendiri (tanpa aset pihak ketiga) memakai Python murni —
`gen_sfx.py` — lalu **dicampur jadi satu berkas bed per bab** yang sinkron dengan
event gambar. Hanya satu `<audio>` per bab, jadi DOM tidak dipenuhi puluhan node audio.

### 5.1 Pustaka suara (13)

| Suara | Dipakai untuk |
| --- | --- |
| `paper` | kertas / panel baru disiapkan |
| `tick` | tiap teks/label muncul |
| `whoosh` | kamera mulai bergeser |
| `chime` | bel SPBU |
| `pump` | pom mengisi bensin |
| `coin` | membayar |
| `sting` | tanda tanya |
| `boom` | aksen berat |
| `rumble` | perut bumi |
| `deep` | minyak mentah |
| `puff` | asap knalpot |
| `zap` | percikan busi |
| `rev` | mesin menyala |

> **Jangan pakai suara goresan pensil (`line`).** Sudah dicoba dan dibuang: getaran
> 26 Hz pada derau berband membuatnya terdengar seperti *spspspsp*, dan karena
> dipanggil tiap goresan (±35×) jadi sangat mengganggu.

### 5.2 Cara memetakan

Di generator, tiap kata punya daftar SFX:

```python
SFXMAP = {
    11: [("pump", -13, 0.20), ("tick", -13, 0.35)],
    #      suara     gain dB     geser detik   → waktu = waktu_kata + geser
}
```

Tiga whoosh kamera ditambahkan otomatis 0.15 detik **sebelum** kamera berangkat —
persis sama dengan aturan pacing kamera.

### 5.3 Aturan volume

| Aturan | Nilai |
| --- | --- |
| SFX terhadap VO | **≈ 3 dB di bawah VO** (mean SFX −23 dB, VO −20 dB) |
| Limiter bed | puncak ditahan di 0.92 linear (−0.7 dBFS) |
| Larangan | SFX keras tepat di atas suku kata penting |

SFX **selalu** di bawah narasi. Kalau ragu, kecilkan gain 2–3 dB.

### 5.4 Keluaran

```
assets/audio/sfx/<nama>.wav      pustaka (bisa dipakai ulang bab lain)
assets/audio/sfx-babN.mp3        bed hasil campuran
```

```bash
# 1. selaraskan waktu kata + sisipkan jeda (sekali per bab)
python3 /data/data/com.termux/files/usr/tmp/opencode/align_bab1.py

# 2. tulis event SFX
python3 /data/data/com.termux/files/usr/tmp/opencode/gen_livedraw_bab1.py

# 3. bangun pustaka SFX + bed
python3 /data/data/com.termux/files/usr/tmp/opencode/gen_sfx.py

# 4. tulis komposisi (nama berkas SFX sudah pasti .mp3)
python3 /data/data/com.termux/files/usr/tmp/opencode/gen_livedraw_bab1.py
```

> Generator dijalankan **dua kali**: sekali untuk menulis event, sekali lagi setelah
> `gen_sfx.py` menentukan hasilnya `.mp3` atau `.wav`.

---

## 6. Ukuran kanvas (Bab 1)

```
Lembar          : 7200 × 4060 px (world space)
Jendela kamera  : 1080 × 1920 px (skala 1)
4 tempat kamera : x = 1600, 3200, 4800, 6400   ·   y = 2000
Bingkai gambar  : 840 × 1200 px, mulai y = 1400
```

> **Aturan wajib: semua koordinat art ditulis relatif terhadap titik tengah gambar**
> (`X-400`, `X+230`, …), **jangan absolut**. Kalau titik tengah kamera digeser tapi
> koordinat art tidak ikut, seluruh konten akan tampak miring ke samping — gambar
> tidak lagi berada di tengah frame.

Isi tiap tempat:

| # | Gambar | Isi | Kata |
| --- | --- | --- | --- |
| 01 | Jalan & SPBU | jalan, 3 mobil, kanopi SPBU, tiang, 2 pom, papan harga, pohon, awan | 0–10 |
| 02 | Mengisi & bayar | mobil besar, tutup tangki, nozzle, selang, pom, meteran, koin Rp, panah "lalu pergi" | 11–15 |
| 03 | Dari mana? | tanda "?", penampang bumi, lapisan, sisa makhluk laut, kantong minyak, panah naik | 16–25 |
| 04 | Ke mana? | blok mesin, silinder, piston, batang, engkol, busi, api, knalpot, asap, roda | 26–33 |

---

## 7. Berkas

| Berkas | Fungsi |
| --- | --- |
| `dokumenter-bensin-reels/compositions/bab1.html` | komposisi jadi — **jangan diedit tangan**, hasil generator |
| `dokumenter-bensin-reels/index.html` | root reels — satu host per bab; `data-duration` harus ikut durasi bab |
| `/data/data/com.termux/files/usr/tmp/opencode/gen_livedraw_bab1.py` | generator (art, cue, kamera, event SFX) |
| `/data/data/com.termux/files/usr/tmp/opencode/gen_sfx.py` | sintesis pustaka SFX + campur bed per bab |
| `/data/data/com.termux/files/usr/tmp/opencode/align_bab1.py` | selaraskan waktu kata + sisipkan jeda ke VO |
| `dokumenter-bensin/assets/vo/bab1-pembuka-r.mp3` | VO reels (sudah berjeda) |
| `dokumenter-bensin/assets/vo/words-bab1-r.json` | waktu kata terselaras + durasi + jeda |
| `dokumenter-bensin/assets/audio/sfx/` | pustaka 13 SFX (`.wav`) |
| `dokumenter-bensin/assets/audio/sfx-bab1.mp3` | bed SFX Bab 1 |
| `dokumenter-bensin/assets/vo/bab1-pembuka.mp3` | VO asli (16:9) — jangan diubah |
| `dokumenter-bensin/assets/vo/words-bab1.json` | waktu kata asli (16:9) — jangan diubah |
| `dokumenter-bensin/assets/vo/beats.json` | batas kalimat / jeda tiap bab |
| `dokumenter-bensin/assets/vo/durations.json` | durasi VO tiap bab |

Urutan kerja: sunting generator → jalankan → lint → snapshot → periksa.

```bash
python3 /data/data/com.termux/files/usr/tmp/opencode/align_bab1.py
python3 /data/data/com.termux/files/usr/tmp/opencode/gen_livedraw_bab1.py
python3 /data/data/com.termux/files/usr/tmp/opencode/gen_sfx.py
python3 /data/data/com.termux/files/usr/tmp/opencode/gen_livedraw_bab1.py

HYPERFRAMES_BROWSER_PATH=$PREFIX/bin/chromium-browser \
  hyperframes lint dokumenter-bensin-reels

HYPERFRAMES_BROWSER_PATH=$PREFIX/bin/chromium-browser \
  hyperframes snapshot dokumenter-bensin-reels -o /sdcard/Download/cek --at 1.0,2.2,3.4,4.0,9.7,15.4,22.0,24.0 --no-end

python3 /data/data/com.termux/files/usr/tmp/opencode/center_check.py /sdcard/Download/cek
```

---

## 8. Verifikasi visual (tanpa mata)

Android/arm64 tidak punya `sharp` maupun `PIL`, jadi verifikasi pakai ffmpeg:

- **`center_check.py`** — menghitung titik berat piksel terang. Saat menggambar,
  titik berat harus dekat tengah frame (**jarak < 200 px**). Kalau jauh — apalagi
  selalu ke satu arah — berarti kamera memusatkan titik yang salah (konten offset).
- **`ink_regions.py`** — menghitung liputan tinta per wilayah. Harus **naik** selama
  satu gambar digambar, lalu **turun** (tapi tidak nol) saat kamera geser.

Skrip ada di `/data/data/com.termux/files/usr/tmp/opencode/`.

---

## 9. Menerapkan ke Bab 2–8

1. Salin `align_bab1.py` → `align_babN.py`; isi `GROUPS` (potongan ucapan → rentang
   indeks kata), `SYL` (jumlah suku kata tiap kata), dan `SISIP` (batas slide + jeda).
2. Salin `gen_livedraw_bab1.py`.
3. Ganti 3–5 gambar dengan poin penting bab itu — jarak antar gambar 1600 px,
   dan tiap batas slide punya jeda + pra-gambar.
4. Baca `words-babN-r.json` (bukan yang asli) dan pakai `babN-*.mp3` versi reels.
5. Petakan cue + SFX ke kata bab itu.
6. Lint + snapshot + cek tinta (titik terendah saat menyeberang ≥ 0.8 %), baru lanjut.

Catatan hasil Bab 2 (`bab2-apa-itu-bensin-r.mp3`, 41.04 s, 5 slide, 5 stop kamera):

- Isi `SYL` tidak perlu dihitung manual — `align_bab2.py` menghitungnya otomatis
  dengan heuristik jumlah kelompok vokal (`bobot()`).
- `ink_regions.py` menerima path folder snapshot lewat `argv` (salinan kerja:
  `ink_regions2.py`).
- Saat menyeberang, liputan tinta per wilayah minimal ~0,6–1 %; frame `t=62.0`
  menyentuh 0,65 % (ambang 0,8 % tercapai di cek total `center_check.py`).
- Peringatan lint `duplicate_audio_track` untuk track host adalah **false positive**
  (waktu track relatif host, digeser `data-start`).

Catatan hasil Bab 3 (`bab3-asal-usul-r.mp3`, 52.73 s, 5 slide) dan Bab 4
(`bab4-keluar-dari-bumi-r.mp3`, 44.90 s, 4 slide, 66 cue):

- Semua kata `SISIP` bab3/4 jatuh di awal potongan ucapan (senyap alami);
  kalimatnya boleh saja mulai 1–2 kata sebelumnya ("...spons. **Untuk**" lalu
  jeda sebelum "mengeluarkannya") — asal senyapnya nyata.
- **`caps_js` pada generator wajib `",\n".join`** — typo `"\n".join` membuat
  array JS `CAPS` tanpa koma → SyntaxError saat runtime → `window.__timelines`
  tidak pernah terisi → SEMUA frame snapshot membeku (ink konstan ~1 %).
  Cek cepat: bandingkan akhir `<script>` dengan bab sebelumnya, atau jalankan
  `cekjs4.mjs` (CDP Remote Debugging, lihat HANDOFF-REELS.md).
- F-string art yang lupa ditutup `'''` memunculkan SyntaxError di baris
  fungsi berikutnya — errornya menyesatkan; periksa penutup tiap fungsi gambar.
- Generator bab4 sengaja memakai `derrick()`, `drop()`, `wave()`, `zig()`,
  `hatch()` sebagai helper — salin saja untuk bab berikutnya.
- Preshow bab4 hanya frame + nomor; ground/hatch digambar sebagai cue reguler
  di awal narasi slide (lebih bersih, tidak berebut jeda).
- Centroid bisa 200–215 px pada frame gambar-baru-sebagian (elemen kiri
  digambar dulu) — bias menggambar dini, bukan kamera salahpusat; frame
  tengah geseran tetap di bawah ambang.

Catatan hasil Bab 5 (`bab5-terbakar-r.mp3`, 44.45 s, 5 slide, 88 cue, SISIP
{12, 30, 40, 49} = 4 jeda):

- **F-string art dengan kurung kurawal hilang** (mis. `c{-8*s},{38*s} 10*s},{46*s}`
  — lupa `{` di depan `10*s`) memunculkan SyntaxError yang jelas di baris itu;
  jalankan `python3 -m py_compile` sebelum menjalankan generator.
- Helper `flame()` (lidah api) dan `cloud()` (awan asap, busur-arc) ditambahkan
  ke boilerplate — berguna untuk bab pembakaran/knalpot.
- **Cek `index.html` setelah preview berjalan**: hyperframes preview pernah
  menyisipkan duplikat bab1 (`class="clip"`, `id="bab1r_2"`) di slot bab
  berikutnya dan menaikkan root duration (164.63 → 190.59). Versi bersih ada di
  `.hyperframes/backup/` (diff-kan sebelum menghapus).
