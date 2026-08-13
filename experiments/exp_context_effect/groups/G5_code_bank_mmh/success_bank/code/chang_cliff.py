"""Bank primitive: 厂 (radical — 2 strokes; short 横 + long 撇).

Promoted from p2_radical_014_厂 (G5 bootstrap PASS, 2026-08-08).
Top stroke has a slight 顿笔 entry tick. Left stroke is a long 撇 that
bows outward (right) and sweeps far down. Joint class N — gap ~19 px
between the two heads at TL.

Reusable component in 厉, 历, 厄, 厚, 原 (upper structure).
"""

from PIL import ImageDraw


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def _stroke_line(d, p0, p1, w0, w1, steps=40):
    (x0, y0), (x1, y1) = p0, p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = (w0 + (w1 - w0) * t) / 2
        d.ellipse([x - r, y - r, x + r, y + r], fill='black')


def _stroke_bezier(d, pts, w0, w1, steps=80):
    (x0, y0), (x1, y1), (x2, y2) = pts
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * x0 + 2 * u * t * x1 + t * t * x2
        y = u * u * y0 + 2 * u * t * y1 + t * t * y2
        r = (w0 + (w1 - w0) * t) / 2
        d.ellipse([x - r, y - r, x + r, y + r], fill='black')


def draw_chang(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    """Draw 厂 at (ox, oy). Reference canvas 300x300."""
    # top heng with entry dun-tick then main body
    _stroke_line(draw,
                 _tx(97, 88, ox, oy, scale),
                 _tx(105, 95, ox, oy, scale),
                 5 * scale, 7 * scale, steps=15)
    _stroke_line(draw,
                 _tx(105, 95, ox, oy, scale),
                 _tx(243, 84, ox, oy, scale),
                 7 * scale, 5 * scale, steps=60)
    # long left-sweeping pie with rightward bow
    _stroke_bezier(draw,
                   [_tx(77, 94, ox, oy, scale),
                    _tx(85, 200, ox, oy, scale),
                    _tx(20, 297, ox, oy, scale)],
                   8 * scale, 3 * scale, steps=90)
