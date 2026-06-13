"""三 (sān) — 3 stacked heng. Tags: tag:character tag:3-strokes. c15."""
from heng import draw_heng
def draw_san(t):
    draw_heng(t, ('TL', 0.716, 0.928), ('TR', 0.34, 0.78))
    draw_heng(t, ('ML', 0.776, 0.92), ('MR', 0.252, 0.82))
    draw_heng(t, ('BL', -0.04, 0.94), ('BR', 1.272, 0.852))
