"""Bank primitive: 幺 (yao, "tiny" — 3 strokes: pie_zhe + pie_zhe + diagonal).

Promoted from p2_radical_078_幺__retry_1 (G5 B3 R1 PASS 2026-08-08).
Sibling of 纟 (silk-radical, still C — 3 strokes: 2 pie_zhe + ti tail).
幺 differs from 纟 in that s3 is a tapered diagonal (like long dot), not
a rising ti.
"""

from PIL import ImageDraw

from pie_zhe import draw_pie_zhe


def _bezier_pt(p0, p1, p2, t):
    u = 1 - t
    return (u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0],
            u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1])


def _draw_diag_taper(draw, head, tail, w_head=3, w_tail=8, bow=4, steps=48):
    mx, my = (head[0] + tail[0]) / 2, (head[1] + tail[1]) / 2
    dx, dy = tail[0] - head[0], tail[1] - head[1]
    L = (dx * dx + dy * dy) ** 0.5 or 1.0
    px, py = -dy / L, dx / L
    ctrl = (mx + px * bow, my + py * bow)
    for i in range(steps + 1):
        t = i / steps
        x, y = _bezier_pt(head, ctrl, tail, t)
        r = w_head + (w_tail - w_head) * t
        draw.ellipse([x - r, y - r, x + r, y + r], fill='black')


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_yao_tiny(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: small 撇折 at top
    draw_pie_zhe(draw, _tx(142, 76, ox, oy, scale),
                 _tx(128, 155, ox, oy, scale),
                 _tx(158, 180, ox, oy, scale),
                 pie_bow=7, zhe_bow=1,
                 w_head=max(2, int(6 * scale)),
                 w_corner=max(2, int(5 * scale)),
                 w_tail=max(2, int(4 * scale)))
    # s2: larger 撇折 in middle
    draw_pie_zhe(draw, _tx(196, 136, ox, oy, scale),
                 _tx(150, 220, ox, oy, scale),
                 _tx(210, 268, ox, oy, scale),
                 pie_bow=9, zhe_bow=2,
                 w_head=max(2, int(7 * scale)),
                 w_corner=max(2, int(6 * scale)),
                 w_tail=max(2, int(5 * scale)))
    # s3: tapered diagonal (like long dot)
    _draw_diag_taper(draw, _tx(191, 226, ox, oy, scale),
                     _tx(232, 293, ox, oy, scale),
                     w_head=max(2, int(3 * scale)),
                     w_tail=max(2, int(8 * scale)),
                     bow=max(2, int(4 * scale)))
