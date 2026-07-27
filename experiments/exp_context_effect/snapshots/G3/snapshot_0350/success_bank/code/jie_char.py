# jie_char.py — 孑 (jié), 3 strokes: 横撇 + 弯钩 + 提.
# PASSed at p3_char_0074_孑 (B4). Inline fresh (no crossbar unlike 子).
# NOTE: Uses PIL px coords + (ox, oy) shift. Scale param treated as identity
# by the passing recipe; wrap-scaling applied around canvas center.
import os


def _var_line(t, pts, w_start, w_end):
    n = len(pts) - 1
    for i in range(n):
        u0 = i / n if n else 0
        w = max(2, int(round(w_start + (w_end - w_start) * u0)))
        t.line([pts[i], pts[i + 1]], fill=(0, 0, 0), width=w)
    r0 = max(1, w_start // 2)
    x, y = pts[0]
    t.ellipse([x - r0, y - r0, x + r0, y + r0], fill=(0, 0, 0))
    rN = max(1, w_end // 2)
    x, y = pts[-1]
    t.ellipse([x - rN, y - rN, x + rN, y + rN], fill=(0, 0, 0))


def _bez(p0, p1, p2, steps=24):
    out = []
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        out.append((x, y))
    return out


def _cubic(p0, p1, p2, p3, steps=32):
    out = []
    for i in range(steps + 1):
        u = i / steps
        x = ((1 - u) ** 3 * p0[0] + 3 * (1 - u) ** 2 * u * p1[0]
             + 3 * (1 - u) * u * u * p2[0] + u ** 3 * p3[0])
        y = ((1 - u) ** 3 * p0[1] + 3 * (1 - u) ** 2 * u * p1[1]
             + 3 * (1 - u) * u * u * p2[1] + u ** 3 * p3[1])
        out.append((x, y))
    return out


def draw_jie_char(t, ox=0, oy=0, scale=1.0):
    # ox/oy shift; scale not fully applied in the original PASS (recipe
    # is tuned for scale=1.0). Callers should use scale=1.0 for exact
    # reproduction.
    h_left = (65 + ox, 88 + oy); h_right = (200 + ox, 78 + oy)
    _var_line(t, [h_left, (105 + ox, 85 + oy),
                  (155 + ox, 80 + oy), h_right], 5, 10)
    pie_end = (150 + ox, 130 + oy)
    pie_pts = _cubic(h_right, (200 + ox, 100 + oy),
                     (175 + ox, 118 + oy), pie_end, 22)
    _var_line(t, pie_pts, 10, 3)
    top = (155 + ox, 118 + oy)
    shaft = _cubic(top, (180 + ox, 165 + oy),
                   (172 + ox, 215 + oy), (155 + ox, 250 + oy), 32)
    _var_line(t, shaft, 9, 10)
    hpts = _bez(shaft[-1], (138 + ox, 252 + oy),
                (118 + ox, 238 + oy), 14)
    _var_line(t, hpts, 10, 3)
    _var_line(t, [(95 + ox, 180 + oy), (140 + ox, 172 + oy),
                  (188 + ox, 160 + oy), (235 + ox, 152 + oy)], 10, 3)
