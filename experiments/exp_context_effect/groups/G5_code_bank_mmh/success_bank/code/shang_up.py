"""Bank primitive: 上 (shang, 'up' — 3 strokes: shu + short-heng + long-heng).

Promoted from p3_char_0045_上 (G5 B4 PASS, 2026-08-08). MMH-anchored,
uses stroke bank. Sibling of 下 / 卜; distinguisher = short-heng points
UP-RIGHT from mid, long-heng sits at base.
"""

from PIL import ImageDraw

from shu import draw_shu
from heng import draw_heng


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_shang(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: shu (long vertical) — TC(0.307,0.712) → BC(0.383,0.602) : (131,71) → (138,260)
    draw_shu(draw,
             _tx(131, 71, ox, oy, scale), _tx(138, 260, ox, oy, scale),
             width=max(2, int(8 * scale)), top_curl=False)
    # s2: short heng — C(0.556,0.688) → MR(0.25,0.547) : (156,169) → (225,155)
    draw_heng(draw,
              _tx(156, 169, ox, oy, scale), _tx(225, 155, ox, oy, scale),
              width_head=max(2, int(8 * scale)),
              width_tail=max(2, int(9 * scale)))
    # s3: long base heng — BL(0.393,0.73) → BR(0.73,0.71) : (39,273) → (273,271)
    draw_heng(draw,
              _tx(39, 273, ox, oy, scale), _tx(273, 271, ox, oy, scale),
              width_head=max(2, int(9 * scale)),
              width_tail=max(2, int(11 * scale)))
