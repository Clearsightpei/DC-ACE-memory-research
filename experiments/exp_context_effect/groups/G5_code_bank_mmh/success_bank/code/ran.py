"""Bank primitive: 冉 (rǎn — 5 strokes: shu + heng_zhe_gou + heng + shu + wide heng).

Promoted from p3_char_0201_冉 (G5 B7 **A** verdict, 2026-08-08).
Recipe: P-A-006 — MMH anchors verbatim + stroke primitives. The
defining feature is s5 (wide horizontal) extending beyond the frame
both sides, piercing s1 and s2 (P-joints via overdraw order).
Reuse targets: 冉, 苒, 再 (frame-with-wide-piercing-bar family).
"""

from PIL import ImageDraw

from shu import draw_shu
from heng import draw_heng
from heng_zhe_gou import draw_heng_zhe_gou


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_ran(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: LEFT vertical of frame
    draw_shu(draw, _tx(79, 120, ox, oy, scale), _tx(82, 289, ox, oy, scale),
             width=max(2, int(7 * scale)))
    # s2: TOP heng + RIGHT vertical + hook (heng_zhe_gou)
    draw_heng_zhe_gou(draw,
                      _tx(97, 125, ox, oy, scale),
                      _tx(215, 122, ox, oy, scale),
                      _tx(215, 262, ox, oy, scale),
                      _tx(165, 279, ox, oy, scale))
    # s3: INNER short middle horizontal
    draw_heng(draw, _tx(115, 169, ox, oy, scale), _tx(179, 160, ox, oy, scale),
              width_head=max(2, int(6 * scale)),
              width_tail=max(2, int(7 * scale)))
    # s4: MIDDLE vertical shaft (crosses top heng)
    draw_shu(draw, _tx(135, 65, ox, oy, scale), _tx(141, 204, ox, oy, scale),
             width=max(2, int(7 * scale)))
    # s5: WIDE horizontal (extends beyond frame both sides; drawn LAST → overdraw welds P-joints)
    draw_heng(draw, _tx(24, 222, ox, oy, scale), _tx(276, 207, ox, oy, scale),
              width_head=max(2, int(8 * scale)),
              width_tail=max(2, int(9 * scale)))
