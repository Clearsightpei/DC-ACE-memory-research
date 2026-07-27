"""Render 仨 (p3_char_0189) to 300x300 PNG.

Composition:
  Left: 亻 (person radical) - short 撇 apex meeting top of 竖, ~40% width.
  Right: 三 - three horizontals, top short, middle shortest, bottom LONGEST.
Standard 三 signature: bottom 横 is clearly the longest; small vertical gaps.
"""

from PIL import Image, ImageDraw
from math import comb

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def line(p1, p2, width=6):
    d.line([p1, p2], fill=BLACK, width=width)


def bezier(pts, width=6, steps=80):
    n = len(pts) - 1
    prev = None
    for i in range(steps + 1):
        t = i / steps
        x = sum(comb(n, k) * (1 - t) ** (n - k) * t ** k * pts[k][0] for k in range(n + 1))
        y = sum(comb(n, k) * (1 - t) ** (n - k) * t ** k * pts[k][1] for k in range(n + 1))
        if prev is not None:
            d.line([prev, (x, y)], fill=BLACK, width=width)
        prev = (x, y)


# ---- LEFT: 亻 (person radical) ----
# 撇: apex at (95, 70), curves down-left to (45, 200)
bezier([(95, 70), (85, 115), (65, 165), (45, 200)], width=6)

# 竖: starts near apex of 撇 and drops straight down
line((95, 78), (95, 275), width=6)

# ---- RIGHT: 三 ----
# Top 横 (medium ~90px), slight upward slant
line((150, 100), (240, 96), width=6)

# Middle 横 (shortest ~75px), roughly centered
line((160, 170), (235, 168), width=6)

# Bottom 横 (LONGEST ~130px)
line((140, 245), (275, 243), width=6)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0189_仨/01_仨.png"
)
print("saved 01_仨.png")
