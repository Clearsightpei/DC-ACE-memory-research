# zhang_ren.py — 仉 (zhǎng), 亻 + 几. PASSed at p3_char_0113_仉 (B5, pos 264).
# Uses tall inline 亻 (pie + long shu) so shu can match 几's height; bank 几
# on the right at scale 0.85.
from pie import draw_pie
from ji import draw_ji


def _to_pixel(mx, my, canvas=300):
    return canvas / 2 + mx, canvas / 2 - my


def _draw_tall_ren_pang(t, ox=0.0, oy=0.0, scale=1.0):
    """亻 tuned for compound-character composition — tall shu."""
    draw_pie(t, ox=ox + (-8) * scale, oy=oy + 25 * scale, scale=0.85 * scale)
    top_x, top_y = _to_pixel(ox + 5 * scale, oy + 30 * scale)
    bot_x, bot_y = _to_pixel(ox + 5 * scale, oy + (-85) * scale)
    thickness = max(1, int(round(9 * scale)))
    t.line([(top_x, top_y), (bot_x, bot_y)], fill=(0, 0, 0), width=thickness)


def draw_zhang_ren(t, ox=0, oy=0, scale=1.0):
    """仉 — tall inline 亻 (left) + bank 几 (right, scale 0.85)."""
    _draw_tall_ren_pang(t, ox=ox - 70.0 * scale, oy=oy, scale=scale)
    draw_ji(t, ox=ox + 30.0 * scale, oy=oy - 10.0 * scale, scale=0.85 * scale)
