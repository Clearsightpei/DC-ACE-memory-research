"""Bank primitive: 卜 (radical — 2 strokes; 竖 + diagonal 点).

Promoted from p2_radical_013_卜 (G5 bootstrap PASS, 2026-08-08).

Left stroke is a vertical with a subtle J-tip curl at the top (not a
full hook). Right stroke is a diagonal 点 (thick belly, thin ends).
Joint class N — dot head sits to the right of the vertical shaft with a
~40 px gap; do NOT weld.

Reusable component in 上, 占, 卡, 外.
"""

from PIL import ImageDraw


def _dot(d, p, r, fill='black'):
    d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=fill)


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_bu(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    """Draw 卜 at (ox, oy). Reference canvas 300x300."""
    # --- Stroke 1: 竖 with subtle J-tip curl at the top ---
    tip = [_tx(100, 82, ox, oy, scale),
           _tx(98, 86, ox, oy, scale),
           _tx(100, 92, ox, oy, scale),
           _tx(104, 96, ox, oy, scale)]
    w1 = max(1, int(8 * scale))
    for i in range(len(tip) - 1):
        draw.line([tip[i], tip[i + 1]], fill='black', width=w1)
    for p in tip:
        _dot(draw, p, 4 * scale)
    body = [_tx(104, 96, ox, oy, scale),
            _tx(106, 140, ox, oy, scale),
            _tx(107, 190, ox, oy, scale),
            _tx(108, 240, ox, oy, scale),
            _tx(109, 285, ox, oy, scale)]
    for i in range(len(body) - 1):
        draw.line([body[i], body[i + 1]], fill='black', width=w1)
    for p in body:
        _dot(draw, p, 4 * scale)

    # --- Stroke 2: 点 diagonal filled tapered quad ---
    head = _tx(148, 158, ox, oy, scale)
    tail = _tx(200, 214, ox, oy, scale)
    mid = _tx(174, 186, ox, oy, scale)
    dx, dy = tail[0] - head[0], tail[1] - head[1]
    length = (dx * dx + dy * dy) ** 0.5 or 1.0
    px, py = -dy / length, dx / length
    w_head, w_mid, w_tail = 3 * scale, 9 * scale, 3 * scale
    poly = [
        (head[0] + px * w_head, head[1] + py * w_head),
        (mid[0] + px * w_mid, mid[1] + py * w_mid),
        (tail[0] + px * w_tail, tail[1] + py * w_tail),
        (tail[0] - px * w_tail, tail[1] - py * w_tail),
        (mid[0] - px * w_mid, mid[1] - py * w_mid),
        (head[0] - px * w_head, head[1] - py * w_head),
    ]
    draw.polygon(poly, fill='black')
    _dot(draw, head, w_head + 1)
    _dot(draw, mid, w_mid)
    _dot(draw, tail, w_tail + 1)
