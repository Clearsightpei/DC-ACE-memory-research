"""Bank primitive: 合 (hé, 'together' — 6 strokes: 人-top + heng + 口).

Promoted from p3_char_0269_合 (G5 B8 PASS). 人-top spans nearly full canvas
width; middle heng just below; 口 bottom centered.

Reuse targets: 合 (identity), 拾, 给, 塔, 蛤, 鸽, 恰, 洽.
"""

from pie import draw_pie
from na import draw_na
from heng import draw_heng
from shu import draw_shu
from heng_zhe_box import draw_heng_zhe_box


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_he_together(draw, ox=0, oy=0, scale=1.0):
    def T(x, y):
        return _tx(x, y, ox, oy, scale)

    def w(v):
        return max(2, int(v * scale))

    # ---- 人 top ----
    # s1: pie
    draw_pie(draw, T(135.6, 66.2), T(22.3, 211.5),
             bow_perp=17, w_head=w(11), w_tail=w(3))
    # s2: na
    draw_na(draw, T(153.8, 95.8), T(290.9, 181.6),
            bow_perp=14, w_head=w(4), w_tail=w(12))

    # ---- 一 (middle heng) ----
    # s3
    draw_heng(draw, T(99.0, 180.2), T(182.8, 172.3),
              width_head=w(7), width_tail=w(8))

    # ---- 口 bottom ----
    # s4: left shu
    draw_shu(draw, T(79.1, 222.1), T(105.5, 299.0), width=w(8))
    # s5: 横折 (top + right)
    draw_heng_zhe_box(draw, T(97.3, 222.7), T(177.5, 264.6), width=w(8))
    # s6: bottom heng
    draw_heng(draw, T(110.2, 278.3), T(198.6, 276.3),
              width_head=w(8), width_tail=w(9))
