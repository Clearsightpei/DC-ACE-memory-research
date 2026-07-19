"""
殳 (shu) — 4-stroke radical. First attempt.

Structure (top-to-bottom):
  Top part = 几-like body:
    Stroke 1: 撇 — short throw from upper-right toward lower-left, tapered.
    Stroke 2: 横折弯 — starts as short 横 (rightward with slight up-tilt),
              shoulder-dab at the corner, then a 竖 dropping down, then
              a SMOOTH tangent-continuous arc (竖弯) into a short
              rightward tail. Blunt terminal (no hook).
  Bottom part = 又:
    Stroke 3: 横撇 — a horizontal beat then a bowed 撇 tail down-left.
    Stroke 4: 捺 — thin→thick press starting from where the 撇 begins
              (crossing under/through the 撇), ending in a broad foot
              at lower-right.

Renderer: PIL brush-dabs.  300×300 white, black ink.
"""

import math
import os
from PIL import Image, ImageDraw

CANVAS = 300
img = Image.new("RGB", (CANVAS, CANVAS), "white")
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
        # ease radius slightly so the tip stays sharp
        tt = t
        r = r0 + (r1 - r0) * tt
        dab(x, y, r)


# ------------------------------------------------------------------
# TOP PART (几-like body)
# ------------------------------------------------------------------

# Stroke 1: 撇  (upper apex → lower-left)
# Start near top-center-left of the top body; throw down-and-left.
p0 = (135, 50)
p1 = (120, 90)
p2 = (85, 145)
# subtle 顿 dab at start (standalone-scale: r+1 only, no "balloon")
dab(p0[0], p0[1], 6)
bezier_dabs(p0, p1, p2, r0=5.5, r1=1.5, steps=220)

# Stroke 2: 横折弯 — top 横 + shoulder + 竖 + smooth arc into short rightward tail
# 横: from just below-right of 撇's start, rightward with a slight up-tilt.
h_start = (135, 58)
h_end = (215, 52)
# subtle start (no visible ball)
dab(h_start[0], h_start[1], 5.5)
line_dabs(h_start[0], h_start[1], h_end[0], h_end[1], r0=5, r1=5.2, steps=180)
# shoulder dab (顿) at corner — this IS a real 折 shoulder so r+2 ok, but slightly reduced
sh = h_end
dab(sh[0], sh[1], 6.5)
# 竖: drop from shoulder downward, slightly leaning left toward the arc
v_end = (200, 120)
line_dabs(sh[0], sh[1], v_end[0], v_end[1], r0=5.5, r1=5.2, steps=180)
# tangent-continuous vertical → rightward arc (KEY PRIMITIVE)
# at v_end, tangent is roughly (down + slight left).  For simplicity treat
# as vertical-going-down and arc rightward-and-down into a horizontal.
x0, y0 = v_end
R = 26
steps = 120
for i in range(steps + 1):
    t = i / steps
    x = x0 + R * (1 - math.cos(t * math.pi / 2))
    y = y0 + R * math.sin(t * math.pi / 2)
    dab(x, y, 5.0)
# arc ends at (x0+R, y0+R)
arc_end = (x0 + R, y0 + R)
# short rightward tail (blunt terminal)
tail_end = (arc_end[0] + 22, arc_end[1] - 2)
line_dabs(arc_end[0], arc_end[1], tail_end[0], tail_end[1], r0=5.0, r1=4.4, steps=100)
# subtle blunt terminal (r+1 only, standalone scale)
dab(tail_end[0], tail_end[1], 5.0)


# ------------------------------------------------------------------
# BOTTOM PART (又)
# ------------------------------------------------------------------

# Stroke 3: 横撇 — a short 横 across the middle-top, then a bowed 撇 down-left
h2_start = (70, 170)
h2_end = (215, 162)
dab(h2_start[0], h2_start[1], 5.5)
line_dabs(h2_start[0], h2_start[1], h2_end[0], h2_end[1], r0=5, r1=5.2, steps=200)
# shoulder dab at the 横→撇 joint (real 折 shoulder, keep it visible but not ballooned)
dab(h2_end[0], h2_end[1], 7)
# 撇 tail: bowed Bezier from the shoulder down-and-left to lower-left
pie_p0 = h2_end
pie_p1 = (185, 210)
pie_p2 = (60, 275)
bezier_dabs(pie_p0, pie_p1, pie_p2, r0=7, r1=1.5, steps=260)

# Stroke 4: 捺 — thin→thick press from upper-left → lower-right foot,
# starting near where the 撇 starts so the two strokes CROSS visibly (又's X).
na_p0 = (115, 190)
na_p1 = (180, 240)
na_p2 = (255, 275)
# thin start
bezier_dabs(na_p0, na_p1, na_p2, r0=2.0, r1=9.5, steps=260)
# terminal broad foot: a slightly larger dab at the end plus a small
# rightward flat tail so it reads as a 捺 foot rather than a rounded end.
foot_end = (na_p2[0] + 12, na_p2[1] - 1)
line_dabs(na_p2[0], na_p2[1], foot_end[0], foot_end[1], r0=9.5, r1=5.0, steps=80)


# ------------------------------------------------------------------
out_path = os.path.join(os.path.dirname(__file__), "01_殳.png")
img.save(out_path)
print(f"wrote {out_path}")
