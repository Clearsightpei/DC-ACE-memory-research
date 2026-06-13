"""月 (yue) — composed character. Tags: tag:character. c28 run_6."""
from heng import draw_heng
from heng_zhe_gou import draw_heng_zhe_gou
from pie import draw_pie

def draw_yue(t):
    draw_pie(t, ('TL', 0.808, 0.456), ('BL', 0.032, 1.3))
    draw_heng_zhe_gou(t, ('TC', 0.112, 0.492), ('TR', 0.176, 0.516), ('BC', 0.604, 1.132))
    draw_heng(t, ('C', 0.12, 0.38), ('C', 0.804, 0.292))
    draw_heng(t, ('BC', 0.048, 0.076), ('C', 0.804, 0.98))
