"""Bank primitive: 欠 (qian, "owe" — 4 strokes: short_pie + heng_gou + long_pie + na).

Promoted from p2_radical_112_欠 (G5 B2 PASS 2026-08-08 via BANK_DEVIATION).
MEDIUM-REUSE right-side radical: appears in 次/欢/歌/欲/歇/... Uses new
heng_gou primitive (also extracted from this PASS).
"""

from PIL import ImageDraw

from pie import draw_pie
from na import draw_na
from heng_gou import draw_heng_gou


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_qian(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1 — short 撇 (top-left of the ⺈ shape)
    draw_pie(draw, head=_tx(120, 62, ox, oy, scale),
             tail=_tx(63, 185, ox, oy, scale),
             bow_perp=max(2, int(10 * scale)),
             w_head=max(2, int(4 * scale)),
             w_tail=max(1, int(2 * scale)))
    # s2 — 横钩 (short horizontal + downward hook)
    draw_heng_gou(draw,
                  head=_tx(112, 141, ox, oy, scale),
                  corner=_tx(194, 164, ox, oy, scale),
                  hook_tip=_tx(180, 198, ox, oy, scale))
    # s3 — long 撇 (main body down-left)
    draw_pie(draw, head=_tx(137, 166, ox, oy, scale),
             tail=_tx(48, 288, ox, oy, scale),
             bow_perp=max(2, int(20 * scale)),
             w_head=max(2, int(5 * scale)),
             w_tail=max(1, int(2 * scale)))
    # s4 — long 捺 (main body down-right; N joint with s3)
    draw_na(draw, head=_tx(157, 200, ox, oy, scale),
            tail=_tx(258, 292, ox, oy, scale),
            bow_perp=max(2, int(14 * scale)),
            w_head=max(1, int(2 * scale)),
            w_tail=max(3, int(8 * scale)))
