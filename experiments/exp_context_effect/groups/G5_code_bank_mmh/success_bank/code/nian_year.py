"""Bank primitive: 年 (nián, 'year' — 6 strokes: pie + 2 hengs + shu + heng + shu).

Promoted from p3_char_0227_年 (G5 B7 PASS, 2026-08-08). Very high-freq.
s6 (central shu) pierces s3 (mid heng) and s5 (bottom heng) as P-joints
via draw-order overdraw. Note: MMH tail y=322 clipped to y=295 for canvas.
Reuse targets: 年 (usually standalone; also as phonetic in 秊/鲇/鲶 rare).
"""

from PIL import ImageDraw

from heng import draw_heng
from pie import draw_pie
from shu import draw_shu


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_nian_year(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: top-left pie
    draw_pie(draw, _tx(109.9, 52.4, ox, oy, scale), _tx(63.3, 133.9, ox, oy, scale),
             bow_perp=int(8 * scale) or 1,
             w_head=max(2, int(8 * scale)),
             w_tail=max(2, int(3 * scale)), steps=70)
    # s2: short top heng (slight upward slant)
    draw_heng(draw, _tx(112.8, 97.0, ox, oy, scale), _tx(215.3, 85.3, ox, oy, scale),
              width_head=max(2, int(7 * scale)),
              width_tail=max(2, int(9 * scale)))
    # s3: short mid heng
    draw_heng(draw, _tx(101.1, 150.6, ox, oy, scale), _tx(214.7, 143.6, ox, oy, scale),
              width_head=max(2, int(7 * scale)),
              width_tail=max(2, int(9 * scale)))
    # s4: short mid shu (slight rightward lean)
    draw_shu(draw, _tx(84.1, 148.2, ox, oy, scale), _tx(105.8, 202.7, ox, oy, scale),
             width=max(2, int(6 * scale)))
    # s5: long bottom heng
    draw_heng(draw, _tx(24.3, 214.2, ox, oy, scale), _tx(272.2, 206.8, ox, oy, scale),
              width_head=max(2, int(9 * scale)),
              width_tail=max(2, int(11 * scale)))
    # s6: central shu piercing s3 + s5 (welded P-joints via draw order)
    draw_shu(draw, _tx(143.6, 104.3, ox, oy, scale), _tx(155.6, 295.0, ox, oy, scale),
             width=max(2, int(7 * scale)))
