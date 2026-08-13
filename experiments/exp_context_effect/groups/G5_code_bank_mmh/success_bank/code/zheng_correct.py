"""Bank primitive: 正 (zheng, "correct/upright" — 5 strokes:
top heng + 止 below).

Promoted from p3_char_0182_正 (G5 B6 PASS, 2026-08-08). Composition = top
long heng + 止 (four sub-strokes inlined, y-shifted down to make room for
top heng).

Reuse targets: 证 (讠+正), 政 (正+攵), 征 (彳+正), 症 (疒+正).

Signature: (draw, ox=0, oy=0, scale=1.0).
"""

from PIL import ImageDraw

from heng import draw_heng
from shu import draw_shu


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_zheng(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: top heng (crown)
    draw_heng(draw,
              _tx(55, 84, ox, oy, scale), _tx(232, 76, ox, oy, scale),
              width_head=max(2, int(8 * scale)),
              width_tail=max(2, int(10 * scale)))
    # s2: upper shu (drops from just under s1)
    draw_shu(draw,
             _tx(145, 108, ox, oy, scale), _tx(150, 250, ox, oy, scale),
             width=max(2, int(7 * scale)))
    # s3: middle short heng (right of s2)
    draw_heng(draw,
              _tx(160, 172, ox, oy, scale), _tx(236, 164, ox, oy, scale),
              width_head=max(2, int(7 * scale)),
              width_tail=max(2, int(8 * scale)))
    # s4: left short shu (baseline drop)
    draw_shu(draw,
             _tx(78, 172, ox, oy, scale), _tx(102, 253, ox, oy, scale),
             width=max(2, int(7 * scale)))
    # s5: long baseline heng
    draw_heng(draw,
              _tx(30, 270, ox, oy, scale), _tx(272, 262, ox, oy, scale),
              width_head=max(2, int(9 * scale)),
              width_tail=max(2, int(11 * scale)))
