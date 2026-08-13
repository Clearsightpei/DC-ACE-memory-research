"""Bank primitive: 找 (zhǎo, "seek/find") — 7 strokes = 扌 + 戈.

Promoted from p3_char_0353_找 (G5 B10 PASS 2026-08-09). P-A-001
identity-reuse wrapper: draw_shou (扌, B1) at (ox=-35, oy=+25,
scale=0.72) + draw_ge (戈, B2) at (ox=+105, oy=+25, scale=0.60).
VERY HIGH REUSE: template for any 扌+X compound (打/找/把/接/拿/挂/推)
— the 扌-position calibration is the reusable piece; also anchors
the 戈-family L-R rendering.
"""

from PIL import ImageDraw

from ge_dagger import draw_ge
from shou_hand import draw_shou


def draw_zhao_seek(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    draw_shou(draw, ox=ox - 35 * scale, oy=oy + 25 * scale, scale=0.72 * scale)
    draw_ge(draw, ox=ox + 105 * scale, oy=oy + 25 * scale, scale=0.60 * scale)
