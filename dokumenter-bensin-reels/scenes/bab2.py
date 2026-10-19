"""Bab 2 "Apa itu bensin" — LIVE-DRAW reels Setetes Bensin (9:16).

Lima gambar besar di satu lembar:
  01  Bensin — bahan bakar cair dari minyak bumi + sifatnya   (kata 0–19)
  02  Di dalam mesin — bercampur udara, lalu dipadatkan       (kata 20–27)
  03  Percikan api dari busi membakarnya dalam sekejap        (kata 28–35)
  04  Ledakan mendorong piston → memutar poros → roda         (kata 36–47)
  05  Ringkasan — energi kimia berubah menjadi gerakan        (kata 48–53)

Koordinat gambar relatif X (titik tengah slide) — kamera memusatkan X.
Catatan pola lama bab2–4 yang dipertahankan: cue terakhir tiap slide (mis.
#conn1..#conn4) boleh menimpa awal pan berikutnya — dipertahankan apa adanya.
"""

SCENE = {
    "id": "bab2",
    "hook": "Kenapa bensin bisa menggerakkan mobil?",
    "hud_left": ("BAB 02", "APA ITU BENSIN"),
    "hud_right": "SETETES BENSIN<br>LIVE-DRAW · 9:16",
    "naskah": "naskah/bab2.txt",          # relatif terhadap path vo
    "vo_raw": "bab2-apa-itu-bensin.mp3",
    "lead": 1.8,
    "jeda": 1.8,
    "spacing": 1600,
    "conn_y": 2300,
}

# batas slide = titik jeda + pergeseran kamera (kata inklusif)
SLIDES = [
    {"words": (0, 19)},
    {"words": (20, 27), "preshow": "v2"},
    {"words": (28, 35), "preshow": "v3"},
    {"words": (36, 47), "preshow": "v4"},
    {"words": (48, 53), "preshow": "v5"},
]

CUES = [
    (0, "#v1Frame", 1.0, "d"), (0, "#v1No", 0.6, "t"), (0, "#v1Title", 0.8, "t"),
    (1, "#v1Sub", 0.7, "t"),
    (2, "#v1Can", 1.5, "d"),
    (3, "#v1Top .d", 1.3, "d"),
    (4, "#v1Liq .d", 1.3, "d"),
    (5, "#v1Ground", 1.0, "d"), (5, "#v1Hatch", 1.2, "d"),
    (6, "#v1Origin .d", 1.0, "d"), (6, "#v1Up", 0.6, "f"),
    (7, "#v1OriginL", 0.7, "t"),
    (10, "#v1Leader", 0.6, "d"),
    (11, "#v1Kuning", 0.7, "t"),
    (12, "#v1Encer .d", 1.1, "d"), (12, "#v1EncerL", 0.6, "t"),
    (13, "#v1Stink .d", 1.1, "d"),
    (14, "#v1Bau", 0.7, "t"),
    (15, "#v1EvapA1", 0.5, "f"),
    (16, "#v1EvapA2", 0.5, "f"), (16, "#v1EvapDots .d", 0.6, "d"),
    (17, "#v1EvapA3", 0.5, "f"), (17, "#v1EvapL", 0.6, "t"),
    (19, "#conn1", 1.4, "d"),

    (20, "#v2Title", 0.8, "t"),
    (21, "#v2Cyl .d", 1.1, "d"),
    (22, "#v2Head", 0.8, "d"), (22, "#v2Piston", 1.0, "d"), (22, "#v2Rings .d", 0.8, "d"),
    (23, "#v2Drops .d", 1.2, "d"), (23, "#v2FuelL", 0.6, "t"), (23, "#v2FuelLead", 0.5, "d"),
    (24, "#v2Swirl", 1.1, "d"),
    (25, "#v2AirL", 0.6, "t"), (25, "#v2AirLead", 0.5, "d"),
    (26, "#v2CompA1", 0.5, "f"), (26, "#v2CompA2", 0.5, "f"),
    (27, "#v2CompL", 0.7, "t"), (27, "#conn2", 1.4, "d"),

    (28, "#v3Title", 0.8, "t"), (28, "#v3Head", 0.9, "d"),
    (29, "#v3Cyl .d", 1.0, "d"), (29, "#v3Plug .d", 1.2, "d"),
    (30, "#v3Spark .d", 1.0, "d"),
    (32, "#v3Cable", 0.9, "d"), (32, "#v3PlugL", 0.6, "t"), (32, "#v3PlugLead", 0.4, "d"),
    (33, "#v3Blast1", 1.1, "d"),
    (34, "#v3Blast2", 1.2, "d"),
    (35, "#v3Piston", 0.9, "d"), (35, "#v3Rings .d", 0.7, "d"), (35, "#v3Shock .d", 0.7, "d"),
    (35, "#v3FastL", 0.6, "t"), (35, "#conn3", 1.4, "d"),

    (36, "#v4Blast", 1.0, "d"), (36, "#v4Title", 0.8, "t"),
    (38, "#v4Piston", 1.0, "d"), (38, "#v4Rings .d", 0.7, "d"),
    (39, "#v4PistonL", 0.6, "t"),
    (40, "#v4PushA1", 0.5, "f"), (40, "#v4PushA2", 0.5, "f"),
    (41, "#v4Rod .d", 1.0, "d"),
    (42, "#v4Crank .d", 1.3, "d"),
    (43, "#v4CrankRot", 0.9, "f"), (43, "#v4CrankL", 0.6, "t"),
    (44, "#v4Axle", 0.6, "d"),
    (45, "#v4Wheel .d", 1.4, "d"),
    (46, "#v4Spokes .d", 1.0, "d"), (46, "#v4WheelL", 0.6, "t"),
    (47, "#v4Speed .d", 0.9, "d"), (47, "#v4GerakL", 0.6, "t"), (47, "#conn4", 1.4, "d"),

    (48, "#v5Title", 0.7, "t"),
    (49, "#v5Drop", 1.4, "d"),
    (50, "#v5Zig", 0.9, "d"), (50, "#v5ChemL", 0.6, "t"),
    (51, "#v5Arrow", 0.6, "f"),
    (52, "#v5Wheel .d", 1.1, "d"),
    (53, "#v5Spokes .d", 0.8, "d"), (53, "#v5MoveL", 0.5, "t"), (53, "#v5Speed .d", 0.6, "d"),
]

CAPTIONS = [
    (0, 9, "BENSIN ADALAH BAHAN BAKAR CAIR DARI MINYAK BUMI"),
    (10, 12, "KEKUNINGAN · ENCER"),
    (13, 14, "BAUNYA MENYENGAT"),
    (15, 19, "DAN MENGUAP DENGAN CEPAT"),
    (20, 25, "DI DALAM MESIN, BENSIN BERCAMPUR UDARA"),
    (26, 27, "LALU DIPADATKAN"),
    (28, 32, "PERCIKAN API DARI BUSI MEMBAKARNYA"),
    (33, 35, "DALAM SEKEJAP"),
    (36, 41, "LEDAKAN KECIL ITULAH YANG MENDORONG PISTON"),
    (42, 47, "MEMUTAR POROS, MENGGERAKKAN RODA"),
    (48, 53, "ENERGI KIMIA BERUBAH MENJADI GERAKAN"),
]

SFXMAP = {
    0:  [("paper", -8, 0.00)],
    2:  [("tick", -14, 0.20)],
    4:  [("tick", -14, 0.15)],
    5:  [("tick", -14, 0.30)],
    7:  [("tick", -13, 0.30)],
    8:  [("deep", -11, 0.00)],
    9:  [("tick", -14, 0.00)],
    10: [("tick", -14, 0.25)],
    11: [("tick", -13, 0.35)],
    12: [("tick", -13, 0.20)],
    13: [("puff", -12, 0.10)],
    14: [("tick", -14, 0.45)],
    15: [("tick", -14, 0.20)],
    17: [("puff", -11, 0.00)],
    18: [("tick", -14, 0.30)],
    19: [("tick", -14, 0.10)],
    20: [("tick", -13, 0.30)],
    21: [("tick", -14, 0.30)],
    22: [("tick", -14, 0.40)],
    23: [("tick", -13, 0.25)],
    24: [("tick", -13, 0.30)],
    25: [("tick", -14, 0.30)],
    26: [("pump", -12, 0.00)],
    27: [("pump", -12, 0.20), ("tick", -13, 0.60)],
    28: [("tick", -13, 0.20)],
    29: [("tick", -14, 0.20)],
    30: [("zap", -11, 0.00)],
    32: [("tick", -13, 0.15)],
    33: [("boom", -13, 0.00)],
    34: [("boom", -13, 0.25)],
    35: [("tick", -13, 0.60)],
    36: [("boom", -12, 0.00)],
    37: [("tick", -14, 0.30)],
    38: [("tick", -14, 0.30)],
    39: [("tick", -14, 0.20)],
    40: [("tick", -14, 0.30)],
    41: [("boom", -14, 0.20)],
    42: [("rev", -13, 0.00)],
    43: [("tick", -13, 0.50)],
    44: [("tick", -14, 0.20)],
    45: [("tick", -14, 0.30)],
    46: [("rev", -13, 0.10)],
    47: [("tick", -13, 0.60)],
    48: [("tick", -13, 0.40)],
    49: [("chime", -12, 0.00)],
    51: [("tick", -14, 0.30)],
    52: [("tick", -14, 0.30)],
    53: [("chime", -13, 0.10)],
}


# ------------------------------------------------------------- helper lokal
def star(A, xc, yc, r1, r2, n=10):
    """bintang ledakan jagged"""
    import math
    pts = []
    for i in range(n * 2):
        r = r1 if i % 2 == 0 else r2
        a = math.pi * i / n - math.pi / 2
        pts.append(f"{xc + r * math.cos(a):.0f},{yc + r * math.sin(a):.0f}")
    return "M" + " L".join(pts) + " Z"


# ==================================================  GAMBAR 1 · BENSIN CAIRAN
def g1(X, A):
    txt, frame, wave, hatch = A.txt, A.frame, A.wave, A.hatch
    FW, FY = A.FW, A.FY
    return f'''        {frame("v1Frame", X)}
        {txt("v1No", X-FW//2+22, FY+52, "01", 30, "#7ef0ff", weight="700")}
        {txt("v1Title", X, 1495, "BENSIN", 64, "#eaf6ff", anchor="middle", weight="700")}
        {txt("v1Sub", X, 1548, "BAHAN BAKAR CAIR", 26, "#7ef0ff", anchor="middle")}
        <rect id="v1Can" class="d" x="{X-170}" y="1720" width="340" height="540" rx="26"
              fill="none" stroke="#e6f4ff" stroke-width="14"/>
        <g id="v1Top">
          <path class="d" d="M{X-90},1720 C{X-90},1662 {X-20},1662 {X-20},1720"
                fill="none" stroke="#e6f4ff" stroke-width="12"/>
          <rect class="d" x="{X+56}" y="1672" width="94" height="48" fill="none"
                stroke="#e6f4ff" stroke-width="11"/>
          <circle class="d" cx="{X+103}" cy="1656" r="26" fill="none" stroke="#e6f4ff" stroke-width="11"/>
        </g>
        <g id="v1Liq">
          <path class="d" d="{wave(X-148, X+148, 1930)}" fill="none" stroke="#7ef0ff" stroke-width="10"/>
          <path class="d" d="M{X-118},2010 h84 M{X+22},2010 h84 M{X-70},2076 h84 M{X+74},2076 h60"
                fill="none" stroke="#a9d8ff" stroke-width="7"/>
        </g>
        <line id="v1Ground" class="d" x1="{X-400}" y1="2260" x2="{X+400}" y2="2260" stroke="#e6f4ff" stroke-width="12"/>
        <path id="v1Hatch" class="d" d="{hatch(X-400, X+390, 2260)}" fill="none" stroke="#a9d8ff" stroke-width="4"/>
        <g id="v1Origin">
          <line class="d" x1="{X-200}" y1="2334" x2="{X+200}" y2="2334" stroke="#e6f4ff" stroke-width="9"/>
          <line class="d" x1="{X-148}" y1="2392" x2="{X+148}" y2="2392" stroke="#e6f4ff" stroke-width="8"/>
        </g>
        <path id="v1Up" class="f" d="M{X},2318 V2278" fill="none" stroke="#7ef0ff" stroke-width="14"
              marker-end="url(#arc)"/>
        {txt("v1OriginL", X, 2452, "DARI MINYAK BUMI", 28, "#7ef0ff", anchor="middle")}
        <path id="v1Leader" class="d" d="M{X-322},1862 L{X-184},1912" fill="none" stroke="#a9d8ff" stroke-width="5"/>
        {txt("v1Kuning", X-292, 1852, "KEKUNINGAN", 24)}
        <g id="v1Encer">
          <path class="d" d="M{X-262},1876 V1952" fill="none" stroke="#a9d8ff" stroke-width="5" stroke-dasharray="10 12"/>
          <path class="d" d="M{X-262},1968 c-30,42 -30,64 0,78 c30,-14 30,-36 0,-78 z"
                fill="none" stroke="#7ef0ff" stroke-width="9"/>
        </g>
        {txt("v1EncerL", X-262, 2094, "ENCER", 24, "#cfe9ff", anchor="middle")}
        <g id="v1Stink">
          <path class="d" d="M{X+36},1632 c-16,-26 16,-38 0,-64" fill="none" stroke="#7ef0ff" stroke-width="8" stroke-linecap="round"/>
          <path class="d" d="M{X+104},1614 c-16,-26 16,-38 0,-64" fill="none" stroke="#7ef0ff" stroke-width="8" stroke-linecap="round"/>
          <path class="d" d="M{X+172},1632 c-16,-26 16,-38 0,-64" fill="none" stroke="#7ef0ff" stroke-width="8" stroke-linecap="round"/>
        </g>
        {txt("v1Bau", X+308, 1600, "BAUNYA MENYENGAT", 20, "#cfe9ff", anchor="middle")}
        <path id="v1EvapA1" class="f" d="M{X+244},2062 V1922" fill="none" stroke="#7ef0ff" stroke-width="13" marker-end="url(#arc)"/>
        <path id="v1EvapA2" class="f" d="M{X+304},2090 V1956" fill="none" stroke="#7ef0ff" stroke-width="13" marker-end="url(#arc)"/>
        <path id="v1EvapA3" class="f" d="M{X+364},2062 V1930" fill="none" stroke="#7ef0ff" stroke-width="13" marker-end="url(#arc)"/>
        <g id="v1EvapDots">
          <circle class="d" cx="{X+228}" cy="1876" r="9" fill="none" stroke="#a9d8ff" stroke-width="6"/>
          <circle class="d" cx="{X+344}" cy="1852" r="8" fill="none" stroke="#a9d8ff" stroke-width="6"/>
        </g>
        {txt("v1EvapL", X+304, 1838, "MENGUAP CEPAT", 24, "#cfe9ff", anchor="middle")}'''


# ================================================  GAMBAR 2 · DI DALAM MESIN
def g2(X, A):
    txt, frame, hatch = A.txt, A.frame, A.hatch
    FW, FY = A.FW, A.FY
    return f'''        {frame("v2Frame", X)}
        {txt("v2No", X-FW//2+22, FY+52, "02", 30, "#7ef0ff", weight="700")}
        {txt("v2Title", X, 1495, "DI DALAM MESIN", 50, "#eaf6ff", anchor="middle", weight="700")}
        <g id="v2Cyl">
          <line class="d" x1="{X-230}" y1="1700" x2="{X-230}" y2="2120" stroke="#e6f4ff" stroke-width="14"/>
          <line class="d" x1="{X+230}" y1="1700" x2="{X+230}" y2="2120" stroke="#e6f4ff" stroke-width="14"/>
        </g>
        <rect id="v2Head" class="d" x="{X-250}" y="1636" width="500" height="64" rx="10"
              fill="none" stroke="#e6f4ff" stroke-width="13"/>
        <rect id="v2Piston" class="d" x="{X-215}" y="1930" width="430" height="110" rx="12"
              fill="none" stroke="#e6f4ff" stroke-width="13"/>
        <g id="v2Rings">
          <line class="d" x1="{X-205}" y1="1958" x2="{X+205}" y2="1958" stroke="#e6f4ff" stroke-width="5"/>
          <line class="d" x1="{X-205}" y1="1986" x2="{X+205}" y2="1986" stroke="#e6f4ff" stroke-width="5"/>
          <line class="d" x1="{X-205}" y1="2014" x2="{X+205}" y2="2014" stroke="#e6f4ff" stroke-width="5"/>
        </g>
        <g id="v2Drops">
          <circle class="d" cx="{X-140}" cy="1780" r="13" fill="none" stroke="#7ef0ff" stroke-width="8"/>
          <circle class="d" cx="{X-52}" cy="1848" r="10" fill="none" stroke="#7ef0ff" stroke-width="7"/>
          <circle class="d" cx="{X+34}" cy="1774" r="12" fill="none" stroke="#7ef0ff" stroke-width="8"/>
          <circle class="d" cx="{X+128}" cy="1842" r="9" fill="none" stroke="#7ef0ff" stroke-width="7"/>
          <circle class="d" cx="{X-96}" cy="1892" r="8" fill="none" stroke="#7ef0ff" stroke-width="6"/>
          <circle class="d" cx="{X+88}" cy="1900" r="11" fill="none" stroke="#7ef0ff" stroke-width="7"/>
        </g>
        <path id="v2Swirl" class="d" d="M{X-160},1876 C{X-70},1806 {X+50},1936 {X+152},1852"
              fill="none" stroke="#a9d8ff" stroke-width="9"/>
        {txt("v2FuelL", X-400, 1748, "BENSIN", 24, "#cfe9ff")}
        <path id="v2FuelLead" class="d" d="M{X-306},1764 L{X-160},1788" fill="none" stroke="#a9d8ff" stroke-width="5"/>
        {txt("v2AirL", X+304, 1742, "UDARA", 24, "#cfe9ff")}
        <path id="v2AirLead" class="d" d="M{X+300},1760 L{X+188},1846" fill="none" stroke="#a9d8ff" stroke-width="5"/>
        <g id="v2Comp">
          <path id="v2CompA1" class="f" d="M{X-152},1746 V1874" fill="none" stroke="#7ef0ff" stroke-width="16" marker-end="url(#arc)"/>
          <path id="v2CompA2" class="f" d="M{X+152},1746 V1874" fill="none" stroke="#7ef0ff" stroke-width="16" marker-end="url(#arc)"/>
        </g>
        <line id="v2Ground" class="d" x1="{X-400}" y1="2360" x2="{X+400}" y2="2360" stroke="#e6f4ff" stroke-width="12"/>
        <path id="v2Hatch" class="d" d="{hatch(X-400, X+390, 2360)}" fill="none" stroke="#a9d8ff" stroke-width="4"/>
        {txt("v2CompL", X, 2452, "LALU DIPADATKAN", 30, "#7ef0ff", anchor="middle", weight="700")}'''


# =====================================================  GAMBAR 3 · PERCIKAN
def g3(X, A):
    txt, frame, hatch = A.txt, A.frame, A.hatch
    FW, FY = A.FW, A.FY
    return f'''        {frame("v3Frame", X)}
        {txt("v3No", X-FW//2+22, FY+52, "03", 30, "#7ef0ff", weight="700")}
        {txt("v3Title", X, 1495, "PERCIKAN API", 50, "#eaf6ff", anchor="middle", weight="700")}
        <rect id="v3Head" class="d" x="{X-250}" y="1620" width="500" height="70" rx="10"
              fill="none" stroke="#e6f4ff" stroke-width="13"/>
        <g id="v3Cyl">
          <line class="d" x1="{X-230}" y1="1690" x2="{X-230}" y2="1960" stroke="#e6f4ff" stroke-width="14"/>
          <line class="d" x1="{X+230}" y1="1690" x2="{X+230}" y2="1960" stroke="#e6f4ff" stroke-width="14"/>
        </g>
        <g id="v3Plug">
          <rect class="d" x="{X-40}" y="1494" width="80" height="126" rx="10" fill="none" stroke="#e6f4ff" stroke-width="12"/>
          <line class="d" x1="{X}" y1="1620" x2="{X}" y2="1690" stroke="#e6f4ff" stroke-width="10"/>
          <path class="d" d="M{X-16},1690 V1738 M{X+16},1744 V1706" fill="none" stroke="#e6f4ff" stroke-width="9"/>
        </g>
        <path id="v3Cable" class="d" d="M{X-40},1536 C{X-150},1508 {X-230},1560 {X-320},1534"
              fill="none" stroke="#e6f4ff" stroke-width="12"/>
        {txt("v3PlugL", X+84, 1560, "BUSI", 26, "#7ef0ff")}
        <path id="v3PlugLead" class="d" d="M{X+78},1572 L{X+48},1590" fill="none" stroke="#a9d8ff" stroke-width="5"/>
        <g id="v3Spark">
          <line class="d" x1="{X}" y1="1748" x2="{X-64}" y2="1782" stroke="#7ef0ff" stroke-width="11" stroke-linecap="round"/>
          <line class="d" x1="{X}" y1="1748" x2="{X+64}" y2="1786" stroke="#7ef0ff" stroke-width="11" stroke-linecap="round"/>
          <line class="d" x1="{X}" y1="1748" x2="{X-44}" y2="1822" stroke="#7ef0ff" stroke-width="11" stroke-linecap="round"/>
          <line class="d" x1="{X}" y1="1748" x2="{X+48}" y2="1818" stroke="#7ef0ff" stroke-width="11" stroke-linecap="round"/>
          <line class="d" x1="{X}" y1="1748" x2="{X}" y2="1836" stroke="#7ef0ff" stroke-width="11" stroke-linecap="round"/>
        </g>
        <path id="v3Blast1" class="d" d="{star(A, X, 1770, 128, 74)}" fill="none" stroke="#7ef0ff" stroke-width="10"/>
        <path id="v3Blast2" class="d" d="{star(A, X, 1770, 198, 128, 12)}" fill="none" stroke="#e6f4ff" stroke-width="8"/>
        <rect id="v3Piston" class="d" x="{X-215}" y="1980" width="430" height="110" rx="12"
              fill="none" stroke="#e6f4ff" stroke-width="13"/>
        <g id="v3Rings">
          <line class="d" x1="{X-205}" y1="2008" x2="{X+205}" y2="2008" stroke="#e6f4ff" stroke-width="5"/>
          <line class="d" x1="{X-205}" y1="2036" x2="{X+205}" y2="2036" stroke="#e6f4ff" stroke-width="5"/>
          <line class="d" x1="{X-205}" y1="2064" x2="{X+205}" y2="2064" stroke="#e6f4ff" stroke-width="5"/>
        </g>
        <g id="v3Shock">
          <path class="d" d="M{X-262},1900 q-26,50 0,100" fill="none" stroke="#a9d8ff" stroke-width="8"/>
          <path class="d" d="M{X+262},1900 q26,50 0,100" fill="none" stroke="#a9d8ff" stroke-width="8"/>
        </g>
        <line id="v3Ground" class="d" x1="{X-400}" y1="2380" x2="{X+400}" y2="2380" stroke="#e6f4ff" stroke-width="12"/>
        <path id="v3Hatch" class="d" d="{hatch(X-400, X+390, 2380)}" fill="none" stroke="#a9d8ff" stroke-width="4"/>
        {txt("v3FastL", X, 2470, "DALAM SEKEJAP", 30, "#7ef0ff", anchor="middle", weight="700")}'''


# ======================================================  GAMBAR 4 · KE RODA
def g4(X, A):
    txt, frame, hatch = A.txt, A.frame, A.hatch
    FW, FY = A.FW, A.FY
    return f'''        {frame("v4Frame", X)}
        {txt("v4No", X-FW//2+22, FY+52, "04", 30, "#7ef0ff", weight="700")}
        {txt("v4Title", X, 1495, "DARI LEDAKAN KE RODA", 40, "#eaf6ff", anchor="middle", weight="700")}
        <path id="v4Blast" class="d" d="{star(A, X-210, 1600, 84, 48, 9)}" fill="none" stroke="#7ef0ff" stroke-width="10"/>
        <rect id="v4Piston" class="d" x="{X-340}" y="1672" width="260" height="96" rx="12"
              fill="none" stroke="#e6f4ff" stroke-width="13"/>
        <g id="v4Rings">
          <line class="d" x1="{X-332}" y1="1700" x2="{X-88}" y2="1700" stroke="#e6f4ff" stroke-width="5"/>
          <line class="d" x1="{X-332}" y1="1726" x2="{X-88}" y2="1726" stroke="#e6f4ff" stroke-width="5"/>
        </g>
        {txt("v4PistonL", X-340, 1628, "PISTON", 26, "#7ef0ff")}
        <g id="v4Push">
          <path id="v4PushA1" class="f" d="M{X-320},1614 V1662" fill="none" stroke="#7ef0ff" stroke-width="14" marker-end="url(#arc)"/>
          <path id="v4PushA2" class="f" d="M{X-100},1614 V1662" fill="none" stroke="#7ef0ff" stroke-width="14" marker-end="url(#arc)"/>
        </g>
        <g id="v4Rod">
          <line class="d" x1="{X-210}" y1="1768" x2="{X-160}" y2="1972" stroke="#e6f4ff" stroke-width="18" stroke-linecap="round"/>
          <circle class="d" cx="{X-210}" cy="1768" r="15" fill="none" stroke="#e6f4ff" stroke-width="9"/>
          <circle class="d" cx="{X-160}" cy="1972" r="15" fill="none" stroke="#e6f4ff" stroke-width="9"/>
        </g>
        <g id="v4Crank">
          <circle class="d" cx="{X-160}" cy="2085" r="110" fill="none" stroke="#e6f4ff" stroke-width="16"/>
          <circle class="d" cx="{X-160}" cy="2085" r="22" fill="none" stroke="#e6f4ff" stroke-width="10"/>
          <line class="d" x1="{X-160}" y1="2085" x2="{X-160}" y2="1972" stroke="#e6f4ff" stroke-width="12"/>
        </g>
        <path id="v4CrankRot" class="f" d="M{X-326},2040 A168,168 0 0 0 {X+2},2116"
              fill="none" stroke="#7ef0ff" stroke-width="13" marker-end="url(#arc)"/>
        {txt("v4CrankL", X-160, 2330, "POROS ENGKOL", 26, "#7ef0ff", anchor="middle")}
        <line id="v4Axle" class="d" x1="{X-46}" y1="2085" x2="{X+150}" y2="2085" stroke="#e6f4ff" stroke-width="14"/>
        <g id="v4Wheel">
          <circle class="d" cx="{X+282}" cy="2085" r="130" fill="none" stroke="#e6f4ff" stroke-width="16"/>
          <circle class="d" cx="{X+282}" cy="2085" r="94" fill="none" stroke="#a9d8ff" stroke-width="8"/>
          <circle class="d" cx="{X+282}" cy="2085" r="24" fill="none" stroke="#e6f4ff" stroke-width="10"/>
        </g>
        <g id="v4Spokes">
          <line class="d" x1="{X+282}" y1="2061" x2="{X+282}" y2="1994" stroke="#e6f4ff" stroke-width="8"/>
          <line class="d" x1="{X+282}" y1="2109" x2="{X+282}" y2="2176" stroke="#e6f4ff" stroke-width="8"/>
          <line class="d" x1="{X+261}" y1="2073" x2="{X+202}" y2="2039" stroke="#e6f4ff" stroke-width="8"/>
          <line class="d" x1="{X+303}" y1="2097" x2="{X+362}" y2="2131" stroke="#e6f4ff" stroke-width="8"/>
          <line class="d" x1="{X+261}" y1="2097" x2="{X+202}" y2="2131" stroke="#e6f4ff" stroke-width="8"/>
          <line class="d" x1="{X+303}" y1="2073" x2="{X+362}" y2="2039" stroke="#e6f4ff" stroke-width="8"/>
        </g>
        {txt("v4WheelL", X+282, 2330, "RODA", 26, "#7ef0ff", anchor="middle")}
        <g id="v4Speed">
          <line class="d" x1="{X+318}" y1="1868" x2="{X+398}" y2="1868" stroke="#7ef0ff" stroke-width="9"/>
          <line class="d" x1="{X+338}" y1="1918" x2="{X+404}" y2="1918" stroke="#7ef0ff" stroke-width="9"/>
          <line class="d" x1="{X+318}" y1="1968" x2="{X+392}" y2="1968" stroke="#7ef0ff" stroke-width="9"/>
        </g>
        {txt("v4GerakL", X+358, 1828, "BERGERAK", 24, "#cfe9ff", anchor="middle")}
        <line id="v4Ground" class="d" x1="{X-400}" y1="2250" x2="{X+400}" y2="2250" stroke="#e6f4ff" stroke-width="12"/>
        <path id="v4Hatch" class="d" d="{hatch(X-400, X+390, 2250)}" fill="none" stroke="#a9d8ff" stroke-width="4"/>'''


# ====================================================  GAMBAR 5 · RINGKASAN
def g5(X, A):
    txt, frame, zig, hatch = A.txt, A.frame, A.zig, A.hatch
    FW, FY = A.FW, A.FY
    return f'''        {frame("v5Frame", X)}
        {txt("v5No", X-FW//2+22, FY+52, "05", 30, "#7ef0ff", weight="700")}
        {txt("v5Title", X, 1495, "RINGKASAN", 50, "#eaf6ff", anchor="middle", weight="700")}
        <path id="v5Drop" class="d" d="M{X-190},1700 c-92,124 -130,196 -130,264 a130,130 0 0 0 260,0 c0,-68 -38,-140 -130,-264 z"
              fill="none" stroke="#e6f4ff" stroke-width="15"/>
        <path id="v5Zig" class="d" d="{zig(X-190, 1962, 4, 30, 40)}" fill="none" stroke="#7ef0ff" stroke-width="12"/>
        {txt("v5ChemL", X-190, 2330, "ENERGI KIMIA", 30, "#7ef0ff", anchor="middle", weight="700")}
        <path id="v5Arrow" class="f" d="M{X+4},2010 H{X+126}" fill="none" stroke="#7ef0ff" stroke-width="26"
              marker-end="url(#arc)"/>
        <g id="v5Wheel">
          <circle class="d" cx="{X+288}" cy="2010" r="118" fill="none" stroke="#e6f4ff" stroke-width="16"/>
          <circle class="d" cx="{X+288}" cy="2010" r="84" fill="none" stroke="#a9d8ff" stroke-width="8"/>
        </g>
        <g id="v5Spokes">
          <circle class="d" cx="{X+288}" cy="2010" r="22" fill="none" stroke="#e6f4ff" stroke-width="10"/>
          <line class="d" x1="{X+288}" y1="1988" x2="{X+288}" y2="1930" stroke="#e6f4ff" stroke-width="8"/>
          <line class="d" x1="{X+288}" y1="2032" x2="{X+288}" y2="2090" stroke="#e6f4ff" stroke-width="8"/>
          <line class="d" x1="{X+269}" y1="1999" x2="{X+218}" y2="1969" stroke="#e6f4ff" stroke-width="8"/>
          <line class="d" x1="{X+307}" y1="2021" x2="{X+358}" y2="2051" stroke="#e6f4ff" stroke-width="8"/>
          <line class="d" x1="{X+269}" y1="2021" x2="{X+218}" y2="2051" stroke="#e6f4ff" stroke-width="8"/>
          <line class="d" x1="{X+307}" y1="1999" x2="{X+358}" y2="1969" stroke="#e6f4ff" stroke-width="8"/>
        </g>
        {txt("v5MoveL", X+288, 2288, "GERAKAN", 30, "#7ef0ff", anchor="middle", weight="700")}
        <g id="v5Speed">
          <line class="d" x1="{X+330}" y1="1838" x2="{X+400}" y2="1838" stroke="#7ef0ff" stroke-width="9"/>
          <line class="d" x1="{X+348}" y1="1882" x2="{X+404}" y2="1882" stroke="#7ef0ff" stroke-width="9"/>
        </g>
        <line id="v5Ground" class="d" x1="{X-400}" y1="2400" x2="{X+400}" y2="2400" stroke="#e6f4ff" stroke-width="12"/>
        <path id="v5Hatch" class="d" d="{hatch(X-400, X+390, 2400)}" fill="none" stroke="#a9d8ff" stroke-width="4"/>'''


DRAW = [g1, g2, g3, g4, g5]

# pra-gambar VERBATIM dari generator lama — frame + no + ground/hatch
# (offset presisi di dalam jeda; jangan diganti turunan otomatis)
PRESHOW = [
    (20, 0.15, '#v2Frame', 0.55, 'd'),
    (20, 0.4, '#v2No', 0.4, 't'),
    (20, 0.55, '#v2Ground', 0.65, 'd'),
    (20, 0.8, '#v2Hatch', 0.85, 'd'),
    (28, 0.15, '#v3Frame', 0.55, 'd'),
    (28, 0.4, '#v3No', 0.4, 't'),
    (28, 0.55, '#v3Ground', 0.65, 'd'),
    (28, 0.8, '#v3Hatch', 0.85, 'd'),
    (36, 0.15, '#v4Frame', 0.55, 'd'),
    (36, 0.4, '#v4No', 0.4, 't'),
    (36, 0.55, '#v4Ground', 0.65, 'd'),
    (36, 0.8, '#v4Hatch', 0.85, 'd'),
    (48, 0.15, '#v5Frame', 0.55, 'd'),
    (48, 0.4, '#v5No', 0.4, 't'),
    (48, 0.55, '#v5Ground', 0.65, 'd'),
    (48, 0.8, '#v5Hatch', 0.85, 'd'),
]
