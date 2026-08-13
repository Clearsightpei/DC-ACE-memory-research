"""Bank primitive: 反 (fan, "reverse" — 4 strokes: pie + pie + heng_pie + na).

Promoted from p3_char_0140_反 (G5 B6 PASS, 2026-08-08). Composition = 厂
(top-left) + 又 (bottom-right) sharing a corner but drawn with all 4
strokes inline (no whole-又 primitive since interior joints must weld).

Reuse targets: 板 (木+反), 饭 (饣+反), 返 (辶+反), 贩 (贝+反),
版 (片+反), 叛 (半+反).

Signature: (draw, ox=0, oy=0, scale=1.0). Baked from MMH anchors on 300×300.
"""

from PIL import ImageDraw

from pie import draw_pie
from na import draw_na
from heng_pie import draw_heng_pie


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_fan(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: short top pie (leftward tick)
    draw_pie(draw,
             _tx(215.0, 81.2, ox, oy, scale),
             _tx(111.0, 100.2, ox, oy, scale),
             bow_perp=6, w_head=max(2, int(7 * scale)),
             w_tail=max(2, int(4 * scale)), steps=60)
    # s2: long main left-descender pie
    draw_pie(draw,
             _tx(85.8, 96.1, ox, oy, scale),
             _tx(25.2, 287.7, ox, oy, scale),
             bow_perp=14, w_head=max(2, int(10 * scale)),
             w_tail=max(2, int(3 * scale)), steps=100)
    # s3: heng_pie interior (heng across then bends down-left)
    draw_heng_pie(draw,
                  _tx(104.9, 169.0, ox, oy, scale),
                  _tx(76.5, 281.0, ox, oy, scale),
                  apex_x=170.0 * scale + ox,
                  corner_x=175.0 * scale + ox)
    # s4: interior na sweeping right — P-joint welds with s3 near BC
    draw_na(draw,
            _tx(108.7, 192.5, ox, oy, scale),
            _tx(268.4, 288.3, ox, oy, scale),
            bow_perp=14, w_head=max(2, int(4 * scale)),
            w_tail=max(2, int(11 * scale)), steps=80)
