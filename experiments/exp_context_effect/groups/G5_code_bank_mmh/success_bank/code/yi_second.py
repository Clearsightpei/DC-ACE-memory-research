"""Bank primitive: 乙 (radical — single continuous S/hook curve).

Promoted from p2_radical_006_乙 (G5 bootstrap PASS, 2026-08-08).

Rendered as a chain of 5 quadratic bezier segments (top curve, throat
descent, bottom-left sweep, bottom-right sweep, terminal hook up).
Single stroke conceptually — one continuous path.
"""

from PIL import ImageDraw


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def _bezier(p0, p1, p2, steps=50):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    return pts


def draw_yi_second(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    """Draw 乙 at (ox, oy). Reference canvas 300x300."""
    top_start = _tx(95, 125, ox, oy, scale)
    top_apex = _tx(135, 108, ox, oy, scale)
    top_end = _tx(175, 128, ox, oy, scale)
    throat_ctrl = _tx(155, 180, ox, oy, scale)
    throat_end = _tx(105, 220, ox, oy, scale)
    bl_ctrl = _tx(82, 255, ox, oy, scale)
    bl_end = _tx(85, 278, ox, oy, scale)
    bot_ctrl = _tx(150, 288, ox, oy, scale)
    bot_end = _tx(220, 275, ox, oy, scale)
    hook_ctrl = _tx(223, 258, ox, oy, scale)
    hook_end = _tx(222, 240, ox, oy, scale)

    segs = []
    segs += _bezier(top_start, top_apex, top_end)
    segs += _bezier(top_end, throat_ctrl, throat_end)
    segs += _bezier(throat_end, bl_ctrl, bl_end)
    segs += _bezier(bl_end, bot_ctrl, bot_end)
    segs += _bezier(bot_end, hook_ctrl, hook_end)

    w = int(6 * scale)
    for i in range(len(segs) - 1):
        draw.line([segs[i], segs[i + 1]], fill='black', width=w)
    r = int(3 * scale)
    for p in [top_start, top_end, throat_end, bl_end, bot_end, hook_end]:
        draw.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill='black')
