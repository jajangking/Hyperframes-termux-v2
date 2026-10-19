"""Bangun index.html root dari daftar scene di project.json.

Durasi tiap scene diambil dari komposisi hasil `pensil gen`
(data-duration pada <div id="root" ...> komposisi anak).
"""

import os
import re

TEMPLATE = '''<!DOCTYPE html>
<html lang="id">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=__VW__, height=__VH__">
    <script src="__GSAP__"></script>
    <style>
      * { margin: 0; padding: 0; box-sizing: border-box; }
      html, body { width: __VW__px; height: __VH__px; overflow: hidden; background: __BG__; }
      #root { position: relative; width: __VW__px; height: __VH__px; overflow: hidden; }
      .host { position: absolute; left: 0; top: 0; width: __VW__px; height: __VH__px; }
    </style>
  </head>
  <body>
    <!-- Dibuat `python3 -m pensil index` — jangan diedit tangan. -->
    <div id="root" data-composition-id="__NAME__" data-start="0" data-duration="__TOTAL__"
         data-width="__VW__" data-height="__VH__">
__HOSTS__
    </div>
    <script>
      window.__timelines = window.__timelines || {};
      window.__timelines["__NAME__"] = gsap.timeline({ paused: true });
      window.__timelines["__NAME__"].seek(0);
    </script>
  </body>
</html>
'''


def comp_duration(project, sid):
    f = os.path.join(project.compositions_dir, f"{sid}.html")
    if not os.path.isfile(f):
        raise SystemExit(f"komposisi belum ada: {f} — jalankan `pensil gen` dulu")
    m = re.search(r'data-duration="([\d.]+)"', open(f, encoding="utf-8").read())
    return float(m.group(1))


def scene_offsets(project):
    """[(sid, mulai, durasi)] sesuai urutan di project.json."""
    out, t = [], 0.0
    for sf in project.scenes:
        sid = os.path.basename(sf).replace(".py", "")
        d = comp_duration(project, scene_id_of(project, sf))
        out.append((sid, t, d))
        t = round(t + d, 3)
    return out


def scene_id_of(project, scene_file):
    from pensil.config import load_scene
    return load_scene(project, scene_file).SCENE["id"]


def build_index(project):
    vw, vh = project.canvas["w"], project.canvas["h"]
    hosts, total = [], 0.0
    for sf in project.scenes:
        sid = scene_id_of(project, sf)
        d = comp_duration(project, sid)
        hosts.append(
            f'      <div id="{sid}host" class="host" data-composition-id="{sid}"\n'
            f'           data-composition-src="{project.paths["compositions"]}/{sid}.html"\n'
            f'           data-start="{total}" data-duration="{d}" data-track-index="0"></div>')
        total = round(total + d, 3)
    html = (TEMPLATE
            .replace("__VW__", str(vw)).replace("__VH__", str(vh))
            .replace("__GSAP__", project.gsap)
            .replace("__BG__", project.theme["bg"])
            .replace("__NAME__", project.name)
            .replace("__TOTAL__", str(total))
            .replace("__HOSTS__", "\n".join(hosts)))
    out = os.path.join(project.root, "index.html")
    open(out, "w", encoding="utf-8").write(html)
    return {"out": out, "total": total, "scenes": len(hosts)}
