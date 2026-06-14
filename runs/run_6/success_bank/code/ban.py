"""半 (bàn, "half") — composed character. 5 strokes.

Mastered: run_6 c52, panel 3/3 YES.
NEW PRIMITIVES THIS CYCLE: dian + pie + heng + heng + shu — first character
in run_6 to use dian.

Reuse:
    from ban import draw_ban
    draw_ban(t)
"""
from dian import draw_dian
from pie import draw_pie
from heng import draw_heng
from shu import draw_shu


def draw_ban(t):
    draw_dian(t, ('TL', 0.604, 0.716), ('C', 0.012, 0.108))
    draw_pie(t, ('TR', 0.308, 0.368), ('TC', 0.908, 0.956))
    draw_heng(t, ('ML', 0.712, 0.528), ('MR', 0.256, 0.38))
    draw_heng(t, ('BL', -0.144, 0.26), ('BR', 1.192, 0.116))
    draw_shu(t, ('TC', 0.264, 0.228), ('BC', 0.48, 1.3))
