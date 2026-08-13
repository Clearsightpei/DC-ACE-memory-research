"""Bank primitive: 主 (zhu, "lord/main" — 5 strokes: dian + 3 hengs + shu).

Promoted from p3_char_0174_主 (G5 B6 PASS, 2026-08-08). Composition = top dian
+ 王-like triple-heng + central shu. Drawer skipped draw_wang_king (BANK_DEVIATION)
because 王 must sit lower inside 主 to leave headroom for the top dian.

Reuse targets: 住 (亻+主), 注 (氵+主), 柱 (木+主), 驻 (马+主), 蛀 (虫+主).

Signature: (draw, ox=0, oy=0, scale=1.0).
"""

from PIL import ImageDraw

from heng import draw_heng
from shu import draw_shu
from dian import draw_dian


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_zhu(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: top dian
    draw_dian(draw,
              _tx(131.0, 61.2, ox, oy, scale),
              _tx(167.9, 92.0, ox, oy, scale),
              w_head=max(2, int(3 * scale)),
              w_tail=max(2, int(7 * scale)), bow=3)
    # s2: top short heng of 王 (lowered vs standalone 王)
    draw_heng(draw,
              _tx(81.7, 141.2, ox, oy, scale),
              _tx(220.0, 124.2, ox, oy, scale),
              width_head=max(2, int(7 * scale)),
              width_tail=max(2, int(8 * scale)))
    # s3: middle short heng of 王
    draw_heng(draw,
              _tx(88.8, 210.1, ox, oy, scale),
              _tx(203.9, 196.3, ox, oy, scale),
              width_head=max(2, int(7 * scale)),
              width_tail=max(2, int(8 * scale)))
    # s4: central shu shaft
    draw_shu(draw,
             _tx(141.2, 145.3, ox, oy, scale),
             _tx(144.1, 265.7, ox, oy, scale),
             width=max(2, int(7 * scale)), top_curl=False)
    # s5: long bottom heng
    draw_heng(draw,
              _tx(34.6, 280.1, ox, oy, scale),
              _tx(278.9, 275.7, ox, oy, scale),
              width_head=max(2, int(9 * scale)),
              width_tail=max(2, int(11 * scale)))
