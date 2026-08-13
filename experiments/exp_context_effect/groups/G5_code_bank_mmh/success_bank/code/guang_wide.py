"""Bank primitive: 广 (guang, 'wide' — 3 strokes: dian + heng + pie).

Promoted from p2_radical_052_广 (G5 B1 PASS, 2026-08-08). HIGH-REUSE:
enclosing radical in 应/床/店/府/座/... The long pie sweeps down-left far
past the horizontal, occupying the whole left side of any enclosed char.
"""

from PIL import ImageDraw

from dian import draw_dian
from heng import draw_heng
from pie import draw_pie


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_guang(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    s1_head = _tx(131, 64, ox, oy, scale)
    s1_tail = _tx(173, 89, ox, oy, scale)
    s2_head = _tx(93, 128, ox, oy, scale)
    s2_tail = _tx(234, 118, ox, oy, scale)
    s3_head = _tx(75, 125, ox, oy, scale)
    s3_tail = _tx(33, 303, ox, oy, scale)
    draw_dian(draw, s1_head, s1_tail,
              w_head=3 * scale, w_tail=7 * scale, bow=2 * scale)
    draw_heng(draw, s2_head, s2_tail,
              width_head=max(2, int(8 * scale)),
              width_tail=max(2, int(9 * scale)))
    draw_pie(draw, s3_head, s3_tail,
             bow_perp=14 * scale, w_head=8 * scale, w_tail=3 * scale)
