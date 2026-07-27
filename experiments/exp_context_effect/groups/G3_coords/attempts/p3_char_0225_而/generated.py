"""
而 (er) — 6 strokes. Reference-only bank (v8): inline fresh.

Decomposition from GT PNG:
  1. 一 top horizontal (long)
  2. 丿 short pie descending from just below top-left
  3. 丨 left vertical of the enclosure (below top heng)
  4. 横折钩 top-inner heng + right vertical + small left hook at bottom
  5. 丨 inner-left vertical (inside the frame)
  6. 丨 inner-right vertical

Widths kept moderate (~4-5 px) to match MMH-style thin ink in GT.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(p0, p1, w=5):
    d.line([p0, p1], fill="black", width=w)

def poly(pts, w=5):
    d.line(pts, fill="black", width=w, joint="curve")

# 1) Top 横 — long horizontal, slight taper by drawing two overlapped lines
line((45, 80), (255, 80), w=5)

# 2) Short 丿 — descends from just below the top, left of center
poly([(105, 100), (95, 118), (78, 138)], w=5)

# 3) Left 丨 of outer frame
line((55, 120), (55, 260), w=5)

# 4) 横折钩 — inner top horizontal + right vertical + small left hook
poly([(70, 120), (250, 120), (250, 245), (238, 260)], w=5)

# 5) Inner-left 丨
line((120, 135), (120, 255), w=5)

# 6) Inner-right 丨
line((185, 135), (185, 255), w=5)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0225_而/01_而.png")
