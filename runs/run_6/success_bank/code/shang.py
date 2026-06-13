"""上 (shang) — composed character. Tags: tag:character. c19 run_6."""
from heng import draw_heng
from shu import draw_shu

def draw_shang(t):
    draw_shu(t, ('TC', 0.236, 0.424), ('BC', 0.34, 1.004))
    draw_heng(t, ('C', 0.576, 0.756), ('MR', 0.524, 0.564))
    draw_heng(t, ('BL', -0.012, 1.18), ('BR', 1.18, 1.152))
