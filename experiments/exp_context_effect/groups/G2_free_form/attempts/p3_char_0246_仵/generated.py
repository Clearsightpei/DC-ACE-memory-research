"""Render 仵 (p3_char_0246) to 300x300 PNG.

仵 = 亻 (left, ~35% width) + 午 (right, ~55% width).

# SIGNATURE CHECK — 午 shares family with 千 (from sibling checklist):
#   千 | 撇-LID top + straight through-竖 (no hook) | sibling: 干, 于
# 午 differs from 千 by having TWO 横 (short top, longer middle) under
# the 撇-lid, then a through-竖 (no hook, flat bottom).

Strokes of 午 (4):
  1. 撇 (short lid at top, slanting down-left)
  2. 横 (shorter, upper) — sits under the 撇-tip
  3. 横 (longer, middle) — through the 竖 mid-body
  4. 竖 (through, no hook) — long, straight down

Left 亻 (2 strokes): 撇 apex meeting 竖 top; ~40% width band.
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
# 撇: apex at (95, 65), curves down-left to (45, 200)
bezier([(95, 65), (85, 110), (65, 160), (45, 200)], width=6)
# 竖: from apex of 撇 straight down
line((95, 75), (95, 275), width=6)

# ---- RIGHT: 午 ----
# 1. 撇 (short lid): from upper-right area sweeping to upper-left
bezier([(230, 55), (215, 68), (195, 82), (170, 92)], width=6)

# 2. 横 (shorter, upper): sits below the 撇-tip
line((160, 115), (255, 112), width=6)

# 3. 横 (longer, middle): through the 竖 mid-body
line((140, 175), (275, 172), width=6)

# 4. 竖 (through, no hook): long straight vertical
line((207, 100), (207, 285), width=6)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0246_仵/01_仵.png"
)
print("saved 01_仵.png")
