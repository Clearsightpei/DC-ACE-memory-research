"""Bank primitive: 口 (kou, 'mouth' — 3 strokes: shu + heng_zhe_box + heng).

Promoted from p2_radical_057_口 (G5 B1 PASS, 2026-08-08). VERY HIGH-REUSE:
appears in almost every 4th character (吃/吗/呢/听/名/号/员/...).

Uses the new heng_zhe_box.py stroke primitive.
"""

from PIL import ImageDraw

from shu import draw_shu
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_kou(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # left 竖
    s1_head = _tx(100, 128, ox, oy, scale)
    s1_tail = _tx(92, 272, ox, oy, scale)
    draw_shu(draw, s1_head, s1_tail, width=max(2, int(8 * scale)))

    # 横折 box: top_left -> bottom_right
    top_left = _tx(115, 122, ox, oy, scale)
    bottom_right = _tx(225, 258, ox, oy, scale)
    draw_heng_zhe_box(draw, top_left, bottom_right, width=max(2, int(8 * scale)))

    # bottom 横
    s3_head = _tx(105, 275, ox, oy, scale)
    s3_tail = _tx(220, 268, ox, oy, scale)
    draw_heng(draw, s3_head, s3_tail,
              width_head=max(2, int(8 * scale)),
              width_tail=max(2, int(9 * scale)))
