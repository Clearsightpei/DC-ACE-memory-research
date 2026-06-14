"""五 (wǔ, "five") — composed character. 4 strokes.

Mastered: run_6 c49, panel 3/3 YES.
Joint-snap fix + corner-by-type heuristic applied:
- heng_zhe corner = (to_x, from_y) — geometric L-corner, NOT MMH max-x.

Reuse:
    from wu import draw_wu
    draw_wu(t)
"""
from heng import draw_heng
from shu import draw_shu
from heng_zhe import draw_heng_zhe


def draw_wu(t):
    draw_heng(t, ('TL', 0.524, 0.232), ('TC', 0.864, 0.244))
    draw_shu(t, ('TL', 0.776, 0.328), ('BC', 0.124, 0.732))
    draw_heng_zhe(t, ('ML', 0.792, 0.704), ('C', 0.692, 0.704), ('C', 0.792, 1.232))
    draw_heng(t, ('BL', 0.224, 0.808), ('BR', 0.276, 0.728))
