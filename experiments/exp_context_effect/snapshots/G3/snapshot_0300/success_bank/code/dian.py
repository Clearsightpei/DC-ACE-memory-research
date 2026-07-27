# dian.py — 点 (dian, short diagonal dot) coord primitive.
# Extracted from attempts/p1_stroke_05_点/generated.py after human PASS.

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    """Math-coord (center origin, +y up) -> PIL pixel (top-left, +y down)."""
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def draw_dian(t, ox=0.0, oy=0.0, scale=1.0):
    """Draw one 点 (short diagonal dot) stroke.

    Canonical unit 点: starts thin at upper-left (-15, +25), curves down
    and rightward to a heavier rounded tail at (+18, -20). Thickness
    grows from ~3 px at the head to ~14 px at the tail (opposite of
    撇's taper — 点 is heavier at the bottom).
    """
    # Endpoints in math coords, relative to (ox, oy)
    x0, y0 = -15.0 * scale, 25.0 * scale     # thin upper-left head
    x1, y1 = 18.0 * scale, -20.0 * scale     # heavy lower-right tail
    # Control point: pulled slightly down-left of chord midpoint so the
    # dot bows out on its lower-left side (characteristic 点 shape).
    mx = (x0 + x1) / 2.0 - 4.0 * scale
    my = (y0 + y1) / 2.0 - 4.0 * scale

    n_segments = 40
    thickness_head = max(1, 3.0 * scale)
    thickness_tail = max(1, 14.0 * scale)

    prev_pt = None
    for i in range(n_segments + 1):
        u = i / n_segments
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel(ox + bx, oy + by)
        if prev_pt is not None:
            w = thickness_head * (1 - u) + thickness_tail * u
            w_int = max(1, int(round(w)))
            t.line([prev_pt, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev_pt = (px, py)
