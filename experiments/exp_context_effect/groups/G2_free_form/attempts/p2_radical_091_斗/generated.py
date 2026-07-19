"""Render radical 斗 (4 strokes) at 300x300 using PIL brush-dabs.

Structure of 斗:
  Stroke 1: left 点 (dian) — short teardrop, upper-left area, slanted down-right.
  Stroke 2: right 点 (dian) — short teardrop, below stroke 1, slanted down-right.
    (Both dots sit to the LEFT of the vertical, in a slight column.)
  Stroke 3: 横 (heng) — long horizontal across middle.
  Stroke 4: 长竖 (long vertical) — from above the horizontal down through it to bottom,
            on the right side (crosses the 横 near its right-third).

Reference: GT shows two small down-right slanting 点 in upper-left,
a long horizontal across middle, and a straight tall vertical descending
through them just right of center.
"""

from PIL import Image, ImageDraw
import math
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def stroke_line(x0, y0, x1, y1, r_start, r_end, steps=400):
    """Straight tapered stroke via brush dabs."""
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def stroke_bezier(p0, p1, p2, r_start, r_end, steps=400, easing=None):
    """Quadratic Bezier tapered stroke."""
    for i in range(steps + 1):
        t = i / steps
        tt = easing(t) if easing else t
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        r = r_start + (r_end - r_start) * tt
        dab(x, y, r)


# ---- Stroke 1: left 点 (upper, more horizontal, short) ----
# 斗's first 点 is actually a short 撇-like slant, thin at tail
# Draw a short down-left slanting teardrop, ~35 px long
stroke_bezier(
    (105, 75), (95, 88), (78, 100),
    r_start=5.5, r_end=1.5,
    easing=lambda t: 1 - (1 - t) ** 1.3,
    steps=160,
)
dab(105, 75, 6)  # start 顿

# ---- Stroke 2: right 点 (below, similar short down-left slant) ----
# clearly separated from stroke 1, positioned lower and slightly right
stroke_bezier(
    (125, 115), (115, 128), (98, 140),
    r_start=5.5, r_end=1.5,
    easing=lambda t: 1 - (1 - t) ** 1.3,
    steps=160,
)
dab(125, 115, 6)  # start 顿

# ---- Stroke 3: 横 (long horizontal across middle) ----
# spans wide, slight up-tilt to the right, uniform ~r=5, 顿 dabs at ends
x0, y0 = 40, 178
x1, y1 = 260, 172
stroke_line(x0, y0, x1, y1, r_start=5, r_end=5, steps=400)
dab(x0, y0, 7)  # start 顿
dab(x1, y1, 7)  # end 顿

# ---- Stroke 4: long 竖 (vertical) ----
# From above the horizontal all the way down; positioned right-of-center
# (crosses the 横 to the right of its midpoint). Straight, uniform ~r=5.
vx = 190
vy0 = 55
vy1 = 275
stroke_line(vx, vy0, vx, vy1, r_start=5.5, r_end=5.5, steps=400)
dab(vx, vy0, 8)  # top 顿
dab(vx, vy1, 7)  # bottom blunt press

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_斗.png")
img.save(out_path)
print(f"Saved: {out_path}")
