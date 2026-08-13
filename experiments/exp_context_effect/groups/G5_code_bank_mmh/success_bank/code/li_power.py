"""Bank primitive: 力 (li, 'power' — 2 strokes: heng_zhe_gou + pie, P-joint).

Promoted from p2_radical_025_力 (G5 B1 PASS, 2026-08-08).
Uses the new heng_zhe_gou.py stroke primitive (also promoted from this item).
"""

from PIL import ImageDraw

from heng_zhe_gou import draw_heng_zhe_gou
from pie import draw_pie


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_li(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    heng_head = _tx(92, 108, ox, oy, scale)
    corner = _tx(192, 100, ox, oy, scale)
    gou_tail = _tx(168, 218, ox, oy, scale)
    hook_tip = _tx(150, 208, ox, oy, scale)
    pie_head = _tx(150, 88, ox, oy, scale)
    pie_tail = _tx(68, 262, ox, oy, scale)

    draw_heng_zhe_gou(draw, heng_head, corner, gou_tail, hook_tip)
    draw_pie(draw, pie_head, pie_tail,
             bow_perp=16 * scale, w_head=8 * scale, w_tail=2 * scale, steps=100)
