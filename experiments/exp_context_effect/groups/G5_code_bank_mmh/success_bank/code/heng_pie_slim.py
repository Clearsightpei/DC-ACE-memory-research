"""Bank primitive: 横撇-slim — slim variant of heng_pie for 夕-family.

Promoted from p3_char_0245_多 (G5 B8 PASS, 2nd DEVIATION on heng_pie per
P-COMP-002). Slimmer bow (~6) and thinner taper than heng_pie.py which
was tuned for 又's fat 横撇.

Reuse targets: 多/名/夜/岁-family (夕's compact 横撇). Also useful for
又/欠-family when the composition wants a slimmer horizontal-then-pie.

Signature: (d, head, tail, apex_x, corner_x, bow_perp=6, w_head=6, w_tail=3)
  - apex_x, corner_x: only used to compute a horizontal tick length;
    passed through for API compatibility with heng_pie.py.
"""


def draw_heng_pie_slim(d, head, tail, apex_x=None, corner_x=None,
                       horiz_len=18, bow_perp=6, w_head=6, w_corner=5, w_tail=3):
    """Slim 横撇 for 夕-family: short horizontal tick + gently-bowed pie.

    - head: (x, y) top-left of horizontal tick.
    - tail: (x, y) bottom-left end of pie.
    - Optional apex_x/corner_x mirror the heng_pie.py signature; if given,
      horiz_len defaults from (corner_x - head_x).
    """
    hx, hy = head
    tx, ty = tail
    if corner_x is not None:
        horiz_len = corner_x - hx
    corner = (hx + horiz_len, hy + 4)

    # Segment A: short horizontal (head -> corner), slight downward drift
    steps_a = 30
    for i in range(steps_a):
        t = i / (steps_a - 1)
        bx = hx + t * (corner[0] - hx)
        by = hy + t * (corner[1] - hy)
        r = w_head + (w_corner - w_head) * t
        d.ellipse([bx - r, by - r, bx + r, by + r], fill='black')

    # Segment B: pie down-left, gently bowed (bow to the right of travel)
    steps_b = 80
    p0 = corner
    p2 = (tx, ty)
    mx, my = (p0[0] + p2[0]) / 2, (p0[1] + p2[1]) / 2
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = (dx * dx + dy * dy) ** 0.5 or 1.0
    px, py = -dy / length, dx / length
    ctrl = (mx + px * bow_perp, my + py * bow_perp)
    for i in range(steps_b):
        t = i / (steps_b - 1)
        u = 1 - t
        bx = u * u * p0[0] + 2 * u * t * ctrl[0] + t * t * p2[0]
        by = u * u * p0[1] + 2 * u * t * ctrl[1] + t * t * p2[1]
        r = w_corner + (w_tail - w_corner) * t
        if r < 1.2:
            r = 1.2
        d.ellipse([bx - r, by - r, bx + r, by + r], fill='black')
