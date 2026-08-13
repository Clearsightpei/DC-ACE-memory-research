"""
没 (mei/mo) = 氵 (left, water radical) + 殳 (right).
Composed by adapting PASS'd components:
  - 氵 from p2_radical_069_氵 (three drops: two 点 + one 提)
  - 殳 from p2_radical_118_殳 (top 几-like body + bottom 又)

Layout (300x300):
  - 氵 compressed to left column, x ~ 30-90
  - 殳 compressed to right block, x ~ 100-275
Both slightly narrowed / repositioned; center of mass balanced.
"""

import math
import os
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=None):
    if steps is None:
        steps = max(40, int(2 * math.hypot(x1 - x0, y1 - y0)))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=200):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def teardrop(p0, p1, r0, r1, steps=200, easing=1.4):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        tt = t ** easing
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * tt
        dab(x, y, r)
    dab(x1, y1, r1 + 1)


def ti_stroke(p0, p1, r_start, r_end, steps=300):
    x0, y0 = p0
    x1, y1 = p1
    dab(x0, y0, r_start + 1)
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


# ------------------------------------------------------------------
# LEFT: 氵 (three-drops water radical), compressed to left column
# ------------------------------------------------------------------
# top 点 (upper-left, small teardrop, slant down-right)
teardrop(p0=(55, 70), p1=(75, 100), r0=1.6, r1=4.8)
# middle 点 (offset left, slightly lower)
teardrop(p0=(35, 130), p1=(58, 158), r0=1.6, r1=4.5)
# 提 (rising thick->thin) at bottom
ti_stroke(p0=(38, 220), p1=(90, 180), r_start=5.0, r_end=1.0, steps=260)


# ------------------------------------------------------------------
# RIGHT: 殳 in right block (x ~ 100-275)
# ------------------------------------------------------------------

# --- TOP 几-like body ---
# Stroke 1: 撇 — throw from top-center-right down-and-left
p0 = (175, 45)
p1 = (155, 75)
p2 = (125, 125)
dab(p0[0], p0[1], 5)
bezier_dabs(p0, p1, p2, r0=4.5, r1=1.5, steps=200)

# Stroke 2: 横折弯 — 横 + shoulder + 竖 + arc into short tail
h_start = (172, 52)
h_end = (245, 47)
dab(h_start[0], h_start[1], 4.8)
line_dabs(h_start[0], h_start[1], h_end[0], h_end[1], r0=4.5, r1=4.6, steps=180)
# shoulder dab
sh = h_end
dab(sh[0], sh[1], 5.8)
# 竖: drop from shoulder
v_end = (232, 105)
line_dabs(sh[0], sh[1], v_end[0], v_end[1], r0=4.8, r1=4.6, steps=160)
# arc rightward-and-down (tangent continuous)
x0, y0 = v_end
R = 20
steps = 100
for i in range(steps + 1):
    t = i / steps
    x = x0 + R * (1 - math.cos(t * math.pi / 2))
    y = y0 + R * math.sin(t * math.pi / 2)
    dab(x, y, 4.4)
arc_end = (x0 + R, y0 + R)
tail_end = (arc_end[0] + 15, arc_end[1] - 2)
line_dabs(arc_end[0], arc_end[1], tail_end[0], tail_end[1], r0=4.4, r1=3.8, steps=80)
dab(tail_end[0], tail_end[1], 4.2)

# --- BOTTOM 又 ---
# Stroke 3: 横撇 — short 横 across upper part of 又, then bowed 撇 down-left
h2_start = (110, 165)
h2_end = (245, 158)
dab(h2_start[0], h2_start[1], 4.8)
line_dabs(h2_start[0], h2_start[1], h2_end[0], h2_end[1], r0=4.5, r1=4.6, steps=180)
# shoulder dab at 折 joint
dab(h2_end[0], h2_end[1], 6.2)
# 撇 tail: bowed from shoulder down-and-left
pie_p0 = h2_end
pie_p1 = (215, 210)
pie_p2 = (105, 275)
bezier_dabs(pie_p0, pie_p1, pie_p2, r0=6.2, r1=1.5, steps=240)

# Stroke 4: 捺 — thin -> thick press from upper-left area of 又 to lower-right foot
na_p0 = (150, 185)
na_p1 = (200, 230)
na_p2 = (275, 270)
bezier_dabs(na_p0, na_p1, na_p2, r0=1.8, r1=8.5, steps=240)
foot_end = (na_p2[0] + 10, na_p2[1] - 1)
line_dabs(na_p2[0], na_p2[1], foot_end[0], foot_end[1], r0=8.5, r1=4.5, steps=60)


out_path = os.path.join(os.path.dirname(__file__), "01_没.png")
img.save(out_path)
print(f"wrote {out_path}")
