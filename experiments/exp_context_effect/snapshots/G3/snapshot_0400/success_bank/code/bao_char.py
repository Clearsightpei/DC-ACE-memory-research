# bao_char.py — 勹 (bāo), 2 strokes: short 撇 + continuous envelope
# (horizontal top → rounded shoulder → descending shaft → up-left hook).
# PASSed at p3_char_0037_勹 (B4).
# Recipe: PIL px coords for 300x300 canvas. (ox, oy, scale) shifts+scales
# the render around canvas center (150, 150).
import os
_HERE = os.path.dirname(os.path.abspath(__file__))


def _qbez(p0, p1, p2, steps):
    pts = []
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        pts.append((x, y))
    return pts


def _cbez(p0, p1, p2, p3, steps):
    pts = []
    for i in range(steps + 1):
        u = i / steps
        b0 = (1 - u) ** 3
        b1 = 3 * (1 - u) ** 2 * u
        b2 = 3 * (1 - u) * u * u
        b3 = u ** 3
        x = b0 * p0[0] + b1 * p1[0] + b2 * p2[0] + b3 * p3[0]
        y = b0 * p0[1] + b1 * p1[1] + b2 * p2[1] + b3 * p3[1]
        pts.append((x, y))
    return pts


def _draw_var(t, pts, widths, ox, oy, scale):
    for i in range(len(pts) - 1):
        w = max(2, int(round(widths[i] * scale)))
        ax = 150 + ox + (pts[i][0] - 150) * scale
        ay = 150 + oy + (pts[i][1] - 150) * scale
        bx = 150 + ox + (pts[i + 1][0] - 150) * scale
        by = 150 + oy + (pts[i + 1][1] - 150) * scale
        t.line([(ax, ay), (bx, by)], fill=(0, 0, 0), width=w)
        r = w / 2.0
        t.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))


def draw_bao_char(t, ox=0, oy=0, scale=1.0):
    # Pie
    pie = _qbez((95, 45), (78, 65), (60, 100), 30)
    _draw_var(t, pie, [5 - 2 * (i / (len(pie) - 1)) for i in range(len(pie))],
              ox, oy, scale)
    # Envelope top
    seg_a = _qbez((80, 100), (147, 100), (215, 95), 24)
    _draw_var(t, seg_a, [7] * len(seg_a), ox, oy, scale)
    # Shoulder
    seg_b = _cbez((215, 95), (228, 95), (232, 110), (230, 125), 18)
    _draw_var(t, seg_b, [7] * len(seg_b), ox, oy, scale)
    # Shaft
    seg_c = _cbez((230, 125), (225, 175), (215, 225), (195, 255), 50)
    _draw_var(t, seg_c, [7 - 2 * (i / (len(seg_c) - 1))
                         for i in range(len(seg_c))],
              ox, oy, scale)
    # Hook
    seg_d = _qbez((195, 255), (183, 253), (168, 238), 15)
    _draw_var(t, seg_d, [5 - 3 * (i / (len(seg_d) - 1))
                         for i in range(len(seg_d))],
              ox, oy, scale)
