"""取 — 8 strokes: 耳 (6) + 又 (2).

耳 (left, compressed narrow-tall):
  1) 横 top
  2) 竖 left (top-left down to bottom-left)
  3) 竖 right (top-right down to bottom-right)
  4) 横 upper inner
  5) 横 lower inner
  6) 横 bottom (extends past both sides — flat baseline)

又 (right):
  7) 横撇 — short horizontal into a diagonal down-left
  8) 捺 — from upper crossing point, diagonal down-right

Layout: left component narrow ~35%, right component ~55%, with a small gap.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 5

def line(p1, p2, w=LW):
    d.line([p1, p2], fill=BLACK, width=w)

# ---- 耳 (left) ----
# bounding: x in [40, 130], y in [55, 260]
# 1) 横 top
line((45, 60), (130, 62), w=LW)
# 2) 竖 left
line((55, 60), (55, 248), w=LW)
# 3) 竖 right (of 耳)
line((125, 62), (125, 248), w=LW)
# 4) 横 upper inner
line((60, 118), (120, 116), w=LW)
# 5) 横 lower inner
line((60, 172), (120, 170), w=LW)
# 6) 横 bottom (extends beyond both sides — long baseline)
line((30, 248), (155, 248), w=LW)

# small tail (竖 left extends past bottom slightly) — merge into baseline

# ---- 又 (right) ----
# bounding: x in [150, 285], y in [85, 265]
# 7) 横撇: short horizontal then sweeping down-left
line((160, 95), (240, 95), w=LW)   # short horizontal part
line((240, 95), (155, 265), w=LW)  # diagonal撇 down-left
# 8) 捺: from around (185, 155) diagonal down-right to (285, 260)
line((185, 155), (285, 260), w=LW)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0401_取/01_取.png")
