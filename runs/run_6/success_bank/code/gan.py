"""干 (gan) — composed character. Tags: tag:character. c17 run_6."""
from heng import draw_heng
from shu import draw_shu

def draw_gan(t):
    draw_heng(t, ('TL', 0.712, 0.58), ('TR', 0.408, 0.396))
    draw_heng(t, ('ML', -0.132, 0.76), ('MR', 1.188, 0.62))
    draw_shu(t, ('TC', 0.312, 0.712), ('BC', 0.476, 1.3))
