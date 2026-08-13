"""Bank primitive: 行 (xíng, 'walk' — 6 strokes L-R 彳+亍).

Promoted from p3_char_0237_行 (G5 B8 PASS). All 3 joints are N (natural
gap; MMH endpoints do not force welding).

Recipe: P-A-006 stroke-primitive layer with MMH-verbatim anchors.

Reuse targets: 行 (identity), 街, 衍, 冲, 徽, 衔.
"""

from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from shu_gou import draw_shu_gou


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_xing_walk(draw, ox=0, oy=0, scale=1.0):
    def T(x, y):
        return _tx(x, y, ox, oy, scale)

    def w(v):
        return max(2, int(v * scale))

    # ---- 彳 (left radical, 3 strokes) ----
    # s1: short pie
    draw_pie(draw, T(97.9, 60.6), T(45.7, 138.0),
             bow_perp=8, w_head=w(7), w_tail=w(3))
    # s2: longer pie (main 彳 sweep)
    draw_pie(draw, T(97.0, 119.8), T(22.6, 221.2),
             bow_perp=14, w_head=w(9), w_tail=w(3))
    # s3: shu (彳 vertical)
    draw_shu(draw, T(79.1, 180.8), T(81.4, 290.0), width=w(7))

    # ---- 亍 (right radical, 3 strokes) ----
    # s4: short heng (top of 亍)
    draw_heng(draw, T(158.5, 106.9), T(236.7, 96.4),
              width_head=w(8), width_tail=w(9))
    # s5: long heng (main horizontal of 亍)
    draw_heng(draw, T(121.3, 168.5), T(284.5, 152.3),
              width_head=w(9), width_tail=w(10))
    # s6: shu-gou (vertical with slight left hook at bottom)
    draw_shu_gou(draw, T(197.2, 166.7), T(169.9, 279.5),
                 width=w(7), hook_start_offset=int(42 * scale))
