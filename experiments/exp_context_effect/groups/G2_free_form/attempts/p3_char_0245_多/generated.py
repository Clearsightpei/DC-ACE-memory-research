"""
多 (duo) — 6-stroke character = 夕 stacked on 夕.

Top 夕: smaller, upper region (rows ~40-160)
Bottom 夕: larger, lower region (rows ~140-280), shifted slightly right

Each 夕:
  1) 撇 — top short flick, upper-right → lower-left
  2) 横折钩/横撇 — short 横 + shoulder, then long bowed 撇 tail arcing down-left
  3) 点/短撇 inside the belly

Reused template from p2_radical_075_夕 (G2 memory).
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=None):
    if steps is None:
        steps = max(40, int(math.hypot(x1 - x0, y1 - y0) * 2))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=200, ease=1.0):
    for i in range(steps + 1):
        t = i / steps
        tt = t ** ease
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * tt
        dab(x, y, r)


def draw_xi(cx, cy, scale, brush_scale=1.0):
    """Draw a 夕 centered near (cx, cy) at given scale.
    Reference shape occupies ~200x200 canvas region internally."""
    # base reference for 夕 (from p2_radical_075_夕 template) — normalized
    # then translated + scaled
    def T(x, y):
        # ref system: char roughly (100..220) horizontal, (60..270) vertical
        # normalize around (160, 165), scale, translate to (cx, cy)
        rx = (x - 160) * scale + cx
        ry = (y - 165) * scale + cy
        return (rx, ry)

    r = brush_scale

    # Stroke 1: top 撇
    p0 = T(175, 65)
    p2 = T(105, 175)
    ctrl = T(155, 115)
    dab(p0[0], p0[1], 5.5 * r)
    bezier_dabs(p0, ctrl, p2, 5.5 * r, 1.2 * r, steps=200, ease=1.2)

    # Stroke 2: 横折 + long bowed 撇 tail
    h_start = T(150, 78)
    h_end = T(210, 70)
    line_dabs(h_start[0], h_start[1], h_end[0], h_end[1], 5.0 * r, 5.0 * r, steps=120)
    dab(h_end[0], h_end[1], 7.0 * r)  # shoulder
    tail_p0 = T(210, 70)
    tail_p2 = T(100, 262)
    tail_ctrl = T(225, 180)
    bezier_dabs(tail_p0, tail_ctrl, tail_p2, 6.0 * r, 1.2 * r, steps=300, ease=1.15)

    # Stroke 3: inside 点/短撇
    in_p0 = T(180, 150)
    in_p2 = T(140, 195)
    in_ctrl = T(168, 172)
    dab(in_p0[0], in_p0[1], 4.0 * r)
    bezier_dabs(in_p0, in_ctrl, in_p2, 4.5 * r, 1.2 * r, steps=100, ease=1.2)


# Top 夕 — upper-left, medium size; tail sweeps down into middle of canvas
draw_xi(cx=130, cy=110, scale=0.60, brush_scale=0.9)

# Bottom 夕 — lower-right, larger; overlaps with top 夕 (they interlock)
draw_xi(cx=175, cy=210, scale=0.62, brush_scale=1.0)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0245_多/01_多.png")
