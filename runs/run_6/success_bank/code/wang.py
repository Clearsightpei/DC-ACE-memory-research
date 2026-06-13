"""王 (wang) — composed character. Tags: tag:character. c23 run_6."""
from heng import draw_heng
from shu import draw_shu

def draw_wang(t):
    draw_heng(t, ('TL', 0.636, 0.888), ('TR', 0.42, 0.74))
    draw_heng(t, ('ML', 0.776, 0.972), ('MR', 0.276, 0.836))
    draw_shu(t, ('C', 0.368, 0.004), ('BC', 0.412, 0.896))
    draw_heng(t, ('BL', -0.06, 1.084), ('BR', 1.156, 1.056))
