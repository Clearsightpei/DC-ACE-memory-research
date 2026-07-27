"""Render 一 (yi) — a single 横 stroke — to 300x300 PNG.

Revision: thinner brush, tighter length, GT-matched shape. The GT
shows a shallow arch: left end angled down (small 顿), body rises
gently to the middle-right, then a short downward-angled 顿 dab at
the right terminal. Body sits around y~195 (slightly below middle).
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def brush_stroke(points, width):
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        d.line([(x1, y1), (x2, y2)], fill="black", width=width)
    r = width // 2
    for (x, y) in points:
        d.ellipse([x - r, y - r, x + r, y + r], fill="black")

# Main body: gentle arch matching GT.
# Left end ~x=75, right end ~x=230. Baseline ~y=195, arches up ~8 px in middle.
N = 40
pts = []
for i in range(N + 1):
    t = i / N
    x = 75 + t * (230 - 75)
    # arch: min-y (highest point) around t=0.55
    y = 195 - 6 * math.sin(math.pi * t) - 2 * t  # slight overall rise to right
    pts.append((x, y))

brush_stroke(pts, width=8)

# Left 顿 dab: small down-left triangular press
lx, ly = pts[0]
d.polygon([
    (lx - 6, ly - 2),
    (lx + 4, ly - 5),
    (lx + 6, ly + 6),
    (lx - 8, ly + 8),
], fill="black")

# Right 顿 dab: down-right press, giving the terminal downturn seen in GT
rx, ry = pts[-1]
d.polygon([
    (rx - 4, ry - 5),
    (rx + 8, ry - 2),
    (rx + 6, ry + 10),
    (rx - 6, ry + 6),
], fill="black")

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0001_一/01_一.png")
print("saved")
