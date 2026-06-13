"""下 (xia) — composed character. Tags: tag:character. c20 run_6."""
from dian import draw_dian
from heng import draw_heng
from shu import draw_shu

def draw_xia(t):
    draw_heng(t, ('TL', -0.096, 0.82), ('TR', 1.148, 0.708))
    draw_shu(t, ('TC', 0.4, 0.824), ('BC', 0.492, 1.3))
    draw_dian(t, ('C', 0.672, 0.472), ('BR', 0.444, 0.04))
