"""Bank primitive: 女 (nu, "woman" — 3 strokes: pie_dian_compound + pie + heng).

Promoted from p2_radical_061_女__retry_2 (G5 B3 R2 PASS 2026-08-08).
VERY HIGH-REUSE (好/她/妈/如/姐/妹/婚/etc.). Encoded fully inline because
the 撇点 compound stroke has no bank primitive, and the joint constraint
(P-P-T triple) requires coherent placement.
"""

from PIL import ImageDraw

_INK = (0, 0, 0)


def _bezier_quad(p0, p1, p2, n):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


def _taper(n, w_head, w_mid, w_tail):
    out = []
    for i in range(n + 1):
        t = i / n
        if t < 0.5:
            u = t / 0.5
            w = w_head * (1 - u) + w_mid * u
        else:
            u = (t - 0.5) / 0.5
            w = w_mid * (1 - u) + w_tail * u
        out.append(w)
    return out


def _stamp_chain(draw, pts, widths):
    for (x, y), w in zip(pts, widths):
        r = max(0.5, w / 2.0)
        draw.ellipse([x - r, y - r, x + r, y + r], fill=_INK)
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        w = max(widths[i], widths[i + 1])
        dx, dy = x1 - x0, y1 - y0
        dist = (dx * dx + dy * dy) ** 0.5
        steps = max(1, int(dist / 0.8))
        for s in range(steps + 1):
            t = s / steps
            xs, ys = x0 + dx * t, y0 + dy * t
            r = max(0.5, w / 2.0)
            draw.ellipse([xs - r, ys - r, xs + r, ys + r], fill=_INK)


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_nu_woman(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: 撇点 compound — pie head down-left to corner, then dian down-right to BR
    p_head = _tx(129.5, 62.7, ox, oy, scale)
    corner = _tx(109.0, 178.0, ox, oy, scale)
    p_tail = _tx(230.6, 296.8, ox, oy, scale)
    pie_ctrl = _tx(122.0, 118.0, ox, oy, scale)
    pie_pts = _bezier_quad(p_head, pie_ctrl, corner, 40)
    pie_w = [w * scale for w in _taper(40, 9.0, 8.0, 6.5)]
    dian_ctrl = _tx(155.0, 230.0, ox, oy, scale)
    dian_pts = _bezier_quad(corner, dian_ctrl, p_tail, 50)
    dian_w = [w * scale for w in _taper(50, 6.5, 9.0, 6.5)]
    _stamp_chain(draw, pie_pts, pie_w)
    _stamp_chain(draw, dian_pts, dian_w)

    # s2: long pie from C down-left to BL
    p_head2 = _tx(184.0, 145.6, ox, oy, scale)
    p_tail2 = _tx(69.7, 283.0, ox, oy, scale)
    ctrl2 = _tx(120.0, 200.0, ox, oy, scale)
    pts2 = _bezier_quad(p_head2, ctrl2, p_tail2, 60)
    w2 = [w * scale for w in _taper(60, 9.5, 8.0, 3.0)]
    _stamp_chain(draw, pts2, w2)

    # s3: long heng across mid with slight upward tilt
    p_head3 = _tx(20.5, 177.0, ox, oy, scale)
    p_tail3 = _tx(278.3, 165.8, ox, oy, scale)
    ctrl3 = _tx(150.0, 168.0, ox, oy, scale)
    pts3 = _bezier_quad(p_head3, ctrl3, p_tail3, 60)
    w3 = [w * scale for w in _taper(60, 6.0, 8.5, 7.5)]
    _stamp_chain(draw, pts3, w3)
