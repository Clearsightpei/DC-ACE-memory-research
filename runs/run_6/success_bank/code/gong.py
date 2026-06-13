"""工 (gong) — composed character. Tags: tag:character. c18 run_6."""
from heng import draw_heng
from shu import draw_shu

def draw_gong(t):
    draw_heng(t, ('ML', 0.636, 0.012), ('TR', 0.528, 0.84))
    draw_shu(t, ('C', 0.392, 0.12), ('BC', 0.42, 0.668))
    draw_heng(t, ('BL', -0.124, 0.856), ('BR', 1.244, 0.84))
