"""Bank primitive: 横撇 (heng-pie — short horizontal bending into a leftward pie).

Extracted from p2_radical_037_又 s1 (PASS 2026-08-08, B1) via BANK_DEVIATION.
Signature: (head, tail) — head at upper-left corner of the horizontal
segment, tail at lower-left where the pie tapers to a point.

Used for 又's first stroke and appears as a component in 叉/支/皮/等.
"""

from PIL import ImageDraw


def draw_heng_pie(draw: ImageDraw.ImageDraw, head, tail,
                  apex_x=None, corner_x=None):
    """Draw 横撇: short horizontal from head arching right, then bending into
    a pie that sweeps down-left to tail.

    head, tail : (x, y) pixel tuples.
    apex_x, corner_x : optional overrides for the horizontal arc apex and
                       the bend corner. Defaults tuned to 又's PASSing shape.
    """
    hx, hy = head
    tx, ty = tail
    if apex_x is None:
        apex_x = hx + 130
    if corner_x is None:
        corner_x = hx + 125
    apex_y = hy - 3
    corner_y = hy + 8

    # --- Segment A: horizontal arc (head -> apex -> corner) ---
    steps_a = 90
    for i in range(steps_a):
        t = i / (steps_a - 1)
        bx = (1 - t) ** 2 * hx + 2 * (1 - t) * t * apex_x + t * t * corner_x
        by = (1 - t) ** 2 * hy + 2 * (1 - t) * t * apex_y + t * t * corner_y
        w = 5.5 + 2.5 * t
        draw.ellipse([bx - w, by - w, bx + w, by + w], fill='black')

    # --- Segment B: pie down-left, bows right ---
    steps_b = 70
    p0 = (corner_x, corner_y)
    p2 = (tx, ty)
    mx, my = (p0[0] + p2[0]) / 2, (p0[1] + p2[1]) / 2
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = (dx * dx + dy * dy) ** 0.5 or 1.0
    px, py = -dy / length, dx / length
    bow_perp = 18
    ctrl = (mx + px * bow_perp, my + py * bow_perp)

    for i in range(steps_b):
        t = i / (steps_b - 1)
        bx = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * ctrl[0] + t * t * p2[0]
        by = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * ctrl[1] + t * t * p2[1]
        w = 8.0 - 6.0 * t
        if w < 1.5:
            w = 1.5
        draw.ellipse([bx - w, by - w, bx + w, by + w], fill='black')
