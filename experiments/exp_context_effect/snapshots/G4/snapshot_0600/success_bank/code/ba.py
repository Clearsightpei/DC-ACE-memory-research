"""八 (bā) — Phase-2 radical, 2画. Composition: 撇 + 捺.

Anchor plan (米字格, PIL-native):
  s1 撇: head @ ('ML', 0.97, 0.623), tail @ ('BL', 0.261, 0.64)
         head_width 11, tail_width 1, curve 0.10
  s2 捺: head @ ('TC', 0.324, 0.964), tail @ ('BR', 0.865, 0.569)
         head_width 3, peak_width 13, peak_t 0.8, curve 0.10

Joints: NONE (S-class — heads sit apart at top, no weld/tangent).

Human PASS (bootstrap batch, 2026-07-17).
"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

from pie import draw_pie
from na import draw_na


def draw_ba(draw,
            s1_head=('ML', 0.97, 0.623),
            s1_tail=('BL', 0.261, 0.64),
            s2_head=('TC', 0.324, 0.964),
            s2_tail=('BR', 0.865, 0.569)):
    """Render 八 as 撇 + 捺 with S-class (separate) joint."""
    draw_pie(draw, s1_head, s1_tail,
             head_width=11, tail_width=1, curve=0.10, segments=48)
    draw_na(draw, s2_head, s2_tail,
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.8, curve=0.10, segments=48)
