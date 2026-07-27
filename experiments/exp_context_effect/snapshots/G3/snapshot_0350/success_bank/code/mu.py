# mu.py — 木 (mù, tree/wood), 4 strokes: 横 + 竖 + 撇 + 捺 crossing at (0,+25).
# Batch B2 (position 136) — human PASSed.
# Fully inlined: heng + shu + pie + na with matched thin (~7px) weight.
# Documents inline-fresh solution for 大-family (heng + crossing pie + na).

import math


CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    return CANVAS_SIZE / 2 + ox, CANVAS_SIZE / 2 - oy


def _inline_heng(t, xc, yc, half_len, thickness):
    xL, yL = _to_pixel(xc - half_len, yc)
    xR, yR = _to_pixel(xc + half_len, yc)
    t.line([(xL, yL), (xR, yR)], fill=(0, 0, 0), width=thickness)


def _inline_shu(t, xc, yc, half_len, thickness):
    xT, yT = _to_pixel(xc, yc + half_len)
    xB, yB = _to_pixel(xc, yc - half_len)
    t.line([(xT, yT), (xB, yB)], fill=(0, 0, 0), width=thickness)


def _inline_pie(t, x0, y0, x1, y1, w_head=7.0, w_tail=1.0, bow_perp=-6.0):
    mx0 = (x0 + x1) / 2.0
    my0 = (y0 + y1) / 2.0
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    perp_x, perp_y = -dy / L, dx / L
    mx = mx0 + perp_x * bow_perp
    my = my0 + perp_y * bow_perp
    n = 60
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel(bx, by)
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def _inline_na(t, x0, y0, x1, y1, w_head=2.0, w_belly=11.0, w_tail=2.0, bow_perp=6.0):
    mx0 = (x0 + x1) / 2.0
    my0 = (y0 + y1) / 2.0
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    perp_x, perp_y = -dy / L, dx / L
    mx = mx0 + perp_x * bow_perp
    my = my0 + perp_y * bow_perp
    n = 60
    u_belly = 0.7
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel(bx, by)
        if u <= u_belly:
            w = w_head + (w_belly - w_head) * (u / u_belly)
        else:
            w = w_belly + (w_tail - w_belly) * ((u - u_belly) / (1 - u_belly))
        wi = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def draw_mu(t, ox=0.0, oy=0.0, scale=1.0):
    """木 radical, 4 strokes with matched thin weight."""
    _inline_heng(t, ox + 0, oy + 25 * scale, 95 * scale, thickness=7)
    _inline_shu(t, ox + 0, oy + (-32.5) * scale, 82.5 * scale, thickness=7)
    _inline_pie(t, x0=ox + 0, y0=oy + 25 * scale,
                x1=ox + (-95) * scale, y1=oy + (-110) * scale,
                w_head=7.0 * scale, w_tail=1.0, bow_perp=-6.0 * scale)
    _inline_na(t, x0=ox + 0, y0=oy + 25 * scale,
               x1=ox + 95 * scale, y1=oy + (-110) * scale,
               w_head=2.0 * scale, w_belly=11.0 * scale, w_tail=2.0 * scale,
               bow_perp=6.0 * scale)
