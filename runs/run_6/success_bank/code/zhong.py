"""中 (zhong) — composed character. Tags: tag:character. c26 run_6."""
from heng import draw_heng
from heng_zhe import draw_heng_zhe
from shu import draw_shu

def draw_zhong(t):
    draw_shu(t, ('ML', 0.228, 0.156), ('BL', 0.632, 0.256))
    draw_heng_zhe(t, ('ML', 0.5, 0.184), ('TR', 0.416, 0.996), ('MR', 0.26, 0.764))
    draw_heng(t, ('BL', 0.716, 0.148), ('MR', 0.524, 0.956))
    draw_shu(t, ('TC', 0.248, 0.256), ('BC', 0.448, 1.3))
