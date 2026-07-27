"""
市 (shi4, city) — 5 strokes:
  1. 点 (top dot, slightly right of center, slanted down-right)
  2. 一 (long horizontal beneath the dot, spans most of width)
  3. 丨 (short left vertical of the 冂 box, starts just under the 一)
  4. 横折钩 (short top + right vertical of 冂, ends with UP-LEFT hook)
  5. 丨 (long central vertical piercing straight down through the whole
        lower half — this is the identity stroke of 市)

Notes from memory_index:
- Hook flick UP-and-LEFT (TIER-0 B). Never DOWN.
- 市 is NOT on the sibling-risk list, so no verbatim signature paste,
  but the long central 丨 must clearly extend BELOW the box.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 7  # main stroke width

def line(p0, p1, w=LW):
    d.line([p0, p1], fill=BLACK, width=w)

def dot_stroke(p0, p1, w_start=5, w_end=9, steps=14):
    # tapered dot: grows in width along the segment
    x0, y0 = p0; x1, y1 = p1
    for i in range(steps):
        t0 = i / steps
        t1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * t0
        ya = y0 + (y1 - y0) * t0
        xb = x0 + (x1 - x0) * t1
        yb = y0 + (y1 - y0) * t1
        w = int(w_start + (w_end - w_start) * ((t0 + t1) / 2))
        d.line([(xa, ya), (xb, yb)], fill=BLACK, width=w)

# 1. 点 — small dot near the top, right-of-center, slanting down-right
dot_stroke((146, 40), (164, 62), w_start=4, w_end=10, steps=18)

# 2. 一 — long horizontal, a bit below the dot
line((52, 92), (252, 96), w=LW)

# 3. 丨 — short left vertical (left wall of 冂)
line((90, 98), (92, 178), w=LW)

# 4. 横折钩 — horizontal top of 冂 + right vertical + UP-LEFT hook
#    top run
line((92, 118), (215, 118), w=LW)
#    right vertical
line((214, 118), (214, 174), w=LW)
#    hook: flick UP-and-LEFT (from bottom-right of the box)
line((214, 174), (198, 162), w=LW)

# 5. 丨 — long central vertical piercing straight down
line((150, 100), (150, 275), w=LW)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0200_市/01_市.png")
print("wrote 01_市.png")
