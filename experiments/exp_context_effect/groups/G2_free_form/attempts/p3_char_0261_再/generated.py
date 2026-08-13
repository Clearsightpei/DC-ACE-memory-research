"""再 — 6 strokes.
Revised: clarify inner box with two internal horizontals; put small
top horizontal on top box; long middle horizontal is widest; central
vertical descends from the middle horizontal down to bottom with hook.

Structure (matching GT):
  1. 一 (short top horizontal — the very top cap)
  2. 丿-ish left drop (from top-left of box down slightly)
  3. 横折钩 (top edge horizontal + right vertical down with UP-LEFT hook)
  4. 长横 (wide middle horizontal, extends far past sides)
  5. 竖 (central vertical, from top box down through bottom)
  6. 横 (small horizontal inside lower box, between long horizontal and hook end)
"""
from PIL import Image, ImageDraw
import random

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

random.seed(7)

def brush(pts, width=8):
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i + 1]], fill="black", width=width)
    for x, y in pts:
        r = width / 2
        draw.ellipse([x - r, y - r, x + r, y + r], fill="black")

def wob(x1, y1, x2, y2, segs=10, j=1.4):
    return [
        (x1 + (x2 - x1) * (i / segs) + random.uniform(-j, j),
         y1 + (y2 - y1) * (i / segs) + random.uniform(-j, j))
        for i in range(segs + 1)
    ]

# 1. Top short horizontal (the cap)
brush(wob(105, 45, 210, 48, segs=8, j=1.0), width=8)

# 2. Left drop: from top area going down (this becomes the left side)
#    In 再, this is a short 丿 or vertical starting near the top cap.
brush(wob(100, 55, 78, 105, segs=6, j=1.2), width=8)

# 3. 横折钩 — top edge horizontal (short) + long right vertical + UP-LEFT hook
#    Horizontal: starts where cap ends, goes right a bit
brush(wob(122, 72, 218, 75, segs=8, j=1.2), width=8)
#    Vertical down
brush(wob(218, 75, 214, 235, segs=12, j=1.4), width=8)
#    Hook flick UP-and-LEFT
brush(wob(214, 235, 196, 218, segs=4, j=0.8), width=8)

# 4. Long middle horizontal — the widest stroke
brush(wob(35, 152, 268, 155, segs=14, j=1.4), width=9)

# 5. Central vertical — from top box down past bottom (descends through)
brush(wob(148, 82, 150, 250), width=8)

# 6. Two inner horizontals: one in the top compartment, one in the bottom
#    Top compartment inner horizontal (between top edge and long middle):
brush(wob(100, 115, 210, 117, segs=8, j=1.0), width=7)
#    Bottom compartment inner horizontal (between long middle and bottom):
brush(wob(100, 200, 208, 202, segs=8, j=1.0), width=7)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0261_再/01_再.png")
print("saved")
