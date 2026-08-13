"""Bank primitive: 花 (huā, "flower") — 7 strokes = 艹 (top) + 化 (bottom).

Promoted from p3_char_0357_花 (G5 B10 PASS 2026-08-09). P-A-001
identity-reuse: wrapper calls draw_cao (艹 top) + draw_hua (化 bottom).
HIGH-REUSE: extends to any 艹+X compound (草/苗/苦/苹/茶/蓝/菜/著) —
use this as reference for 艹-position calibration (ox=+38, oy=-55,
scale=0.75) when 化 sits at (ox=+48, oy=+90, scale=0.72).
"""

from PIL import ImageDraw

from cao_grass import draw_cao
from hua_change import draw_hua


def draw_hua_flower(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    draw_cao(draw, ox=ox + 38 * scale, oy=oy - 55 * scale, scale=0.75 * scale)
    draw_hua(draw, ox=ox + 48 * scale, oy=oy + 90 * scale, scale=0.72 * scale)
