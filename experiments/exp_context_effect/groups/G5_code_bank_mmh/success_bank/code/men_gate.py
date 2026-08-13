"""Bank primitive: 门 (men, "gate/door" — 3 strokes: dian + shu + heng_zhe_gou).

Promoted from p2_radical_059_门__retry_2 (G5 B3 R2 PASS 2026-08-08).
High-reuse whole-glyph radical (们/闲/间/闭/闪/闷/etc.). Note the dot
sits at TOP-LEFT above the horizontal, NOT touching the frame's corner.
"""

from PIL import ImageDraw

from dian import draw_dian
from shu import draw_shu
from heng_zhe_gou import draw_heng_zhe_gou


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_men_gate(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: top-left dot (compact, does NOT touch frame corner)
    draw_dian(draw, _tx(80, 72, ox, oy, scale),
              _tx(102, 100, ox, oy, scale),
              w_head=3, w_tail=max(2, int(7 * scale)),
              bow=max(2, int(3 * scale)))
    # s2: left shu (thin frame post)
    draw_shu(draw, _tx(55, 100, ox, oy, scale),
             _tx(56, 283, ox, oy, scale),
             width=max(2, int(5 * scale)))
    # s3: right frame heng_zhe_gou
    draw_heng_zhe_gou(draw, _tx(128, 92, ox, oy, scale),
                      _tx(215, 92, ox, oy, scale),
                      _tx(202, 265, ox, oy, scale),
                      _tx(182, 252, ox, oy, scale))
