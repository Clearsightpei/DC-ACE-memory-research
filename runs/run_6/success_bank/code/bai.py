"""白 (bái, "white") — composed character. 5 strokes.

Mastered: run_6 c50, panel 3/3 YES.
Joint-snap + geometric L-corner.

Reuse:
    from bai import draw_bai
    draw_bai(t)
"""
from pie import draw_pie
from shu import draw_shu
from heng_zhe import draw_heng_zhe
from heng import draw_heng


def draw_bai(t):
    draw_pie(t, ('TC', 0.248, 0.312), ('ML', 0.748, 0.442))
    draw_shu(t, ('ML', 0.342, 0.466), ('BL', 0.62, 1.196))
    draw_heng_zhe(t, ('ML', 0.342, 0.466), ('MR', 0.156, 0.466), ('BR', 0.156, 1.008))
    draw_heng(t, ('BL', 0.524, 0.161), ('BC', 0.932, 0.128))
    draw_heng(t, ('BL', 0.616, 0.91), ('BR', 0.156, 1.008))
