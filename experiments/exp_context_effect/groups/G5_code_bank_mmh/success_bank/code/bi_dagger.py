"""Bank primitive: 匕 (radical — 2 strokes; short 撇 + 竖弯钩).

Promoted from p2_radical_011_匕 (G5 bootstrap PASS, 2026-08-08).
Composes pie + shu_wan_gou. Joint class N — the pie tail approaches the
vertical body of the 竖弯钩 but does NOT weld (natural ~16 px gap).

Reusable component in 化, 北, 老, 死.
"""

from PIL import ImageDraw

from pie import draw_pie
from shu_wan_gou import draw_shu_wan_gou


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_bi(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    """Draw 匕 at (ox, oy). Reference canvas 300x300."""
    # stroke 1: 撇 from upper-right to center
    pie_head = _tx(218, 125, ox, oy, scale)
    pie_tail = _tx(103, 193, ox, oy, scale)
    draw_pie(draw, pie_head, pie_tail,
             bow_perp=-8 * scale,  # slight upward bow (negative perp)
             w_head=6 * scale, w_tail=3 * scale)

    # stroke 2: 竖弯钩 from left-upper down and right
    swg_head = _tx(78, 100, ox, oy, scale)
    swg_tail = _tx(250, 204, ox, oy, scale)
    draw_shu_wan_gou(draw, swg_head, swg_tail,
                     width=int(7 * scale),
                     bottom_extra=int(60 * scale),
                     knee_ratio=0.75)
