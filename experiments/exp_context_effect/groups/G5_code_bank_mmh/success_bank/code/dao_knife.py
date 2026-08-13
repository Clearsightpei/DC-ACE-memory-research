"""Bank primitive: 刀 (radical — 2 strokes; 横折钩 + 撇).

Promoted from p2_radical_015_刀 (G5 bootstrap PASS, 2026-08-08).
Reusable component in 分, 切, 召, 忍.
"""

from PIL import ImageDraw


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def _smooth_polyline(d, pts, width=7):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill='black', width=int(width))
    r = int(width) // 2
    for x, y in pts:
        d.ellipse([x - r, y - r, x + r, y + r], fill='black')


def draw_dao(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    """Draw 刀 at (ox, oy). Reference canvas 300x300."""
    s1 = [_tx(76, 116, ox, oy, scale),
          _tx(100, 108, ox, oy, scale),
          _tx(135, 102, ox, oy, scale),
          _tx(170, 100, ox, oy, scale),
          _tx(200, 102, ox, oy, scale),
          _tx(220, 110, ox, oy, scale),
          _tx(228, 128, ox, oy, scale),
          _tx(226, 155, ox, oy, scale),
          _tx(220, 185, ox, oy, scale),
          _tx(208, 213, ox, oy, scale),
          _tx(190, 232, ox, oy, scale),
          _tx(170, 242, ox, oy, scale),
          _tx(150, 246, ox, oy, scale)]
    _smooth_polyline(draw, s1, width=7 * scale)

    s2 = [_tx(132, 123, ox, oy, scale),
          _tx(122, 145, ox, oy, scale),
          _tx(108, 172, ox, oy, scale),
          _tx(92, 198, ox, oy, scale),
          _tx(74, 223, ox, oy, scale),
          _tx(55, 248, ox, oy, scale),
          _tx(35, 272, ox, oy, scale)]
    _smooth_polyline(draw, s2, width=7 * scale)
