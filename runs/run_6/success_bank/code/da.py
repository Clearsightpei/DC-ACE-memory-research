"""大 (da) — composed character. Tags: tag:character. c21 run_6."""
from heng import draw_heng
from na import draw_na
from pie import draw_pie

def draw_da(t):
    draw_heng(t, ('ML', 0.292, 0.716), ('MR', 0.692, 0.48))
    draw_pie(t, ('TC', 0.116, 0.308), ('BL', 0.004, 1.3))
    draw_na(t, ('C', 0.396, 0.828), ('BR', 1.264, 1.3))
