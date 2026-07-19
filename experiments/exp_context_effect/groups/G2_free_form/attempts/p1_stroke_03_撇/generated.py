"""
Render 撇 (pie) — sweep from upper-right to lower-left — as a 300x300 PNG.

Free-form memory (G2). Building on 横/竖 experience:
- 300x300 canvas, white background, black ink.
- 起笔 (upper-right): brush lands with a small press-in, producing the
  thickest part of the stroke.
- Body: curves gently down-and-left, subtly bowing out (concave up-right,
  convex down-left) — canonical 撇 has a slight arc, not a straight line.
- 收笔 (lower-left): tapers to a sharp point (锋).

Implementation: build a tapered polygon by walking a parametric curve and
laying perpendicular half-widths that shrink from ~thick at start to 0
at the tail. Use a Bezier-like quadratic curve for the mild arc.
"""

from PIL import Image, ImageDraw
import math

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

# Endpoints and control point for a quadratic Bezier curve.
# 起笔 near upper-right, 收笔 near lower-left.
P0 = (225.0,  60.0)   # start (upper-right)
P1 = (170.0, 150.0)   # control (pulls curve slightly to the right, so
                      # the arc bows toward upper-right — canonical 撇)
P2 = ( 55.0, 250.0)   # end (lower-left, sharp tip)

START_WIDTH = 16.0    # half-width at 起笔 (thickest)
END_WIDTH   = 0.5     # near-point at 收笔 (tapered)

STEPS = 120

def bezier(t):
    x = (1 - t) ** 2 * P0[0] + 2 * (1 - t) * t * P1[0] + t * t * P2[0]
    y = (1 - t) ** 2 * P0[1] + 2 * (1 - t) * t * P1[1] + t * t * P2[1]
    return x, y

def bezier_tangent(t):
    dx = 2 * (1 - t) * (P1[0] - P0[0]) + 2 * t * (P2[0] - P1[0])
    dy = 2 * (1 - t) * (P1[1] - P0[1]) + 2 * t * (P2[1] - P1[1])
    return dx, dy

# Width profile: begin slightly plumped (press-in), then taper.
# Use a curve that stays thick near start and tapers hard near end.
def width_at(t):
    # Slight bulge just after start (0.05..0.15), then quadratic taper.
    if t < 0.1:
        # ramp up from ~70% to 100%
        return START_WIDTH * (0.7 + 0.3 * (t / 0.1))
    # taper from 1.0 to END_WIDTH/START_WIDTH along (1-t)^1.5
    u = (t - 0.1) / 0.9
    frac = (1 - u) ** 1.5
    return END_WIDTH + (START_WIDTH - END_WIDTH) * frac

left_edge = []
right_edge = []
for i in range(STEPS + 1):
    t = i / STEPS
    x, y = bezier(t)
    dx, dy = bezier_tangent(t)
    # Perpendicular unit vector (rotate tangent 90°).
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

# Emphasize 起笔 with a small rounded press-in blob at P0 area.
draw.ellipse(
    [P0[0] - 14, P0[1] - 10, P0[0] + 10, P0[1] + 18],
    fill="black",
)

# Ensure a crisp point at 收笔 — a tiny black triangle at the tip.
tip = P2
prev_x, prev_y = bezier(1 - 1 / STEPS)
tdx, tdy = tip[0] - prev_x, tip[1] - prev_y
tl = math.hypot(tdx, tdy) or 1.0
tdx, tdy = tdx / tl, tdy / tl
# extend tip a couple pixels along tangent for a sharper look
tip_ext = (tip[0] + tdx * 3, tip[1] + tdy * 3)
# perpendicular near tip
px, py = -tdy, tdx
base_w = 1.5
draw.polygon(
    [
        (prev_x + px * base_w, prev_y + py * base_w),
        (prev_x - px * base_w, prev_y - py * base_w),
        tip_ext,
    ],
    fill="black",
)

out_path = (
    "/Users/peilinwu/Documents/AI memory research/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p1_stroke_03_撇/01_撇.png"
)
img.save(out_path)
print(f"Wrote {out_path} size={img.size}")
