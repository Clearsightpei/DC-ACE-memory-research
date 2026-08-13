"""Bank primitive: 八 (radical — 2 strokes, pie + na).

Promoted from p2_radical_009_八 (G5 bootstrap PASS, 2026-08-08).

Layout preserved from the PASSing 300x300 render. Callers can translate/scale
via (ox, oy, scale). Individual sub-strokes use pie.draw_pie / na.draw_na.
"""

from PIL import ImageDraw

from pie import draw_pie
from na import draw_na


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_ba(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    """Draw 八 at position (ox, oy) with given scale.

    Reference layout (scale=1.0): the pie originates near (97, 162)
    descending to (26, 264); the na originates near (132, 96) descending
    to (287, 257). No joint — clear separation.
    """
    pie_head = _tx(97, 162, ox, oy, scale)
    pie_tail = _tx(26, 264, ox, oy, scale)
    na_head = _tx(132, 96, ox, oy, scale)
    na_tail = _tx(287, 257, ox, oy, scale)

    draw_pie(draw, pie_head, pie_tail,
             bow_perp=12 * scale, w_head=9 * scale, w_tail=3 * scale)
    draw_na(draw, na_head, na_tail,
            bow_perp=14 * scale, w_head=4 * scale, w_tail=11 * scale)
