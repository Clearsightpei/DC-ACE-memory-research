# diao_char.py — 刁 (diāo), 2 strokes: 横折竖 (with corner blob + slight
# left-hook) + 提 (inline for correct angle).
# PASSed at p3_char_0034_刁 (B4). PIL px coords; scale=1.0 recommended.
import os


def _tapered_line(t, p0, p1, w0, w1, steps=24):
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = p0[0] + (p1[0] - p0[0]) * u0
        ya = p0[1] + (p1[1] - p0[1]) * u0
        xb = p0[0] + (p1[0] - p0[0]) * u1
        yb = p0[1] + (p1[1] - p0[1]) * u1
        w = max(1, int(w0 + (w1 - w0) * u0))
        t.line([(xa, ya), (xb, yb)], fill=(0, 0, 0), width=w)


def _tapered_bezier(t, p0, pc, p1, w0, w1, steps=40):
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps

        def bez(u):
            x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * pc[0] + u * u * p1[0]
            y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * pc[1] + u * u * p1[1]
            return x, y
        xa, ya = bez(u0)
        xb, yb = bez(u1)
        w = max(1, int(w0 + (w1 - w0) * u0))
        t.line([(xa, ya), (xb, yb)], fill=(0, 0, 0), width=w)


def draw_diao_char(t, ox=0, oy=0, scale=1.0):
    def P(x, y):
        return (150 + (x - 150) * scale + ox, 150 + (y - 150) * scale + oy)
    _tapered_line(t, P(55, 95), P(215, 88),
                  w0=int(6 * scale), w1=int(11 * scale), steps=28)
    cx, cy = P(215, 88)
    r = 7 * scale
    t.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))
    _tapered_bezier(t, P(215, 88), P(196, 178), P(200, 258),
                    w0=int(11 * scale), w1=int(9 * scale), steps=48)
    _tapered_bezier(t, P(200, 258), P(192, 273), P(170, 275),
                    w0=int(9 * scale), w1=max(1, int(2 * scale)), steps=22)
    _tapered_bezier(t, P(55, 185), P(120, 155), P(185, 138),
                    w0=int(12 * scale), w1=max(1, int(1 * scale)), steps=44)
