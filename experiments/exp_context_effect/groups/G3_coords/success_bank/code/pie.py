# pie.py — 撇 (pie, left-falling tapered sweep) coord primitive.
# Canonical: starts thick at upper-right (+65, +90), curves down-left,
# tapers to a fine tip at lower-left (-45, -85).

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    """Math-coord (center origin, +y up) -> PIL pixel (top-left, +y down)."""
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def draw_pie(t, ox=0.0, oy=0.0, scale=1.0):
    """Draw one 撇 stroke: tapered curve from upper-right to lower-left."""
    x0, y0 = 65.0 * scale, 90.0 * scale     # thick upper-right head
    x1, y1 = -45.0 * scale, -85.0 * scale   # thin lower-left tail
    # Control point: pulled slightly left of chord to bow the sweep.
    mx = (x0 + x1) / 2.0 - 10.0 * scale
    my = (y0 + y1) / 2.0 + 5.0 * scale

    n_segments = 60
    w_head = max(1, 10.0 * scale)
    w_tail = 1.0

    prev_pt = None
    for i in range(n_segments + 1):
        u = i / n_segments
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel(ox + bx, oy + by)
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev_pt is not None:
            t.line([prev_pt, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev_pt = (px, py)
