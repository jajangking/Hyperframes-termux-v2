# Hook Pembuka per Bab — Setetes Bensin (reels)

Setiap bab membuka dengan **kartu hook**: pertanyaan besar (teks utama kartu
pembuka), lalu subjudul kecil `BAB NN · JUDUL`. Tampil selama `lead`
(kartu pembuka, default 1,8 s) sebelum narasi mulai.

Dipakai lewat `SCENE["hook"]` di `scenes/babN.py` (fitur framework pensil —
lihat `pensil/pensil/compose.py`). Narasi VO tidak diubah sama sekali; hook
murni elemen visual yang pertanyaannya dijawab oleh isi bab itu.

| Bab | File VO | Hook pertanyaan |
|---|---|---|
| 1 · Pembuka | `bab1-pembuka.mp3` | Dari mana cairan di pom bensin itu datang — dan ke mana perginya? |
| 2 · Apa itu bensin | `bab2-apa-itu-bensin.mp3` | Kenapa bensin bisa menggerakkan mobil? |
| 3 · Asal usul | `bab3-asal-usul-r.mp3` | Kalau minyak butuh jutaan tahun terbentuk, ia berasal dari apa? |
| 4 · Keluar dari bumi | `bab4-keluar-dari-bumi-r.mp3` | Di mana bumi menyimpan bensin, dan bagaimana kita mengeluarkannya? |
| 5 · Terbakar | `bab5-terbakar-r.mp3` | Saat bensin terbakar, apa yang benar-benar habis? |
| 6 · Kelangkaan | `bab6-kelangkaan.mp3` | Kalau dibutuhkan jutaan tahun untuk terbentuk — berapa lama bensin tersisa? |
| 7 · Solusi | `bab7-solusi.mp3` | Lalu, apa yang bisa kita lakukan mulai hari ini? |
| 8 · Penutup | `bab8-penutup.mp3` | Ke mana arah cerita bensin — di tangan siapa? |

Catatan:
- Bab 1 & 7 pertanyaannya selaras kalimat pembuka VO (VO sudah mengajukan
  pertanyaan sejenis di detik-detik pertama) — tulisan jadi penguat, bukan bentrok.
- Bab 6–8: hook ini sudah final; tinggal tempel ke `SCENE["hook"]` saat scene
  bab itu dibuat (`pensil new scenes/babN.py`, pola di `pensil-demo/scenes/bab5.py`).
