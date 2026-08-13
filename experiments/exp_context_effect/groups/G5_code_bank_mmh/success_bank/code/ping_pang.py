"""Bank primitive: 乓 (pāng — 6 strokes: pie + pie + heng + shu + heng + pie).

Promoted from p3_char_0224_乓 (G5 B7 **A** verdict, 2026-08-08).
Recipe: P-A-006 — MMH anchors verbatim, stroke primitives, all N joints.
Composition = 丘 (top block) + trailing 丿 (bottom-right descender).
Sibling of 乒 (mirror, bottom-left descender) and 兵/丘.
Reuse targets: 乓 (identity), 乒 (mirror s6).
"""

from PIL import ImageDraw

from pie import draw_pie
from shu import draw_shu
from heng import draw_heng


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_ping_pang(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: top short pie (down-left)
    draw_pie(draw, _tx(205, 76, ox, oy, scale), _tx(115, 111, ox, oy, scale),
             bow_perp=int(6 * scale) or 1,
             w_head=max(2, int(7 * scale)),
             w_tail=max(2, int(3 * scale)), steps=40)
    # s2: left long slant (near-vertical, slight right drift + gentle bow)
    draw_pie(draw, _tx(88, 103, ox, oy, scale), _tx(107, 211, ox, oy, scale),
             bow_perp=int(-4 * scale) or -1,
             w_head=max(2, int(8 * scale)),
             w_tail=max(2, int(6 * scale)), steps=60)
    # s3: short horizontal near center
    draw_heng(draw, _tx(115, 150, ox, oy, scale), _tx(223, 134, ox, oy, scale),
              width_head=max(2, int(7 * scale)),
              width_tail=max(2, int(8 * scale)))
    # s4: short vertical middle
    draw_shu(draw, _tx(169, 152, ox, oy, scale), _tx(167, 205, ox, oy, scale),
             width=max(2, int(7 * scale)))
    # s5: long bottom horizontal (base of 丘)
    draw_heng(draw, _tx(33, 227, ox, oy, scale), _tx(270, 212, ox, oy, scale),
              width_head=max(2, int(9 * scale)),
              width_tail=max(2, int(11 * scale)))
    # s6: final pie/descender (tail runs off-canvas at BR)
    draw_pie(draw, _tx(171, 242, ox, oy, scale), _tx(231, 303, ox, oy, scale),
             bow_perp=int(4 * scale) or 1,
             w_head=max(2, int(8 * scale)),
             w_tail=max(2, int(2 * scale)), steps=50)
