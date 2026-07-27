"""p3_char_0046_久 — G3 first attempt.

久 is a 3-stroke character:
  1. Short 撇 at top (from upper mid-right, sweeping down-left).
  2. Middle stroke: a small 横撇 (short heng, then hook down-left) —
     starts where stroke 1 ended, goes right then curls down-left.
  3. Long 捺 sweeping from the middle-crossing area down-right.

Strokes 2 and 3 kiss/cross near the character center. We compute
the crossing pixel with kiss_apex-style logic so the 撇-tail of
stroke 2 and the head of stroke 3 share a pixel.
"""
import sys, os
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                "..", "..", "success_bank", "code"))
from _shared_helpers import variant_pie, variant_na, tapered_line, to_px

CANVAS = 300
img = Image.new("RGB", (CANVAS, CANVAS), "white")
draw = ImageDraw.Draw(img)

# Revised: shift character down, expand to fill canvas, make top pie
# more prominent (it sweeps from upper-right to lower-left, longer),
# and extend the na further down-right to the corner region.

# ---- Stroke 1: top 撇 (upper right area, sweeping down-left long) ----
# GT: head PIL(155,45), tail PIL(80,140). math: head=(+5,+105), tail=(-70,+10)
variant_pie(draw,
            head=(+5, +105),
            tail=(-70, +10),
            bow_perp=-8, w_head=9, w_tail=1)

# ---- Stroke 2: middle 横撇 (short heng then curl down-left) ----
# Positioned in upper-middle: heng from math(-25,+40) to math(+40,+45)
# Then 撇 curling down-left to math(-60,-40)
heng_start = (-25, +40)
heng_end = (+40, +45)
tapered_line(draw, heng_start, heng_end, w0=5, w1=8)

# small 顿笔 blob at corner
cx, cy = to_px(heng_end[0], heng_end[1])
r = 5
draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

# 撇 continuation from corner sweeping down-left
pie2_head = (heng_end[0] - 2, heng_end[1] - 2)
pie2_tail = (-70, -50)
variant_pie(draw,
            head=pie2_head,
            tail=pie2_tail,
            bow_perp=-10, w_head=8, w_tail=1)

# ---- Stroke 3: long 捺 sweeping from mid crossing down-right to corner ----
# The 捺 head kisses the stroke-2 pie around its midpoint.
# From math(-10, -20) sweeping down-right to math(+100, -125).
na_head = (-10, -20)
na_tail = (+105, -125)
variant_na(draw,
           head=na_head,
           tail=na_tail,
           bow_perp=+10, w_head=2, w_belly=14, w_tail=2, belly_u=0.72)

out_path = os.path.join(os.path.dirname(__file__), "01_久.png")
img.save(out_path)
print(f"Wrote {out_path}")
