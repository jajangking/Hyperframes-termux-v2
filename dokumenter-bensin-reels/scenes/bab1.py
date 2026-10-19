"""Bab 1 "Pembuka — Pertanyaan" — LIVE-DRAW reels Setetes Bensin (9:16).

Port dari gen_livedraw_bab1.py (+ align_bab1.py untuk LEAD/SISIP).

Empat gambar besar di satu lembar:
  01  Jalan & SPBU — jutaan kendaraan berhenti di tempat yang sama   (kata 0–10)
  02  Mengisi, membayar, lalu pergi                                  (kata 11–15)
  03  Dari mana cairan ini datang?                                   (kata 16–25)
  04  Ke mana ia pergi setelah mesin menyala?                        (kata 26–33)

Koordinat gambar relatif X (titik tengah slide) — kamera memusatkan X.

Catatan port (lihat ringkasan subagen):
  - PRESHOW lama (11 entri) berisi juga v2Ground/v2Hatch (kata 11, off 0.55/0.80),
    v3Surf/v3Hatch (kata 16, off 0.55/0.80), v4Block (kata 26, off 0.20), plus
    frame+no slide 4 dengan offset/durasi beda (0.05/0.40 & 0.15/0.30). Framework
    hanya menghasilkan pra-gambar frame+no (off 0.15/0.40) — kelima elemen ekstra
    itu TIDAK tergambar di port ini (mereka juga tidak ada di CUES lama).
  - CONN lama: `M{X±460},2200`, stroke #7ef0ff; framework auto: `X±470`, y=conn_y,
    stroke currentColor (ink2). conn_y di-set 2200; sisanya beda 10px + warna.
"""

SCENE = {
    "id": "bab1",
    "hook": "Dari mana cairan di pom bensin itu datang — dan ke mana perginya?",
    "hud_left": ("BAB 01", "PEMBUKA — PERTANYAAN"),   # .bab / .ttl generator lama
    "hud_right": "SETETES BENSIN<br />LIVE-DRAW · 9:16",   # .trblk generator lama
    # #opening generator lama — ditimpa "hook" saat render (hook = kartu pembuka)
    "opening": ("SETETES<br />BENSIN", "DARI PERUT BUMI KE KNALPOT"),
    "naskah": "naskah/bab1.txt",
    "vo_raw": "bab1-pembuka.mp3",
    "lead": 3.0,
    "tail": 1.2,        # ekor senyap: animasi akhir (smoke) tak kepotong        # align_bab1.py: LEAD = 3.0
    "jeda": 1.8,        # align_bab1.py: SISIP = {11: 1.8, 16: 1.8, 26: 1.0}
    "spacing": 1600,    # X2 − X1
    "conn_y": 2200, "conn_half": 460,     # y garis CONN lama (default framework 2300)
}

# batas slide = titik jeda + pergeseran kamera (kata inklusif); CAM lama 0/11/16/26
SLIDES = [
    {"words": (0, 10)},
    {"words": (11, 15), "preshow": "v2"},          # PRESHOW lama: #v2Frame + #v2No
    {"words": (16, 25), "preshow": "v3"},          # PRESHOW lama: #v3Frame + #v3No
    {"words": (26, 33), "preshow": "v4", "jeda": 1.0},   # SISIP[26] = 1.0
]

CUES = [
    (0, "#v1Frame", 1.0, "d"), (0, "#v1No", 0.6, "t"),
    (1, "#v1Ground", 1.1, "d"), (1, "#v1Hatch", 1.3, "d"),
    (2, "#v1Car1 .d", 1.4, "d"),
    (3, "#v1Car2 .d", 1.2, "d"),
    (4, "#v1Car3 .d", 1.2, "d"),
    (5, "#v1Canopy", 1.4, "d"),
    (6, "#v1Pillars .d", 1.3, "d"),
    (7, "#v1Pumps .d", 1.4, "d"),
    (8, "#v1Board .d", 1.1, "d"),
    (9, "#v1Sign", 0.8, "t"), (9, "#v1Tree", 1.2, "d"), (9, "#conn1", 1.4, "d"),
    (10, "#v1BoardTxt", 0.7, "t"), (10, "#v1Cloud", 1.0, "d"),

    (11, "#v2Car .d", 1.6, "d"),
    (11, "#v2Tnk", 0.7, "t"),
    (12, "#v2Flap .d", 1.0, "d"), (12, "#v2Nozzle .d", 1.0, "d"),
    (12, "#v2Hose", 1.3, "d"), (12, "#v2Drop", 0.7, "d"),
    (13, "#v2Pump", 1.3, "d"), (13, "#v2Win", 0.9, "d"), (13, "#v2Dig", 0.8, "t"),
    (13, "#v2Ltr", 0.7, "t"),
    (14, "#v2Coin .d", 1.2, "d"), (14, "#v2Rp", 0.7, "t"), (14, "#v2Pay", 0.7, "t"),
    (15, "#v2Go .d", 0.9, "d"), (15, "#v2GoTxt", 0.7, "t"), (15, "#conn2", 1.4, "d"),

    (16, "#v3Q", 1.4, "d"),
    (17, "#v3Qdot", 0.7, "d"),
    (18, "#v3Title", 0.8, "t"),
    (19, "#v3Sb .d", 1.1, "d"), (19, "#v3Car .d", 0.9, "d"),
    (20, "#v3Strata .d", 1.5, "d"),
    (21, "#v3Org .d", 1.3, "d"), (21, "#v3L2", 0.7, "t"),
    (22, "#v3Oil", 1.5, "d"),
    (23, "#v3Drops .d", 1.0, "d"),
    (24, "#v3Depth .d", 1.0, "d"), (24, "#v3L1", 0.7, "t"),
    (25, "#v3Arrow", 0.8, "t"), (25, "#v3L3", 0.7, "t"), (25, "#conn3", 1.4, "d"),

    (26, "#v4Bolts .d", 1.0, "d"),
    (27, "#v4Cyl", 1.1, "d"), (27, "#v4Head", 0.8, "d"), (27, "#v4Fin .d", 1.0, "d"),
    (28, "#v4Piston", 1.0, "d"), (28, "#v4Rings .d", 0.8, "d"),
    (29, "#v4Rod .d", 1.0, "d"),
    (30, "#v4Crank .d", 1.3, "d"),
    (31, "#v4Exh", 1.3, "d"), (31, "#v4Muff .d", 1.1, "d"), (31, "#v4Tail", 0.6, "d"),
    (31, "#v4ExhL", 0.7, "t"),
    (32, "#v4Plug .d", 1.0, "d"), (32, "#v4PlugTxt", 0.7, "t"), (32, "#v4MesinL", 0.7, "t"),
    (33, "#v4Spark .d", 1.0, "d"), (33, "#v4Smoke .d", 1.4, "d"),
    (33, "#v4Asap", 0.7, "t"), (33, "#v4Title", 0.8, "t"),
]

CAPTIONS = [
    (0, 8, "JUTAAN KENDARAAN BERHENTI DI TEMPAT YANG SAMA"),
    (9, 10, "POM BENSIN"),
    (11, 12, "KITA MENGISI"),
    (13, 13, "MEMBAYAR"),
    (14, 15, "LALU PERGI"),
    (16, 20, "PERNAHKAH KITA BERTANYA?"),
    (21, 25, "DARI MANA CAIRAN INI DATANG?"),
    (26, 33, "DAN KE MANA IA PERGI SETELAH MESIN MENYALA?"),
]

SFXMAP = {
    0:  [("paper", -8, 0.00)],
    6:  [("tick", -14, 0.25)],
    7:  [("tick", -14, 0.35)],
    9:  [("chime", -12, 0.00)],
    10: [("tick", -14, 0.00)],
    12: [("pump", -13, 0.20)],
    13: [("pump", -11, 0.00), ("tick", -13, 0.35), ("tick", -13, 0.50)],
    14: [("coin", -10, 0.00), ("tick", -14, 0.40)],
    15: [("tick", -13, 0.45)],
    16: [("sting", -11, 0.00)],
    17: [("boom", -13, 0.00)],
    18: [("tick", -14, 0.80)],
    20: [("rumble", -13, 0.00)],
    21: [("tick", -14, 0.45)],
    22: [("deep", -10, 0.00)],
    23: [("tick", -14, 0.25)],
    24: [("tick", -13, 0.00), ("tick", -13, 0.30)],
    25: [("tick", -13, 0.00), ("tick", -14, 0.30)],
    28: [("tick", -14, 0.35)],
    31: [("puff", -11, 0.00), ("tick", -14, 0.45)],
    32: [("tick", -14, 0.35)],
    33: [("zap", -11, 0.00), ("rev", -12, 0.15), ("tick", -14, 0.70)],
}


# --- helper lokal generator lama (tidak ada di Art; isi tidak berubah) ---
def car(A, cid, x, y, s):
    return (f'<g id="{cid}" transform="translate({x},{y}) scale({s})">'
            '<path class="d" d="M0,0 h400 a44,44 0 0 0 44,-44 v-90 h-104 l-86,-84 h-132 l-86,84 h-36 v90 a44,44 0 0 0 44,44 z"'
            ' fill="none" stroke="#e6f4ff" stroke-width="40"/>'
            '<circle class="d" cx="120" cy="6" r="54" fill="none" stroke="#e6f4ff" stroke-width="40"/>'
            '<circle class="d" cx="340" cy="6" r="54" fill="none" stroke="#e6f4ff" stroke-width="40"/></g>')


# ==================================================  GAMBAR 1 · JALAN & SPBU
def g1(X, A):
    txt, frame, hatch = A.txt, A.frame, A.hatch
    FW, FY = A.FW, A.FY
    return f'''        {frame("v1Frame", X)}
        {txt("v1No", X-FW//2+22, FY+52, "01", 30, "#7ef0ff", weight="700")}
        <line id="v1Ground" class="d" x1="{X-400}" y1="2150" x2="{X+400}" y2="2150" stroke="#e6f4ff" stroke-width="14"/>
        <path id="v1Hatch" class="d" d="{hatch(X-400, X+390, 2150)}" fill="none" stroke="#a9d8ff" stroke-width="4"/>
        {car(A, "v1Car1", X-400, 2120, 0.5)}{car(A, "v1Car2", X-130, 2120, 0.5)}{car(A, "v1Car3", X+140, 2120, 0.5)}
        <path id="v1Canopy" class="d" d="M{X-350},1560 H{X+300} L{X+275},1650 H{X-325} Z"
              fill="none" stroke="#e6f4ff" stroke-width="14" stroke-linejoin="round"/>
        <g id="v1Pillars">
          <line class="d" x1="{X-270}" y1="1650" x2="{X-270}" y2="2150" stroke="#e6f4ff" stroke-width="30"/>
          <line class="d" x1="{X-30}" y1="1650" x2="{X-30}" y2="2150" stroke="#e6f4ff" stroke-width="30"/>
          <line class="d" x1="{X+210}" y1="1650" x2="{X+210}" y2="2150" stroke="#e6f4ff" stroke-width="30"/>
        </g>
        <g id="v1Pumps">
          <rect class="d" x="{X-300}" y="1830" width="110" height="190" rx="12" fill="none" stroke="#e6f4ff" stroke-width="11"/>
          <rect class="d" x="{X-284}" y="1858" width="78" height="58" fill="none" stroke="#e6f4ff" stroke-width="7"/>
          <rect class="d" x="{X+20}" y="1830" width="110" height="190" rx="12" fill="none" stroke="#e6f4ff" stroke-width="11"/>
          <rect class="d" x="{X+36}" y="1858" width="78" height="58" fill="none" stroke="#e6f4ff" stroke-width="7"/>
        </g>
        {txt("v1Sign", X-25, 1628, "SPBU", 60, "#7ef0ff", anchor="middle", weight="700")}
        <g id="v1Board">
          <rect class="d" x="{X+320}" y="1830" width="90" height="320" rx="10" fill="none" stroke="#e6f4ff" stroke-width="10"/>
          <line class="d" x1="{X+334}" y1="1930" x2="{X+396}" y2="1930" stroke="#e6f4ff" stroke-width="6"/>
          <line class="d" x1="{X+334}" y1="2000" x2="{X+396}" y2="2000" stroke="#e6f4ff" stroke-width="6"/>
          <line class="d" x1="{X+334}" y1="2070" x2="{X+396}" y2="2070" stroke="#e6f4ff" stroke-width="6"/>
        </g>
        {txt("v1BoardTxt", X+365, 1900, "BBM", 28, "#7ef0ff", anchor="middle")}
        <g id="v1Tree">
          <line class="d" x1="{X-370}" y1="2150" x2="{X-370}" y2="1950" stroke="#e6f4ff" stroke-width="14"/>
          <path class="d" d="M{X-370},1950 q-62,-30 -92,12" fill="none" stroke="#e6f4ff" stroke-width="11" stroke-linecap="round"/>
          <path class="d" d="M{X-370},1950 q-6,-62 48,-74" fill="none" stroke="#e6f4ff" stroke-width="11" stroke-linecap="round"/>
          <path class="d" d="M{X-370},1950 q62,-22 82,20" fill="none" stroke="#e6f4ff" stroke-width="11" stroke-linecap="round"/>
        </g>
        <path id="v1Cloud" class="d" d="M{X+232},1512 q26,-42 68,-28 q16,-40 60,-32 q42,6 44,44 q36,10 20,46 h-192 q-26,-16 0,-30 z"
              fill="none" stroke="#a9d8ff" stroke-width="9"/>'''


# ================================================  GAMBAR 2 · MENGISI & BAYAR
def g2(X, A):
    txt, frame, hatch = A.txt, A.frame, A.hatch
    FW, FY = A.FW, A.FY
    return f'''        {frame("v2Frame", X)}
        {txt("v2No", X-FW//2+22, FY+52, "02", 30, "#7ef0ff", weight="700")}
        <line id="v2Ground" class="d" x1="{X-410}" y1="2334" x2="{X+410}" y2="2334" stroke="#e6f4ff" stroke-width="12"/>
        <path id="v2Hatch" class="d" d="{hatch(X-410, X+400, 2334)}" fill="none" stroke="#a9d8ff" stroke-width="4"/>
        {car(A, "v2Car", X-400, 2280, 0.9)}
        <g id="v2Flap">
          <rect class="d" x="{X-52}" y="2166" width="46" height="46" rx="6" fill="none" stroke="#e6f4ff" stroke-width="9"/>
          <path class="d" d="M{X-6},2166 q30,-16 36,22" fill="none" stroke="#e6f4ff" stroke-width="9"/>
        </g>
        <g id="v2Nozzle">
          <rect class="d" x="{X+12}" y="2174" width="64" height="42" rx="14" fill="none" stroke="#e6f4ff" stroke-width="11"/>
          <line class="d" x1="{X+12}" y1="2192" x2="{X-12}" y2="2192" stroke="#e6f4ff" stroke-width="11"/>
        </g>
        <path id="v2Hose" class="d" d="M{X+76},2196 C{X+156},2164 {X+186},2122 {X+230},2062"
              fill="none" stroke="#e6f4ff" stroke-width="14"/>
        <circle id="v2Drop" class="d" cx="{X-18}" cy="2242" r="10" fill="none" stroke="#7ef0ff" stroke-width="8"/>
        <rect id="v2Pump" class="d" x="{X+230}" y="1860" width="150" height="330" rx="14" fill="none" stroke="#e6f4ff" stroke-width="14"/>
        <rect id="v2Win" class="d" x="{X+252}" y="1900" width="106" height="84" fill="none" stroke="#e6f4ff" stroke-width="9"/>
        {txt("v2Dig", X+305, 1968, "0 0 4 2", 42, "#7ef0ff", anchor="middle", weight="700")}
        {txt("v2Ltr", X+305, 2044, "LITER", 26, "#cfe9ff", anchor="middle")}
        {txt("v2Tnk", X-400, 2040, "TANGKI BAHAN BAKAR", 26)}
        <g id="v2Coin">
          <circle class="d" cx="{X-300}" cy="1876" r="64" fill="none" stroke="#7ef0ff" stroke-width="12"/>
          {txt("v2Rp", X-300, 1898, "Rp", 52, "#7ef0ff", anchor="middle", weight="700")}
        </g>
        {txt("v2Pay", X-300, 1780, "MEMBAYAR", 26, "#cfe9ff", anchor="middle")}
        <g id="v2Go">
          <path class="d" d="M{X-100},2430 H{X-330}" fill="none" stroke="#7ef0ff" stroke-width="11" marker-end="url(#arc)"/>
        </g>
        {txt("v2GoTxt", X-70, 2440, "LALU PERGI", 28, "#7ef0ff")}'''


# =====================================================  GAMBAR 3 · DARI MANA
def g3(X, A):
    txt, frame, hatch = A.txt, A.frame, A.hatch
    FW, FY = A.FW, A.FY
    return f'''        {frame("v3Frame", X)}
        {txt("v3No", X-FW//2+22, FY+52, "03", 30, "#7ef0ff", weight="700")}
        <path id="v3Q" class="d" d="M{X-52},1516 A74,74 0 1 1 {X+22},1590 L{X+22},1660"
              fill="none" stroke="#7ef0ff" stroke-width="24" stroke-linecap="round"/>
        <circle id="v3Qdot" class="d" cx="{X+22}" cy="1730" r="25" fill="none" stroke="#7ef0ff" stroke-width="24"/>
        {txt("v3Title", X, 1906, "DARI MANA?", 50, "#7ef0ff", anchor="middle", weight="700")}
        <path id="v3Surf" class="d" d="M{X-380},2050 L{X-120},2050 q46,-30 92,0 q46,30 92,0 L{X+380},2050"
              fill="none" stroke="#e6f4ff" stroke-width="13" stroke-linejoin="round"/>
        <path id="v3Hatch" class="d" d="{hatch(X-380, X+380, 2050, step=86)}" fill="none" stroke="#a9d8ff" stroke-width="4"/>
        <g id="v3Sb">
          <path class="d" d="M{X-310},1958 H{X-188} L{X-200},1926 H{X-298} Z"
                fill="none" stroke="#e6f4ff" stroke-width="9" stroke-linejoin="round"/>
          <rect class="d" x="{X-294}" y="1958" width="90" height="92" fill="none" stroke="#e6f4ff" stroke-width="8"/>
        </g>
        {car(A, "v3Car", X-100, 2040, 0.16)}
        <g id="v3Strata">
          <line class="d" x1="{X-340}" y1="2150" x2="{X+380}" y2="2150" stroke="#e6f4ff" stroke-width="11"/>
          <line class="d" x1="{X-340}" y1="2270" x2="{X+380}" y2="2270" stroke="#e6f4ff" stroke-width="11"/>
          <line class="d" x1="{X-340}" y1="2390" x2="{X+380}" y2="2390" stroke="#e6f4ff" stroke-width="11"/>
          <line class="d" x1="{X-340}" y1="2510" x2="{X+380}" y2="2510" stroke="#e6f4ff" stroke-width="11"/>
        </g>
        <g id="v3Org">
          <ellipse class="d" cx="{X-220}" cy="2210" rx="36" ry="19" fill="none" stroke="#e6f4ff" stroke-width="7"/>
          <ellipse class="d" cx="{X-80}" cy="2218" rx="27" ry="15" fill="none" stroke="#e6f4ff" stroke-width="7"/>
          <ellipse class="d" cx="{X+66}" cy="2206" rx="31" ry="17" fill="none" stroke="#e6f4ff" stroke-width="7"/>
          <ellipse class="d" cx="{X+202}" cy="2214" rx="24" ry="13" fill="none" stroke="#e6f4ff" stroke-width="7"/>
        </g>
        <path id="v3Oil" class="d" d="M{X-138},2432 q130,-56 232,8 q92,52 40,112 q-60,72 -194,40 q-124,-32 -102,-96 q-16,-46 24,-64 z"
              fill="none" stroke="#7ef0ff" stroke-width="14"/>
        <g id="v3Drops">
          <circle class="d" cx="{X}" cy="2482" r="15" fill="none" stroke="#7ef0ff" stroke-width="8"/>
          <circle class="d" cx="{X+124}" cy="2512" r="11" fill="none" stroke="#7ef0ff" stroke-width="7"/>
        </g>
        <path id="v3Arrow" class="f" d="M{X+20},2358 V2112" fill="none" stroke="#7ef0ff" stroke-width="16" marker-end="url(#arc)"/>
        <g id="v3Depth">
          <line class="d" x1="{X+336}" y1="2150" x2="{X+380}" y2="2150" stroke="#a9d8ff" stroke-width="8"/>
          <line class="d" x1="{X+336}" y1="2270" x2="{X+380}" y2="2270" stroke="#a9d8ff" stroke-width="8"/>
          <line class="d" x1="{X+336}" y1="2390" x2="{X+380}" y2="2390" stroke="#a9d8ff" stroke-width="8"/>
          <line class="d" x1="{X+336}" y1="2510" x2="{X+380}" y2="2510" stroke="#a9d8ff" stroke-width="8"/>
        </g>
        {txt("v3L1", X-340, 2112, "PERMUKAAN BUMI", 26)}
        {txt("v3L2", X+86, 2244, "SISA MAKHLUK LAUT", 26)}
        {txt("v3L3", X-148, 2348, "MINYAK MENTAH", 30, "#7ef0ff")}'''


# ======================================================  GAMBAR 4 · KE MANA
def g4(X, A):
    txt, frame = A.txt, A.frame
    FW, FY = A.FW, A.FY
    return f'''        {frame("v4Frame", X)}
        {txt("v4No", X-FW//2+22, FY+52, "04", 30, "#7ef0ff", weight="700")}
        <rect id="v4Block" class="d" x="{X-390}" y="2090" width="360" height="290" rx="30" fill="none" stroke="#e6f4ff" stroke-width="14"/>
        <g id="v4Bolts">
          <circle class="d" cx="{X-354}" cy="2128" r="13" fill="none" stroke="#e6f4ff" stroke-width="8"/>
          <circle class="d" cx="{X-66}" cy="2128" r="13" fill="none" stroke="#e6f4ff" stroke-width="8"/>
          <circle class="d" cx="{X-354}" cy="2346" r="13" fill="none" stroke="#e6f4ff" stroke-width="8"/>
          <circle class="d" cx="{X-66}" cy="2346" r="13" fill="none" stroke="#e6f4ff" stroke-width="8"/>
        </g>
        <rect id="v4Cyl" class="d" x="{X-338}" y="1768" width="256" height="322" rx="16" fill="none" stroke="#e6f4ff" stroke-width="14"/>
        <g id="v4Fin">
          <line class="d" x1="{X-368}" y1="1836" x2="{X-338}" y2="1836" stroke="#a9d8ff" stroke-width="9"/>
          <line class="d" x1="{X-368}" y1="1906" x2="{X-338}" y2="1906" stroke="#a9d8ff" stroke-width="9"/>
          <line class="d" x1="{X-368}" y1="1976" x2="{X-338}" y2="1976" stroke="#a9d8ff" stroke-width="9"/>
          <line class="d" x1="{X-82}" y1="1836" x2="{X-52}" y2="1836" stroke="#a9d8ff" stroke-width="9"/>
          <line class="d" x1="{X-82}" y1="1906" x2="{X-52}" y2="1906" stroke="#a9d8ff" stroke-width="9"/>
          <line class="d" x1="{X-82}" y1="1976" x2="{X-52}" y2="1976" stroke="#a9d8ff" stroke-width="9"/>
        </g>
        <rect id="v4Head" class="d" x="{X-356}" y="1712" width="292" height="56" rx="10" fill="none" stroke="#e6f4ff" stroke-width="14"/>
        <rect id="v4Piston" class="d" x="{X-316}" y="1888" width="212" height="100" rx="12" fill="none" stroke="#e6f4ff" stroke-width="13"/>
        <g id="v4Rings">
          <line class="d" x1="{X-310}" y1="1912" x2="{X-110}" y2="1912" stroke="#e6f4ff" stroke-width="5"/>
          <line class="d" x1="{X-310}" y1="1936" x2="{X-110}" y2="1936" stroke="#e6f4ff" stroke-width="5"/>
          <line class="d" x1="{X-310}" y1="1960" x2="{X-110}" y2="1960" stroke="#e6f4ff" stroke-width="5"/>
        </g>
        <g id="v4Rod">
          <line class="d" x1="{X-210}" y1="1988" x2="{X-170}" y2="2172" stroke="#e6f4ff" stroke-width="20" stroke-linecap="round"/>
          <circle class="d" cx="{X-210}" cy="1988" r="17" fill="none" stroke="#e6f4ff" stroke-width="10"/>
          <circle class="d" cx="{X-170}" cy="2172" r="17" fill="none" stroke="#e6f4ff" stroke-width="10"/>
        </g>
        <g id="v4Crank">
          <circle class="d" cx="{X-170}" cy="2250" r="88" fill="none" stroke="#e6f4ff" stroke-width="16"/>
          <circle class="d" cx="{X-170}" cy="2250" r="20" fill="none" stroke="#e6f4ff" stroke-width="10"/>
          <line class="d" x1="{X-170}" y1="2250" x2="{X-170}" y2="2172" stroke="#e6f4ff" stroke-width="12"/>
        </g>
        <g id="v4Plug">
          <rect class="d" x="{X-236}" y="1622" width="52" height="90" rx="10" fill="none" stroke="#e6f4ff" stroke-width="12"/>
          <line class="d" x1="{X-210}" y1="1712" x2="{X-210}" y2="1800" stroke="#e6f4ff" stroke-width="10"/>
        </g>
        {txt("v4PlugTxt", X-210, 1600, "BUSI", 26, "#7ef0ff", anchor="middle")}
        <path id="v4Exh" class="d" d="M{X-64},1740 H{X+16} Q{X+60},1740 {X+60},1784 V2130"
              fill="none" stroke="#e6f4ff" stroke-width="16" stroke-linecap="round"/>
        <g id="v4Muff">
          <rect class="d" x="{X-10}" y="2130" width="330" height="130" rx="52" fill="none" stroke="#e6f4ff" stroke-width="15"/>
          <line class="d" x1="{X+60}" y1="2146" x2="{X+60}" y2="2244" stroke="#e6f4ff" stroke-width="7"/>
          <line class="d" x1="{X+140}" y1="2146" x2="{X+140}" y2="2244" stroke="#e6f4ff" stroke-width="7"/>
          <line class="d" x1="{X+220}" y1="2146" x2="{X+220}" y2="2244" stroke="#e6f4ff" stroke-width="7"/>
        </g>
        <line id="v4Tail" class="d" x1="{X+320}" y1="2195" x2="{X+376}" y2="2195" stroke="#e6f4ff" stroke-width="20" stroke-linecap="round"/>
        <g id="v4Smoke">
          <circle class="d" cx="{X+372}" cy="2106" r="40" fill="none" stroke="#7ef0ff" stroke-width="10"/>
          <circle class="d" cx="{X+360}" cy="2004" r="30" fill="none" stroke="#7ef0ff" stroke-width="9"/>
          <circle class="d" cx="{X+354}" cy="1912" r="22" fill="none" stroke="#7ef0ff" stroke-width="8"/>
        </g>
        <g id="v4Spark">
          <line class="d" x1="{X-238}" y1="1810" x2="{X-288}" y2="1858" stroke="#7ef0ff" stroke-width="12" stroke-linecap="round"/>
          <line class="d" x1="{X-210}" y1="1814" x2="{X-210}" y2="1866" stroke="#7ef0ff" stroke-width="12" stroke-linecap="round"/>
          <line class="d" x1="{X-182}" y1="1810" x2="{X-132}" y2="1858" stroke="#7ef0ff" stroke-width="12" stroke-linecap="round"/>
        </g>
        {txt("v4MesinL", X-210, 2452, "MESIN", 28, "#7ef0ff", anchor="middle")}
        {txt("v4ExhL", X+155, 2322, "KNALPOT", 28, "#7ef0ff", anchor="middle")}
        {txt("v4Asap", X+272, 1872, "ASAP", 28, "#7ef0ff", anchor="middle")}
        {txt("v4Title", X, 2570, "KE MANA?", 50, "#7ef0ff", anchor="middle", weight="700")}'''


DRAW = [g1, g2, g3, g4]

# pra-gambar VERBATIM dari generator lama — frame + no + ground/hatch
# (offset presisi di dalam jeda; jangan diganti turunan otomatis)
PRESHOW = [
    (11, 0.15, '#v2Frame', 0.55, 'd'),
    (11, 0.4, '#v2No', 0.4, 't'),
    (11, 0.55, '#v2Ground', 0.65, 'd'),
    (11, 0.8, '#v2Hatch', 0.85, 'd'),
    (16, 0.15, '#v3Frame', 0.55, 'd'),
    (16, 0.4, '#v3No', 0.4, 't'),
    (16, 0.55, '#v3Surf', 0.65, 'd'),
    (16, 0.8, '#v3Hatch', 0.85, 'd'),
    (26, 0.05, '#v4Frame', 0.4, 'd'),
    (26, 0.15, '#v4No', 0.3, 't'),
    (26, 0.2, '#v4Block', 0.65, 'd'),
]

# pemetaan kata -> potongan ucapan + suku kata — VERBATIM dari align_bab1.py
# (alokasi otomatis framework beda untuk bab ini; jangan dihapus)
GROUPS = [(0, 1), (2, 8), (9, 10), (11, 12), (13, 13), (14, 15),
          (16, 20), (21, 25), (26, 33)]
SYL = [3, 2,                      # Setiap hari,
       3, 4, 3, 1, 2, 1, 2,       # jutaan kendaraan berhenti di tempat yang sama:
       1, 2,                      # pom bensin.
       2, 3,                      # Kita mengisi,
       3,                         # membayar,
       2, 2,                      # lalu pergi.
       2, 3, 2, 4, 3,             # Tapi pernahkah kita benar-benar bertanya,
       2, 2, 3, 2, 2,             # dari mana cairan ini datang,
       1, 1, 2, 2, 2, 3, 2, 3]    # dan ke mana ia pergi setelah mesin menyala?
