"""
p2_radical_021_丷  —  G2 attempt #1 (Phase-2 restart, batch-6 errata refresh)

丷 (two-dots-open-down radical, as in top of 兰, 关, 兴).
Two short strokes near the mid-upper portion of the canvas, diverging
outward downward: LEFT = 丶 slanting down-right (short teardrop dot),
RIGHT = 丿 short 撇 slanting down-left.

Rendering: PIL brush-dabs (see drawer_memory.md).
Canvas 300x300, white background, black ink.
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(cx, cy, r):
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")


def taper_dab_line(x0, y0, x1, y1, r0, r1, steps=200, ease=1.0):
    """Draw a taper stroke as a chain of filled circles from (x0,y0) to (x1,y1)."""
    for i in range(steps + 1):
        t = i / steps
        tt = t ** ease
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * tt
        dab(x, y, r)


def bezier_taper(P0, P1, P2, r0, r1, steps=250, ease=1.0):
    """Quadratic Bezier with tapered radius via brush-dabs."""
    for i in range(steps + 1):
        t = i / steps
        tt = t ** ease
        omt = 1 - t
        x = omt * omt * P0[0] + 2 * omt * t * P1[0] + t * t * P2[0]
        y = omt * omt * P0[1] + 2 * omt * t * P1[1] + t * t * P2[1]
        r = r0 + (r1 - r0) * tt
        dab(x, y, r)


# ---------------------------------------------------------------
# LEFT stroke: 丶 (dot), starts thin at upper-left, thickens down-and-right
# short teardrop. GT is small/delicate — keep short and thinner than
# first attempt.
# ---------------------------------------------------------------
L_P0 = (108, 128)  # thin start (upper-left)
L_P1 = (118, 142)  # midpoint control (slight rightward bow)
L_P2 = (135, 160)  # thick end (lower-right)
bezier_taper(L_P0, L_P1, L_P2, r0=1.2, r1=5.0, steps=220, ease=1.5)
# small terminal press at end
dab(L_P2[0], L_P2[1], 5.5)


# ---------------------------------------------------------------
# RIGHT stroke: short 撇, starts thickish at upper-right, thins down-and-left.
# Keep proportions delicate to match GT (thinner/shorter than first attempt).
# ---------------------------------------------------------------
R_P0 = (192, 128)  # thickish start (upper-right)
R_P1 = (183, 148)  # midpoint control (bow toward right/interior)
R_P2 = (168, 172)  # sharp tip (lower-left)
# small 顿笔 dab at start
dab(R_P0[0], R_P0[1], 5.5)
bezier_taper(R_P0, R_P1, R_P2, r0=5.0, r1=1.0, steps=240, ease=1.2)


img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_021_丷/01_丷.png")
