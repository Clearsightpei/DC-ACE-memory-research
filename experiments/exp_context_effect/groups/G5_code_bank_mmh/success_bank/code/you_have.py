"""Bank primitive: 有 (yǒu, 'have' — 6 strokes: heng + pie + pie + heng_zhe_gou + 2 hengs).

Promoted from p3_char_0221_有 (G5 B7 PASS, 2026-08-08). Composition:
top heng + long pie crossing it + 月 (inlined at 有's proper aspect).
Very high-freq char.
Reuse targets: 有, 侑, 宥, 贿, 郁, 囿, 洧.
"""

from PIL import ImageDraw

from heng import draw_heng
from pie import draw_pie
from heng_zhe_gou import draw_heng_zhe_gou


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_you_have(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: top long heng (slight upward tilt)
    draw_heng(draw, _tx(46.6, 120.1, ox, oy, scale), _tx(258.7, 105.8, ox, oy, scale),
              width_head=max(2, int(8 * scale)),
              width_tail=max(2, int(9 * scale)))
    # s2: long pie (starts above s1, crosses through, sweeps down-left)
    draw_pie(draw, _tx(137.7, 53.3, ox, oy, scale), _tx(24.3, 243.5, ox, oy, scale),
             bow_perp=int(14 * scale) or 1,
             w_head=max(2, int(8 * scale)),
             w_tail=max(2, int(3 * scale)))
    # s3: 月's left curved pie (short, mild bow)
    draw_pie(draw, _tx(120.7, 158.8, ox, oy, scale), _tx(107.5, 295.3, ox, oy, scale),
             bow_perp=int(6 * scale) or 1,
             w_head=max(2, int(6 * scale)),
             w_tail=max(2, int(4 * scale)))
    # s4: 月's right frame (heng_zhe_gou)
    draw_heng_zhe_gou(draw,
                      _tx(127.7, 158.2, ox, oy, scale),
                      _tx(161.0, 158.0, ox, oy, scale),
                      _tx(161.1, 285.9, ox, oy, scale),
                      _tx(148.5, 279.0, ox, oy, scale))
    # s5: upper inner heng
    draw_heng(draw, _tx(128.6, 203.3, ox, oy, scale), _tx(174.3, 195.4, ox, oy, scale),
              width_head=max(2, int(6 * scale)),
              width_tail=max(2, int(7 * scale)))
    # s6: lower inner heng
    draw_heng(draw, _tx(126.0, 240.2, ox, oy, scale), _tx(175.2, 233.8, ox, oy, scale),
              width_head=max(2, int(6 * scale)),
              width_tail=max(2, int(7 * scale)))
