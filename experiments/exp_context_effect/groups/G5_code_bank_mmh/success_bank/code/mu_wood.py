"""Bank primitive: 木 (mu, "wood/tree" — 4 strokes: heng + shu + pie + na).

Promoted from p2_radical_104_木 (G5 B2 PASS 2026-08-08). VERY HIGH-REUSE:
appears in 林/森/树/杯/校/... Symmetric composition — pie and na fork
from just under the heng down to BL and BR. Central shu pierces the
heng at C (P joint); pie/na heads sit BELOW heng (N gaps).
"""

from PIL import ImageDraw

from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
from na import draw_na


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_mu(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1 heng across middle band
    draw_heng(draw, _tx(66.8, 143.6, ox, oy, scale),
              _tx(224.4, 131.8, ox, oy, scale),
              width_head=max(2, int(9 * scale)),
              width_tail=max(2, int(10 * scale)))
    # s2 central shu (tail clips below canvas naturally)
    draw_shu(draw, _tx(132.7, 58.3, ox, oy, scale),
             _tx(142.4, 295.0, ox, oy, scale),
             width=max(2, int(7 * scale)))
    # s3 left pie
    draw_pie(draw, _tx(138.9, 147.9, ox, oy, scale),
             _tx(38.1, 263.7, ox, oy, scale),
             bow_perp=max(2, int(8 * scale)),
             w_head=max(2, int(6 * scale)),
             w_tail=max(1, int(2 * scale)))
    # s4 right na
    draw_na(draw, _tx(154.7, 149.7, ox, oy, scale),
            _tx(278.6, 253.4, ox, oy, scale),
            bow_perp=max(2, int(12 * scale)),
            w_head=max(2, int(4 * scale)),
            w_tail=max(3, int(10 * scale)))
