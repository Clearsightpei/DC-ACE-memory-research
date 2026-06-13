"""田 (tian) — composed character. Tags: tag:character. c29 run_6."""
from heng import draw_heng
from heng_zhe import draw_heng_zhe
from shu import draw_shu

def draw_tian(t):
    draw_shu(t, ('ML', 0.124, 0.028), ('BL', 0.592, 1.052))
    draw_heng_zhe(t, ('ML', 0.388, 0.076), ('MR', 0.744, 0.012), ('BR', 0.348, 1.116))
    draw_heng(t, ('ML', 0.836, 0.98), ('MR', 0.112, 0.856))
    draw_shu(t, ('C', 0.324, 0.116), ('BC', 0.388, 0.636))
    draw_heng(t, ('BL', 0.672, 0.864), ('BR', 0.236, 0.68))
