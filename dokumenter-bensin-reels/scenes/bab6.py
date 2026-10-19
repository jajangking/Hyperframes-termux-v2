"""Scene: bab6 — KELANGKAAN.

Isi bagian bertanda TODO. Alur:
  python3 -m pensil timing scenes/bab6.py
  python3 -m pensil align  scenes/bab6.py     (jeda jatuh di senyap alami)
  python3 -m pensil gen    scenes/bab6.py
  python3 -m pensil verify scenes/bab6.py
"""

SCENE = {
    "id": "bab6",
    "hud_left": ("BAB6", "KELANGKAAN"),     # kiri atas; None = tanpa HUD
    "hud_right": "",                      # kanan atas (HTML boleh); "" = kosong
    "naskah": "bab6.txt",               # di path vo
    "vo_raw": "bab6.mp3",               # VO mentah di path vo
    "lead": 1.8,                          # senyap awal (kartu pembuka)
    "jeda": 1.8,                          # jeda per batas slide
    "spacing": 1600,                      # jarak antar gambar (px)
}

# TODO: rentang kata per slide (indeks kata di words-*.json, inklusif).
# Batas slide otomatis jadi titik jeda + pergeseran kamera.
SLIDES = [
    {"words": (0, 9)},
    {"words": (10, -1), "preshow": "v2"},   # v2 = pra-gambar frame+no slide 2
]

# TODO: isyarat gambar (kata, selector, durasi, "d"=gores "t"=teks "f"=sekali jadi)
CUES = [
    (0, "#v1Frame", 1.0, "d"),
    (0, "#v1No", 0.6, "t"),
]

# TODO: caption (kata_awal, kata_akhir, teks); kata_akhir -1 = sampai akhir
CAPTIONS = [
    (0, -1, "TEKS CAPTION PERTAMA"),
]

# TODO: peta suara: kata → [(nama_suara, gain_dB, offset_detik)]
# suara tersedia: paper tick whoosh coin pump rev rumble deep zap puff sting chime boom
SFXMAP = {
    0: [("paper", -8, 0.0)],
}


def g1(X, A):
    """GAMBAR 1 — TODO ganti dengan gambar slide 1 (koordinat relatif X)."""
    return f'''        {A.frame("v1Frame", X)}
        {A.txt("v1No", X - A.FW // 2 + 22, A.FY + 52, "01", 30, A.accent, weight="700")}
        {A.txt("v1Title", X, A.FY + 95, "JUDUL GAMBAR", 44, A.text2, anchor="middle", weight="700")}
        <line id="v1Ground" class="d" x1="{X - 400}" y1="2330" x2="{X + 400}" y2="2330"
              stroke="{A.ink}" stroke-width="12"/>'''


# TODO: tambah g2, g3, ... lalu daftarkan di sini (urut = urut slide)
DRAW = [g1]
