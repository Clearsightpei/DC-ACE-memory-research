"""立 (lì, "stand") — composed character. 5 strokes.

Mastered: run_6 c62, panel 3/3 YES.
(NOTE: file named li_stand.py to avoid clash with 力 if/when promoted.)

Strokes: 点 + 横 (top 亠) + 点 + 撇 (interior pair) + 横 (long base)

Reuse:
    from li_stand import draw_li_stand
    draw_li_stand(t)
"""
from dian import draw_dian
from heng import draw_heng
from pie import draw_pie


def draw_li_stand(t):
    draw_dian(t, ('TC', 0.148, 0.46), ('TC', 0.708, 0.792))
    draw_heng(t, ('ML', 0.552, 0.552), ('MR', 0.456, 0.292))
    draw_dian(t, ('BL', 0.732, 0.008), ('BC', 0.068, 0.556))
    draw_pie(t, ('C', 0.864, 0.704), ('BC', 0.584, 0.912))
    draw_heng(t, ('BL', -0.092, 1.184), ('BR', 1.152, 1.16))
