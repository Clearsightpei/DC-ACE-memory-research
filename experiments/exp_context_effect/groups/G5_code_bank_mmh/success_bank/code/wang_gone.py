"""Bank primitive: 亡 (wang, 'gone/perish' — 3 strokes: dian + heng + shu_zhe).

Promoted from p3_char_0052_亡 (G5 B4 PASS, 2026-08-08). Component of
忘/忙/氓/慌/望/妄/盲 — HIGH reuse. Composition: top dot, mid heng,
bottom L-shape (竖折) forming the bottom-left cradle.
"""

from PIL import ImageDraw

from dian import draw_dian
from heng import draw_heng
from shu_zhe import draw_shu_zhe


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_wang_gone(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: dian at top-center
    draw_dian(draw,
              _tx(131, 69, ox, oy, scale), _tx(173, 104, ox, oy, scale),
              w_head=max(2, int(3 * scale)),
              w_tail=max(2, int(8 * scale)),
              bow=max(2, int(3 * scale)))
    # s2: middle heng — wide, spans canvas
    draw_heng(draw,
              _tx(37, 165, ox, oy, scale), _tx(269, 149, ox, oy, scale),
              width_head=max(2, int(9 * scale)),
              width_tail=max(2, int(11 * scale)))
    # s3: shu_zhe (down-then-right L)
    s3_head = _tx(97, 168, ox, oy, scale)
    s3_tail = _tx(239, 251, ox, oy, scale)
    s3_corner = (s3_head[0], s3_tail[1])
    draw_shu_zhe(draw, s3_head, s3_corner, s3_tail,
                 width=max(2, int(8 * scale)))
