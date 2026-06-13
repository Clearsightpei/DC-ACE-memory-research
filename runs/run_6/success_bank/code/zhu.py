"""主 (zhu) — composed character. Tags: tag:character. c24 run_6."""
from dian import draw_dian
from heng import draw_heng
from shu import draw_shu

def draw_zhu(t):
    draw_dian(t, ('TC', 0.24, 0.288), ('TC', 0.744, 0.708))
    draw_heng(t, ('ML', 0.568, 0.38), ('MR', 0.456, 0.148))
    draw_heng(t, ('BL', 0.664, 0.32), ('BR', 0.236, 0.132))
    draw_shu(t, ('C', 0.38, 0.436), ('BC', 0.42, 1.08))
    draw_heng(t, ('BL', -0.076, 1.276), ('BR', 1.26, 1.216))
