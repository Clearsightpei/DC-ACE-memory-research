"""勹 (bāo) — Phase-2 radical, 2画. Composition: 撇 + 横折钩.

Anchor plan (米字格, PIL-native — from passing bootstrap attempt):
  s1 撇:      head @ ('TC', 0.116, 0.645), tail @ ('ML', 0.56, 0.682)
              head_width 12, tail_width 2, curve 0.05 (shallow bow)
  s2 横折钩:  head   @ ('ML', 0.99, 0.34)
              corner @ ('MR', 0.45, 0.30)   — tight 横 span
              tail   @ ('BC', 0.35, 0.78)   — descent slants down-left
              tip    @ ('BC', 0.15, 0.60)   — hook flick up-and-left
              h_width 9, v_width 9, shoulder 12, tip_w 2

Joints:
  s1.mid ⇆ s2.head @ ML — N-class (small natural gap, ~15-20 px). DO NOT weld.
  Enforced by keeping s2.head anchor slightly right/above s1.tail.

Human PASS (bootstrap batch, 2026-07-17).
"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

from pie import draw_pie
from heng_zhe_gou import draw_heng_zhe_gou


def draw_bao(draw,
             s1_head=('TC', 0.116, 0.645),
             s1_tail=('ML', 0.56, 0.682),
             s2_head=('ML', 0.99, 0.34),
             s2_corner=('MR', 0.45, 0.30),
             s2_tail=('BC', 0.35, 0.78),
             s2_tip=('BC', 0.15, 0.60)):
    """Render 勹 as 撇 + 横折钩 with N-class joint at ML."""
    draw_pie(draw, s1_head, s1_tail,
             head_width=12, tail_width=2, curve=0.05, segments=48)
    draw_heng_zhe_gou(draw, s2_head, s2_corner, s2_tail, s2_tip,
                      h_width=9, v_width=9, shoulder=12, tip_w=2)
