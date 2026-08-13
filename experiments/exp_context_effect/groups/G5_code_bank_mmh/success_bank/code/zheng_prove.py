"""Bank primitive: 证 (zhèng, "prove") — 7 strokes = 讠 + 正.

Promoted from p3_char_0347_证 (G5 B10 PASS 2026-08-09). P-A-001
identity-reuse wrapper: draw_yan_speech (讠, B3 R2 bank) at
(ox=-5, oy=+30, scale=0.72) + draw_zheng (正, B6 bank) at
(ox=+90, oy=+50, scale=0.75). HIGH REUSE: template for any 讠+X
compound (说/话/讲/询/记/让/请) — the 讠-position calibration is the
key reusable piece.
"""

from PIL import ImageDraw

from yan_speech import draw_yan_speech
from zheng_correct import draw_zheng


def draw_zheng_prove(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    draw_yan_speech(draw, ox=ox - 5 * scale, oy=oy + 30 * scale, scale=0.72 * scale)
    draw_zheng(draw, ox=ox + 90 * scale, oy=oy + 50 * scale, scale=0.75 * scale)
