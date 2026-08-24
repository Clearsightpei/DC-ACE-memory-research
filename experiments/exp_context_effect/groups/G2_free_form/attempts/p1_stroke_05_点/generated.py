"""
Render 点 (diǎn) — short diagonal dot — as a 300x300 PNG.

Free-form memory (G2). From drawer_memory.md:
- 点 is a compact tapered teardrop over a very short curve.
- Reuse the tapered-polygon technique from 撇/捺.

Canonical 点 (右点, the most common form used in 六, 主, 广, etc.):
- Short diagonal stroke, slanting from upper-left to lower-right.
- Thin at 起笔 (upper-left, light landing), swells to thickest at
  lower-right (the belly = 收笔 area).
- Distinctly shorter than any other stroke — length roughly the
  width of a single character grid unit at ~1/3 canvas.
- Ends with a small pointed pull-back (回锋) or a rounded belly; here
  we use a rounded, filled teardrop end to keep it crisp.

Implementation: quadratic Bezier from upper-left to lower-right,
short span (~80 px), width profile thin -> thick (0.8 -> 12 px),
capped with an ellipse at the belly to give the classic teardrop.
"""

from PIL import Image, ImageDraw
import math

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

# Center the dot roughly in the canvas. Short diagonal, upper-left
# to lower-right, spanning ~90 px total.
P0 = (125.0, 120.0)   # 起笔, upper-left, thin
P1 = (155.0, 150.0)   # control — mild bow (belly toward lower-left)
P2 = (185.0, 195.0)   # 收笔, lower-right, thickest (belly)

START_WIDTH = 1.2     # near-point at 起笔
END_WIDTH   = 11.0    # thick belly at 收笔

STEPS = 100


def bezier(t):
    x = (1 - t) ** 2 * P0[0] + 2 * (1 - t) * t * P1[0] + t * t * P2[0]
    y = (1 - t) ** 2 * P0[1] + 2 * (1 - t) * t * P1[1] + t * t * P2[1]
    return x, y


def bezier_tangent(t):
    dx = 2 * (1 - t) * (P1[0] - P0[0]) + 2 * t * (P2[0] - P1[0])
    dy = 2 * (1 - t) * (P1[1] - P0[1]) + 2 * t * (P2[1] - P1[1])
    return dx, dy


def width_at(t):
    # Thin at start, swells toward the end (belly).
    # t^1.4 keeps the early part thin so the head is crisp.
    frac = t ** 1.4
    return START_WIDTH + (END_WIDTH - START_WIDTH) * frac


left_edge = []
right_edge = []
for i in range(STEPS + 1):
    t = i / STEPS
    x, y = bezier(t)
    dx, dy = bezier_tangent(t)
    length = math.hypot(dx, dy) or 1.0
    nx, ny = -dy / length, dx / length
    w = width_at(t)
    left_edge.append((x + nx * w, y + ny * w))
    right_edge.append((x - nx * w, y - ny * w))

polygon = left_edge + list(reversed(right_edge))
draw.polygon(polygon, fill="black")

# Rounded belly at 收笔 — an ellipse at P2 to give the classic
# teardrop bulge and hide any polygon-edge jaggies.
belly_r = END_WIDTH * 1.05
draw.ellipse(
    [P2[0] - belly_r, P2[1] - belly_r, P2[0] + belly_r, P2[1] + belly_r],
    fill="black",
)

# Tiny 起笔 nub — 点 lands very lightly, essentially a point.
draw.ellipse(
    [P0[0] - 1.5, P0[1] - 1.5, P0[0] + 2.0, P0[1] + 2.0],
    fill="black",
)

out_path = (
    "<REPO_ROOT>/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p1_stroke_05_点/01_点.png"
)
img.save(out_path)
print(f"Wrote {out_path} size={img.size}")
