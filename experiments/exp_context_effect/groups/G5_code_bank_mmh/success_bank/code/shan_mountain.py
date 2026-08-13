"""Bank primitive: 山 (shan, 'mountain' — 3 strokes: shu + shu_zhe + shu).

Promoted from p2_radical_063_山 (G5 B1 PASS, 2026-08-08).
Uses the new shu_zhe.py primitive for the 竖折 base stroke.

Reference layout compressed relative to raw MMH per the drawer's own
GT-calibration (MMH placed the verticals too wide).
"""

from PIL import ImageDraw

from shu import draw_shu
from shu_zhe import draw_shu_zhe


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_shan(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # middle vertical (tallest, with top curl)
    s1_head = _tx(150, 55, ox, oy, scale)
    s1_tail = _tx(152, 195, ox, oy, scale)
    draw_shu(draw, s1_head, s1_tail, width=max(2, int(7 * scale)), top_curl=True)

    # 竖折: left short vertical + bottom horizontal
    s2_head = _tx(95, 125, ox, oy, scale)
    s2_corner = _tx(97, 220, ox, oy, scale)
    s2_tail = _tx(215, 218, ox, oy, scale)
    draw_shu_zhe(draw, s2_head, s2_corner, s2_tail, width=max(2, int(7 * scale)))

    # right vertical
    s3_head = _tx(203, 125, ox, oy, scale)
    s3_tail = _tx(200, 218, ox, oy, scale)
    draw_shu(draw, s3_head, s3_tail, width=max(2, int(7 * scale)))
