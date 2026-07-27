# p3_char_0219_在 — G3 attempt
# 在 (zài, "at/in") — 6 strokes:
#   1. 横 (top heng, upper-right)
#   2. 撇 (long pie, from upper-right curving down-left to lower-left corner)
#   3. 竖 (vertical, inside pie, meets the top heng)
#   4. 短横 (short heng — top of 土 component, right side)
#   5. 竖 (short vertical of 土)
#   6. 长横 (bottom heng of 土, longest — base)
#
# GT-derived: uniform thin strokes (~4 px). PIL direct rendering.

import os
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 4


def line(p1, p2, w=LW):
    d.line([p1, p2], fill=INK, width=w)


def curve(pts, w=LW):
    # polyline through pts
    for a, b in zip(pts[:-1], pts[1:]):
        d.line([a, b], fill=INK, width=w)


# 1. Top heng — slight upward slant, upper-right dominant
line((80, 95), (230, 85), w=LW)

# 2. Long pie (撇) — from ABOVE the heng, crossing through it, curving
#    down-left to lower-left corner
pie = [
    (185, 55),
    (170, 95),
    (150, 135),
    (125, 175),
    (95, 220),
    (60, 265),
]
curve(pie, w=LW)

# 3. Left shu of 土 — short vertical from the heng down into 土 region
line((130, 95), (130, 175), w=LW)

# 4. Middle heng of 土 — spans from behind pie to right edge
line((115, 175), (245, 172), w=LW)

# 5. Center shu of 土 — vertical stem, centered under top heng of 土
line((180, 172), (180, 245), w=LW)

# 6. Long bottom heng (base of 土) — widest
line((105, 250), (270, 248), w=LW)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_在.png")
img.save(out)
print("wrote", out)
