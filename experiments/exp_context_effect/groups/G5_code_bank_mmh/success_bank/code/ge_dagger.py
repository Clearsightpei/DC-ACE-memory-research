"""Bank primitive: 戈 (ge, "dagger-axe" — 4 strokes: heng + xie_gou + pie + dian).

Promoted from p2_radical_096_戈 (G5 B2 PASS 2026-08-08 via BANK_DEVIATION).
MEDIUM-REUSE: appears in 我/找/成/战/戏/戒/... Uses new xie_gou primitive
(also extracted from this PASS).
"""

from PIL import ImageDraw

from heng import draw_heng
from pie import draw_pie
from dian import draw_dian
from xie_gou import draw_xie_gou


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_ge(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: heng (short, slightly rising)
    draw_heng(draw, _tx(54.5, 167.9, ox, oy, scale),
              _tx(173.4, 133.0, ox, oy, scale),
              width_head=max(2, int(8 * scale)),
              width_tail=max(2, int(9 * scale)))
    # s2: xie-gou (long diagonal + terminal up-hook)
    draw_xie_gou(draw, head=_tx(95.0, 78.0, ox, oy, scale),
                 tail=_tx(238.0, 250.0, ox, oy, scale),
                 width=max(2, int(8 * scale)),
                 hook_up=max(6, int(34 * scale)))
    # s3: pie (upper-right diagonally down-left)
    draw_pie(draw, _tx(192.2, 157.0, ox, oy, scale),
             _tx(69.7, 278.6, ox, oy, scale),
             bow_perp=-max(2, int(16 * scale)),
             w_head=max(2, int(9 * scale)),
             w_tail=max(1, int(3 * scale)))
    # s4: dian (short down-right dot at top)
    draw_dian(draw, _tx(178.0, 78.0, ox, oy, scale),
              _tx(212.7, 105.0, ox, oy, scale),
              w_head=max(1, int(2 * scale)),
              w_tail=max(2, int(7 * scale)),
              bow=max(1, int(3 * scale)))
