"""Bank primitive: 饣 (shi, "food-side" simplified radical — 3 strokes: pie + short_heng_gou + shu_ti).

Promoted from p2_radical_066_饣__retry_1 (G5 B2 PASS 2026-08-08 — R1
recovery after B1 C). HIGH-REUSE left-position radical: appears in
饭/饮/饱/饺/馆/饼/饿/... The 竖提 (s3) is built as shu + ti in sequence.
"""

from PIL import ImageDraw

from pie import draw_pie
from shu import draw_shu
from ti import draw_ti


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def _draw_heng_gou_short(draw, head, corner, hook_tip, width=6):
    """Inline mini-heng-gou for 饣 s2 (short horizontal, sharp corner, small down-left tick).

    Kept as-is from the retry_1 PASS render — 饣's top hook is shorter
    than the generic heng_gou primitive.
    """
    draw.line([head, corner], fill='black', width=width)
    draw.line([corner, hook_tip], fill='black', width=width)
    r = width // 2
    for pt in (head, corner, hook_tip):
        draw.ellipse((pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r), fill='black')


def draw_shi_food(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1 撇 (from top down-left)
    draw_pie(draw, head=_tx(145, 67, ox, oy, scale),
             tail=_tx(78, 205, ox, oy, scale),
             bow_perp=max(2, int(14 * scale)),
             w_head=max(2, int(9 * scale)),
             w_tail=max(1, int(3 * scale)))
    # s2 short horizontal → sharp corner → small down-left tick
    heng_head = _tx(146, 130, ox, oy, scale)
    heng_corner = _tx(196, 130, ox, oy, scale)
    heng_hook_tip = _tx(184, 148, ox, oy, scale)
    _draw_heng_gou_short(draw, heng_head, heng_corner, heng_hook_tip,
                         width=max(2, int(6 * scale)))
    # s3a — shu (vertical descent)
    shu_head = _tx(146, 170, ox, oy, scale)
    shu_corner = _tx(146, 208, ox, oy, scale)
    draw_shu(draw, head=shu_head, tail=shu_corner,
             width=max(2, int(6 * scale)))
    # s3b — ti (rising tail)
    ti_tail = _tx(210, 215, ox, oy, scale)
    draw_ti(draw, head=shu_corner, tail=ti_tail,
            w_head=max(2, int(8 * scale)),
            w_tail=max(1, int(2 * scale)))
