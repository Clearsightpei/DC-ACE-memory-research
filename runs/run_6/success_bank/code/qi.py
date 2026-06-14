"""七 (qī, "seven") — composed character. 2 strokes.

Mastered: run_6 c35, panel 3/3 YES (re-judged 2026-06-13 with calligraphy-
aware standard). 横 + 竖弯钩 cross at a NEIGHBOR joint — small placement
offset between the heng and the shu_wan_gou's head is correct handwriting,
not a defect.

Reuse:
    from qi import draw_qi
    draw_qi(t)
"""
from heng import draw_heng
from shu_wan_gou import draw_shu_wan_gou


def draw_qi(t):
    draw_heng(t, ('BL', -0.144, 0.188), ('MR', 0.98, 0.704))
    draw_shu_wan_gou(t, ('TL', 0.908, 0.548), ('BC', 0.628, 1.184), ('BR', 0.588, 1.1))
