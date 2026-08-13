"""Bank primitive: 元 (yuan, "first" — 4 strokes: heng + heng + pie + shu_wan_gou).

Promoted from p3_char_0152_元 (G5 B6 PASS, 2026-08-08). Sibling of 无:
same 4-primitive family; 元's pie is SHORT and starts at the LEVEL of the
lower heng (does not cross above the top heng like 无 does).

Reuse targets: 完 (宀+元), 园 (囗+元), 院 (阝+完), 远 (辶+元),
玩 (王+元), 冠 (冖+元-derivative).

Signature: (draw, ox=0, oy=0, scale=1.0). Baked from MMH anchors on 300×300.
"""

from PIL import ImageDraw

from heng import draw_heng
from pie import draw_pie
from shu_wan_gou import draw_shu_wan_gou


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_yuan(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: top short heng
    draw_heng(draw,
              _tx(99, 96, ox, oy, scale), _tx(189, 82, ox, oy, scale),
              width_head=max(2, int(8 * scale)),
              width_tail=max(2, int(9 * scale)))
    # s2: middle long heng
    draw_heng(draw,
              _tx(52, 167, ox, oy, scale), _tx(220, 139, ox, oy, scale),
              width_head=max(2, int(9 * scale)),
              width_tail=max(2, int(10 * scale)))
    # s3: pie (starts at s2 mid-level; does NOT cross above top heng)
    draw_pie(draw,
             _tx(99, 173, ox, oy, scale), _tx(33, 282, ox, oy, scale),
             bow_perp=10, w_head=max(2, int(8 * scale)),
             w_tail=max(2, int(2 * scale)))
    # s4: shu_wan_gou (descends, curves right, hooks up)
    draw_shu_wan_gou(draw,
                     _tx(144, 159, ox, oy, scale),
                     _tx(267, 222, ox, oy, scale),
                     width=max(2, int(7 * scale)),
                     bottom_extra=52, knee_ratio=0.72)
