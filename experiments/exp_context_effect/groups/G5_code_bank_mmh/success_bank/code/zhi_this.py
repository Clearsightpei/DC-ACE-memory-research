"""Bank primitive: 之 (zhi, 'this/of' — 3 strokes: dian + heng_pie + ping_na).

Promoted from p3_char_0039_之 (G5 B4 PASS, 2026-08-08). Note: 之 is
also the base pattern for the 走之底 (辶) component (already in bank
as `chuo_walk.py` with the 3-stroke wrap-around); this primitive is
for the standalone character.
"""

from PIL import ImageDraw

from dian import draw_dian
from heng_pie import draw_heng_pie
from ping_na import draw_ping_na


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_zhi_this(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: top dian
    draw_dian(draw,
              _tx(124, 63, ox, oy, scale), _tx(160, 91, ox, oy, scale),
              w_head=max(2, int(3 * scale)),
              w_tail=max(2, int(8 * scale)),
              bow=max(2, int(3 * scale)))
    # s2: heng_pie (short 横撇 in middle band)
    draw_heng_pie(draw,
                  _tx(65, 142, ox, oy, scale), _tx(78, 217, ox, oy, scale))
    # s3: ping_na (flat wide sweep across bottom)
    draw_ping_na(draw,
                 _tx(25, 228, ox, oy, scale), _tx(277, 274, ox, oy, scale),
                 belly_drop=max(2, int(6 * scale)))
