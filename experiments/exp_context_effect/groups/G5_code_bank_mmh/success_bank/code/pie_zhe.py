"""Bank primitive: 撇折 (pie-zhe, curved pie + short zhe corner).

Promoted from p2_radical_078_幺__retry_1 (G5 B3 R1 PASS 2026-08-08).
The 幺 attempt inlined this as `draw_pie_zhe`; extracting to bank for
reuse in the yao/mi/xian-family (幺/纟/么/糸/etc.).

head->corner sweeps down-left with clear bow (like a 撇); corner->tail
runs shorter, near-straight down-right (the 折). Distinct corner
(not a smooth arc).

Endpoint signature. head, corner, tail are all (x, y).
"""

from PIL import ImageDraw


def _bezier_pt(p0, p1, p2, t):
    u = 1 - t
    return (u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0],
            u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1])


def draw_pie_zhe(draw: ImageDraw.ImageDraw, head, corner, tail,
                 pie_bow=7, zhe_bow=1,
                 w_head=6, w_corner=5, w_tail=4, steps=70):
    # Pie segment (curved, bows LEFT of travel)
    mx, my = (head[0] + corner[0]) / 2, (head[1] + corner[1]) / 2
    dx, dy = corner[0] - head[0], corner[1] - head[1]
    L = (dx * dx + dy * dy) ** 0.5 or 1.0
    px, py = dy / L, -dx / L  # left-of-travel
    ctrl = (mx + px * pie_bow, my + py * pie_bow)
    for i in range(steps + 1):
        t = i / steps
        x, y = _bezier_pt(head, ctrl, corner, t)
        r = w_head + (w_corner - w_head) * t
        draw.ellipse([x - r, y - r, x + r, y + r], fill='black')

    # Zhe segment (short, near-straight, mild right-bow)
    mx, my = (corner[0] + tail[0]) / 2, (corner[1] + tail[1]) / 2
    dx, dy = tail[0] - corner[0], tail[1] - corner[1]
    L = (dx * dx + dy * dy) ** 0.5 or 1.0
    px, py = -dy / L, dx / L  # right-of-travel
    ctrl = (mx + px * zhe_bow, my + py * zhe_bow)
    for i in range(steps + 1):
        t = i / steps
        x, y = _bezier_pt(corner, ctrl, tail, t)
        r = w_corner + (w_tail - w_corner) * t
        draw.ellipse([x - r, y - r, x + r, y + r], fill='black')
