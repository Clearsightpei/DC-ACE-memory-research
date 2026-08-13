"""Bank primitive: 问 (wèn, 'ask' — 6 strokes: 门 + 口).

Promoted from p3_char_0257_问 (G5 B8 PASS). Calls draw_men_gate for the
outer 门 frame + inlines inner 口 (3 strokes: shu + heng_zhe_box + heng).

Reuse targets: 问 (identity), 闷, 阔, 阗.
"""

from men_gate import draw_men_gate
from shu import draw_shu
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_wen_ask(draw, ox=0, oy=0, scale=1.0):
    def T(x, y):
        return _tx(x, y, ox, oy, scale)

    def w(v):
        return max(2, int(v * scale))

    # ------- Outer 门 (strokes 1-3) via bank whole-radical -------
    draw_men_gate(draw, ox=ox, oy=oy, scale=scale)

    # ------- Inner 口 (strokes 4-6) inlined per MMH pixels -------
    left_x, right_x = 108, 180
    top_y, bot_y = 160, 218

    # s4: inner left 竖
    draw_shu(draw, T(left_x, top_y + 2), T(left_x + 8, bot_y), width=w(6))
    # s5: inner 横折 (top + right)
    draw_heng_zhe_box(draw, top_left=T(left_x + 3, top_y),
                      bottom_right=T(right_x, bot_y - 3), width=w(6))
    # s6: inner bottom 横
    draw_heng(draw, T(left_x + 6, bot_y), T(right_x - 2, bot_y - 4),
              width_head=w(6), width_tail=w(7))
