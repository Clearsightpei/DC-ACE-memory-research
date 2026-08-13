"""Bank primitive: 勹 (radical — 2 strokes; short 撇 + 橫折鉤 wrapper).

Promoted from p2_radical_010_勹 (G5 bootstrap PASS, 2026-08-08).
Reusable in 包, 匆, 匀, 勺.
"""

from PIL import ImageDraw

from pie import draw_pie


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def _catmull(p0, p1, p2, p3, N=25):
    pts = []
    for i in range(N):
        t = i / N
        t2, t3 = t * t, t * t * t
        x = 0.5 * ((2 * p1[0]) +
                   (-p0[0] + p2[0]) * t +
                   (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * t2 +
                   (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * t3)
        y = 0.5 * ((2 * p1[1]) +
                   (-p0[1] + p2[1]) * t +
                   (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * t2 +
                   (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * t3)
        pts.append((x, y))
    return pts


def draw_bao(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    """Draw 勹 at (ox, oy). Reference canvas 300x300."""
    # stroke 1: short pie
    draw_pie(draw,
             _tx(111.6, 64.5, ox, oy, scale),
             _tx(56.0, 168.2, ox, oy, scale),
             bow_perp=6 * scale,
             w_head=6 * scale, w_tail=3 * scale)

    # stroke 2: 橫折鉤 wrapper as a catmull spline through hand-tuned pts
    p_head = _tx(98.7, 133.6, ox, oy, scale)
    p_tail = _tx(145.3, 274.2, ox, oy, scale)
    ctrl = [p_head,
            _tx(150, 118, ox, oy, scale),
            _tx(215, 108, ox, oy, scale),
            _tx(232, 150, ox, oy, scale),
            _tx(230, 200, ox, oy, scale),
            _tx(200, 258, ox, oy, scale),
            p_tail]
    padded = [ctrl[0]] + ctrl + [ctrl[-1]]
    all_pts = []
    for i in range(len(padded) - 3):
        all_pts.extend(_catmull(padded[i], padded[i + 1],
                                padded[i + 2], padded[i + 3]))
    all_pts.append(p_tail)
    w = int(6 * scale)
    for i in range(len(all_pts) - 1):
        draw.line([all_pts[i], all_pts[i + 1]], fill='black', width=w)

    # small hook at tail
    tx_, ty_ = p_tail
    draw.line([p_tail, (tx_ - 10 * scale, ty_ - 14 * scale)],
              fill='black', width=w)
