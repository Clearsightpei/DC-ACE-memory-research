"""Bank primitive: 无 (wu, "none" — 4 strokes: heng + heng + pie + shu_wan_gou).

Promoted from p2_radical_135_无 (G5 B3 PASS 2026-08-08). High-reuse
whole-glyph radical (无/旡/既-family). Sibling: 旡 (also has 4 strokes,
still C-verdict — see errata).
"""

from PIL import ImageDraw

from heng import draw_heng
from pie import draw_pie
from shu_wan_gou import draw_shu_wan_gou


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_wu_none(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1 top heng (shorter)
    draw_heng(draw, _tx(88, 101, ox, oy, scale),
              _tx(211, 88, ox, oy, scale),
              width_head=max(2, int(8 * scale)),
              width_tail=max(2, int(9 * scale)))
    # s2 middle heng (longer)
    draw_heng(draw, _tx(47, 182, ox, oy, scale),
              _tx(242, 168, ox, oy, scale),
              width_head=max(2, int(9 * scale)),
              width_tail=max(2, int(10 * scale)))
    # s3 pie (down-left)
    draw_pie(draw, _tx(130, 109, ox, oy, scale),
             _tx(41, 294, ox, oy, scale),
             bow_perp=int(14 * scale),
             w_head=max(2, int(8 * scale)),
             w_tail=max(2, int(2 * scale)))
    # s4 shu_wan_gou (right leg, curls right + up-hook)
    draw_shu_wan_gou(draw, _tx(146, 187, ox, oy, scale),
                     _tx(260, 238, ox, oy, scale),
                     width=max(2, int(7 * scale)),
                     bottom_extra=int(55 * scale),
                     knee_ratio=0.75)
