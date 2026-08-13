"""Bank primitive: 刂 (radical — right-side knife; 2 strokes).

Promoted from p2_radical_016_刂 (G5 bootstrap PASS, 2026-08-08).
Short left vertical + long right vertical with a hook at bottom (竖钩).
Common as the right radical in 到, 别, 利, 前, 剩.
"""

from PIL import ImageDraw

from shu_gou import draw_shu_gou


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_dao_right(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    """Draw 刂 at (ox, oy). Reference canvas 300x300."""
    # short left vertical (a plain 竖 line)
    s1_head = _tx(111, 116, ox, oy, scale)
    s1_tail = _tx(119, 217, ox, oy, scale)
    draw.line([s1_head, s1_tail], fill='black', width=int(6 * scale))

    # long right vertical + hook (竖钩)
    s2_head = _tx(161, 71, ox, oy, scale)
    s2_tail = _tx(134, 270, ox, oy, scale)
    draw_shu_gou(draw, s2_head, s2_tail,
                 width=int(6 * scale),
                 hook_start_offset=int(40 * scale))
