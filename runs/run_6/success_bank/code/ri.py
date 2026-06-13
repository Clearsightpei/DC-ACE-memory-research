"""日 (ri) — composed character. Tags: tag:character. c27 run_6."""
from heng import draw_heng
from heng_zhe import draw_heng_zhe
from shu import draw_shu

def draw_ri(t):
    draw_shu(t, ('TL', 0.588, 0.812), ('BL', 0.66, 1.268))
    draw_heng_zhe(t, ('TL', 0.888, 0.908), ('TR', 0.212, 0.888), ('BR', 0.204, 1.3))
    draw_heng(t, ('ML', 0.88, 0.896), ('C', 0.776, 0.824))
    draw_heng(t, ('BL', 0.812, 1.124), ('BC', 0.98, 0.976))
