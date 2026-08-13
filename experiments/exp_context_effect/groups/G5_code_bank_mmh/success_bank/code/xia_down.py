"""Bank primitive: 下 (xia, 'down' — 3 strokes: heng + shu + dian).

Promoted from p3_char_0053_下 (G5 B4 PASS, 2026-08-08). Sibling of 上 / 卜.
"""

from PIL import ImageDraw

from heng import draw_heng
from shu import draw_shu
from dian import draw_dian


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_xia(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: heng — ML(0.331,0.002) → TR(0.707,0.92) : (33,100) → (271,92)
    draw_heng(draw,
              _tx(33, 100, ox, oy, scale), _tx(271, 92, ox, oy, scale),
              width_head=max(2, int(9 * scale)),
              width_tail=max(2, int(10 * scale)))
    # s2: shu — C(0.427,0.005) → BC(0.494,1.006) : (143,101) → (149,295)
    draw_shu(draw,
             _tx(143, 101, ox, oy, scale), _tx(149, 295, ox, oy, scale),
             width=max(2, int(8 * scale)))
    # s3: dian — C(0.626,0.479) → MR(0.191,0.896) : (163,148) → (219,190)
    draw_dian(draw,
              _tx(163, 148, ox, oy, scale), _tx(219, 190, ox, oy, scale),
              w_head=max(2, int(3 * scale)),
              w_tail=max(2, int(7 * scale)),
              bow=max(2, int(4 * scale)))
