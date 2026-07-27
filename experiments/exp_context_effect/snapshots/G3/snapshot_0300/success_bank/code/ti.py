# ti.py — 提 (ti, rising stroke) coord primitive.
# Extracted from attempts/p1_stroke_06_提/generated.py after human PASS.

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    """Math-coord (center origin, +y up) -> PIL pixel (top-left, +y down)."""
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def draw_ti(t, ox=0.0, oy=0.0, scale=1.0):
    """Draw one 提 (rising stroke) from lower-left to upper-right.

    Head thick pressed at (-70, -70); tip needle at (+80, +60);
    slight upward bow.
    """
    x0, y0 = -70.0 * scale, -70.0 * scale
    x1, y1 = 80.0 * scale, 60.0 * scale
    mx = (x0 + x1) / 2.0 - 5.0 * scale
    my = (y0 + y1) / 2.0 + 12.0 * scale

    n_segments = 60
    thickness_head = max(1, 16.0 * scale)
    thickness_tip = 1.0

    prev_pt = None
    for i in range(n_segments + 1):
        u = i / n_segments
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel(ox + bx, oy + by)
        if u < 0.1:
            w = thickness_head
        else:
            w = thickness_head + (thickness_tip - thickness_head) * ((u - 0.1) / 0.9)
        w_int = max(1, int(round(w)))
        if prev_pt is not None:
            t.line([prev_pt, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev_pt = (px, py)
