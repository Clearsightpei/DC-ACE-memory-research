"""Bank primitive: 法 (fǎ, "law") — 8 strokes = 氵 (left) + 去 (right).

Promoted from p3_char_0377_法 (G5 B10 PASS 2026-08-09). VERY HIGH REUSE.
氵 = 2 dians + ti (left-position water radical). 去 = heng + shu + heng
+ 2 dians (下-like base). This is a canonical 氵+X template — reuse
for 河/海/江/清/游/汉/洗/汽/波/漂 family. Note 氵 here inlined (not
draw_sanshui wrapper) so per-endpoint anchors match MMH.
"""

from PIL import ImageDraw

from dian import draw_dian
from heng import draw_heng
from shu import draw_shu
from ti import draw_ti


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_fa_law(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # --- 氵 (left) ---
    draw_dian(draw, _tx(72.1, 84.7, ox, oy, scale),
              _tx(105.8, 113.7, ox, oy, scale),
              w_head=3, w_tail=9, bow=4)
    draw_dian(draw, _tx(44.8, 137.7, ox, oy, scale),
              _tx(71.2, 162.0, ox, oy, scale),
              w_head=3, w_tail=8, bow=3)
    draw_ti(draw, _tx(56.5, 281.2, ox, oy, scale),
            _tx(96.1, 178.4, ox, oy, scale),
            w_head=10, w_tail=2)
    # --- 去 (right) ---
    draw_heng(draw, _tx(128.0, 135.6, ox, oy, scale),
              _tx(230.9, 120.4, ox, oy, scale),
              width_head=8, width_tail=9)
    draw_shu(draw, _tx(162.3, 64.5, ox, oy, scale),
             _tx(168.8, 181.3, ox, oy, scale),
             width=max(2, int(7 * scale)))
    draw_heng(draw, _tx(101.4, 198.0, ox, oy, scale),
              _tx(266.3, 180.8, ox, oy, scale),
              width_head=9, width_tail=10)
    # closing 厶 = 2 dians
    draw_dian(draw, _tx(174.0, 210.0, ox, oy, scale),
              _tx(150.0, 270.0, ox, oy, scale),
              w_head=3, w_tail=7, bow=-2)
    draw_dian(draw, _tx(178.0, 232.0, ox, oy, scale),
              _tx(220.0, 285.0, ox, oy, scale),
              w_head=3, w_tail=7, bow=3)
