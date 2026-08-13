"""Bank primitive: 三 (san, 'three' — 3 hengs stacked).

Promoted from p3_char_0055_三 (G5 B4 PASS, 2026-08-08). Bottom heng
longest, top heng medium, middle heng shortest and tucked between.
"""

from PIL import ImageDraw

from heng import draw_heng


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_san(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    draw_heng(draw,
              _tx(93, 108, ox, oy, scale), _tx(212, 97, ox, oy, scale),
              width_head=max(2, int(8 * scale)),
              width_tail=max(2, int(9 * scale)))
    draw_heng(draw,
              _tx(97, 181, ox, oy, scale), _tx(205, 173, ox, oy, scale),
              width_head=max(2, int(8 * scale)),
              width_tail=max(2, int(9 * scale)))
    draw_heng(draw,
              _tx(37, 256, ox, oy, scale), _tx(280, 249, ox, oy, scale),
              width_head=max(2, int(10 * scale)),
              width_tail=max(2, int(11 * scale)))
