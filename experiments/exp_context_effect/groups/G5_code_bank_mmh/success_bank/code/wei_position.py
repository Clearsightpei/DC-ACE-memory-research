"""Bank primitive: 位 (wèi, "position") — 7 strokes.

Promoted from p3_char_0313_位 (G5 B9 A verdict 2026-08-09). TEXTBOOK
P-A-007 clause-2 fallback: considered whole-radical draw_li_stand but
立 in 位 is aspect-skewed (~0.75× width / ~0.98× height) vs standalone
li_stand — uniform scale would render 立 too short. Fell back to P-A-006
stroke-primitive layer with MMH anchors verbatim.

HIGH-REUSE: 亻+X 7-stroke L-R template where X = 立-family (立/竝/竟/章).
Recipe replicable: for 亻 use draw_pie + draw_shu at MMH endpoints; for
right-side straight-stroke radical use stroke-primitive layer at MMH.
"""

from PIL import ImageDraw

from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from dian import draw_dian


def _tapered_line(draw, head, tail, w_head, w_tail, steps=44):
    for i in range(steps):
        t = i / (steps - 1)
        x = head[0] + t * (tail[0] - head[0])
        y = head[1] + t * (tail[1] - head[1])
        w = w_head + (w_tail - w_head) * t
        draw.ellipse((x - w / 2, y - w / 2, x + w / 2, y + w / 2), fill=(0, 0, 0))


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_wei_position(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # --- 亻 (2 strokes) ---
    draw_pie(draw, _tx(86.7, 69.7, ox, oy, scale),
             _tx(18.8, 203.9, ox, oy, scale),
             bow_perp=15, w_head=9, w_tail=3, steps=80)
    draw_shu(draw, _tx(71.5, 150.9, ox, oy, scale),
             _tx(76.8, 285.9, ox, oy, scale),
             width=max(2, int(7 * scale)))
    # --- 立 (5 strokes) inline ---
    draw_dian(draw, _tx(157.6, 67.1, ox, oy, scale),
              _tx(193.4, 94.9, ox, oy, scale),
              w_head=3, w_tail=8, bow=4, steps=48)
    draw_heng(draw, _tx(125.1, 143.6, ox, oy, scale),
              _tx(242.3, 126.6, ox, oy, scale),
              width_head=max(2, int(8 * scale)),
              width_tail=max(2, int(9 * scale)))
    _tapered_line(draw, _tx(133.3, 181.3, ox, oy, scale),
                  _tx(153.5, 218.3, ox, oy, scale),
                  w_head=4, w_tail=9, steps=44)
    _tapered_line(draw, _tx(205.4, 161.7, ox, oy, scale),
                  _tx(179.6, 247.9, ox, oy, scale),
                  w_head=4, w_tail=10, steps=60)
    draw_heng(draw, _tx(98.4, 262.2, ox, oy, scale),
              _tx(276.3, 254.3, ox, oy, scale),
              width_head=max(2, int(10 * scale)),
              width_tail=max(2, int(11 * scale)))
