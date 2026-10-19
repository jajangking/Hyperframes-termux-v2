"""Bab 4 "Keluar dari bumi" — LIVE-DRAW reels Setetes Bensin (9:16).

Empat gambar besar di satu lembar:
  01  Terperangkap di pori-pori batuan, seperti spons        (kata 0–19)
  02  Dibor, dipompa naik, didorong tekanan bumi             (kata 20–39)
  03  Merembes sendiri — sumur tradisional turun-temurun     (kata 40–51)
  04  Sumur bor raksasa + jaringan pipa sepanjang benua      (kata 52–67)

Kamera diam saat gambar digambar, lalu geser pelan ke gambar berikutnya.
Koordinat gambar relatif X (titik tengah slide) — kamera memusatkan X.
"""

SCENE = {
    "id": "bab4",
    "hook": "Di mana bumi menyimpan bensin, dan bagaimana kita mengeluarkannya?",
    "hud_left": ("BAB 04", "KELUAR DARI BUMI"),
    "hud_right": "SETETES BENSIN<br>LIVE-DRAW · 9:16",
    "naskah": "naskah/bab4.txt",          # relatif terhadap path vo
    "vo_raw": "bab4-keluar-dari-bumi.mp3",
    "lead": 1.8,
    "jeda": 1.8,
    "spacing": 1600,
}

# batas slide = titik jeda + pergeseran kamera (kata inklusif)
SLIDES = [
    {"words": (0, 19)},
    {"words": (20, 39), "preshow": "v2"},
    {"words": (40, 51), "preshow": "v3"},
    {"words": (52, 67), "preshow": "v4"},
]

CUES = [
    (0, "#v1Frame", 1.0, "d"), (0, "#v1No", 0.6, "t"), (0, "#v1Title", 0.8, "t"),
    (2, "#v1Surface", 1.0, "d"), (2, "#v1Grass", 0.6, "d"), (2, "#v1SurfL", 0.5, "t"),
    (4, "#v1DepthA", 0.9, "d"), (4, "#v1DepthL1", 0.5, "t"), (4, "#v1DepthL2", 0.5, "t"),
    (7, "#v1Rock", 1.2, "d"),
    (9, "#v1Pores .d", 1.1, "d"),
    (11, "#v1Drops .d", 1.0, "d"), (11, "#v1RockL", 0.5, "t"),
    (13, "#v1Sponge", 0.9, "d"),
    (15, "#v1SpongeHoles .d", 0.8, "d"), (15, "#v1SpongeDrip", 0.5, "d"), (15, "#v1SpongeL", 0.5, "t"),
    (17, "#v1Ground", 0.9, "d"), (17, "#v1Hatch", 1.0, "d"),
    (18, "#v1TrappedL", 0.6, "t"),
    (19, "#conn1", 1.0, "d"),

    (20, "#v2Title", 0.8, "t"),
    (22, "#v2Derrick", 1.3, "d"), (22, "#v2DerrickL", 0.5, "t"),
    (24, "#v2Ground", 0.9, "d"), (24, "#v2Hatch", 1.0, "d"),
    (25, "#v2Strata .d", 0.9, "d"),
    (27, "#v2Pipe", 0.8, "d"), (27, "#v2PipeL", 0.5, "t"),
    (29, "#v2Tank", 0.8, "d"), (29, "#v2TankPipe", 0.6, "d"), (29, "#v2TankL", 0.5, "t"),
    (31, "#v2Flow1", 0.5, "f"), (31, "#v2Flow2", 0.5, "f"), (31, "#v2PumpL", 0.5, "t"),
    (33, "#v2Pressure .d", 1.0, "d"), (33, "#v2PressL", 0.5, "t"),
    (36, "#conn2", 1.0, "d"),

    (40, "#v3Title", 0.7, "t"),
    (41, "#v3Crack", 0.9, "d"),
    (42, "#v3Seep", 0.5, "f"), (42, "#v3Puddle", 0.6, "d"), (42, "#v3SmallL", 0.5, "t"),
    (44, "#v3ArrowL", 0.5, "f"),
    (45, "#v3WellRim", 0.7, "d"),
    (46, "#v3Posts .d", 0.7, "d"),
    (47, "#v3Rope", 0.4, "d"), (47, "#v3Bucket", 0.6, "d"),
    (48, "#v3WellL", 0.5, "t"),
    (49, "#v3HeritageL1", 0.4, "t"), (49, "#v3HeritageL2", 0.4, "t"),
    (50, "#v3DeepL", 0.5, "t"),
    (51, "#conn3", 0.8, "d"),

    (52, "#v4Title", 0.7, "t"),
    (53, "#v4Ground", 0.9, "d"), (53, "#v4Hatch", 1.0, "d"),
    (54, "#v4Derrick", 1.3, "d"), (54, "#v4DerrickL", 0.5, "t"),
    (56, "#v4Wellhead", 0.6, "d"),
    (58, "#v4Pipe", 1.2, "d"),
    (60, "#v4Joints .d", 0.6, "d"),
    (61, "#v4SmallWells .d", 1.0, "d"), (61, "#v4NetL", 0.5, "t"),
    (63, "#v4ArrowRight", 0.4, "f"),
    (64, "#v4SpanL1", 0.5, "t"), (64, "#v4SpanL2", 0.5, "t"),
]

CAPTIONS = [
    (0, 5, "MINYAK BUMI TERPERANGKAP DI PORI-PORI BATUAN"),
    (6, 12, "RATUSAN HINGGA RIBUAN METER DI BAWAH KITA"),
    (13, 17, "SEPERTI AIR DI DALAM SPONS"),
    (18, 21, "UNTUK MENGELUARKANNYA MANUSIA MENGEBOR"),
    (22, 31, "BATUAN DITEMBUS — MINYAK DIPOMPA NAIK KE PERMUKAAN"),
    (32, 36, "DIDORONG TEKANAN DARI DALAM BUMI"),
    (37, 39, "DI BEBERAPA TEMPAT,"),
    (40, 45, "MINYAK BAHKAN MEREMBES SENDIRI KE PERMUKAAN"),
    (46, 51, "SEPERTI SUMUR TRADISIONAL YANG DIWARISKAN TURUN-TEMURUN"),
    (52, 54, "NAMUN JUMLAHNYA KECIL"),
    (55, 62, "YANG MEMENUHI KEBUTUHAN DUNIA ADALAH SUMUR BOR RAKSASA"),
    (63, 67, "DAN JARINGAN PIPA SEPANJANG BENUA"),
]

# kata -> [(suara, gain dB, geser detik), ...]
# catatan: suara goresan pensil ("line") sengaja TIDAK dipakai (terdengar spspspsp)
SFXMAP = {
    0:  [("paper", -8, 0.00)],
    2:  [("tick", -14, 0.20)],
    4:  [("tick", -14, 0.30)],
    7:  [("deep", -12, 0.00)],
    9:  [("tick", -13, 0.20)],
    11: [("tick", -14, 0.30)],
    13: [("tick", -13, 0.25)],
    15: [("puff", -12, 0.00)],
    17: [("tick", -14, 0.30)],
    19: [("tick", -13, 0.50)],
    20: [("tick", -13, 0.20)],
    22: [("deep", -11, 0.00)],
    24: [("tick", -14, 0.35)],
    25: [("tick", -14, 0.30)],
    27: [("tick", -13, 0.25)],
    29: [("tick", -14, 0.30)],
    31: [("pump", -12, 0.00)],
    33: [("puff", -11, 0.05)],
    36: [("tick", -13, 0.50)],
    40: [("tick", -13, 0.25)],
    41: [("tick", -14, 0.30)],
    42: [("puff", -12, 0.00)],
    44: [("tick", -14, 0.30)],
    45: [("tick", -13, 0.25)],
    46: [("tick", -14, 0.30)],
    47: [("tick", -14, 0.20)],
    49: [("tick", -14, 0.35)],
    51: [("tick", -13, 0.50)],
    52: [("tick", -13, 0.25)],
    54: [("deep", -11, 0.00)],
    56: [("tick", -14, 0.30)],
    58: [("tick", -13, 0.25)],
    60: [("tick", -14, 0.30)],
    61: [("pump", -12, 0.00)],
    63: [("tick", -14, 0.35)],
    64: [("chime", -11, 0.00)],
}


# ==========================================  GAMBAR 1 · TERPERANGKAP DI BATUAN
def g1(X, A):
    txt, frame, drop, hatch = A.txt, A.frame, A.drop, A.hatch
    FW, FY = A.FW, A.FY
    return f'''        {frame("v1Frame", X)}
        {txt("v1No", X-FW//2+22, FY+52, "01", 30, "#7ef0ff", weight="700")}
        {txt("v1Title", X, 1495, "DI DALAM BATUAN", 48, "#eaf6ff", anchor="middle", weight="700")}
        <line id="v1Surface" class="d" x1="{X-400}" y1="1640" x2="{X+400}" y2="1640" stroke="#e6f4ff" stroke-width="10"/>
        <path id="v1Grass" class="d" d="M{X-320},1640 l0,-22 M{X-240},1640 l0,-22 M{X-160},1640 l0,-22 M{X+180},1640 l0,-22 M{X+260},1640 l0,-22" fill="none" stroke="#a9d8ff" stroke-width="5"/>
        {txt("v1SurfL", X+320, 1622, "PERMUKAAN", 22, "#cfe9ff")}
        <path id="v1DepthA" class="d" d="M{X-350},1680 V1980 M{X-362},1700 l12,-20 l12,20 M{X-362},1960 l12,20 l12,-20" fill="none" stroke="#7ef0ff" stroke-width="8"/>
        {txt("v1DepthL1", X-330, 1790, "RATUSAN HINGGA", 24, "#cfe9ff")}
        {txt("v1DepthL2", X-330, 1826, "RIBUAN METER", 24, "#cfe9ff")}
        <rect id="v1Rock" class="d" x="{X-260}" y="1880" width="330" height="330" rx="34"
              fill="none" stroke="#e6f4ff" stroke-width="12"/>
        <g id="v1Pores">
          <circle class="d" cx="{X-190}" cy="1950" r="26" fill="none" stroke="#a9d8ff" stroke-width="6"/>
          <circle class="d" cx="{X-90}" cy="1935" r="22" fill="none" stroke="#a9d8ff" stroke-width="6"/>
          <circle class="d" cx="{X-140}" cy="2050" r="24" fill="none" stroke="#a9d8ff" stroke-width="6"/>
          <circle class="d" cx="{X-30}" cy="2035" r="26" fill="none" stroke="#a9d8ff" stroke-width="6"/>
          <circle class="d" cx="{X-175}" cy="2145" r="22" fill="none" stroke="#a9d8ff" stroke-width="6"/>
          <circle class="d" cx="{X-70}" cy="2140" r="24" fill="none" stroke="#a9d8ff" stroke-width="6"/>
        </g>
        <g id="v1Drops">
          <path class="d" d="{drop(X-190, 1938, 0.24)}" fill="none" stroke="#7ef0ff" stroke-width="5"/>
          <path class="d" d="{drop(X-140, 2038, 0.22)}" fill="none" stroke="#7ef0ff" stroke-width="5"/>
          <path class="d" d="{drop(X-30, 2022, 0.24)}" fill="none" stroke="#7ef0ff" stroke-width="5"/>
          <path class="d" d="{drop(X-70, 2126, 0.22)}" fill="none" stroke="#7ef0ff" stroke-width="5"/>
        </g>
        {txt("v1RockL", X-95, 2258, "PORI-PORI BATUAN", 26, "#eaf6ff", anchor="middle", weight="700")}
        <rect id="v1Sponge" class="d" x="{X+120}" y="1920" width="210" height="170" rx="20"
              fill="none" stroke="#e6f4ff" stroke-width="10"/>
        <g id="v1SpongeHoles">
          <circle class="d" cx="{X+170}" cy="1965" r="17" fill="none" stroke="#a9d8ff" stroke-width="5"/>
          <circle class="d" cx="{X+230}" cy="1995" r="14" fill="none" stroke="#a9d8ff" stroke-width="5"/>
          <circle class="d" cx="{X+282}" cy="1960" r="12" fill="none" stroke="#a9d8ff" stroke-width="5"/>
          <circle class="d" cx="{X+185}" cy="2045" r="13" fill="none" stroke="#a9d8ff" stroke-width="5"/>
          <circle class="d" cx="{X+262}" cy="2048" r="16" fill="none" stroke="#a9d8ff" stroke-width="5"/>
        </g>
        <path id="v1SpongeDrip" class="d" d="{drop(X+225, 2115, 0.42)}" fill="none" stroke="#7ef0ff" stroke-width="7"/>
        {txt("v1SpongeL", X+225, 2200, "SEPERTI SPONS", 26, "#cfe9ff", anchor="middle")}
        {txt("v1TrappedL", X, 2300, "AIR + MINYAK TERPERANGKAP", 26, "#7ef0ff", anchor="middle", weight="700")}
        <line id="v1Ground" class="d" x1="{X-400}" y1="2330" x2="{X+400}" y2="2330" stroke="#e6f4ff" stroke-width="12"/>
        <path id="v1Hatch" class="d" d="{hatch(X-400, X+390, 2330)}" fill="none" stroke="#a9d8ff" stroke-width="4"/>'''


# ================================================  GAMBAR 2 · DIBOR & DIPOMPA
def g2(X, A):
    txt, frame, hatch, derrick = A.txt, A.frame, A.hatch, A.derrick
    FW, FY = A.FW, A.FY
    return f'''        {frame("v2Frame", X)}
        {txt("v2No", X-FW//2+22, FY+52, "02", 30, "#7ef0ff", weight="700")}
        {txt("v2Title", X, 1495, "MENGEBOR & MENGANGKUT", 38, "#eaf6ff", anchor="middle", weight="700")}
        <path id="v2Derrick" class="d" d="{derrick(X-160, 1660, 1980)}" fill="none" stroke="#e6f4ff" stroke-width="10"/>
        {txt("v2DerrickL", X-160, 1628, "MENARA BOR", 24, "#cfe9ff", anchor="middle")}
        <g id="v2Strata">
          <path class="d" d="M{X-400},2060 H{X+400}" fill="none" stroke="#a9d8ff" stroke-width="9"/>
          <path class="d" d="M{X-400},2130 H{X+400}" fill="none" stroke="#a9d8ff" stroke-width="9"/>
        </g>
        <path id="v2Pipe" class="d" d="M{X-160},1980 V2200" fill="none" stroke="#e6f4ff" stroke-width="13"/>
        {txt("v2PipeL", X-140, 2035, "BATUAN DITEMBUS", 22, "#cfe9ff")}
        <rect id="v2Tank" class="d" x="{X+140}" y="1900" width="180" height="140" rx="14"
              fill="none" stroke="#e6f4ff" stroke-width="11"/>
        <path id="v2TankPipe" class="d" d="M{X-160},1940 H{X+140}" fill="none" stroke="#7ef0ff" stroke-width="10"/>
        {txt("v2TankL", X+230, 2075, "KE PERMUKAAN", 22, "#cfe9ff", anchor="middle")}
        <path id="v2Flow1" class="f" d="M{X-230},2170 V2010" fill="none" stroke="#7ef0ff" stroke-width="12" marker-end="url(#arc)"/>
        <path id="v2Flow2" class="f" d="M{X-90},2170 V2010" fill="none" stroke="#7ef0ff" stroke-width="12" marker-end="url(#arc)"/>
        {txt("v2PumpL", X-160, 2215, "DIPOMPA NAIK", 26, "#7ef0ff", anchor="middle", weight="700")}
        <g id="v2Pressure">
          <path class="d" d="M{X+150},2330 c-22,-52 22,-78 0,-130" fill="none" stroke="#7ef0ff" stroke-width="8"/>
          <path class="d" d="M{X+260},2330 c-22,-52 22,-78 0,-130" fill="none" stroke="#7ef0ff" stroke-width="8"/>
        </g>
        {txt("v2PressL", X+205, 2380, "TEKANAN DARI DALAM BUMI", 22, "#cfe9ff", anchor="middle")}
        <line id="v2Ground" class="d" x1="{X-400}" y1="2330" x2="{X+140}" y2="2330" stroke="#e6f4ff" stroke-width="12"/>
        <path id="v2Hatch" class="d" d="{hatch(X-400, X+130, 2330)}" fill="none" stroke="#a9d8ff" stroke-width="4"/>'''


# =============================================  GAMBAR 3 · MEREMBES SENDIRI
def g3(X, A):
    txt, frame, hatch = A.txt, A.frame, A.hatch
    FW, FY = A.FW, A.FY
    return f'''        {frame("v3Frame", X)}
        {txt("v3No", X-FW//2+22, FY+52, "03", 30, "#7ef0ff", weight="700")}
        {txt("v3Title", X, 1495, "MEREMBES SENDIRI", 44, "#eaf6ff", anchor="middle", weight="700")}
        <line id="v3Ground" class="d" x1="{X-400}" y1="1980" x2="{X+400}" y2="1980" stroke="#e6f4ff" stroke-width="12"/>
        <path id="v3Hatch" class="d" d="{hatch(X-400, X+390, 1980)}" fill="none" stroke="#a9d8ff" stroke-width="4"/>
        <path id="v3Crack" class="d" d="M{X-260},2200 l30,-60 l-14,-52 l34,-58 l18,-50" fill="none" stroke="#a9d8ff" stroke-width="8"/>
        <path id="v3Seep" class="f" d="M{X-210},1960 V1890" fill="none" stroke="#7ef0ff" stroke-width="12" marker-end="url(#arc)"/>
        <ellipse id="v3Puddle" class="d" cx="{X-210}" cy="1958" rx="86" ry="17"
                 fill="none" stroke="#7ef0ff" stroke-width="8"/>
        {txt("v3SmallL", X-210, 1856, "SEDIKIT SEKALI", 24, "#cfe9ff", anchor="middle")}
        <ellipse id="v3WellRim" class="d" cx="{X+170}" cy="1955" rx="88" ry="26"
                 fill="none" stroke="#e6f4ff" stroke-width="10"/>
        <g id="v3Posts">
          <line class="d" x1="{X+95}" y1="1950" x2="{X+95}" y2="1780" stroke="#e6f4ff" stroke-width="9"/>
          <line class="d" x1="{X+245}" y1="1950" x2="{X+245}" y2="1780" stroke="#e6f4ff" stroke-width="9"/>
          <line class="d" x1="{X+80}" y1="1780" x2="{X+260}" y2="1780" stroke="#e6f4ff" stroke-width="9"/>
        </g>
        <path id="v3Rope" class="d" d="M{X+170},1785 V1865" fill="none" stroke="#a9d8ff" stroke-width="6"/>
        <path id="v3Bucket" class="d" d="M{X+138},1865 h64 l-10,64 h-44 z" fill="none" stroke="#e6f4ff" stroke-width="8"/>
        {txt("v3WellL", X+170, 2070, "SUMUR TRADISIONAL", 24, "#eaf6ff", anchor="middle", weight="700")}
        {txt("v3HeritageL1", X+170, 2112, "DIWARISKAN", 22, "#cfe9ff", anchor="middle")}
        {txt("v3HeritageL2", X+170, 2144, "TURUN-TEMURUN", 22, "#cfe9ff", anchor="middle")}
        <path id="v3ArrowL" class="f" d="M{X-120},1900 H{X+55}" fill="none" stroke="#a9d8ff" stroke-width="8" marker-end="url(#arc)"/>
        {txt("v3DeepL", X-260, 2260, "REMBESAN ALAMI DARI BAWAH TANAH", 22, "#cfe9ff")}'''


# ==========================================  GAMBAR 4 · SUMUR BOR RAKSASA
def g4(X, A):
    txt, frame, hatch, derrick = A.txt, A.frame, A.hatch, A.derrick
    FW, FY = A.FW, A.FY
    return f'''        {frame("v4Frame", X)}
        {txt("v4No", X-FW//2+22, FY+52, "04", 30, "#7ef0ff", weight="700")}
        {txt("v4Title", X, 1495, "SKALA DUNIA", 52, "#eaf6ff", anchor="middle", weight="700")}
        <path id="v4Derrick" class="d" d="{derrick(X-320, 1620, 1960, 130)}" fill="none" stroke="#e6f4ff" stroke-width="11"/>
        {txt("v4DerrickL", X-320, 1588, "BOR RAKSASA", 24, "#7ef0ff", anchor="middle", weight="700")}
        <path id="v4Wellhead" class="d" d="M{X-350},1960 h60 v-40 h-20 v-24 h-20 v24 h-20 z" fill="none" stroke="#e6f4ff" stroke-width="8"/>
        <path id="v4Pipe" class="d" d="M{X-320},2120 H{X+380}" fill="none" stroke="#e6f4ff" stroke-width="14"/>
        <g id="v4Joints">
          <path class="d" d="M{X-180},2100 v40 M{X+40},2100 v40 M{X+260},2100 v40" fill="none" stroke="#a9d8ff" stroke-width="7"/>
        </g>
        <g id="v4SmallWells">
          <path class="d" d="M{X-180},2120 v-80 l26,-46 l26,46 v80" fill="none" stroke="#a9d8ff" stroke-width="8"/>
          <path class="d" d="M{X+40},2120 v-80 l26,-46 l26,46 v80" fill="none" stroke="#a9d8ff" stroke-width="8"/>
          <path class="d" d="M{X+260},2120 v-80 l26,-46 l26,46 v80" fill="none" stroke="#a9d8ff" stroke-width="8"/>
        </g>
        {txt("v4NetL", X+40, 1980, "BANYAK SUMUR TERHUBUNG", 24, "#cfe9ff", anchor="middle")}
        <path id="v4ArrowRight" class="f" d="M{X+380},2120 H{X+400}" fill="none" stroke="#7ef0ff" stroke-width="14" marker-end="url(#arc)"/>
        {txt("v4SpanL1", X, 2230, "JARINGAN PIPA", 28, "#7ef0ff", anchor="middle", weight="700")}
        {txt("v4SpanL2", X, 2272, "SEPANJANG BENUA", 28, "#7ef0ff", anchor="middle", weight="700")}
        <line id="v4Ground" class="d" x1="{X-400}" y1="2350" x2="{X+400}" y2="2350" stroke="#e6f4ff" stroke-width="12"/>
        <path id="v4Hatch" class="d" d="{hatch(X-400, X+390, 2350)}" fill="none" stroke="#a9d8ff" stroke-width="4"/>'''


DRAW = [g1, g2, g3, g4]

# pra-gambar VERBATIM dari generator lama — frame + no + ground/hatch
# (offset presisi di dalam jeda; jangan diganti turunan otomatis)
PRESHOW = [
    (20, 0.15, '#v2Frame', 0.55, 'd'),
    (20, 0.4, '#v2No', 0.4, 't'),
    (40, 0.15, '#v3Frame', 0.55, 'd'),
    (40, 0.4, '#v3No', 0.4, 't'),
    (52, 0.15, '#v4Frame', 0.55, 'd'),
    (52, 0.4, '#v4No', 0.4, 't'),
]
