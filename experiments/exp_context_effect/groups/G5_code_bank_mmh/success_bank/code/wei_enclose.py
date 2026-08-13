"""Bank primitive: 囗 (wei, enclosure radical — 3 strokes: shu + heng_zhe_box + heng).

Promoted from p2_radical_073_囗 (G5 B2 PASS 2026-08-08). Encloses
whole characters (国/回/图/固/围/四/因/园/圆). Same 3-stroke skeleton
as 口 (kou) but scaled to fill the whole canvas; keep the position
signature so callers can specify a smaller enclosure via `scale`.
"""

from PIL import ImageDraw

from shu import draw_shu
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_wei(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1 left 竖
    draw_shu(draw, _tx(64.5, 79.4, ox, oy, scale),
             _tx(68.0, 286.8, ox, oy, scale),
             width=max(2, int(8 * scale)))
    # s2 横折 box: top_left → bottom_right
    draw_heng_zhe_box(draw, _tx(80.3, 83.2, ox, oy, scale),
                      _tx(229.7, 296.2, ox, oy, scale),
                      width=max(2, int(8 * scale)))
    # s3 bottom 横
    draw_heng(draw, _tx(76.8, 278.0, ox, oy, scale),
              _tx(214.7, 264.8, ox, oy, scale),
              width_head=max(2, int(8 * scale)),
              width_tail=max(2, int(9 * scale)))
