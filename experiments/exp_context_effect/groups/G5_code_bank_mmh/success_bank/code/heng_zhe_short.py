"""Bank primitive: 乛 (short 横折 — horizontal then downward hook curve).

Promoted from p2_radical_004_乛 (G5 bootstrap PASS, 2026-08-08).

A single-stroke component that starts as a horizontal segment then
bends downward with a smooth corner into the tail. Useful as a component
of 冖, 宀, 予 etc.
"""

from PIL import ImageDraw


def draw_heng_zhe_short(draw: ImageDraw.ImageDraw, head, tail,
                        corner_offset=(0, 4)):
    """Draw a short 乛 from head (top-left) to tail (mid-right, lower).

    head, tail    : (x, y) pixel tuples
    corner_offset : (dx, dy) placing the visible corner relative to a
                    default location computed as the near-tail x, near-head y.
                    Adjust if the character wants a squarer or rounder bend.
    """
    x0, y0 = head
    x1, y1 = tail

    # default corner: horizontal reaches the tail x, then drops to tail y
    corner_x = x1 - 27 + corner_offset[0]
    corner_y = y0 + 4 + corner_offset[1]

    # Segment A: slight arched horizontal, thin lead-in
    steps_a = 30
    for i in range(steps_a):
        t = i / (steps_a - 1)
        bx = x0 + (corner_x - x0) * t
        by = y0 + (corner_y - y0) * t - 2.5 * (1 - (2 * t - 1) ** 2)
        w = 3.2 + 2.0 * t
        draw.ellipse([bx - w, by - w, bx + w, by + w], fill='black')

    # Segment B: quadratic Bezier for the bend, control near tail-x, head-y
    cx, cy = x1 + 4, y0 + 1
    steps_b = 40
    for i in range(steps_b):
        t = i / (steps_b - 1)
        bx = (1 - t) ** 2 * corner_x + 2 * (1 - t) * t * cx + t ** 2 * x1
        by = (1 - t) ** 2 * corner_y + 2 * (1 - t) * t * cy + t ** 2 * y1
        w = 4.8 - 2.6 * t
        draw.ellipse([bx - w, by - w, bx + w, by + w], fill='black')
