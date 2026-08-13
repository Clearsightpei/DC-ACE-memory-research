"""Bank primitive: 犬 (quan, "dog" — 4 strokes = 大 skeleton + top-right dian).

Promoted from p2_radical_113_犬 (G5 B2 PASS 2026-08-08). Same skeleton as
大 (draw_da) plus an extra 丶 in upper right. Anchors are 犬-specific
(differ slightly from da_big.py's baked-in coords).
"""

from PIL import ImageDraw

from heng import draw_heng
from pie import draw_pie
from na import draw_na
from dian import draw_dian


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_quan(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1 heng
    draw_heng(draw, _tx(60.6, 165.5, ox, oy, scale),
              _tx(223.5, 149.7, ox, oy, scale),
              width_head=max(2, int(7 * scale)),
              width_tail=max(2, int(7 * scale)))
    # s2 pie (long sweep TC→BL)
    draw_pie(draw, _tx(129.2, 64.7, ox, oy, scale),
             _tx(41.6, 291.5, ox, oy, scale),
             bow_perp=-max(2, int(22 * scale)),
             w_head=max(2, int(5 * scale)),
             w_tail=max(1, int(2 * scale)))
    # s3 na (head at C, below heng — N-gap)
    draw_na(draw, _tx(148.8, 170.2, ox, oy, scale),
            _tx(283.6, 294.4, ox, oy, scale),
            bow_perp=-max(2, int(6 * scale)),
            w_head=max(2, int(3 * scale)),
            w_tail=max(3, int(10 * scale)))
    # s4 dian (upper-right small dot)
    draw_dian(draw, _tx(195.7, 89.4, ox, oy, scale),
              _tx(232.6, 113.7, ox, oy, scale),
              w_head=max(2, int(3 * scale)),
              w_tail=max(3, int(8 * scale)),
              bow=max(2, int(3 * scale)))
