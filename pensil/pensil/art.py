"""Pustaka gambar live-draw (SVG path builder + elemen kecil).

Semua koordinat bersifat absolut di ruang lembar; gambar per-slide sebaiknya
relatif terhadap X (titik tengah gambar) supaya kamera (yang memusatkan X)
selalu tepat di tengah konten.

Scene memakai objek Art (argumen `A` tiap fungsi gambar) yang sudah diisi
tata letak + warna oleh generator.
"""


class Art:
    def __init__(self, layout, colors):
        # layout: cy, sh, frame{w,y,h}, sw
        self.CY = layout["cy"]
        self.SH = layout["sh"]
        self.SW = layout.get("sw", 0)
        self.FW = layout["frame"]["w"]
        self.FY = layout["frame"]["y"]
        self.FH = layout["frame"]["h"]
        self.ink = colors["ink"]
        self.ink2 = colors["ink2"]
        self.accent = colors["accent"]
        self.text = colors["text"]
        self.text2 = colors["text2"]

    # ------------------------------------------------------------- elemen
    def txt(self, tid, x, y, t, size=26, fill=None, anchor="start", weight="normal"):
        fill = fill or self.text
        return (f'<text id="{tid}" class="t" x="{x}" y="{y}" fill="{fill}" font-size="{size}"'
                f' letter-spacing="3" text-anchor="{anchor}" font-weight="{weight}"'
                f' font-family=\'DejaVu Sans Mono\', monospace">{t}</text>')

    def frame(self, fid, X):
        return (f'<rect id="{fid}" class="d" x="{X - self.FW // 2}" y="{self.FY}"'
                f' width="{self.FW}" height="{self.FH}"'
                f' fill="none" stroke="{self.ink2}" stroke-width="5" opacity=".5"/>')

    # ------------------------------------------------------------- path builder
    def hatch(self, x0, x1, y, step=78, ln=40):
        p, x = "", x0
        while x <= x1:
            p += f"M{x},{y} l{ln},{ln}"
            x += step
        return p

    def wave(self, x0, x1, y, amp=18):
        """garis berombak horizontal (permukaan cairan)"""
        n = int((x1 - x0) / (2 * amp * 2))
        p = f"M{x0},{y} q{amp},{-amp} {amp * 2},0"
        for _ in range(n - 1):
            p += f" t{amp * 2},0"
        return p

    def zig(self, xc, yc, n=5, w=26, h=34):
        """petir/zigzag kecil di sekitar (xc, yc)"""
        x = xc - n * w // 2
        p = f"M{x},{yc}"
        for i in range(n):
            p += f" l{w // 2},{h if i % 2 == 0 else -h} l{w // 2},{-h if i % 2 == 0 else h}"
        return p

    def drop(self, xc, ytop, s=1.0):
        """tetesan cairan (xc = sumbu, ytop = puncak)"""
        return (f"M{xc},{ytop} c{-46*s},{62*s} {-66*s},{96*s} {-66*s},{130*s}"
                f" a{66*s},{66*s} 0 0 0 {132*s},0 c0,{-34*s} {-20*s},{-68*s} {-66*s},{-130*s} z")

    def derrick(self, xc, ytop, ybot, half=110):
        """menara bor segitiga berpagar silang, xc = sumbu, ytop = puncak"""
        p = (f"M{xc-half},{ybot} L{xc},{ytop} L{xc+half},{ybot}"
             f" M{xc-half},{ybot} H{xc+half}")
        n = 4
        for i in range(n):
            y0 = ybot - (ybot - ytop) * i / n
            y1 = ybot - (ybot - ytop) * (i + 1) / n
            w0 = half * (ybot - y0) / (ybot - ytop)
            w1 = half * (ybot - y1) / (ybot - ytop)
            p += f" M{xc-w0},{y0} L{xc+w1},{y1} M{xc+w0},{y0} L{xc-w1},{y1}"
        return p

    def flame(self, xc, ybase, s=1.0):
        """lidah api sederhana, (xc, ybase) = titik dasar"""
        return (f"M{xc},{ybase} c{-40*s},{-30*s} {-46*s},{-70*s} {-16*s},{-110*s}"
                f" c{-8*s},{38*s} {10*s},{46*s} {22*s},{22*s}"
                f" c{12*s},{-28*s} {34*s},{-16*s} {30*s},{14*s}"
                f" c{22*s},{-6*s} {30*s},{30*s} {-20*s},{52*s} z")

    def cloud(self, xc, yc, s=1.0):
        """awan asap (busur-busur bulat berpagar)"""
        return (f"M{xc-70*s},{yc} a{30*s},{30*s} 0 1 1 {60*s},{-20*s}"
                f" a{36*s},{36*s} 0 1 1 {58*s},{18*s}"
                f" a{28*s},{28*s} 0 1 1 {-40*s},{26*s}"
                f" a{30*s},{30*s} 0 1 1 {-78*s},{-24*s} z")
