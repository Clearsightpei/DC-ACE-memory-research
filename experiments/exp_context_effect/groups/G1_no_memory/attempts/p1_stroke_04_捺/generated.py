"""
G1 no-memory attempt: 捺 (nà) stroke.
从左上向右下 sweep — thin at head, thick swelling middle, tapered 出锋 tail extending right.
Rendered with PIL (variable-width polygon), 300x300, white bg, black ink.
"""
from PIL import Image, ImageDraw
import math
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# Control points for the 捺 spine, from head (upper-left) to tail (lower-right, then flicking right).
# Coordinates in image space (y grows down).
# Head at upper-left, thick belly lower-middle, tail flicks out to the right almost horizontal.
p0 = (85, 70)    # head (thin)
p1 = (140, 140)  # upper mid
p2 = (185, 210)  # belly (thickest)
p3 = (245, 235)  # near tail base
p4 = (275, 232)  # tapered 出锋 tail (thin, extending right)

# Sample a cubic-ish path via piecewise quadratics (Catmull-Rom-ish via Bezier segments).
def quad_bezier(a, b, c, t):
    x = (1 - t) ** 2 * a[0] + 2 * (1 - t) * t * b[0] + t ** 2 * c[0]
    y = (1 - t) ** 2 * a[1] + 2 * (1 - t) * t * b[1] + t ** 2 * c[1]
    return (x, y)

def cubic_bezier(a, b, c, d, t):
    x = ((1 - t) ** 3 * a[0]
         + 3 * (1 - t) ** 2 * t * b[0]
         + 3 * (1 - t) * t ** 2 * c[0]
         + t ** 3 * d[0])
    y = ((1 - t) ** 3 * a[1]
         + 3 * (1 - t) ** 2 * t * b[1]
         + 3 * (1 - t) * t ** 2 * c[1]
         + t ** 3 * d[1])
    return (x, y)

# Build the spine as one cubic Bezier from p0 to p4 with p1,p2/p3 informing shape.
# Use p0, p2, p3, p4 for a natural swelling arc.
N = 200
spine = [cubic_bezier(p0, p1, p3, p4, t / N) for t in range(N + 1)]

# Width profile: thin -> thick belly -> tapered flick.
# Peak thickness around t = 0.65.
def width_at(t):
    # thin head (2 px), swelling middle (~22 px), tapered tail (1 px).
    head = 2.0
    belly = 22.0
    tail = 1.0
    if t <= 0.65:
        # ease from head to belly
        u = t / 0.65
        # smoothstep
        s = u * u * (3 - 2 * u)
        return head + (belly - head) * s
    else:
        u = (t - 0.65) / 0.35
        s = u * u * (3 - 2 * u)
        return belly + (tail - belly) * s

# Compute left/right offsets perpendicular to tangent.
def tangent(i):
    if i == 0:
        dx = spine[1][0] - spine[0][0]
        dy = spine[1][1] - spine[0][1]
    elif i == len(spine) - 1:
        dx = spine[-1][0] - spine[-2][0]
        dy = spine[-1][1] - spine[-2][1]
    else:
        dx = spine[i + 1][0] - spine[i - 1][0]
        dy = spine[i + 1][1] - spine[i - 1][1]
    L = math.hypot(dx, dy) or 1.0
    return dx / L, dy / L

left_edge = []
right_edge = []
for i, pt in enumerate(spine):
    t = i / N
    w = width_at(t) / 2.0
    tx, ty = tangent(i)
    # perpendicular (rotate tangent 90 deg)
    nx, ny = -ty, tx
    left_edge.append((pt[0] + nx * w, pt[1] + ny * w))
    right_edge.append((pt[0] - nx * w, pt[1] - ny * w))

polygon = left_edge + list(reversed(right_edge))
draw.polygon(polygon, fill="black")

# Slight rounding at head to avoid sharp cut.
draw.ellipse((p0[0] - 2, p0[1] - 2, p0[0] + 2, p0[1] + 2), fill="black")

out_path = os.path.join(os.path.dirname(__file__), "01_捺.png")
img.save(out_path)
print(f"Saved {out_path} size={img.size}")
