# 市 (shì) — bank entry (B7 curator promotion, main PASS)
# Source: groups/G3_coords/attempts/p3_char_0200_市/generated.py
# Note: 5 (top dot + heng + shu-gou spine + side dots; PIL inline)
# v8 signature freedom — this file preserves the drawer's original
# module-level script form; callable via `exec(open(...).read())` or
# copy the drawing block into a new function.

"""市 (shi, market) — G3 attempt, p3_char_0200.

Decomposition (5 strokes):
  1. 点 — small dot at top, upper-right of center
  2. 一 — wide horizontal, spans most of canvas width, slight downturn on right
  3. 竖 — short left vertical of the 冂 box
  4. 横折钩 — top+right of the 冂, with small leftward hook at bottom
  5. 丨 — long central vertical, extends from top-horizontal down past the box

Inline PIL. Trust GT — thin uniform widths, no bank helper needed.
"""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
WID = 5  # thin uniform width matching GT

def line(p0, p1, w=WID):
    d.line([p0, p1], fill=INK, width=w)

def poly(points, w=WID):
    d.line(points, fill=INK, width=w, joint="curve")

# 1. 点 — small diagonal dot at top, upper-right of center
line((165, 55), (185, 80), w=6)

# 2. 一 — wide horizontal top stroke, slight downturn on right
poly([(45, 115), (150, 108), (255, 118)], w=6)

# 3. 竖 — left vertical of the 冂 (starts just under top 一, ends at box bottom)
line((90, 135), (90, 225), w=5)

# 4. 横折钩 — top-right corner: short horizontal then down, then small hook
poly([(90, 135), (215, 135), (215, 225), (195, 220)], w=5)

# 5. 丨 — central long vertical, from just below top 一 down past box bottom
line((150, 130), (150, 275), w=6)

# save
out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_市.png"))
