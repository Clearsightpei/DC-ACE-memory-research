"""Bank primitive: 由 (yóu, 'by/from' — 5 strokes: shu + heng_zhe_gou-like + heng + shu + heng).

Promoted from p3_char_0204_由 (G5 B7 PASS, 2026-08-08). Phonetic
radical (box + central-top shu). Sibling of 甲/申/田.
Reuse targets: 由, 抽, 油, 宙, 届, 邮, 袖, 轴, 笛.
"""

from PIL import ImageDraw

from shu import draw_shu
from heng import draw_heng
from heng_zhe_gou import draw_heng_zhe_gou


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_you_by(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: LEFT vertical of box
    draw_shu(draw, _tx(51.6, 148.5, ox, oy, scale), _tx(85.5, 281.0, ox, oy, scale),
             width=max(2, int(7 * scale)))
    # s2: heng_zhe (top + right of box) — using heng_zhe_gou without hook (hook_tip == gou_tail)
    draw_heng_zhe_gou(draw,
                      _tx(71.8, 152.1, ox, oy, scale),
                      _tx(210.6, 152.1, ox, oy, scale),
                      _tx(210.6, 289.5, ox, oy, scale),
                      _tx(210.6, 289.5, ox, oy, scale))
    # s3: middle heng
    draw_heng(draw, _tx(100.5, 208.3, ox, oy, scale), _tx(188.4, 199.8, ox, oy, scale),
              width_head=max(2, int(8 * scale)),
              width_tail=max(2, int(9 * scale)))
    # s4: central shu (top extends above box, tail inside box)
    draw_shu(draw, _tx(131.8, 63.3, ox, oy, scale), _tx(139.5, 254.6, ox, oy, scale),
             width=max(2, int(7 * scale)))
    # s5: bottom heng (closes box)
    draw_heng(draw, _tx(92.0, 271.9, ox, oy, scale), _tx(201.0, 257.8, ox, oy, scale),
              width_head=max(2, int(8 * scale)),
              width_tail=max(2, int(9 * scale)))
