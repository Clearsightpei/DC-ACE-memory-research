"""Bank primitive: 户 (hu, "door/household" — 4 strokes: dian + heng_zhe_short + heng + pie).

Promoted from p2_radical_097_户 (G5 B2 PASS 2026-08-08). MEDIUM-REUSE:
appears in 房/所/扇/雇/... The top dot (dian) is what distinguishes 户 from
尸 (which has no top dot).
"""

from PIL import ImageDraw

from dian import draw_dian
from heng import draw_heng
from heng_zhe_short import draw_heng_zhe_short
from pie import draw_pie


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_hu(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: 点 — top short slanted dot
    draw_dian(draw, _tx(137, 56, ox, oy, scale),
              _tx(175, 84, ox, oy, scale),
              w_head=max(2, int(3 * scale)),
              w_tail=max(3, int(8 * scale)),
              bow=max(2, int(3 * scale)))
    # s2: 横折 — mid-canvas heng that turns down
    draw_heng_zhe_short(draw, _tx(115, 130, ox, oy, scale),
                        _tx(191, 165, ox, oy, scale),
                        corner_offset=(max(2, int(4 * scale)),
                                       max(1, int(2 * scale))))
    # s3: 横 — middle horizontal
    draw_heng(draw, _tx(109, 192, ox, oy, scale),
              _tx(214, 176, ox, oy, scale),
              width_head=max(2, int(8 * scale)),
              width_tail=max(2, int(9 * scale)))
    # s4: 撇 — long left-sweep (belly right, big bow)
    draw_pie(draw, _tx(90, 124, ox, oy, scale),
             _tx(28, 288, ox, oy, scale),
             bow_perp=-max(4, int(38 * scale)),
             w_head=max(2, int(10 * scale)),
             w_tail=max(1, int(2 * scale)))
