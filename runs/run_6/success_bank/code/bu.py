"""不 (bu) — composed character. Tags: tag:character. c25 run_6."""
from dian import draw_dian
from heng import draw_heng
from pie import draw_pie
from shu import draw_shu

def draw_bu(t):
    draw_heng(t, ('TL', 0.2, 0.88), ('TR', 0.968, 0.756))
    draw_pie(t, ('TC', 0.724, 0.84), ('BL', -0.088, 0.904))
    draw_shu(t, ('C', 0.288, 0.356), ('BC', 0.464, 1.3))
    draw_dian(t, ('C', 0.98, 0.88), ('BR', 0.988, 0.748))
