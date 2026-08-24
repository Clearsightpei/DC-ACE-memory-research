"""
女 (radical, 3画) — Phase-2 render for G2_free_form.
Stroke order (per MMH convention):
  1. 撇点 (piedian): 撇 goes down-left, then 反捺 down-right from the tip.
  2. 撇 (pie): long throw from upper-right to lower-left, crossing stroke 1.
  3. 横 (heng): horizontal, crossing through the middle.

PIL brush-dab technique. 300x300 white, black ink.
"""
import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_taper(p0, p1, r0, r1, steps=None):
    x0, y0 = p0
    x1, y1 = p1
    if steps is None:
        L = math.hypot(x1 - x0, y1 - y0)
        steps = max(60, int(L * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_taper(p0, p1, p2, r0, r1, steps=200):
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * x0 + 2 * u * t * x1 + t * t * x2
        y = u * u * y0 + 2 * u * t * y1 + t * t * y2
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# ---- Stroke 1: 撇点 ----
# 撇 primary: starts upper-mid, sweeps down-left with a gentle bow.
pie_start = (168, 65)
pie_tip = (110, 165)
pie_ctrl = (155, 130)
# 顿笔 dab at start
dab(pie_start[0], pie_start[1], 7)
bezier_taper(pie_start, pie_ctrl, pie_tip, 7.0, 2.2, steps=220)

# joining dab at joint (shared vertex per 撇点 rule)
dab(pie_tip[0], pie_tip[1], 6.5)

# 反捺/点 secondary: from pie_tip going down-right, thin -> thick, terminal press.
# Shorter than a full 捺; ends near the horizontal band, below the 横.
dot_end = (168, 210)
dot_ctrl = (138, 190)
bezier_taper(pie_tip, dot_ctrl, dot_end, 3.0, 8.0, steps=180)
# terminal press
dab(dot_end[0], dot_end[1], 9.0)


# ---- Stroke 2: 撇 (long) ----
# Long sweep from upper-right down to lower-left, crossing through stroke 1's mid-body.
p2_start = (215, 100)
p2_tip = (50, 250)
p2_ctrl = (190, 175)  # bow toward interior (right)
# 顿笔 dab at start
dab(p2_start[0], p2_start[1], 7.5)
bezier_taper(p2_start, p2_ctrl, p2_tip, 7.5, 1.8, steps=280)


# ---- Stroke 3: 横 (crossing horizontal) ----
# Slight up-tilt from left to right; passes through the middle band.
h_start = (40, 160)
h_end = (265, 148)
# 顿笔 dabs at both ends
dab(h_start[0], h_start[1], 6.5)
line_taper(h_start, h_end, 5.0, 5.0, steps=260)
dab(h_end[0], h_end[1], 6.5)


img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_061_女/01_女.png")
