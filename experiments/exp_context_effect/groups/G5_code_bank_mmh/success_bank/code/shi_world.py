"""Bank primitive: 世 (shì, 'world' — 5 strokes: heng + 2 shus + short-heng + shu_zhe).

Promoted from p3_char_0194_世 (G5 B7 PASS, 2026-08-08). HIGH-freq char.
Sibling of 五/亚 (top-heng + middle grid + bottom wrap). Both inner shus
pierce s1 heng as P-joints.
Reuse targets: 世, 贳, 泄, 屉, 蝶 (right), 揲 (right).
"""

from PIL import ImageDraw

from heng import draw_heng
from shu import draw_shu
from shu_zhe import draw_shu_zhe


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_shi_world(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: long heng across middle
    draw_heng(draw, _tx(27.2, 179.3, ox, oy, scale), _tx(277.7, 160.8, ox, oy, scale),
              width_head=max(2, int(8 * scale)),
              width_tail=max(2, int(9 * scale)))
    # s2: left-center vertical (passes through heng)
    draw_shu(draw, _tx(135.1, 89.1, ox, oy, scale), _tx(139.5, 216.2, ox, oy, scale),
             width=max(2, int(6 * scale)))
    # s3: right-center vertical (passes through heng)
    draw_shu(draw, _tx(193.7, 78.2, ox, oy, scale), _tx(192.2, 203.9, ox, oy, scale),
             width=max(2, int(6 * scale)))
    # s4: short bottom horizontal between inner verticals' bases
    draw_heng(draw, _tx(140.6, 221.8, ox, oy, scale), _tx(208.0, 213.9, ox, oy, scale),
              width_head=max(2, int(7 * scale)),
              width_tail=max(2, int(8 * scale)))
    # s5: outer 竖折 (down then right, wraps bottom-left)
    draw_shu_zhe(draw,
                 _tx(77.1, 113.7, ox, oy, scale),
                 _tx(77.1, 264.5, ox, oy, scale),
                 _tx(245.2, 264.5, ox, oy, scale),
                 width=max(2, int(7 * scale)))
