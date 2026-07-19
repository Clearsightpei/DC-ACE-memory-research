# na.py — 捺 (na, rightward downward sweep) coord primitive.
# Extracted from attempts/p1_stroke_04_捺/generated.py after human PASS.

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    """Math-coord (center origin, +y up) -> PIL pixel (top-left, +y down)."""
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def draw_na(t, ox=0.0, oy=0.0, scale=1.0):
    """Draw one 捺 (rightward downward sweep).

    Canonical unit 捺: starts thin at upper-left (-70, +80), curves down
    and rightward, swells in the middle, tapers off to a foot at (+80, -90).
    """
    x0, y0 = -70.0 * scale, 80.0 * scale
    x1, y1 = 80.0 * scale, -90.0 * scale
    mx = (x0 + x1) / 2.0 + 10.0 * scale
    my = (y0 + y1) / 2.0 - 15.0 * scale

    n_segments = 60
    thickness_head = max(1, 2.0 * scale)
    thickness_belly = max(1, 18.0 * scale)
    thickness_tail = max(1, 3.0 * scale)

    prev_pt = None
    for i in range(n_segments + 1):
        u = i / n_segments
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel(ox + bx, oy + by)
        t_belly = 0.7
        if u <= t_belly:
            w = thickness_head + (thickness_belly - thickness_head) * (u / t_belly)
        else:
            w = thickness_belly + (thickness_tail - thickness_belly) * ((u - t_belly) / (1 - t_belly))
        w_int = max(1, int(round(w)))
        if prev_pt is not None:
            t.line([prev_pt, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev_pt = (px, py)
