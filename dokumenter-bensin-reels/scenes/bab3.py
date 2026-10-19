"""Bab 3 "Asal usul: minyak bumi" — LIVE-DRAW reels Setetes Bensin (9:16).

Lima gambar besar di satu lembar:
  01  Laut purba — sisa makhluk hidup terkubur di dasar laut   (kata 0–27)
  02  Tekanan + panas bumi → cairan hitam pekat, minyak mentah (kata 28–42)
  03  Bahan bakar fosil — tidak bisa diperbarui                (kata 43–61)
  04  Kilang — cairan dipanaskan, uap naik                     (kata 62–68)
  05  Destilasi — uap didinginkan, fraksi ringan = bensin      (kata 69–83)

Koordinat gambar relatif X (titik tengah slide) — kamera memusatkan X.
"""

SCENE = {
    "id": "bab3",
    "hook": "Kalau minyak butuh jutaan tahun terbentuk, ia berasal dari apa?",
    "hud_left": ("BAB 03", "ASAL USUL: MINYAK BUMI"),
    "hud_right": "SETETES BENSIN<br />LIVE-DRAW · 9:16",
    "opening": ("BAB 03", "ASAL USUL: MINYAK BUMI"),
    "naskah": "naskah/bab3.txt",          # relatif terhadap path vo
    "vo_raw": "bab3-asal-usul.mp3",
    "lead": 1.8,
    "jeda": 1.8,
    "spacing": 1600,
    "conn_y": 2300,
}

# batas slide = titik jeda + pergeseran kamera (kata inklusif)
SLIDES = [
    {"words": (0, 27)},
    {"words": (28, 42), "preshow": "v2"},
    {"words": (43, 61), "preshow": "v3"},
    {"words": (62, 68), "preshow": "v4"},
    {"words": (69, 83), "preshow": "v5"},
]

CUES = [
    (0, "#v1Frame", 1.0, "d"), (0, "#v1No", 0.6, "t"), (0, "#v1Title", 0.8, "t"),
    (1, "#v1Sub", 0.7, "t"),
    (2, "#v1Sea", 1.2, "d"), (2, "#v1Sea2", 1.0, "d"),
    (6, "#v1Alive .d", 1.5, "d"), (6, "#v1AliveL", 0.6, "t"),
    (14, "#v1Ground", 1.0, "d"), (14, "#v1Hatch", 1.2, "d"),
    (19, "#v1Dead .d", 1.1, "d"), (19, "#v1Sink", 0.6, "f"),
    (21, "#v1Bones .d", 1.3, "d"),
    (24, "#v1Sedim .d", 1.4, "d"),
    (26, "#v1BuriedL", 0.5, "t"), (26, "#v1BuriedLead", 0.3, "d"),

    (28, "#v2Title", 0.8, "t"), (28, "#v2Strata .d", 1.4, "d"),
    (30, "#v2PressA1", 0.5, "f"), (30, "#v2PressA2", 0.5, "f"), (30, "#v2PressL", 0.7, "t"),
    (32, "#v2Ground", 1.0, "d"), (32, "#v2Hatch", 1.2, "d"),
    (33, "#v2HeatW .d", 1.4, "d"), (33, "#v2HeatL", 0.6, "t"),
    (36, "#v2Pool", 1.2, "d"),
    (38, "#v2PoolIn", 0.9, "d"),
    (40, "#v2Drip", 0.5, "f"),
    (41, "#v2DarkL", 0.6, "t"), (41, "#v2OilL", 0.7, "t"), (41, "#conn2", 1.3, "d"),

    (43, "#v3Title", 0.8, "t"),
    (44, "#v3Glass .d", 1.4, "d"),
    (45, "#v3SandT", 0.6, "d"), (45, "#v3Stream", 0.5, "d"), (45, "#v3SandB", 0.6, "d"),
    (46, "#v3TimeL", 0.6, "t"),
    (47, "#v3Ground", 1.0, "d"), (47, "#v3Hatch", 1.2, "d"),
    (49, "#v3Drop", 1.1, "d"),
    (51, "#v3Bone .d", 0.9, "d"),
    (55, "#v3Cross1", 0.4, "f"), (55, "#v3Cross2", 0.4, "f"),
    (57, "#v3NoRenewL", 0.5, "t"), (57, "#v3NoRenewL2", 0.5, "t"),
    (60, "#conn3", 1.3, "d"),

    (62, "#v4Title", 0.7, "t"),
    (63, "#v4Tower", 1.2, "d"), (63, "#v4Decks .d", 0.8, "d"),
    (64, "#v4Ground", 0.9, "d"), (64, "#v4Hatch", 1.0, "d"),
    (65, "#v4Fire", 0.9, "d"), (65, "#v4HeatL", 0.5, "t"),
    (67, "#v4Vap .d", 1.0, "d"), (67, "#v4VapL", 0.5, "t"), (67, "#conn4", 1.2, "d"),

    (69, "#v5Title", 0.7, "t"),
    (70, "#v5Col", 1.2, "d"), (70, "#v5Trays .d", 0.9, "d"),
    (71, "#v5Ground", 0.9, "d"), (71, "#v5Hatch", 1.0, "d"),
    (72, "#v5In", 0.5, "f"), (72, "#v5InL", 0.5, "t"),
    (73, "#v5CoolA1", 0.5, "f"), (73, "#v5CoolL", 0.5, "t"),
    (74, "#v5Out1", 0.5, "f"), (74, "#v5Out1L", 0.5, "t"), (74, "#v5Out1L2", 0.5, "t"),
    (76, "#v5Out2", 0.5, "f"), (76, "#v5Out2L", 0.5, "t"),
    (78, "#v5TankPipe", 0.8, "f"),
    (79, "#v5Tank", 1.0, "d"),
    (81, "#v5Bensin", 0.8, "d"),
    (82, "#v5BensinL", 0.5, "t"),
]

CAPTIONS = [
    (0, 5, "JAWABANNYA TERLETAK JAUH SEBELUM MANUSIA ADA"),
    (6, 13, "DARI SISA MAKHLUK HIDUP: PLANKTON, TUMBUHAN, HEWAN LAUT"),
    (14, 23, "YANG MATI DAN TERKUBUR DI DASAR LAUT"),
    (24, 27, "JUTAAN TAHUN LALU"),
    (28, 34, "TERTIMBUN, TERHIMPIT, TERPANGGANG PANAS BUMI"),
    (35, 42, "BERUBAH JADI CAIRAN HITAM PEKAT — MINYAK MENTAH"),
    (43, 47, "PROSESNYA BUTUH JUTAAN TAHUN"),
    (48, 53, "DISEBUT BAHAN BAKAR FOSIL"),
    (54, 61, "DAN TIDAK BISA DIPERBARUI DALAM WAKTU SINGKAT"),
    (62, 68, "CAIRAN INI DIPANASKAN DI KILANG"),
    (69, 75, "UAPNYA DIDINGINKAN PADA SUHU BERBEDA-BEDA"),
    (76, 83, "YANG PALING RINGAN ITULAH BENSIN"),
]

# kata -> [(suara, gain dB, geser detik), ...]
# catatan: suara goresan pensil ("line") sengaja TIDAK dipakai (terdengar spspspsp)
SFXMAP = {
    0:  [("paper", -8, 0.00)],
    2:  [("tick", -14, 0.20)],
    4:  [("tick", -14, 0.25)],
    6:  [("tick", -13, 0.15)],
    8:  [("tick", -14, 0.30)],
    10: [("tick", -14, 0.25)],
    14: [("tick", -13, 0.20)],
    16: [("tick", -14, 0.30)],
    19: [("puff", -12, 0.00)],
    21: [("tick", -13, 0.20)],
    24: [("deep", -11, 0.00)],
    26: [("tick", -14, 0.30)],
    28: [("tick", -13, 0.20)],
    30: [("tick", -14, 0.30)],
    32: [("tick", -14, 0.35)],
    33: [("puff", -11, 0.10)],
    36: [("deep", -12, 0.00)],
    38: [("tick", -14, 0.30)],
    40: [("puff", -12, 0.00)],
    41: [("chime", -12, 0.10)],
    43: [("tick", -13, 0.25)],
    44: [("tick", -14, 0.30)],
    45: [("tick", -14, 0.20)],
    47: [("tick", -14, 0.30)],
    49: [("tick", -13, 0.25)],
    51: [("tick", -14, 0.35)],
    55: [("zap", -12, 0.00)],
    57: [("tick", -13, 0.30)],
    60: [("tick", -13, 0.50)],
    62: [("tick", -13, 0.25)],
    63: [("deep", -12, 0.00)],
    65: [("puff", -12, 0.10)],
    67: [("puff", -11, 0.00)],
    69: [("tick", -13, 0.30)],
    70: [("tick", -14, 0.35)],
    72: [("pump", -12, 0.00)],
    73: [("puff", -12, 0.05)],
    74: [("tick", -13, 0.25)],
    76: [("tick", -14, 0.30)],
    78: [("tick", -14, 0.25)],
    79: [("tick", -13, 0.30)],
    81: [("tick", -13, 0.25)],
    82: [("chime", -11, 0.00)],
}


# helper lokal generator lama — tidak memakai A/FW/FY, A tetap diterima
# (argumen default) supaya signature mengikuti konvensi scene tanpa mengubah
# pemanggilan verbatim di dalam g1.
def fish(x, y, s=1.0, A=None):
    """ikan sederhana menghadap kanan, (x,y) = titik ekor"""
    return (f"M{x},{y} c{28*s},{-24*s} {76*s},{-24*s} {104*s},0"
            f" c{-28*s},{24*s} {-76*s},{24*s} {-104*s},0 z"
            f" M{x},{y} l{-26*s},{-18*s} v{36*s} z")


# ==================================================  GAMBAR 1 · LAUT PURBA
def g1(X, A):
    txt, frame, wave, hatch = A.txt, A.frame, A.wave, A.hatch
    FW, FY = A.FW, A.FY
    return f'''        {frame("v1Frame", X)}
        {txt("v1No", X-FW//2+22, FY+52, "01", 30, "#7ef0ff", weight="700")}
        {txt("v1Title", X, 1495, "LAUT PURBA", 54, "#eaf6ff", anchor="middle", weight="700")}
        {txt("v1Sub", X, 1548, "JUTAAN TAHUN LALU", 26, "#7ef0ff", anchor="middle")}
        <path id="v1Sea" class="d" d="{wave(X-380, X+380, 1660)}" fill="none" stroke="#7ef0ff" stroke-width="9"/>
        <path id="v1Sea2" class="d" d="{wave(X-320, X+340, 1712, 14)}" fill="none" stroke="#a9d8ff" stroke-width="6"/>
        <g id="v1Alive">
          <path class="d" d="{fish(X-330, 1840)}" fill="none" stroke="#e6f4ff" stroke-width="9"/>
          <path class="d" d="{fish(X-90, 1930, 0.8)}" fill="none" stroke="#e6f4ff" stroke-width="8"/>
          <path class="d" d="{fish(X+150, 1810, 1.1)}" fill="none" stroke="#e6f4ff" stroke-width="10"/>
        </g>
        {txt("v1AliveL", X-330, 1798, "MAKHLUK LAUT", 24, "#cfe9ff")}
        <g id="v1Dead">
          <path class="d" d="{fish(X-250, 2050, 0.9)}" fill="none" stroke="#a9d8ff" stroke-width="8"/>
          <path class="d" d="M{X-190},2032 l16,16 M{X-174},2032 l-16,16" fill="none" stroke="#a9d8ff" stroke-width="5"/>
        </g>
        <path id="v1Sink" class="f" d="M{X-40},1990 V2100" fill="none" stroke="#7ef0ff" stroke-width="13" marker-end="url(#arc)"/>
        <g id="v1Bones">
          <line class="d" x1="{X-240}" y1="2185" x2="{X-40}" y2="2185" stroke="#cfe9ff" stroke-width="7"/>
          <line class="d" x1="{X-215}" y1="2165" x2="{X-215}" y2="2205" stroke="#cfe9ff" stroke-width="5"/>
          <line class="d" x1="{X-185}" y1="2160" x2="{X-185}" y2="2210" stroke="#cfe9ff" stroke-width="5"/>
          <line class="d" x1="{X-155}" y1="2162" x2="{X-155}" y2="2208" stroke="#cfe9ff" stroke-width="5"/>
          <path class="d" d="{fish(X-320, 2185, 0.55)}" fill="none" stroke="#cfe9ff" stroke-width="6"/>
        </g>
        <g id="v1Sedim">
          <path class="d" d="{wave(X-380, X+380, 2120, 16)}" fill="none" stroke="#a9d8ff" stroke-width="8"/>
          <path class="d" d="{wave(X-360, X+360, 2170, 12)}" fill="none" stroke="#a9d8ff" stroke-width="6"/>
          <path class="d" d="{wave(X-380, X+380, 2230, 14)}" fill="none" stroke="#a9d8ff" stroke-width="7"/>
        </g>
        <line id="v1Ground" class="d" x1="{X-400}" y1="2330" x2="{X+400}" y2="2330" stroke="#e6f4ff" stroke-width="12"/>
        <path id="v1Hatch" class="d" d="{hatch(X-400, X+390, 2330)}" fill="none" stroke="#a9d8ff" stroke-width="4"/>
        {txt("v1BuriedL", X+30, 2280, "TERKUBUR", 26, "#7ef0ff", anchor="middle", weight="700")}
        <path id="v1BuriedLead" class="d" d="M{X+30},2258 V2240" fill="none" stroke="#a9d8ff" stroke-width="5"/>'''


# ================================================  GAMBAR 2 · TEKANAN & PANAS
def g2(X, A):
    txt, frame, wave, hatch = A.txt, A.frame, A.wave, A.hatch
    FW, FY = A.FW, A.FY
    return f'''        {frame("v2Frame", X)}
        {txt("v2No", X-FW//2+22, FY+52, "02", 30, "#7ef0ff", weight="700")}
        {txt("v2Title", X, 1495, "TEKANAN & PANAS", 46, "#eaf6ff", anchor="middle", weight="700")}
        <g id="v2Strata">
          <path class="d" d="M{X-360},1650 H{X+360}" fill="none" stroke="#e6f4ff" stroke-width="12"/>
          <path class="d" d="M{X-360},1700 H{X+360}" fill="none" stroke="#a9d8ff" stroke-width="6"/>
          <path class="d" d="M{X-360},1790 H{X+360}" fill="none" stroke="#e6f4ff" stroke-width="12"/>
          <path class="d" d="M{X-360},1840 H{X+360}" fill="none" stroke="#a9d8ff" stroke-width="6"/>
        </g>
        <path id="v2PressA1" class="f" d="M{X-230},1560 V1630" fill="none" stroke="#7ef0ff" stroke-width="15" marker-end="url(#arc)"/>
        <path id="v2PressA2" class="f" d="M{X+230},1560 V1630" fill="none" stroke="#7ef0ff" stroke-width="15" marker-end="url(#arc)"/>
        {txt("v2PressL", X, 1545, "TERHIMPIT LAPISAN BUMI", 24, "#cfe9ff", anchor="middle")}
        <g id="v2HeatW">
          <path class="d" d="M{X-260},2330 c-24,-56 24,-84 0,-140" fill="none" stroke="#7ef0ff" stroke-width="8"/>
          <path class="d" d="M{X-90},2330 c-24,-56 24,-84 0,-140" fill="none" stroke="#7ef0ff" stroke-width="8"/>
          <path class="d" d="M{X+90},2330 c-24,-56 24,-84 0,-140" fill="none" stroke="#7ef0ff" stroke-width="8"/>
          <path class="d" d="M{X+260},2330 c-24,-56 24,-84 0,-140" fill="none" stroke="#7ef0ff" stroke-width="8"/>
        </g>
        {txt("v2HeatL", X, 2432, "PANAS BUMI", 26, "#7ef0ff", anchor="middle", weight="700")}
        <line id="v2Ground" class="d" x1="{X-400}" y1="2350" x2="{X+400}" y2="2350" stroke="#e6f4ff" stroke-width="12"/>
        <path id="v2Hatch" class="d" d="{hatch(X-400, X+390, 2350)}" fill="none" stroke="#a9d8ff" stroke-width="4"/>
        <path id="v2Pool" class="d" d="M{X-240},2010 c60,-56 140,-64 240,-64 c100,0 180,8 240,64 c-60,52 -140,60 -240,60 c-100,0 -180,-8 -240,-60 z"
              fill="none" stroke="#e6f4ff" stroke-width="13"/>
        <path id="v2PoolIn" class="d" d="{wave(X-200, X+200, 2010, 13)}" fill="none" stroke="#7ef0ff" stroke-width="8"/>
        <path id="v2Drip" class="f" d="M{X},2090 V2160" fill="none" stroke="#7ef0ff" stroke-width="12" marker-end="url(#arc)"/>
        {txt("v2DarkL", X, 2210, "CAIRAN HITAM PEKAT", 26, "#cfe9ff", anchor="middle")}
        {txt("v2OilL", X, 2258, "MINYAK MENTAH", 30, "#7ef0ff", anchor="middle", weight="700")}'''


# ====================================================  GAMBAR 3 · FOSIL
def g3(X, A):
    txt, frame, drop, hatch = A.txt, A.frame, A.drop, A.hatch
    FW, FY = A.FW, A.FY
    return f'''        {frame("v3Frame", X)}
        {txt("v3No", X-FW//2+22, FY+52, "03", 30, "#7ef0ff", weight="700")}
        {txt("v3Title", X, 1495, "BAHAN BAKAR FOSIL", 40, "#eaf6ff", anchor="middle", weight="700")}
        <g id="v3Glass">
          <path class="d" d="M{X-150},1600 H{X+150}" fill="none" stroke="#e6f4ff" stroke-width="12"/>
          <path class="d" d="M{X-150},1900 H{X+150}" fill="none" stroke="#e6f4ff" stroke-width="12"/>
          <path class="d" d="M{X-136},1600 L{X+136},1600 L{X},1740 Z" fill="none" stroke="#e6f4ff" stroke-width="10"/>
          <path class="d" d="M{X-136},1900 L{X+136},1900 L{X},1760 Z" fill="none" stroke="#e6f4ff" stroke-width="10"/>
        </g>
        <path id="v3SandT" class="d" d="M{X-90},1632 L{X+90},1632 L{X},1702 Z" fill="none" stroke="#7ef0ff" stroke-width="8"/>
        <path id="v3Stream" class="d" d="M{X},1748 V1830" fill="none" stroke="#7ef0ff" stroke-width="7"/>
        <path id="v3SandB" class="d" d="M{X-80},1878 Q{X},1808 {X+80},1878" fill="none" stroke="#7ef0ff" stroke-width="8"/>
        {txt("v3TimeL", X, 1972, "PROSES JUTAAN TAHUN", 26, "#cfe9ff", anchor="middle")}
        <path id="v3Drop" class="d" d="{drop(X, 2080, 1.1)}" fill="none" stroke="#e6f4ff" stroke-width="13"/>
        <g id="v3Bone">
          <line class="d" x1="{X-52}" y1="2222" x2="{X+52}" y2="2222" stroke="#7ef0ff" stroke-width="6"/>
          <line class="d" x1="{X-30}" y1="2204" x2="{X-30}" y2="2240" stroke="#7ef0ff" stroke-width="4"/>
          <line class="d" x1="{X}" y1="2200" x2="{X}" y2="2244" stroke="#7ef0ff" stroke-width="4"/>
          <line class="d" x1="{X+30}" y1="2204" x2="{X+30}" y2="2240" stroke="#7ef0ff" stroke-width="4"/>
        </g>
        <path id="v3Cross1" class="f" d="M{X-330},2130 L{X-170},2290" fill="none" stroke="#7ef0ff" stroke-width="14"/>
        <path id="v3Cross2" class="f" d="M{X-170},2130 L{X-330},2290" fill="none" stroke="#7ef0ff" stroke-width="14"/>
        {txt("v3NoRenewL", X-250, 2345, "TIDAK BISA", 24, "#cfe9ff", anchor="middle")}
        {txt("v3NoRenewL2", X-250, 2380, "DIPERBARUI", 24, "#cfe9ff", anchor="middle")}
        <line id="v3Ground" class="d" x1="{X-400}" y1="2450" x2="{X+400}" y2="2450" stroke="#e6f4ff" stroke-width="12"/>
        <path id="v3Hatch" class="d" d="{hatch(X-400, X+390, 2450)}" fill="none" stroke="#a9d8ff" stroke-width="4"/>'''


# =====================================================  GAMBAR 4 · KILANG
def g4(X, A):
    txt, frame, zig, hatch = A.txt, A.frame, A.zig, A.hatch
    FW, FY = A.FW, A.FY
    return f'''        {frame("v4Frame", X)}
        {txt("v4No", X-FW//2+22, FY+52, "04", 30, "#7ef0ff", weight="700")}
        {txt("v4Title", X, 1495, "DI KILANG", 54, "#eaf6ff", anchor="middle", weight="700")}
        <rect id="v4Tower" class="d" x="{X-120}" y="1660" width="240" height="560" rx="14"
              fill="none" stroke="#e6f4ff" stroke-width="13"/>
        <g id="v4Decks">
          <line class="d" x1="{X-150}" y1="1800" x2="{X+150}" y2="1800" stroke="#e6f4ff" stroke-width="8"/>
          <line class="d" x1="{X-150}" y1="1960" x2="{X+150}" y2="1960" stroke="#e6f4ff" stroke-width="8"/>
        </g>
        <path id="v4Fire" class="d" d="{zig(X, 2330, 5, 30, 30)}" fill="none" stroke="#7ef0ff" stroke-width="11"/>
        {txt("v4HeatL", X, 2410, "DIPANASKAN", 28, "#7ef0ff", anchor="middle", weight="700")}
        <g id="v4Vap">
          <path class="d" d="M{X-60},1630 c-20,-44 20,-66 0,-110" fill="none" stroke="#a9d8ff" stroke-width="8"/>
          <path class="d" d="M{X},1610 c-20,-44 20,-66 0,-110" fill="none" stroke="#a9d8ff" stroke-width="8"/>
          <path class="d" d="M{X+60},1630 c-20,-44 20,-66 0,-110" fill="none" stroke="#a9d8ff" stroke-width="8"/>
        </g>
        {txt("v4VapL", X+170, 1530, "UAP NAIK", 24, "#cfe9ff")}
        <line id="v4Ground" class="d" x1="{X-400}" y1="2350" x2="{X+400}" y2="2350" stroke="#e6f4ff" stroke-width="12"/>
        <path id="v4Hatch" class="d" d="{hatch(X-400, X+390, 2350)}" fill="none" stroke="#a9d8ff" stroke-width="4"/>'''


# ===================================================  GAMBAR 5 · DESTILASI
def g5(X, A):
    txt, frame, drop, hatch = A.txt, A.frame, A.drop, A.hatch
    FW, FY = A.FW, A.FY
    return f'''        {frame("v5Frame", X)}
        {txt("v5No", X-FW//2+22, FY+52, "05", 30, "#7ef0ff", weight="700")}
        {txt("v5Title", X, 1495, "SARINGAN SUHU", 48, "#eaf6ff", anchor="middle", weight="700")}
        <rect id="v5Col" class="d" x="{X-130}" y="1620" width="260" height="620" rx="14"
              fill="none" stroke="#e6f4ff" stroke-width="13"/>
        <g id="v5Trays">
          <line class="d" x1="{X-130}" y1="1745" x2="{X+130}" y2="1745" stroke="#a9d8ff" stroke-width="7"/>
          <line class="d" x1="{X-130}" y1="1870" x2="{X+130}" y2="1870" stroke="#a9d8ff" stroke-width="7"/>
          <line class="d" x1="{X-130}" y1="1995" x2="{X+130}" y2="1995" stroke="#a9d8ff" stroke-width="7"/>
        </g>
        <path id="v5In" class="f" d="M{X-330},2170 H{X-150}" fill="none" stroke="#7ef0ff" stroke-width="13" marker-end="url(#arc)"/>
        {txt("v5InL", X-330, 2130, "UAP MASUK", 24, "#cfe9ff")}
        <path id="v5Out1" class="f" d="M{X+130},1700 H{X+290}" fill="none" stroke="#7ef0ff" stroke-width="12" marker-end="url(#arc)"/>
        {txt("v5Out1L", X+300, 1690, "SUHU TINGGI", 22, "#cfe9ff")}
        {txt("v5Out1L2", X+300, 1722, "FRAGSI RINGAN", 22, "#cfe9ff")}
        <path id="v5Out2" class="f" d="M{X+130},1950 H{X+290}" fill="none" stroke="#a9d8ff" stroke-width="10" marker-end="url(#arc)"/>
        {txt("v5Out2L", X+300, 1960, "FRAGSI BERAT", 22, "#a9d8ff")}
        <path id="v5TankPipe" class="f" d="M{X-130},1700 H{X-300} V1880" fill="none" stroke="#7ef0ff" stroke-width="12"/>
        <rect id="v5Tank" class="d" x="{X-380}" y="1880" width="160" height="150" rx="16"
              fill="none" stroke="#e6f4ff" stroke-width="12"/>
        <path id="v5Bensin" class="d" d="{drop(X-300, 1916, 0.52)}" fill="none" stroke="#7ef0ff" stroke-width="9"/>
        {txt("v5BensinL", X-300, 2090, "BENSIN", 30, "#7ef0ff", anchor="middle", weight="700")}
        <path id="v5CoolA1" class="f" d="M{X+220},1600 V1660" fill="none" stroke="#a9d8ff" stroke-width="11" marker-end="url(#arc)"/>
        {txt("v5CoolL", X+220, 1565, "DIDINGINKAN", 22, "#cfe9ff", anchor="middle")}
        <line id="v5Ground" class="d" x1="{X-400}" y1="2280" x2="{X+400}" y2="2280" stroke="#e6f4ff" stroke-width="12"/>
        <path id="v5Hatch" class="d" d="{hatch(X-400, X+390, 2280)}" fill="none" stroke="#a9d8ff" stroke-width="4"/>'''


DRAW = [g1, g2, g3, g4, g5]

# pra-gambar VERBATIM dari generator lama — frame + no + ground/hatch
# (offset presisi di dalam jeda; jangan diganti turunan otomatis)
PRESHOW = [
    (28, 0.15, '#v2Frame', 0.55, 'd'),
    (28, 0.4, '#v2No', 0.4, 't'),
    (28, 0.55, '#v2Ground', 0.65, 'd'),
    (28, 0.8, '#v2Hatch', 0.85, 'd'),
    (43, 0.15, '#v3Frame', 0.55, 'd'),
    (43, 0.4, '#v3No', 0.4, 't'),
    (43, 0.55, '#v3Ground', 0.65, 'd'),
    (43, 0.8, '#v3Hatch', 0.85, 'd'),
    (62, 0.15, '#v4Frame', 0.55, 'd'),
    (62, 0.4, '#v4No', 0.4, 't'),
    (62, 0.55, '#v4Ground', 0.65, 'd'),
    (62, 0.8, '#v4Hatch', 0.85, 'd'),
    (69, 0.15, '#v5Frame', 0.55, 'd'),
    (69, 0.4, '#v5No', 0.4, 't'),
    (69, 0.55, '#v5Ground', 0.65, 'd'),
    (69, 0.8, '#v5Hatch', 0.85, 'd'),
]
