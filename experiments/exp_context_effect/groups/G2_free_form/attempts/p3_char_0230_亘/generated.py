"""
亘 — 6 strokes:
  1) top 一 (short-medium, upper region)
  2) left 丨 of the inner 日-like box
  3) 横折 (top+right of box)
  4) middle 一 inside the box
  5) bottom 一 closing the box
  6) bottom long 一 (widest)

Not a sibling-risk target. Simple layout: 一 / 日 / 一 stacked, with
the bottom 一 the widest, top 一 medium, inner box narrower.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def hline(x0, x1, y, w=6):
    d.line([(x0, y), (x1, y)], fill=BLACK, width=w)

def vline(x, y0, y1, w=6):
    d.line([(x, y0), (x, y1)], fill=BLACK, width=w)

# 1) top 一 — medium width, slight rise to the right (calligraphic)
hline(70, 220, 55, w=7)

# Inner 日-like box: from y~85 to y~200, x from ~85 to ~215
BOX_L, BOX_R = 90, 210
BOX_T, BOX_B = 90, 205
BOX_MID = 150

# 2) left 丨 of box
vline(BOX_L, BOX_T, BOX_B, w=6)

# 3) 横折 — top horizontal + right vertical (one stroke conceptually)
hline(BOX_L, BOX_R, BOX_T, w=6)
vline(BOX_R, BOX_T, BOX_B, w=6)

# 4) middle 一 inside the box
hline(BOX_L + 8, BOX_R - 8, BOX_MID, w=5)

# 5) bottom 一 closing the box
hline(BOX_L, BOX_R, BOX_B, w=6)

# 6) bottom long 一 — widest of all
hline(40, 260, 240, w=8)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0230_亘/01_亘.png")
