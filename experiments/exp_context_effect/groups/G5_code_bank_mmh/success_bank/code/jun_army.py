"""Bank primitive: 军 (jūn, "army") — 6 strokes.

Promoted from p3_char_0247_军 R1 (G5 B9 PASS 2026-08-09). VALIDATES P-A-007:
main-batch inline FAILed; R1 called draw_mi_cover (2) + draw_che (4) as
whole-radical primitives per errata instruction and PASSed. Textbook
P-A-007 rule-1 outcome.

HIGH-REUSE: 冖+X wrap pattern (军/军/冠/冢/冥/冤). The mi_cover positioning
(ox=8, oy=-18) puts 冖 as a top cover; che_car (ox=28, oy=49, scale=0.85)
compresses 车 to fit under 冖 with shu bottom at y=300.
"""

from PIL import ImageDraw

from che_car import draw_che
from mi_cover import draw_mi_cover


def draw_jun_army(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # Top 冖 via bank primitive (2 strokes: dian + heng_zhe_short)
    draw_mi_cover(draw, ox=ox + 8 * scale, oy=oy - 18 * scale, scale=scale)
    # Body 车 via bank primitive (4 strokes), vertically compressed
    draw_che(draw, ox=ox + 28 * scale, oy=oy + 49 * scale, scale=0.85 * scale)
