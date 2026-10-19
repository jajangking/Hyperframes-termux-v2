#!/data/data/com.termux/files/usr/bin/python3
"""Generate VO 8 bab pakai edge-tts (Brian), lalu catat durasinya."""
import os, json, subprocess, sys

VOICE = "en-US-BrianMultilingualNeural"   # Brian
RATE  = "-5%"                              # agak lambat, tempo dokumenter
ROOT  = "/data/data/com.termux/files/home/video/dokumenter-bensin/assets/vo"
NASKA = os.path.join(ROOT, "naskah")
os.makedirs(NASKA, exist_ok=True)

BAB = [
 (1, "pembuka", "Pembuka - pertanyaan yang belum terjawab",
  "Setiap hari, jutaan kendaraan berhenti di tempat yang sama: pom bensin. "
  "Kita mengisi, membayar, lalu pergi. Tapi pernahkah kita benar-benar bertanya, "
  "dari mana cairan ini datang, dan ke mana ia pergi setelah mesin menyala?"),

 (2, "apa-itu-bensin", "Apa itu bensin",
  "Bensin adalah bahan bakar cair yang lahir dari minyak bumi. Warnanya kekuningan, encer, "
  "baunya menyengat, dan ia menguap dengan cepat. Di dalam mesin, bensin bercampur udara, "
  "lalu dipadatkan. Sebuah percikan api dari busi membakarnya dalam sekejap. Ledakan kecil "
  "itulah yang mendorong piston, memutar poros, dan akhirnya menggerakkan roda. Singkatnya, "
  "energi kimia berubah menjadi gerakan."),

 (3, "asal-usul", "Asal usul: minyak bumi",
  "Jawabannya terletak jauh sebelum manusia ada. Minyak bumi terbentuk dari sisa makhluk hidup, "
  "plankton, tumbuhan, dan hewan laut, yang mati dan terkubur di dasar laut jutaan tahun lalu. "
  "Tertimbun, terhimpit, dan terpanggang panas bumi, mereka perlahan berubah menjadi cairan hitam "
  "pekat, minyak mentah. Karena prosesnya butuh jutaan tahun, minyak bumi disebut bahan bakar fosil, "
  "dan ia tidak bisa diperbarui dalam waktu singkat. Cairan inilah yang kemudian dipanaskan di kilang. "
  "Uapnya didinginkan pada suhu berbeda-beda, dan bagian yang paling ringan itulah yang kita sebut bensin."),

 (4, "keluar-dari-bumi", "Keluar dari perut bumi",
  "Minyak bumi terperangkap di pori-pori batuan, ratusan hingga ribuan meter di bawah kita, "
  "seperti air di dalam spons. Untuk mengeluarkannya, manusia mengebor. Batuan ditembus, lalu "
  "minyak mengalir dan dipompa naik ke permukaan, didorong tekanan dari dalam bumi. Di beberapa "
  "tempat, minyak bahkan merembes sendiri ke permukaan, seperti sumur tradisional yang diwariskan "
  "turun-temurun. Namun jumlahnya kecil. Yang memenuhi kebutuhan dunia adalah sumur bor raksasa "
  "dan jaringan pipa sepanjang benua."),

 (5, "terbakar", "Terbakar: hilang atau berubah?",
  "Di dalam mesin, bensin dibakar. Tapi ia tidak benar-benar hilang. Ia berubah. Bensin bertemu "
  "oksigen dan berubah menjadi karbon dioksida dan uap air, yang kita lihat sebagai asap knalpot, "
  "sementara energinya berubah menjadi panas dan gerakan. Alam punya aturan sederhana: energi tidak "
  "diciptakan dan tidak dimusnahkan, hanya berubah bentuk. Yang benar-benar habis adalah kesempatannya "
  "untuk kita pakai lagi. Sekali terbakar, ia tak bisa kembali menjadi bensin."),

 (6, "kelangkaan", "Bayang-bayang kelangkaan",
  "Dan di sinilah masalahnya. Minyak bumi butuh jutaan tahun untuk terbentuk, sementara kita "
  "menghabiskannya setiap detik. Jumlahnya terbatas, sementara pemakainya terus bertambah. Kelangkaan "
  "bukan lagi kemungkinan, ia sudah mulai terjadi. Dulu Indonesia dikenal sebagai pengekspor minyak. "
  "Kini, kita justru mengimpor bensin dan solar untuk memenuhi kebutuhan sehari-hari. Semakin cepat "
  "kita menghabiskan, semakin cepat pula penggantinya dituntut ada."),

 (7, "solusi", "Kita harus bagaimana?",
  "Lalu kita harus bagaimana? Mulailah dari yang kecil, hari ini. Berjalan kaki atau bersepeda untuk "
  "jarak dekat. Menggabungkan perjalanan. Menggunakan transportasi umum, agar satu bus menggantikan "
  "puluhan mobil. Merawat kendaraan agar tidak boros. Lalu, beranilah beralih: kendaraan listrik, "
  "dan listrik dari matahari, air, dan angin. Dukung bahan bakar nabati yang bisa ditanam ulang. "
  "Dan secara bersama, bangun transportasi umum yang layak serta pembangkit energi terbarukan. "
  "Karena satu bus, satu panel surya, satu kebiasaan kecil, jika dilakukan jutaan orang, akan "
  "mengubah arah cerita ini."),

 (8, "penutup", "Penutup",
  "Bensin adalah warisan jutaan tahun yang kita habiskan dalam sekejap. Ia tidak hilang, ia berubah, "
  "dan berkurang. Maka pilihan kita sederhana: hemat yang ada, siapkan yang baru, dan jangan "
  "bergantung pada satu sumber saja. Sebab cerita tentang bensin bukan hanya tentang mesin. "
  "Ia tentang seberapa bijak kita mengelola masa depan."),
]

def durasi(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", path],
        stdout=subprocess.PIPE, stderr=subprocess.DEVNULL).stdout.decode().strip()
    try:
        return float(out)
    except ValueError:
        return 0.0

hasil = []
for num, slug, judul, teks in BAB:
    txt = os.path.join(NASKA, f"bab{num}.txt")
    with open(txt, "w", encoding="utf-8") as f:
        f.write(teks)
    mp3 = os.path.join(ROOT, f"bab{num}-{slug}.mp3")
    cmd = ["edge-tts", "--voice", VOICE, "--rate", RATE,
           "--file", txt, "--write-media", mp3]
    r = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    d = durasi(mp3) if os.path.exists(mp3) else 0.0
    status = "OK" if d > 0 else "GAGAL"
    print(f"[bab {num}] {judul:42s} {d:6.2f}s  {status}", flush=True)
    hasil.append({"bab": num, "slug": slug, "judul": judul,
                  "file": os.path.basename(mp3), "durasi_detik": round(d, 3)})

total = sum(h["durasi_detik"] for h in hasil)
with open(os.path.join(ROOT, "durations.json"), "w", encoding="utf-8") as f:
    json.dump({"voice": VOICE, "rate": RATE, "total_detik": round(total, 3),
               "total_menit": round(total / 60, 2), "bab": hasil},
              f, ensure_ascii=False, indent=2)
print(f"\nTOTAL VO: {total:.2f}s ({total/60:.2f} menit)")
print(f"durasi tercatat di: {os.path.join(ROOT, 'durations.json')}")
