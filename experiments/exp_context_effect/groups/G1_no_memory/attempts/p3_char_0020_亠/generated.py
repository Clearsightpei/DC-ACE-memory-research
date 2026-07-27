"""Render 亠 (character p3_char_0020) as a 300x300 PNG.

亠 has 2 strokes:
  1. A short dian (点) at the top — in GT it curves slightly (concave toward lower-left).
  2. A long horizontal (横) below it — in GT it's slightly dipped at the middle
     and has small end-nibs at both ends (start tucks up-then-down, end has slight lift).
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"


def stamp(draw, x, y, r):
    draw.ellipse([x - r, y - r, x + r, y + r], fill=INK)


def draw_curved_dian(draw, x0, y0, x1, y1, curvature=8, w_start=3, w_end=7, steps=40):
    """Slightly curved tapering dot: control point offset perpendicular to line."""
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    # perpendicular direction (rotate line vector 90deg CCW)
    dx, dy = x1 - x0, y1 - y0
    length = math.hypot(dx, dy)
    px, py = -dy / length, dx / length
    cx, cy = mx + px * curvature, my + py * curvature
    for i in range(steps):
        t = i / (steps - 1)
        # Quadratic Bezier
        x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * cx + t ** 2 * x1
        y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * cy + t ** 2 * y1
        w = w_start + (w_end - w_start) * t
        stamp(draw, x, y, w / 2)


# Stroke 1: dian — starts thin near top, thickens toward lower-right, slightly curves
# GT shows it curving so the belly is on the lower-left (concave toward upper-right)
# From (~140, ~108) to (~160, ~140), with curvature pushing lower-left
draw_curved_dian(draw, 140, 108, 160, 142, curvature=-4, w_start=3, w_end=8, steps=40)


def draw_heng(draw, x0, y0, x1, y1, w_body=5, w_end_nib=9, steps=100):
    """Horizontal with small tick at start (slightly higher then drops), body slightly dipping,
    and slight lift with a small nib at the end."""
    for i in range(steps):
        t = i / (steps - 1)
        x = x0 + (x1 - x0) * t
        # subtle dip in middle
        dip = 2 * (1 - (2 * t - 1) ** 2)
        y = y0 + (y1 - y0) * t + dip
        # tick / nib profile
        if t < 0.06:
            # starting tick — thicker
            w = w_body + (w_end_nib - w_body) * (1 - t / 0.06)
        elif t > 0.94:
            # ending nib — thicker
            w = w_body + (w_end_nib - w_body) * ((t - 0.94) / 0.06)
        else:
            w = w_body
        stamp(draw, x, y, w / 2)


# Stroke 2: heng — spans roughly x=42 to x=258, at about y=188
draw_heng(draw, 45, 190, 258, 186, w_body=5, w_end_nib=9, steps=110)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0020_亠/01_亠.png")
print("Saved 01_亠.png")
