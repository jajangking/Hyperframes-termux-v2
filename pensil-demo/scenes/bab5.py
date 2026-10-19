"""Scene demo: Bab 5 "Terbakar" — reproduksi Bab 5 dokumenter-bensin
lewat framework pensil (VO & naskah asli dipakai baca-saja).

Lima gambar besar di satu lembar:
  01  Di dalam mesin bensin dibakar — tapi tidak hilang, ia berubah   (kata 0–11)
  02  Bertemu oksigen → karbon dioksida + uap air = asap knalpot      (kata 12–29)
  03  Energi berubah jadi panas dan gerakan                          (kata 30–39)
  04  Aturan alam: energi tidak diciptakan/dimusnahkan               (kata 40–48)
  05  Yang habis kesempatannya — sekali terbakar tak bisa kembali    (kata 49–65)

Koordinat gambar relatif X (titik tengah slide) — kamera memusatkan X.
"""

SCENE = {
    "id": "bab5t",
    "hud_left": ("BAB 05", "TERBAKAR"),
    "hud_right": "SETETES BENSIN<br>LIVE-DRAW · 9:16",
    "naskah": "naskah/bab5.txt",          # relatif terhadap path vo
    "vo_raw": "bab5-terbakar.mp3",
    "lead": 1.8,
    "jeda": 1.8,
    "spacing": 1600,
}

# batas slide = titik jeda + pergeseran kamera (kata inklusif)
SLIDES = [
    {"words": (0, 11)},
    {"words": (12, 29), "preshow": "v2"},
    {"words": (30, 39), "preshow": "v3"},
    {"words": (40, 48), "preshow": "v4"},
    {"words": (49, 65), "preshow": "v5"},
]

CUES = [
    (0, "#v1Frame", 1.0, "d"), (0, "#v1No", 0.6, "t"), (0, "#v1Title", 0.8, "t"),
    (2, "#v1Cyl", 1.0, "d"), (2, "#v1Piston", 0.8, "d"), (2, "#v1Rod", 0.5, "d"),
    (2, "#v1CylL", 0.4, "t"),
    (4, "#v1Fuel", 0.6, "d"), (4, "#v1FuelL", 0.4, "t"), (4, "#v1Inj", 0.4, "f"),
    (5, "#v1Spark", 0.9, "d"), (5, "#v1SparkL", 0.5, "t"),
    (7, "#v1Ground", 0.8, "d"), (7, "#v1Hatch", 0.9, "d"),
    (8, "#v1Arrow1", 0.5, "f"), (8, "#v1NotL1", 0.4, "t"), (8, "#v1NotL2", 0.4, "t"),
    (10, "#conn1", 1.0, "d"),

    (12, "#v2Frame", 0.9, "d"), (12, "#v2No", 0.5, "t"), (12, "#v2Title", 0.8, "t"),
    (13, "#v2Ground", 0.8, "d"), (13, "#v2Hatch", 0.9, "d"),
    (14, "#v2Fuel", 0.7, "d"), (14, "#v2FuelL", 0.4, "t"),
    (15, "#v2O2a", 0.5, "d"), (15, "#v2O2b", 0.5, "d"), (15, "#v2O2L", 0.4, "t"),
    (17, "#v2Arrow1", 0.5, "f"),
    (18, "#v2CO2 .d", 0.9, "d"), (18, "#v2CO2L", 0.4, "t"),
    (20, "#v2H2O .d", 0.9, "d"), (20, "#v2H2OL", 0.4, "t"),
    (23, "#v2Arrow2", 0.5, "f"),
    (24, "#v2Exh", 0.9, "d"), (24, "#v2ExhL", 0.4, "t"),
    (26, "#v2Smoke", 1.0, "d"), (26, "#v2SmokeL", 0.5, "t"),
    (28, "#conn2", 1.0, "d"),

    (30, "#v3Frame", 0.9, "d"), (30, "#v3No", 0.5, "t"), (30, "#v3Title", 0.8, "t"),
    (31, "#v3Ground", 0.8, "d"), (31, "#v3Hatch", 0.9, "d"),
    (32, "#v3Wheel", 0.9, "d"), (32, "#v3Spokes .d", 0.7, "d"),
    (33, "#v3Spin", 0.5, "f"), (33, "#v3MoveL", 0.4, "t"),
    (35, "#v3HeatW .d", 1.0, "d"), (35, "#v3HeatL", 0.4, "t"),
    (37, "#v3FromL", 0.5, "f"), (37, "#v3EnL", 0.5, "t"),
    (38, "#conn3", 1.0, "d"),

    (40, "#v4Frame", 0.9, "d"), (40, "#v4No", 0.5, "t"), (40, "#v4Title", 0.8, "t"),
    (41, "#v4Ground", 0.8, "d"), (41, "#v4Hatch", 0.9, "d"),
    (42, "#v4Ring", 1.2, "d"), (42, "#v4EnL", 0.5, "t"),
    (44, "#v4Spin1", 0.5, "f"), (44, "#v4Spin2", 0.5, "f"),
    (45, "#v4InArrow", 0.5, "f"), (45, "#v4NoCreate", 0.5, "f"), (45, "#v4NoCreateL", 0.4, "t"),
    (46, "#v4OutArrow", 0.5, "f"), (46, "#v4NoDestroy", 0.5, "f"), (46, "#v4NoDestroyL", 0.4, "t"),
    (47, "#v4ShapeL", 0.6, "t"),
    (48, "#conn4", 1.0, "d"),

    (49, "#v5Frame", 0.9, "d"), (49, "#v5No", 0.5, "t"), (49, "#v5Title", 0.8, "t"),
    (51, "#v5Ground", 0.8, "d"), (51, "#v5Hatch", 0.9, "d"),
    (52, "#v5Fuel", 0.8, "d"), (52, "#v5FuelL", 0.4, "t"),
    (54, "#v5ArrowR", 0.5, "f"),
    (55, "#v5Flame", 1.0, "d"), (55, "#v5BurnL", 0.4, "t"),
    (56, "#v5GasL1", 0.7, "d"),
    (58, "#v5Back", 0.8, "f"),
    (60, "#v5Cross1", 0.4, "f"), (60, "#v5Cross2", 0.4, "f"), (60, "#v5NoBackL", 0.5, "t"),
    (62, "#v5GoneL1", 0.4, "t"), (62, "#v5GoneL2", 0.4, "t"), (62, "#v5GoneL3", 0.4, "t"),
]

CAPTIONS = [
    (0, 4, "DI DALAM MESIN, BENSIN DIBAKAR"),
    (5, 11, "TAPI IA TIDAK BENAR-BENAR HILANG — IA BERUBAH"),
    (12, 17, "BENSIN BERTEMU OKSIGEN, BERUBAH MENJADI"),
    (18, 22, "KARBON DIOKSIDA DAN UAP AIR"),
    (23, 28, "YANG KITA LIHAT SEBAGAI ASAP KNALPOT"),
    (30, 35, "ENERGINYA BERUBAH MENJADI PANAS DAN GERAKAN"),
    (36, 39, "ALAM PUNYA ATURAN SEDERHANA"),
    (40, 48, "ENERGI TIDAK DICIPTAKAN & TIDAK DIMUSNAHKAN, HANYA BERUBAH BENTUK"),
    (49, 57, "YANG BENAR-BENAR HABIS ADALAH KESEMPATANNYA DIPAKAI LAGI"),
    (58, 65, "SEKALI TERBAKAR, TAK BISA KEMBALI MENJADI BENSIN"),
]

SFXMAP = {
    0:  [("paper", -8, 0.00)],
    2:  [("tick", -14, 0.20)],
    4:  [("tick", -14, 0.25)],
    5:  [("boom", -13, 0.05)],
    7:  [("tick", -14, 0.30)],
    8:  [("tick", -13, 0.35)],
    10: [("tick", -13, 0.50)],
    12: [("tick", -13, 0.25)],
    14: [("tick", -13, 0.25)],
    15: [("tick", -14, 0.30)],
    17: [("tick", -14, 0.35)],
    18: [("tick", -14, 0.30)],
    20: [("tick", -14, 0.30)],
    23: [("tick", -14, 0.35)],
    24: [("deep", -12, 0.00)],
    26: [("puff", -11, 0.00)],
    28: [("tick", -13, 0.50)],
    30: [("tick", -13, 0.25)],
    32: [("deep", -12, 0.00)],
    33: [("tick", -14, 0.30)],
    35: [("puff", -11, 0.00)],
    37: [("tick", -13, 0.30)],
    38: [("tick", -13, 0.50)],
    40: [("tick", -13, 0.25)],
    42: [("deep", -12, 0.00)],
    44: [("tick", -14, 0.30)],
    45: [("zap", -12, 0.05)],
    46: [("zap", -12, 0.05)],
    47: [("chime", -12, 0.00)],
    48: [("tick", -13, 0.50)],
    49: [("tick", -13, 0.25)],
    52: [("tick", -13, 0.25)],
    54: [("tick", -14, 0.35)],
    55: [("boom", -13, 0.05)],
    56: [("puff", -12, 0.10)],
    58: [("tick", -13, 0.30)],
    60: [("zap", -12, 0.00)],
    62: [("tick", -13, 0.30)],
}


# ==============================================  GAMBAR 1 · TERBAKAR DI MESIN
def g1(X, A):
    txt, frame, drop, flame, hatch = A.txt, A.frame, A.drop, A.flame, A.hatch
    FW, FY = A.FW, A.FY
    return f'''        {frame("v1Frame", X)}
        {txt("v1No", X-FW//2+22, FY+52, "01", 30, "#7ef0ff", weight="700")}
        {txt("v1Title", X, 1495, "DI DALAM MESIN", 48, "#eaf6ff", anchor="middle", weight="700")}
        <rect id="v1Cyl" class="d" x="{X-200}" y="1640" width="400" height="380" rx="10"
              fill="none" stroke="#e6f4ff" stroke-width="13"/>
        <rect id="v1Piston" class="d" x="{X-170}" y="1860" width="340" height="110" rx="8"
              fill="none" stroke="#a9d8ff" stroke-width="10"/>
        <path id="v1Rod" class="d" d="M{X},1970 V2100" fill="none" stroke="#a9d8ff" stroke-width="12"/>
        {txt("v1CylL", X+230, 1720, "SILINDER", 22, "#cfe9ff")}
        <path id="v1Fuel" class="d" d="{drop(X-280, 1700, 0.55)}" fill="none" stroke="#7ef0ff" stroke-width="8"/>
        {txt("v1FuelL", X-280, 1668, "BENSIN", 24, "#7ef0ff", anchor="middle", weight="700")}
        <path id="v1Inj" class="f" d="M{X-210},1760 H{X-190}" fill="none" stroke="#7ef0ff" stroke-width="10" marker-end="url(#arc)"/>
        <path id="v1Spark" class="d" d="{flame(X, 1850, 0.95)}" fill="none" stroke="#e6f4ff" stroke-width="10"/>
        {txt("v1SparkL", X, 1705, "DIBAKAR", 26, "#eaf6ff", anchor="middle", weight="700")}
        <path id="v1Arrow1" class="f" d="M{X+220},2100 H{X+360}" fill="none" stroke="#7ef0ff" stroke-width="12" marker-end="url(#arc)"/>
        {txt("v1NotL1", X+230, 2170, "TIDAK HILANG,", 24, "#cfe9ff")}
        {txt("v1NotL2", X+230, 2206, "TAPI BERUBAH", 26, "#7ef0ff", weight="700")}
        <line id="v1Ground" class="d" x1="{X-400}" y1="2330" x2="{X+400}" y2="2330" stroke="#e6f4ff" stroke-width="12"/>
        <path id="v1Hatch" class="d" d="{hatch(X-400, X+390, 2330)}" fill="none" stroke="#a9d8ff" stroke-width="4"/>'''


# =============================================  GAMBAR 2 · REAKSI + KNALPOT
def g2(X, A):
    txt, drop, cloud, hatch = A.txt, A.drop, A.cloud, A.hatch
    FW, FY = A.FW, A.FY
    return f'''        {A.frame("v2Frame", X)}
        {txt("v2No", X-FW//2+22, FY+52, "02", 30, "#7ef0ff", weight="700")}
        {txt("v2Title", X, 1495, "BERUBAH JADI GAS", 44, "#eaf6ff", anchor="middle", weight="700")}
        <path id="v2Fuel" class="d" d="{drop(X-330, 1650, 0.62)}" fill="none" stroke="#e6f4ff" stroke-width="9"/>
        {txt("v2FuelL", X-330, 1620, "BENSIN", 22, "#cfe9ff", anchor="middle")}
        <circle id="v2O2a" class="d" cx="{X-240}" cy="1790" r="34" fill="none" stroke="#a9d8ff" stroke-width="8"/>
        <circle id="v2O2b" class="d" cx="{X-170}" cy="1790" r="34" fill="none" stroke="#a9d8ff" stroke-width="8"/>
        {txt("v2O2L", X-205, 1880, "OKSIGEN", 22, "#cfe9ff", anchor="middle")}
        <path id="v2Arrow1" class="f" d="M{X-140},1740 H{X-30}" fill="none" stroke="#7ef0ff" stroke-width="12" marker-end="url(#arc)"/>
        <g id="v2CO2">
          <circle class="d" cx="{X+60}" cy="1700" r="30" fill="none" stroke="#e6f4ff" stroke-width="8"/>
          <circle class="d" cx="{X+122}" cy="1672" r="20" fill="none" stroke="#a9d8ff" stroke-width="6"/>
          <circle class="d" cx="{X+122}" cy="1730" r="20" fill="none" stroke="#a9d8ff" stroke-width="6"/>
        </g>
        {txt("v2CO2L", X+90, 1790, "KARBON DIOKSIDA", 22, "#eaf6ff", anchor="middle")}
        <g id="v2H2O">
          <circle class="d" cx="{X+60}" cy="1900" r="26" fill="none" stroke="#e6f4ff" stroke-width="8"/>
          <circle class="d" cx="{X+115}" cy="1875" r="17" fill="none" stroke="#a9d8ff" stroke-width="6"/>
          <circle class="d" cx="{X+115}" cy="1928" r="17" fill="none" stroke="#a9d8ff" stroke-width="6"/>
        </g>
        {txt("v2H2OL", X+90, 1985, "UAP AIR", 22, "#eaf6ff", anchor="middle")}
        <path id="v2Arrow2" class="f" d="M{X+160},1800 H{X+240}" fill="none" stroke="#7ef0ff" stroke-width="12" marker-end="url(#arc)"/>
        <path id="v2Exh" class="d" d="M{X+300},2140 h80 v-200 h-80 l20,-40 h40 l20,40" fill="none" stroke="#e6f4ff" stroke-width="10"/>
        {txt("v2ExhL", X+340, 2200, "KNALPOT", 22, "#cfe9ff", anchor="middle")}
        <path id="v2Smoke" class="d" d="{cloud(X+330, 1780, 0.85)}" fill="none" stroke="#a9d8ff" stroke-width="8"/>
        {txt("v2SmokeL", X+330, 1690, "ASAP KNALPOT", 24, "#7ef0ff", anchor="middle", weight="700")}
        <line id="v2Ground" class="d" x1="{X-400}" y1="2330" x2="{X+400}" y2="2330" stroke="#e6f4ff" stroke-width="12"/>
        <path id="v2Hatch" class="d" d="{hatch(X-400, X+390, 2330)}" fill="none" stroke="#a9d8ff" stroke-width="4"/>'''


# ============================================  GAMBAR 3 · PANAS & GERAKAN
def g3(X, A):
    txt, hatch = A.txt, A.hatch
    FW, FY = A.FW, A.FY
    return f'''        {A.frame("v3Frame", X)}
        {txt("v3No", X-FW//2+22, FY+52, "03", 30, "#7ef0ff", weight="700")}
        {txt("v3Title", X, 1495, "PANAS & GERAKAN", 46, "#eaf6ff", anchor="middle", weight="700")}
        <circle id="v3Wheel" class="d" cx="{X-190}" cy="1820" r="150" fill="none" stroke="#e6f4ff" stroke-width="12"/>
        <g id="v3Spokes">
          <path class="d" d="M{X-190},1670 V1970 M{X-340},1820 H{X-40} M{X-296},1714 L{X-84},1926 M{X-84},1714 L{X-296},1926" fill="none" stroke="#a9d8ff" stroke-width="7"/>
        </g>
        <path id="v3Spin" class="f" d="M{X-30},1750 a170,170 0 0 1 -60,140" fill="none" stroke="#7ef0ff" stroke-width="12" marker-end="url(#arc)"/>
        {txt("v3MoveL", X-190, 2050, "GERAKAN", 28, "#7ef0ff", anchor="middle", weight="700")}
        <g id="v3HeatW">
          <path class="d" d="M{X+120},2100 c-24,-56 24,-84 0,-140" fill="none" stroke="#7ef0ff" stroke-width="8"/>
          <path class="d" d="M{X+220},2100 c-24,-56 24,-84 0,-140" fill="none" stroke="#7ef0ff" stroke-width="8"/>
          <path class="d" d="M{X+320},2100 c-24,-56 24,-84 0,-140" fill="none" stroke="#7ef0ff" stroke-width="8"/>
        </g>
        {txt("v3HeatL", X+220, 2150, "PANAS", 28, "#7ef0ff", anchor="middle", weight="700")}
        <path id="v3FromL" class="f" d="M{X-30},2260 H{X+330}" fill="none" stroke="#a9d8ff" stroke-width="10" marker-end="url(#arc)"/>
        {txt("v3EnL", X+150, 2300, "ENERGI BENSIN BERUBAH BENTUK", 24, "#cfe9ff", anchor="middle")}
        <line id="v3Ground" class="d" x1="{X-400}" y1="2350" x2="{X+400}" y2="2350" stroke="#e6f4ff" stroke-width="12"/>
        <path id="v3Hatch" class="d" d="{hatch(X-400, X+390, 2350)}" fill="none" stroke="#a9d8ff" stroke-width="4"/>'''


# ===============================================  GAMBAR 4 · ATURAN ALAM
def g4(X, A):
    txt, hatch = A.txt, A.hatch
    FW, FY = A.FW, A.FY
    return f'''        {A.frame("v4Frame", X)}
        {txt("v4No", X-FW//2+22, FY+52, "04", 30, "#7ef0ff", weight="700")}
        {txt("v4Title", X, 1495, "ATURAN ALAM", 52, "#eaf6ff", anchor="middle", weight="700")}
        <path id="v4Ring" class="d" d="M{X},1660 a220,220 0 1 1 -1,0" fill="none" stroke="#e6f4ff" stroke-width="13"/>
        {txt("v4EnL", X, 2000, "ENERGI", 40, "#7ef0ff", anchor="middle", weight="700")}
        <path id="v4Spin1" class="f" d="M{X+180},1730 a220,220 0 0 1 -70,180" fill="none" stroke="#7ef0ff" stroke-width="12" marker-end="url(#arc)"/>
        <path id="v4Spin2" class="f" d="M{X-180},1930 a220,220 0 0 1 70,-180" fill="none" stroke="#7ef0ff" stroke-width="12" marker-end="url(#arc)"/>
        <path id="v4InArrow" class="f" d="M{X-390},1880 H{X-240}" fill="none" stroke="#a9d8ff" stroke-width="11" marker-end="url(#arc)"/>
        <path id="v4NoCreate" class="f" d="M{X-370},1840 l40,80 M{X-330},1840 l-40,80" fill="none" stroke="#7ef0ff" stroke-width="10"/>
        {txt("v4NoCreateL", X-305, 1830, "TIDAK DICIPTAKAN", 22, "#cfe9ff")}
        <path id="v4OutArrow" class="f" d="M{X+240},1880 H{X+390}" fill="none" stroke="#a9d8ff" stroke-width="11" marker-end="url(#arc)"/>
        <path id="v4NoDestroy" class="f" d="M{X+280},1840 l40,80 M{X+320},1840 l-40,80" fill="none" stroke="#7ef0ff" stroke-width="10"/>
        {txt("v4NoDestroyL", X+315, 1830, "TIDAK DIMUSNAHKAN", 22, "#cfe9ff", anchor="middle")}
        {txt("v4ShapeL", X, 2240, "HANYA BERUBAH BENTUK", 30, "#7ef0ff", anchor="middle", weight="700")}
        <line id="v4Ground" class="d" x1="{X-400}" y1="2330" x2="{X+400}" y2="2330" stroke="#e6f4ff" stroke-width="12"/>
        <path id="v4Hatch" class="d" d="{hatch(X-400, X+390, 2330)}" fill="none" stroke="#a9d8ff" stroke-width="4"/>'''


# ===========================================  GAMBAR 5 · TAK BISA KEMBALI
def g5(X, A):
    txt, drop, flame, cloud, hatch = A.txt, A.drop, A.flame, A.cloud, A.hatch
    FW, FY = A.FW, A.FY
    return f'''        {A.frame("v5Frame", X)}
        {txt("v5No", X-FW//2+22, FY+52, "05", 30, "#7ef0ff", weight="700")}
        {txt("v5Title", X, 1495, "SEKALI TERBAKAR", 46, "#eaf6ff", anchor="middle", weight="700")}
        <path id="v5Fuel" class="d" d="{drop(X-300, 1680, 0.66)}" fill="none" stroke="#e6f4ff" stroke-width="10"/>
        {txt("v5FuelL", X-300, 1650, "BENSIN", 24, "#eaf6ff", anchor="middle", weight="700")}
        <path id="v5ArrowR" class="f" d="M{X-180},1830 H{X-40}" fill="none" stroke="#7ef0ff" stroke-width="12" marker-end="url(#arc)"/>
        <path id="v5Flame" class="d" d="{flame(X+80, 1850, 1.1)}" fill="none" stroke="#e6f4ff" stroke-width="11"/>
        {txt("v5BurnL", X+80, 1620, "TERBAKAR", 26, "#eaf6ff", anchor="middle", weight="700")}
        <path id="v5GasL1" class="d" d="{cloud(X+80, 1540, 0.55)}" fill="none" stroke="#a9d8ff" stroke-width="7"/>
        <path id="v5Back" class="f" d="M{X+40},2000 C{X-60},2120 {X-220},2120 {X-300},1960" fill="none" stroke="#a9d8ff" stroke-width="12" marker-end="url(#arc)"/>
        <path id="v5Cross1" class="f" d="M{X-250},1930 l90,150" fill="none" stroke="#7ef0ff" stroke-width="16"/>
        <path id="v5Cross2" class="f" d="M{X-160},1930 l-90,150" fill="none" stroke="#7ef0ff" stroke-width="16"/>
        {txt("v5NoBackL", X-205, 2150, "TAK BISA KEMBALI", 28, "#7ef0ff", anchor="middle", weight="700")}
        {txt("v5GoneL1", X+230, 2100, "YANG HABIS:", 24, "#cfe9ff")}
        {txt("v5GoneL2", X+230, 2136, "KESEMPATAN UNTUK", 24, "#cfe9ff")}
        {txt("v5GoneL3", X+230, 2172, "KITA PAKAI LAGI", 24, "#7ef0ff", weight="700")}
        <line id="v5Ground" class="d" x1="{X-400}" y1="2330" x2="{X+400}" y2="2330" stroke="#e6f4ff" stroke-width="12"/>
        <path id="v5Hatch" class="d" d="{hatch(X-400, X+390, 2330)}" fill="none" stroke="#a9d8ff" stroke-width="4"/>'''


DRAW = [g1, g2, g3, g4, g5]
