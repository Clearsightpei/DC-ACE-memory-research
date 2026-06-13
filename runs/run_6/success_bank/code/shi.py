"""十 (shi) — composed character. Tags: tag:character. c16 run_6."""
from heng import draw_heng
from shu import draw_shu

def draw_shi(t):
    draw_heng(t, ('ML', -0.112, 0.78), ('MR', 1.18, 0.644))
    draw_shu(t, ('TC', 0.276, 0.304), ('BC', 0.48, 1.3))
