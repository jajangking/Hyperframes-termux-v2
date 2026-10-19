"""Muat konfigurasi proyek (project.json) + modul scene (scenes/*.py)."""

import importlib.util
import json
import os

DEFAULT_THEME = {
    "bg": "#082a4e",
    "sheet": "#0b2f56",
    "grid_minor": "rgba(255,255,255,.05)",
    "grid_major": "rgba(255,255,255,.1)",
    "ink": "#e6f4ff",
    "ink2": "#a9d8ff",
    "accent": "#7ef0ff",
    "text": "#cfe9ff",
    "text2": "#eaf6ff",
    "font": '"DejaVu Sans Mono", "Liberation Mono", monospace',
    "caption_size": 34,
    "caption_bottom": 26,
    "bar_h": 10,
    # tata letak lembar (koordinat SVG)
    "cy": 2000,          # titik tengah kamera (vertikal)
    "sh": 4060,          # tinggi lembar
    "frame": {"w": 840, "y": 1400, "h": 1200},   # bingkai tiap gambar
}

DEFAULT_PROJECT = {
    "name": "proyek-baru",
    "canvas": {"w": 1080, "h": 1920},
    "paths": {
        "vo": "assets/vo",            # naskah + VO mentah + words-*.json
        "audio": "assets/audio",      # pustaka SFX + bed per scene
        "work": "assets/vo",          # keluaran timing/align (words-<id>-r, vo -r)
        "compositions": "compositions",
        "gsap": "assets/gsap.min.js", # dipakai index.html root (path relatif root)
        # awalan path dipakai di dalam HTML komposisi (relatif ke compositions/)
        "work_prefix": "../assets/vo",
        "audio_prefix": "../assets/audio",
    },
    "scenes": [],                     # daftar file scene (urut = urutan tayang)
    "theme": {},
    "browser": None,                  # path chromium utk lint/snapshot (default $PREFIX/bin/chromium-browser)
    "verify": {"ink_min": 0.8, "centroid_max": 200},
}


class Project:
    def __init__(self, root, cfg):
        self.root = root
        self.cfg = cfg
        self.name = cfg["name"]
        self.canvas = cfg["canvas"]
        self.theme = {**DEFAULT_THEME, **(cfg.get("theme") or {})}
        p = {**DEFAULT_PROJECT["paths"], **(cfg.get("paths") or {})}
        self.paths = {k: v for k, v in p.items() if k not in ("work_prefix", "audio_prefix")}
        self.gsap = self.paths.get("gsap", "assets/gsap.min.js")
        self.work_prefix = p["work_prefix"]
        self.audio_prefix = p["audio_prefix"]
        self.browser = cfg.get("browser") or os.path.join(
            os.environ.get("PREFIX", ""), "bin", "chromium-browser")
        self.verify_cfg = {**DEFAULT_PROJECT["verify"], **(cfg.get("verify") or {})}

    def path(self, key, *parts):
        p = self.paths[key]
        if not os.path.isabs(p):
            p = os.path.join(self.root, p)
        return os.path.join(p, *parts) if parts else p

    @property
    def scenes(self):
        return self.cfg.get("scenes") or []

    @property
    def compositions_dir(self):
        return self.path("compositions")


def find_project(start=None):
    """Cari project.json ke atas dari start (default cwd)."""
    d = os.path.abspath(start or os.getcwd())
    while True:
        f = os.path.join(d, "project.json")
        if os.path.isfile(f):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            raise SystemExit("project.json tidak ditemukan — jalankan di dalam proyek atau buat dulu: python3 -m pensil init <dir>")
        d = parent


def load_project(root=None):
    root = root or find_project()
    cfg = json.load(open(os.path.join(root, "project.json"), encoding="utf-8"))
    merged = {**DEFAULT_PROJECT, **cfg}
    return Project(root, merged)


SCENE_REQUIRED = ("id",)


def load_scene(project, scene_file):
    """Impor modul scene. scene_file relatif terhadap root proyek."""
    path = scene_file if os.path.isabs(scene_file) else os.path.join(project.root, scene_file)
    if not os.path.isfile(path):
        raise SystemExit(f"scene tidak ada: {path}")
    name = "pensil_scene_" + os.path.basename(path).replace(".py", "").replace("-", "_")
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    for k in SCENE_REQUIRED:
        if not hasattr(mod, "SCENE") or k not in mod.SCENE:
            raise SystemExit(f"{path}: SCENE['{k}'] wajib diisi")
    if not hasattr(mod, "SLIDES") or not mod.SLIDES:
        raise SystemExit(f"{path}: SLIDES (daftar rentang kata per slide) wajib diisi")
    if not hasattr(mod, "DRAW") or not mod.DRAW:
        raise SystemExit(f"{path}: DRAW (daftar fungsi gambar) wajib diisi")
    if len(mod.DRAW) != len(mod.SLIDES):
        raise SystemExit(f"{path}: jumlah DRAW ({len(mod.DRAW)}) != SLIDES ({len(mod.SLIDES)})")
    mod.SCENE.setdefault("jeda", 1.8)
    mod.SCENE.setdefault("lead", 0.0)
    mod.SCENE.setdefault("spacing", 1600)
    return mod


def jeda_map(scene):
    """{kata_pertama_slide: durasi_jeda} — dipakai align + kamera."""
    jeda = scene.SCENE["jeda"]
    out = {}
    for k, sl in enumerate(scene.SLIDES[1:], start=1):
        w = sl["words"][0]
        out[w] = float(sl.get("jeda", jeda[k] if isinstance(jeda, (list, tuple)) else jeda))
    return out
