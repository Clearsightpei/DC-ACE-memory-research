"""Render radical 攴 (pu) — 4 strokes: 竖, 横, 撇, 捺.

Layout inferred from GT PNG:
  Top compact 卜-like element: short vertical + small horizontal to the right.
  Bottom: a 撇 (top-right → bottom-left, gentle bow) and a 捺
    (top-left → bottom-right) that CROSS near the middle to form an X.

PIL brush-dab technique from G2 memory.
"""

from PIL import Image, ImageDraw
import math
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(p0, p1, r0, r1, steps=None):
    x0, y0 = p0
    x1, y1 = p1
    dist = math.hypot(x1 - x0, y1 - y0)
    if steps is None:
        steps = max(60, int(dist * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=200):
    x0, y0 = p0
    xc, yc = p1
    x1, y1 = p2
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * x0 + 2 * u * t * xc + t * t * x1
        y = u * u * y0 + 2 * u * t * yc + t * t * y1
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# -----------------------------------------------------------------
# Stroke 1: short 竖 at top (the vertical of the 卜-like top)
# Located a bit left of center, top region.
# -----------------------------------------------------------------
v_top = (135, 55)
v_bot = (135, 118)
# start 顿 dab
dab(*v_top, 6)
line_dabs(v_top, v_bot, 5, 5)
dab(*v_bot, 6)

# -----------------------------------------------------------------
# Stroke 2: short 横 near the TOP of the 竖 (卜-like where 点 is 横)
# Slight up-tilt. Positioned to the right of the 竖's upper portion.
# -----------------------------------------------------------------
h_left = (150, 78)
h_right = (200, 73)
dab(*h_left, 6)
line_dabs(h_left, h_right, 5, 5)
dab(*h_right, 6)

# -----------------------------------------------------------------
# Stroke 3: 撇 (throw-away)
# Starts upper-right, curves down-and-left, sharp tip.
# Passes through the center of the bottom half so it crosses the 捺.
# -----------------------------------------------------------------
pie_start = (175, 130)
pie_ctrl = (145, 200)
pie_end = (55, 265)
dab(*pie_start, 10)  # 顿笔 start
bezier_dabs(pie_start, pie_ctrl, pie_end, 9, 1.5)

# -----------------------------------------------------------------
# Stroke 4: 捺 (press-down)
# Starts upper-left (a bit right of the 撇 start's x), goes
# down-and-right, thin→thick, ending in broad flat foot.
# Must cross the 撇.
# -----------------------------------------------------------------
na_start = (110, 145)
na_ctrl = (170, 225)
na_end = (255, 260)
bezier_dabs(na_start, na_ctrl, na_end, 2.5, 9)
# broad terminal press ("flat foot")
dab(*na_end, 10)
# slight extension to make the foot look flat
line_dabs(na_end, (265, 258), 9, 6)

out = os.path.join(os.path.dirname(__file__), "01_攴.png")
img.save(out)
print("Saved:", out)
