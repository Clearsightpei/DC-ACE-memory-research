"""
p2_radical_064_彡 — three 撇 strokes stacked vertically.

Observation from GT (300x300):
  - Three 撇 (throw-away) strokes, each thick→thin, gently rightward-bowed
    Bezier from upper-right to lower-left.
  - Stacked with the top 撇 highest and shortest, the bottom 撇 lowest and
    longest, forming a diagonal cascade.
  - Each 撇 starts with a small 顿 dab (r+2) and tapers to a sharp tip.
  - Each successive 撇 sits BELOW and slightly LEFT of the previous one's
    tip (the cascade slants down-and-left overall).

Renderer: PIL brush-dab (per drawer_memory principle — preferred at 300x300).
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def bezier_pie(p0, p1, p2, r_start=8.0, r_end=1.3, steps=400, press_r=0):
    """Quadratic Bezier 撇 with taper thick→thin. Optional subtle 顿 dab."""
    if press_r > 0:
        dab(p0[0], p0[1], press_r)
    for i in range(steps + 1):
        t = i / steps
        one_m = 1 - t
        x = one_m * one_m * p0[0] + 2 * one_m * t * p1[0] + t * t * p2[0]
        y = one_m * one_m * p0[1] + 2 * one_m * t * p1[1] + t * t * p2[1]
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


# Three 撇 stacked; each shorter/higher above, longer/lower below.
# Coordinates from GT observation (image coords, y grows DOWN).
# Revision: removed the r+2 顿 dabs (per "no visible 顿-dab balls at standalone
# endpoints" rule in drawer_memory — they were reading as balloon heads).
# Kept a very subtle r+0.5 press to hint at the head. Also nudged bottom 撇
# rightward a touch to sit under the middle 撇's tip.

# Top 撇 — short.
bezier_pie(
    p0=(188, 62),
    p1=(178, 90),
    p2=(150, 118),
    r_start=6.5,
    r_end=1.2,
    press_r=7.0,
)

# Middle 撇 — medium.
bezier_pie(
    p0=(178, 122),
    p1=(163, 155),
    p2=(128, 192),
    r_start=7.0,
    r_end=1.2,
    press_r=7.5,
)

# Bottom 撇 — longest, sweeps deepest.
bezier_pie(
    p0=(165, 188),
    p1=(140, 225),
    p2=(90, 268),
    r_start=7.5,
    r_end=1.2,
    press_r=8.0,
)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_064_彡/01_彡.png"
)
