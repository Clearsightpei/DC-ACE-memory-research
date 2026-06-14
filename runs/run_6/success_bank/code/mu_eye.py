"""目 (mù, "eye") — composed character. 5 strokes (shu + heng_zhe + 3×heng).

Mastered: run_6 c42 (restart after c40 froze, panel 3/3 YES).

NOTE: avoid name clash with 木 (mu, "tree", already in bank as `mu.py`).
This file is `mu_eye.py`; the draw fn is `draw_mu_eye`.

Anchors derived from MMH medians. The horizontal-folding stroke (heng_zhe)
uses the **geometric L-corner heuristic** `(to_x, from_y)` — NOT the MMH
max-x bend, which placed the corner at the bottom-right of the right
vertical instead of the top-right L-bend and caused the c40 regression.

Reuse:
    from mu_eye import draw_mu_eye
    draw_mu_eye(t)
"""
from heng import draw_heng
from heng_zhe import draw_heng_zhe
from shu import draw_shu


def draw_mu_eye(t):
    draw_shu(t, ('TL', 0.576, 0.656), ('BL', 0.684, 1.244))
    draw_heng_zhe(t, ('TL', 0.804, 0.704), ('TC', 0.872, 0.704), ('BC', 0.872, 1.020))
    draw_heng(t, ('ML', 0.844, 0.556), ('C', 0.764, 0.420))
    draw_heng(t, ('BL', 0.836, 0.180), ('BC', 0.776, 0.072))
    draw_heng(t, ('BL', 0.792, 1.064), ('BC', 0.956, 0.948))
