"""Bangun komposisi HTML (GSAP, live-draw follow-cam) dari modul scene.

Mesin yang sama dipakai Bab 1-5 dokumenter-bensin, dirapikan jadi satu
template terpusat:

  - kamera diam saat menggambar, geser `jeda` detik di tiap batas slide;
  - pra-gambar (frame + nomor slide) digambar DI DALAM jeda;
  - caption dipatok ke rentang kata (ikut otomatis waktu/jeda berubah);
  - SFX: peta scene + whoosh otomatis di tiap pergeseran kamera.

Scene menyediakan:
  SCENE  dict metadata (lihat templates/scene)
  SLIDES daftar {"words": (awal, akhir)} per gambar
  CUES   [(kata, selector, dur, "d"|"t"|"f"), ...]
  CAPTIONS [(kata_awal, kata_akhir, teks), ...]  (opsional)
  DRAW   [fungsi_gambar(X, A) -> svg, ...]       (opsional, default polos)
  SFXMAP {kata: [(suara, gain_dB, offset), ...]} (opsional)
"""

import json
import os

from pensil.art import Art
from pensil.config import jeda_map


def scene_layout(project, scene):
    sc = scene.SCENE
    th = {**project.theme, **(sc.get("layout") or {})}
    n = len(scene.SLIDES)
    spacing = int(sc["spacing"])
    layout = {
        "spacing": spacing,
        "n": n,
        "xs": [spacing * (k + 1) for k in range(n)],
        "sw": int(sc.get("sheet_w", spacing * n + spacing // 2)),
        "sh": th["sh"],
        "cy": th["cy"],
        "frame": th["frame"],
    }
    return layout


def load_words(project, scene):
    """words-<id>-r.json (reels) jika ada, fallback words-<id>.json (diam)."""
    sid = scene.SCENE["id"]
    r = project.path("work", f"words-{sid}-r.json")
    p = project.path("work", f"words-{sid}.json")
    path = r if os.path.isfile(r) else p
    if not os.path.isfile(path):
        raise SystemExit(f"words tidak ada: {r} — jalankan `pensil timing` (+ `align` dulu)")
    spec = json.load(open(path, encoding="utf-8"))
    words = spec["words"]
    dur = spec.get("dur") or round(max(w["e"] for w in words) + 0.4, 3)
    return words, dur, spec, path


def build_captions(scene, words, dur):
    caps = []
    for i, j, t in getattr(scene, "CAPTIONS", []) or []:
        a = 0.0 if i is None else max(0.0, words[i]["t"] - 0.15)
        b = dur - 0.30 if (j < 0 or j >= len(words) - 1) else words[j + 1]["t"] - 0.15
        caps.append((round(a, 3), round(b, 3), t))
    return caps


def build_preshow(scene):
    """pra-gambar slide 2..n: frame + nomor, digambar di awal jeda.

    Scene boleh menentukan `PRESHOW` verbatim — daftar
    [(kata, offset, selector, dur, kind), ...] — untuk menggantikan turunan
    otomatis (mis. generator lama ikut pra-gambar ground/hatch, atau offset
    khusus slide pendek). Preshow menyangkut waktu jeda, jadi wajib presisi.
    """
    verbatim = getattr(scene, "PRESHOW", None)
    if verbatim is not None:
        return [tuple(x) for x in verbatim]
    out = []
    for k, sl in enumerate(scene.SLIDES[1:], start=1):
        pre = sl.get("preshow", f"v{k + 1}")
        if not pre:
            continue
        w = sl["words"][0]
        out.append((w, 0.15, f"#{pre}Frame", 0.55, "d"))
        out.append((w, 0.40, f"#{pre}No", 0.40, "t"))
    return out


def build_cam(project, scene, layout):
    jm = jeda_map(scene)
    cam = [(scene.SLIDES[0]["words"][0], layout["xs"][0], layout["cy"], 0.0)]
    for k, sl in enumerate(scene.SLIDES[1:], start=1):
        cam.append((sl["words"][0], layout["xs"][k], layout["cy"],
                    jm[sl["words"][0]]))
    return cam


def build_connectors(scene, layout, accent):
    parts = []
    xs = layout["xs"]
    y = int(scene.SCENE.get("conn_y", 2300))
    half = int(scene.SCENE.get("conn_half", layout["frame"]["w"] // 2 + 50))
    for k in range(len(xs) - 1):
        parts.append(
            f'        <path id="conn{k + 1}" class="d" '
            f'd="M{xs[k] + half},{y} H{xs[k + 1] - half}" fill="none" '
            f'stroke="{accent}" stroke-width="9" marker-end="url(#arc)"/>')
    return "\n".join(parts)


def build_sfx_events(project, scene, words, cam, preshow):
    ev = []
    for idx, items in (getattr(scene, "SFXMAP", {}) or {}).items():
        t0 = words[idx]["t"]
        for snd, g, off in items:
            ev.append({"t": round(t0 + off, 3), "s": snd, "g": g})
    for w, _x, _y, lead in cam[1:]:            # kamera mulai bergeser
        ev.append({"t": round(words[w]["t"] - lead + 0.05, 3), "s": "whoosh", "g": -10})
    for w, off, sel, _d, _k in preshow:        # kertas saat panel disiapkan
        if sel.endswith("Frame"):
            ev.append({"t": round(words[w]["t"] - jeda_map(scene)[w] + off - 0.03, 3),
                       "s": "paper", "g": -11})
    ev.sort(key=lambda e: e["t"])
    return ev


DEFS = '''<defs>
  <marker id="arc" viewBox="0 0 12 12" refX="10" refY="6" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
    <path d="M0,1 L11,6 L0,11 z" fill="__ACCENT__"/>
  </marker>
</defs>'''

HTML = '''<!doctype html>
<html lang="id">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=__VW__, height=__VH__" />
    <script src="__GSAP__"></script>
    <style>
      * { margin: 0; padding: 0; box-sizing: border-box; }
      html, body { width: __VW__px; height: __VH__px; overflow: hidden; background: __BG__; }
      .clip { position: absolute; inset: 0; width: __VW__px; height: __VH__px; }
      #root { position: relative; width: __VW__px; height: __VH__px; overflow: hidden;
              font-family: __FONT__; }
      #stage { position: absolute; inset: 0; background: __BG__; overflow: hidden; }

      #world {
        position: absolute; top: 0; left: 0; width: __SW__px; height: __SH__px;
        will-change: transform;
        background-color: __SHEET__;
        background-image:
          linear-gradient(__GRIDMIN__ 1px, transparent 1px),
          linear-gradient(90deg, __GRIDMIN__ 1px, transparent 1px),
          linear-gradient(__GRIDMAJ__ 1px, transparent 1px),
          linear-gradient(90deg, __GRIDMAJ__ 1px, transparent 1px);
        background-size: 30px 30px, 30px 30px, 150px 150px, 150px 150px;
      }
      #sheet { position: absolute; top: 0; left: 0; color: __INK2__; }

      .meta { position: absolute; color: __TEXT__; text-transform: uppercase; }
      .tlblk { top: 44px; left: 40px; }
      .bab { font-size: 32px; font-weight: 700; letter-spacing: 6px; color: __ACCENT__; }
      .ttl { font-size: 20px; letter-spacing: 6px; margin-top: 8px; opacity: .9; }
      .trblk { top: 52px; right: 40px; text-align: right; font-size: 18px;
               letter-spacing: 4px; opacity: .7; line-height: 1.7; }

      #opening { position: absolute; inset: 0; display: flex; flex-direction: column;
                 align-items: center; justify-content: center; opacity: 0; }
      #opening .t1 { font-size: 104px; font-weight: 700; letter-spacing: 12px;
                     color: __TEXT2__; text-align: center; line-height: 1.05;
                     text-shadow: 0 6px 34px rgba(0,0,0,.95); }
      #opening .t2 { margin-top: 22px; font-size: 30px; letter-spacing: 9px;
                     color: __ACCENT__; text-align: center; }
      /* kartu hook: pertanyaan besar, bab + judul jadi subjudul */
      #opening.hook .t1 { font-size: 44px; letter-spacing: 2.5px; line-height: 1.32;
                          max-width: 980px; }
      #opening.hook .t2 { font-size: 24px; letter-spacing: 7px; margin-top: 26px; }

      #caps > div {
        position: absolute; left: 0; right: 0; bottom: __CAPBOT__px; top: auto; height: auto;
        width: __VW__px;
        padding: 14px 60px; text-align: center;
        font-size: __CAPSIZE__px; letter-spacing: 2px; color: __TEXT2__;
        text-transform: uppercase; line-height: 1.36;
        text-shadow: 0 3px 16px rgba(0,0,0,.98), 0 0 22px rgba(0,0,0,.9);
      }

      /* PENTING: #barwrap ikut class="clip" sehingga ikut inset:0 (top:0). */
      #barwrap { position: absolute; left: 0; right: auto; top: auto; bottom: 0;
                 width: __VW__px; height: __BARH__px;
                 background: rgba(255,255,255,.13); }
      #bar { position: absolute; left: 0; top: 0; width: __VW__px; height: __BARH__px;
             background: linear-gradient(90deg, __ACCENT__, __TEXT2__); transform-origin: 0 50%; }
      #vig { position: absolute; inset: 0; pointer-events: none;
             background: radial-gradient(ellipse at center, rgba(0,0,0,0) 56%, rgba(0,0,0,.38) 100%); }
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="__TLID__" data-start="0" data-duration="__DUR__"
         data-width="__VW__" data-height="__VH__">

      <div id="stage" class="clip" data-start="0" data-duration="__DUR__" data-track-index="0">
        <div id="world">
          <svg id="sheet" width="__SW__" height="__SH__" viewBox="0 0 __SW__ __SH__"
               xmlns="http://www.w3.org/2000/svg">
            __DEFS__
__SHEETSVG__
          </svg>
        </div>
      </div>

      <div id="hud" class="clip" data-start="0" data-duration="__DUR__" data-track-index="1">
__HUD__
__OPEN__
      </div>

      <div id="caps" class="clip" data-start="0" data-duration="__DUR__" data-track-index="2">
__CAPS__
      </div>

      <div id="barwrap" class="clip" data-start="0" data-duration="__DUR__" data-track-index="3">
        <div id="bar"></div>
      </div>
      <div id="vig"></div>

__AUDIO__
    </div>

    <script>
      window.__timelines = window.__timelines || {};
      const tl = gsap.timeline({ paused: true });
      const VW = __VW__, VH = __VH__;
      const world = document.getElementById("world");

      /* live-draw: garis disembunyikan lewat dash */
      document.querySelectorAll(".d").forEach(function (el) {
        var L = 0;
        try { L = el.getTotalLength(); } catch (e) { L = 0; }
        if (!L || !isFinite(L)) { var b = el.getBBox(); L = 2 * (b.width + b.height) + 24; }
        el.style.strokeDasharray = L + " " + L;
        el.style.strokeDashoffset = L;
      });
      document.querySelectorAll(".t, .f, #caps > div").forEach(function (el) {
        el.style.opacity = 0;
      });

      const WORDS = [__WORDS__];
      const JEDA = __JEDA__;
      const LEAD = __LEAD__;
      const CUES = [
  __CUES__
      ];
      CUES.forEach(function (c) {
        var t = WORDS[c[0]].t, sel = c[1], dur = c[2], kind = c[3];
        if (kind === "t") {
          tl.to(sel, { opacity: 1, duration: dur, ease: "power1.out" }, t);
        } else {
          tl.to(sel, { strokeDashoffset: 0, duration: dur, ease: "power1.inOut" }, t);
        }
      });

      /* pra-gambar: digambar di dalam jeda, sebelum kalimat berikutnya mulai */
      const PRESHOW = [
  __PRESHOW__
      ];
      PRESHOW.forEach(function (c) {
        var t = WORDS[c[0]].t - JEDA[c[0]] + c[1], sel = c[2], dur = c[3], kind = c[4];
        if (kind === "t") {
          tl.to(sel, { opacity: 1, duration: dur, ease: "power1.out" }, t);
        } else {
          tl.to(sel, { strokeDashoffset: 0, duration: dur, ease: "power1.inOut" }, t);
        }
      });

      /* ---- kamera: diam saat menggambar, geser pelan ke gambar berikutnya ---- */
      const CAM = [
  __CAM__
      ];
      CAM.forEach(function (k) {
        var w = k[0], t = WORDS[w].t, lead = k[3];
        var tx = VW / 2 - k[1], ty = VH / 2 - k[2];
        if (k === CAM[0]) {
          gsap.set(world, { x: tx, y: ty });
          return;
        }
        /* geser pas di jeda: berangkat saat jeda mulai, tiba saat kalimat mulai */
        tl.to(world, { x: tx, y: ty, duration: lead, ease: "power2.inOut" },
              Math.max(0, t - lead));
      });

__OPENJS__

      var CAPS = [
__CAPSJS__
      ];
      CAPS.forEach(function (c) {
        var el = document.getElementById(c[0]);
        if (!el) return;
        tl.to(el, { opacity: 1, duration: 0.32, ease: "power1.out" }, c[1] + 0.05);
        tl.to(el, { opacity: 0, duration: 0.26, ease: "power1.in" }, c[2] - 0.26);
      });

      tl.fromTo("#bar", { scaleX: 0 },
                { scaleX: 1, duration: __DUR__, ease: "none", transformOrigin: "0px 50%" }, 0);

      window.__timelines["__TLID__"] = tl;
      tl.seek(0);
    </script>
  </body>
</html>
'''


def compose(project, scene, write_events=True):
    sc = scene.SCENE
    sid = sc["id"]
    vw, vh = project.canvas["w"], project.canvas["h"]
    th = {**project.theme, **(sc.get("layout") or {})}
    layout = scene_layout(project, scene)
    A = Art(layout, th)

    words, dur, _spec, words_path = load_words(project, scene)
    cam = build_cam(project, scene, layout)
    preshow = build_preshow(scene)
    caps = build_captions(scene, words, dur)

    # ---------------------------------------------------------- lembar SVG
    parts = []
    for k, fn in enumerate(getattr(scene, "DRAW", []) or []):
        parts.append(fn(layout["xs"][k], A))
    if scene.SCENE.get("connectors", True) and len(layout["xs"]) > 1:
        parts.append(build_connectors(scene, layout, th["accent"]))
    extra = sc.get("extra_svg")
    if extra:
        parts.append(extra(A) if callable(extra) else extra)
    sheet_svg = "\n".join(parts)

    # ---------------------------------------------------------------- HUD
    hud = sc.get("hud_left")
    hud_html = ""
    if hud:
        hud_html = (f'        <div class="meta tlblk">\n'
                    f'          <div class="bab">{hud[0]}</div>\n'
                    f'          <div class="ttl">{hud[1]}</div>\n'
                    f'        </div>')
    if sc.get("hud_right"):
        hud_html += (f'\n        <div class="meta trblk">{sc["hud_right"]}</div>')

    hook = sc.get("hook")            # pertanyaan pembuka — jadi teks utama kartu
    opening = sc.get("opening") or (tuple(hud) if hud else None)
    open_cls = ""
    if hook:
        sub = (f"{hud[0]} · {hud[1]}" if hud
               else (opening[1] if opening else project.name))
        opening = (hook, sub)
        open_cls = ' class="hook"'
    open_html, open_js = "", ""
    if opening:
        open_html = (f'        <div id="opening"{open_cls}>\n'
                     f'          <div class="t1">{opening[0]}</div>\n'
                     f'          <div class="t2">{opening[1]}</div>\n'
                     f'        </div>')
        open_js = (f'      tl.fromTo("#opening", {{ opacity: 0, scale: 0.96 }},\n'
                   f'                {{ opacity: 1, scale: 1, duration: 0.6, ease: "power2.out" }}, 0.2);\n'
                   f'      tl.to("#opening", {{ opacity: 0, duration: 0.5, ease: "power1.in" }}, '
                   f'LEAD + 0.25);')

    # -------------------------------------------------------------- audio
    audio_tags = []
    events = build_sfx_events(project, scene, words, cam, preshow) \
        if sc.get("sfx", True) and (getattr(scene, "SFXMAP", None) or sc.get("sfx_auto", True)) else []
    sfx_name = None
    if events:
        from pensil import sfx as S
        sfx_path = S.build_bed(project, events, dur, sid)
        sfx_name = os.path.basename(sfx_path)
        if write_events:
            json.dump({"slug": sid, "dur": dur, "events": events},
                      open(project.path("work", f"sfx-{sid}.json"), "w",
                           encoding="utf-8"), ensure_ascii=False)
        audio_tags.append(
            f'      <audio id="sfx" src="{project.audio_prefix}/{sfx_name}"\n'
            f'             data-start="0" data-duration="{dur}" data-track-index="8" data-volume="1"></audio>')

    vo_raw = sc.get("vo_raw")
    if vo_raw:
        aligned = os.path.splitext(vo_raw)[0] + "-r.mp3"
        aligned_path = project.path("work", aligned)
        vo_name = aligned if os.path.isfile(aligned_path) else vo_raw
        audio_tags.append(
            f'      <audio id="vo" src="{project.work_prefix}/{vo_name}"\n'
            f'             data-start="0" data-duration="{dur}" data-track-index="9" data-volume="1"></audio>')

    # ------------------------------------------------------------- potongan
    cues_js = ",\n  ".join(f'[{w}, {json.dumps(s)}, {d}, {json.dumps(k)}]'
                           for w, s, d, k in getattr(scene, "CUES", []) or [])
    words_js = ", ".join(f'{{t:{w["t"]}}}' for w in words)
    cam_js = ",\n  ".join(f'[{w}, {x}, {y}, {lead}]' for w, x, y, lead in cam)
    jm = jeda_map(scene)
    jeda_js = "{" + ", ".join(f"{k}: {v}" for k, v in sorted(jm.items())) + "}"
    preshow_js = ",\n  ".join(f'[{w}, {off}, {json.dumps(sel)}, {d}, {json.dumps(k)}]'
                              for w, off, sel, d, k in preshow)
    caps_html = "\n".join(
        f'        <div id="c{i}" class="clip" data-start="{a}" '
        f'data-duration="{b - a:.2f}">{t}</div>'
        for i, (a, b, t) in enumerate(caps))
    caps_js = ",\n".join(f'  ["c{i}", {a}, {b}]' for i, (a, b, _t) in enumerate(caps))

    # ---- peringatan: animasi yang selesai setelah akhir video (akan terpotong)
    _end = 0.0
    for w, _sel, d, _k in (getattr(scene, "CUES", []) or []):
        _end = max(_end, words[int(w)]["t"] + float(d))
    for w, off, _sel, d, _k in preshow:
        _end = max(_end, words[int(w)]["t"] - jm.get(int(w), 0.0) + float(off) + float(d))
    if _end > dur - 0.05:
        print(f"  PERINGATAN: animasi terakhir selesai {_end:.2f}s > dur {dur:.2f}s "
              f"— AKAN TERPOTONG di batas video! Tambah SCENE['tail'] (senyap ekor, "
              f"butuh {round(_end - dur + 0.6, 2)}s) atau pendekkan cue terakhir.")

    html = HTML
    for ph, val in [
        ("__GSAP__", project.audio_prefix + "/../gsap.min.js"),
        ("__VW__", vw), ("__VH__", vh),
        ("__BG__", th["bg"]), ("__SHEET__", th["sheet"]),
        ("__GRIDMIN__", th["grid_minor"]), ("__GRIDMAJ__", th["grid_major"]),
        ("__FONT__", th["font"]), ("__INK2__", th["ink2"]),
        ("__TEXT__", th["text"]), ("__TEXT2__", th["text2"]),
        ("__ACCENT__", th["accent"]),
        ("__CAPSIZE__", th["caption_size"]), ("__CAPBOT__", th["caption_bottom"]),
        ("__BARH__", th["bar_h"]),
        ("__SW__", layout["sw"]), ("__SH__", layout["sh"]),
        ("__TLID__", sid), ("__DUR__", dur),
        ("__DEFS__", DEFS.replace("__ACCENT__", th["accent"])),
        ("__SHEETSVG__", sheet_svg),
        ("__HUD__", hud_html), ("__OPEN__", open_html), ("__OPENJS__", open_js),
        ("__CAPS__", caps_html), ("__AUDIO__", "\n".join(audio_tags)),
        ("__WORDS__", words_js), ("__JEDA__", jeda_js),
        ("__LEAD__", float(sc.get("lead", 0.0))),
        ("__CUES__", cues_js), ("__CAM__", cam_js),
        ("__CAPSJS__", caps_js), ("__PRESHOW__", preshow_js),
    ]:
        html = html.replace(ph, str(val))

    for ph in ("__GSAP__", "__VW__", "__VH__", "__BG__", "__SHEET__",
               "__GRIDMIN__", "__GRIDMAJ__", "__FONT__", "__INK2__", "__TEXT__",
               "__TEXT2__", "__ACCENT__", "__CAPSIZE__", "__CAPBOT__", "__BARH__",
               "__SW__", "__SH__", "__TLID__", "__DUR__", "__DEFS__", "__SHEETSVG__",
               "__HUD__", "__OPEN__", "__OPENJS__", "__CAPS__", "__AUDIO__",
               "__WORDS__", "__JEDA__", "__LEAD__", "__CUES__", "__CAM__",
               "__CAPSJS__", "__PRESHOW__"):
        assert ph not in html, ph

    os.makedirs(project.compositions_dir, exist_ok=True)
    out = os.path.join(project.compositions_dir, f"{sid}.html")
    open(out, "w", encoding="utf-8").write(html)
    return {"out": out, "dur": dur, "cues": len(getattr(scene, "CUES", []) or []),
            "sfx": len(events), "cam": len(cam), "words_path": words_path}
