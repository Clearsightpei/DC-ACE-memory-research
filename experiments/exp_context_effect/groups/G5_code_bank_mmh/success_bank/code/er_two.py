"""Bank primitive: 二 (radical — 2 horizontal strokes; upper shorter).

Promoted from p2_radical_018_二 (G5 bootstrap PASS, 2026-08-08).
Convention: upper 横 is thinner AND shorter; lower is heavier and wider.
Named er_two to avoid Python 2/keyword-ish confusion.
"""

from PIL import ImageDraw

from heng import draw_heng


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_er(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    """Draw 二 at (ox, oy) with given scale (reference canvas 300x300)."""
    h1_head = _tx(85.8, 128, ox, oy, scale)
    h1_tail = _tx(214.7, 115.7, ox, oy, scale)
    h2_head = _tx(36.9, 235.8, ox, oy, scale)
    h2_tail = _tx(268.4, 232.6, ox, oy, scale)

    draw_heng(draw, h1_head, h1_tail,
              width_head=int(13 * scale), width_tail=int(13 * scale))
    draw_heng(draw, h2_head, h2_tail,
              width_head=int(15 * scale), width_tail=int(15 * scale))
