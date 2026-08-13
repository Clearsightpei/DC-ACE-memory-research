"""Bank primitive: 文 (wen, "text/writing" — 4 strokes: dian+heng+pie+na).

Promoted from p2_radical_124_文 (G5 B3 PASS 2026-08-08).
Medium-reuse whole-glyph radical (文/纹/蚊/这-related-family).
Position signature; reference canvas 300x300.
"""

from PIL import ImageDraw

from dian import draw_dian
from heng import draw_heng
from pie import draw_pie
from na import draw_na


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_wen(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1 top dian
    draw_dian(draw, _tx(114.3, 57.4, ox, oy, scale),
              _tx(150.6, 85.5, ox, oy, scale),
              w_head=3, w_tail=max(2, int(7 * scale)),
              bow=max(2, int(4 * scale)))
    # s2 heng (spans middle)
    draw_heng(draw, _tx(54.8, 138.9, ox, oy, scale),
              _tx(223.8, 118.9, ox, oy, scale),
              width_head=max(2, int(8 * scale)),
              width_tail=max(2, int(9 * scale)))
    # s3 pie
    draw_pie(draw, _tx(147.1, 136.2, ox, oy, scale),
             _tx(36.9, 274.8, ox, oy, scale),
             bow_perp=int(10 * scale),
             w_head=max(2, int(8 * scale)),
             w_tail=max(2, int(3 * scale)))
    # s4 na (crosses s3 at P-joint)
    draw_na(draw, _tx(79.4, 174.3, ox, oy, scale),
            _tx(282.4, 285.6, ox, oy, scale),
            bow_perp=int(12 * scale),
            w_head=max(2, int(4 * scale)),
            w_tail=max(2, int(11 * scale)))
