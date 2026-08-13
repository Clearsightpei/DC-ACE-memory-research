"""Bank primitive: 同 (tóng, 'same' — 6 strokes: 冂 + heng + 口).

Promoted from p3_char_0249_同 (G5 B8 PASS). Uses heng_zhe_gou for the
right shoulder of 冂; inline inner 口 (as shu + heng_zhe_box + heng).

Reuse targets: 同 (identity), 铜, 桐, 洞, 筒, 峒, 侗.
"""

from shu import draw_shu
from heng import draw_heng
from heng_zhe_gou import draw_heng_zhe_gou
from heng_zhe_box import draw_heng_zhe_box


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_tong_same(draw, ox=0, oy=0, scale=1.0):
    def T(x, y):
        return _tx(x, y, ox, oy, scale)

    def w(v):
        return max(2, int(v * scale))

    # s1: LEFT frame vertical shu
    draw_shu(draw, T(65.6, 80.6), T(66.5, 281.5), width=w(7))
    # s2: RIGHT frame 横折钩
    draw_heng_zhe_gou(draw,
                      heng_head=T(85.5, 86.4),
                      corner=T(215.0, 86.0),
                      gou_tail=T(210.0, 268.0),
                      hook_tip=T(183.1, 273.0))
    # s3: interior top short 一
    draw_heng(draw, T(110.4, 131.0), T(184.0, 123.0),
              width_head=w(6), width_tail=w(7))
    # s4: inner 口 left shu
    draw_shu(draw, T(105.5, 170.2), T(123.3, 228.8), width=w(5))
    # s5: inner 口 heng_zhe (top + right)
    draw_heng_zhe_box(draw, top_left=T(121.9, 177.0),
                      bottom_right=T(164.6, 218.0), width=w(5))
    # s6: inner 口 bottom heng
    draw_heng(draw, T(128.9, 218.0), T(180.2, 212.1),
              width_head=w(5), width_tail=w(6))
