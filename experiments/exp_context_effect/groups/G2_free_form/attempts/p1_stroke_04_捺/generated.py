"""
Render 捺 (nà) — right-falling sweep — as a 300x300 PNG.

Free-form memory (G2). Building on 撇 (item 03) — 捺 is its mirror:
- 起笔 (upper-left): thin, light landing (almost a point).
- Body: swells thicker as it sweeps down-and-right, subtly bowing
  (canonical 捺 bows so the top edge is concave, belly points
  toward lower-left). Peak thickness ~75% along the stroke.
- 收笔 (lower-right): after the belly, the brush lifts into a
  horizontal 出锋 — a flat, tapered right-going flare (not a point
  going down-right; the tail flattens out).

Implementation: reuse the tapered-polygon technique from 撇 but
reverse the width profile (thin -> thick around t~0.75 -> thin flare)
and force the final segment to be nearly horizontal so the 出锋 is
crisp.
"""

from PIL import Image, ImageDraw
import math

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

# Endpoints for the main curved body (before the flat 出锋).
# 起笔 near upper-left, belly around lower-right, 出锋 extends further right.
P0 = ( 75.0,  60.0)   # start (upper-left), thin
P1 = (150.0, 170.0)   # control — pulls curve so it bows (belly lower-left)
P2 = (225.0, 235.0)   # belly point (thickest ~ here)

# 出锋 endpoint — horizontal flare tail extending right from P2.
FLARE_END = (270.0, 235.0)   # roughly same y => nearly horizontal outward
FLARE_STEPS = 30

START_WIDTH = 1.5     # near-point at 起笔
PEAK_WIDTH  = 18.0    # thickest at the belly (near end of Bezier)
FLARE_END_WIDTH = 0.5 # taper flare to a point

STEPS = 120

def bezier(t):
    x = (1 - t) ** 2 * P0[0] + 2 * (1 - t) * t * P1[0] + t * t * P2[0]
    y = (1 - t) ** 2 * P0[1] + 2 * (1 - t) * t * P1[1] + t * t * P2[1]
    return x, y

def bezier_tangent(t):
    dx = 2 * (1 - t) * (P1[0] - P0[0]) + 2 * t * (P2[0] - P1[0])
    dy = 2 * (1 - t) * (P1[1] - P0[1]) + 2 * t * (P2[1] - P1[1])
    return dx, dy

def width_at(t):
    # Grow width from START_WIDTH at t=0 to PEAK_WIDTH at t=1 (belly).
    # Use a curve that stays thin early then swells (t^1.3).
    frac = t ** 1.3
    return START_WIDTH + (PEAK_WIDTH - START_WIDTH) * frac

# Build main body polygon.
left_edge = []
right_edge = []
for i in range(STEPS + 1):
    t = i / STEPS
    x, y = bezier(t)
    dx, dy = bezier_tangent(t)
    length = math.hypot(dx, dy)
    if length == 0:
        nx, ny = 0.0, 0.0
    else:
        nx, ny = -dy / length, dx / length
    w = width_at(t)
    left_edge.append((x + nx * w, y + ny * w))
    right_edge.append((x - nx * w, y - ny * w))

polygon = left_edge + list(reversed(right_edge))
draw.polygon(polygon, fill="black")

# 出锋 flare: horizontal tapered polygon from P2 outward to FLARE_END.
# It starts at PEAK_WIDTH and tapers to FLARE_END_WIDTH.
# Direction is roughly horizontal, so perpendicular is vertical.
flare_left = []
flare_right = []
for i in range(FLARE_STEPS + 1):
    t = i / FLARE_STEPS
    x = P2[0] + (FLARE_END[0] - P2[0]) * t
    y = P2[1] + (FLARE_END[1] - P2[1]) * t
    # tangent
    dx = FLARE_END[0] - P2[0]
    dy = FLARE_END[1] - P2[1]
    length = math.hypot(dx, dy) or 1.0
    nx, ny = -dy / length, dx / length
    # Width shrinks from PEAK_WIDTH*0.9 (blend at junction) to FLARE_END_WIDTH.
    # Also flatten: reduce upward extent more than downward to give a "lift".
    w = (PEAK_WIDTH * 0.9) * (1 - t) ** 1.2 + FLARE_END_WIDTH * t
    # asymmetric: top edge (nx,ny with ny<0) shrinks faster so tail flattens on top
    top_scale = 0.55 + 0.45 * (1 - t)  # top edge pulls in
    bot_scale = 1.0
    flare_left.append((x + nx * w * top_scale, y + ny * w * top_scale))
    flare_right.append((x - nx * w * bot_scale, y - ny * w * bot_scale))

flare_poly = flare_left + list(reversed(flare_right))
draw.polygon(flare_poly, fill="black")

# Small 起笔 nub — 捺 lands very lightly, so just a tiny dot to avoid
# a jagged polygon opening.
draw.ellipse(
    [P0[0] - 2, P0[1] - 2, P0[0] + 3, P0[1] + 3],
    fill="black",
)

# Crisp point at 出锋 tip — small triangle extending horizontally right.
tip = FLARE_END
prev_x = P2[0] + (FLARE_END[0] - P2[0]) * (1 - 1 / FLARE_STEPS)
prev_y = P2[1] + (FLARE_END[1] - P2[1]) * (1 - 1 / FLARE_STEPS)
tdx, tdy = tip[0] - prev_x, tip[1] - prev_y
tl = math.hypot(tdx, tdy) or 1.0
tdx, tdy = tdx / tl, tdy / tl
tip_ext = (tip[0] + tdx * 4, tip[1] + tdy * 4)
px, py = -tdy, tdx
base_w = 1.2
draw.polygon(
    [
        (prev_x + px * base_w, prev_y + py * base_w),
        (prev_x - px * base_w, prev_y - py * base_w),
        tip_ext,
    ],
    fill="black",
)

out_path = (
    "<REPO_ROOT>/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p1_stroke_04_捺/01_捺.png"
)
img.save(out_path)
print(f"Wrote {out_path} size={img.size}")
