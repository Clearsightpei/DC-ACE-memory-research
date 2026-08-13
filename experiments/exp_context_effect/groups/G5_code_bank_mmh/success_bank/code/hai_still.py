"""Bank primitive: 还 (hái/huán) — 7 strokes.

Promoted from p3_char_0305_还 (G5 B9 A verdict 2026-08-09). TEXTBOOK
P-A-007 application: 不 (top-right, 4 strokes) INLINE via stroke primitives
at MMH anchors, 辶 (wrap, 3 strokes) CALLED as `draw_chuo` bank primitive.

HIGH-REUSE: 辶+X wrap pattern generalizes to 这/进/远/近/追/送/边/达/... family.
The pattern "wrap 辶 via draw_chuo + inline the enclosed radical" is the
canonical A-recipe for 辶-wrap chars where the inner has no bank primitive.
"""

from PIL import ImageDraw

from chuo_walk import draw_chuo
from heng import draw_heng
from na import draw_na
from pie import draw_pie
from shu import draw_shu


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_hai_still(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # ---- 不 (strokes 1-4) inlined at MMH anchors ----
    # s1 heng
    draw_heng(draw, _tx(121.6, 113.1, ox, oy, scale),
              _tx(246.1, 102.0, ox, oy, scale),
              width_head=max(2, int(8 * scale)),
              width_tail=max(2, int(9 * scale)))
    # s2 long pie
    draw_pie(draw, _tx(175.5, 118.4, ox, oy, scale),
             _tx(106.3, 223.5, ox, oy, scale),
             bow_perp=10, w_head=7, w_tail=2)
    # s3 shu
    draw_shu(draw, _tx(163.8, 144.7, ox, oy, scale),
             _tx(174.0, 259.6, ox, oy, scale),
             width=max(2, int(6 * scale)))
    # s4 na (short right dot)
    draw_na(draw, _tx(202.1, 173.1, ox, oy, scale),
            _tx(247.6, 212.7, ox, oy, scale),
            bow_perp=6, w_head=3, w_tail=8)
    # ---- 辶 (strokes 5-7) via bank primitive ----
    # Native chuo_walk needs +3 ox, +7 oy shift to match MMH targets here.
    draw_chuo(draw, ox=ox + 3 * scale, oy=oy + 7 * scale, scale=scale)
