"""Bank primitive: 巾 (jin, "towel" — 3 strokes: shu + heng_zhe_gou + shu).

Promoted from p2_radical_056_巾__retry_1 (G5 B2 PASS 2026-08-08 —
R1 recovery after B1 C). MEDIUM-REUSE: appears in 布/带/帽/帮/常/帅/...
Uses heng_zhe_gou primitive (from B1) for a continuous 横折钩 top-right.
"""

from PIL import ImageDraw

from shu import draw_shu
from heng_zhe_gou import draw_heng_zhe_gou


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_jin(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1 left short 竖
    draw_shu(draw, _tx(72.4, 135.6, ox, oy, scale),
             _tx(78.8, 235.3, ox, oy, scale),
             width=max(2, int(8 * scale)))
    # s2 横折钩 (continuous: heng head → corner → gou tail → hook tip)
    s2_head = _tx(89.9, 138.9, ox, oy, scale)
    s2_corner = _tx(180.5, 138.9, ox, oy, scale)
    s2_gou_tail = _tx(180.5, 209.5, ox, oy, scale)
    s2_hook_tip = _tx(170.5, 203.5, ox, oy, scale)
    draw_heng_zhe_gou(draw, s2_head, s2_corner, s2_gou_tail, s2_hook_tip)
    # s3 middle tall 竖 (piercing, extends past baseline)
    draw_shu(draw, _tx(133.6, 64.7, ox, oy, scale),
             _tx(147.4, 292.0, ox, oy, scale),
             width=max(2, int(9 * scale)))
