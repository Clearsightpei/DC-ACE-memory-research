# bu_char.py — 不 (bù), 4 strokes: 横 + 丿 + 丨 + 丶.
# PASSed at p3_char_0094_不 (B5, pos 256). Inline PIL thin (~7px) recipe
# adapted from mu.py — heng at top, pie from heng center down-left, short
# shu descending from heng center, dian on the right.
import math


def draw_bu_char(t, ox=0.0, oy=0.0, scale=1.0):
    """不 — 4 strokes (inline PIL bezier + line, thin ~7px)."""
    def _to_pixel(mx, my):
        return 150 + mx, 150 - my

    def _heng(xc, yc, half_len, thickness):
        xL, yL = _to_pixel(xc - half_len, yc)
        xR, yR = _to_pixel(xc + half_len, yc)
        t.line([(xL, yL), (xR, yR)], fill=(0, 0, 0), width=thickness)

    def _shu(xc, yc, half_len, thickness):
        xT, yT = _to_pixel(xc, yc + half_len)
        xB, yB = _to_pixel(xc, yc - half_len)
        t.line([(xT, yT), (xB, yB)], fill=(0, 0, 0), width=thickness)

    def _pie(x0, y0, x1, y1, w_head, w_tail, bow_perp=-6.0):
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

    def _dian(x0, y0, x1, y1, w_head, w_tail):
        dx, dy = x1 - x0, y1 - y0
        L = math.hypot(dx, dy) or 1.0
        perp_x, perp_y = -dy / L, dx / L
        bow_perp = -2.0
        mx = (x0 + x1) / 2.0 + perp_x * bow_perp
        my = (y0 + y1) / 2.0 + perp_y * bow_perp
        n = 40
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

    # Apply ox/oy/scale
    _heng(ox + 0, oy + 75 * scale, 105 * scale, thickness=6)
    _pie(ox + 10 * scale, oy + 65 * scale,
         ox + (-90) * scale, oy + (-110) * scale,
         w_head=7.0 * scale, w_tail=2.0, bow_perp=-7.0 * scale)
    _shu(ox + 8 * scale, oy + (-45) * scale, 75 * scale, thickness=6)
    _dian(ox + 40 * scale, oy + (-5) * scale,
          ox + 85 * scale, oy + (-70) * scale,
          w_head=3.0 * scale, w_tail=8.0 * scale)
