"""Bank primitive: 生 (sheng, "born/life" — 5 strokes:
pie + heng + heng + shu + heng).

Promoted from p3_char_0162_生 (G5 B6 PASS, 2026-08-08). Sibling of 龶
(p3_char_0129) with an extra top pie. Shu pierces s2 & s3 (P/P), ends
above s5 (N gap ~20px).

Reuse targets: 性 (忄+生), 星 (日+生), 姓 (女+生), 胜 (月+生),
牲 (牛+生), 甥 (生+男-derivative).

Signature: (draw, ox=0, oy=0, scale=1.0).
"""

from PIL import ImageDraw

from heng import draw_heng
from shu import draw_shu
from pie import draw_pie


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_sheng(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: top pie (extended head y=82 per P-MMH-002; medial vs visible ink)
    draw_pie(draw,
             _tx(95.0, 82.0, ox, oy, scale),
             _tx(58.0, 178.0, ox, oy, scale),
             bow_perp=10, w_head=max(2, int(8 * scale)),
             w_tail=max(2, int(2 * scale)), steps=70)
    # s2: middle heng
    draw_heng(draw,
              _tx(93.8, 161.1, ox, oy, scale),
              _tx(219.7, 144.4, ox, oy, scale),
              width_head=max(2, int(7 * scale)),
              width_tail=max(2, int(8 * scale)))
    # s3: lower short heng
    draw_heng(draw,
              _tx(99.0, 216.5, ox, oy, scale),
              _tx(206.0, 204.8, ox, oy, scale),
              width_head=max(2, int(7 * scale)),
              width_tail=max(2, int(8 * scale)))
    # s4: tall central shu (stops above s5 for N-gap)
    draw_shu(draw,
             _tx(142.4, 59.8, ox, oy, scale),
             _tx(145.9, 262.0, ox, oy, scale),
             width=max(2, int(7 * scale)), top_curl=False)
    # s5: long bottom heng
    draw_heng(draw,
              _tx(41.3, 288.6, ox, oy, scale),
              _tx(270.4, 279.5, ox, oy, scale),
              width_head=max(2, int(9 * scale)),
              width_tail=max(2, int(11 * scale)))
