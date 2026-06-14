"""口 (kǒu, "mouth") — composed character. 3 strokes.

Mastered: run_6 c32, panel 3/3 YES (re-judged 2026-06-13 with calligraphy-
aware standard). The original c32 render's small gaps at the three
NEIGHBOR corners (top-left, bottom-left, bottom-right) are CORRECT
calligraphy, not defects — only the top-right corner is WELDED because
it's inside the 横折 primitive.

Reuse:
    from kou import draw_kou
    draw_kou(t)
"""
from shu import draw_shu
from heng_zhe import draw_heng_zhe
from heng import draw_heng


def draw_kou(t):
    draw_shu(t, ('ML', 0.368, 0.212), ('BL', 0.844, 0.94))
    draw_heng_zhe(t, ('ML', 0.668, 0.272), ('MR', 0.488, 0.312), ('BR', 0.096, 0.456))
    draw_heng(t, ('BL', 0.928, 0.808), ('BR', 0.428, 0.652))
