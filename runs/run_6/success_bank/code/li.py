"""里 (li) — composed character. Tags: tag:character. c30 run_6."""
from heng import draw_heng
from heng_zhe import draw_heng_zhe
from shu import draw_shu

def draw_li(t):
    draw_heng(t, ('TL', 0.416, 0.684), ('ML', 0.9, 1.0))
    draw_shu(t, ('TL', 0.62, 0.696), ('MR', 0.14, 0.956))
    draw_heng_zhe(t, ('C', 0.044, 0.308), ('C', 0.86, 0.18), ('C', 0.956, 0.204))
    draw_heng(t, ('ML', 0.972, 0.82), ('C', 0.992, 0.716))
    draw_shu(t, ('TC', 0.296, 0.756), ('BC', 0.364, 1.064))
    draw_heng(t, ('BL', 0.76, 0.52), ('BR', 0.216, 0.396))
    draw_heng(t, ('BL', -0.08, 1.28), ('BR', 1.22, 1.16))
