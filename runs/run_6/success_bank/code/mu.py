"""木 (mu) — composed character. Tags: tag:character. c22 run_6."""
from heng import draw_heng
from na import draw_na
from pie import draw_pie
from shu import draw_shu

def draw_mu(t):
    draw_heng(t, ('ML', 0.364, 0.412), ('MR', 0.516, 0.252))
    draw_shu(t, ('TC', 0.264, 0.248), ('BC', 0.396, 1.3))
    draw_pie(t, ('C', 0.348, 0.472), ('BL', -0.028, 1.052))
    draw_na(t, ('C', 0.564, 0.496), ('BR', 1.256, 0.912))
