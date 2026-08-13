"""卜 (bǔ) — Phase-2 radical, 2画. Composition: 竖 + 点.

Anchor plan (米字格, PIL-native — from passing bootstrap attempt):
  s1 竖: head @ ('TC', 0.213, 0.642), tail @ ('BC', 0.342, 1.0), width 10
         (BC tail y_frac clamped from MMH's 1.117 -> 1.0)
  s2 点: head @ ('C', 0.62, 0.477), tail @ ('MR', 0.396, 0.91)
         head_width 3, peak_width 10, curve 0.06, segments 32

Joints:
  s1.mid(t=0.32) ⇆ s2.head @ cell C — N-class (natural gap ~35-77 px).
  Do NOT weld; the small horizontal gap is canonical.

Human PASS (bootstrap batch, 2026-07-17).
"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

from shu import draw_shu
from dian import draw_dian


def draw_bu(draw,
            s1_head=('TC', 0.213, 0.642),
            s1_tail=('BC', 0.342, 1.0),
            s2_head=('C', 0.62, 0.477),
            s2_tail=('MR', 0.396, 0.91)):
    """Render 卜 as 竖 + 点 with N-class right-side joint."""
    draw_shu(draw, s1_head, s1_tail, width=10)
    draw_dian(draw, s2_head, s2_tail,
              head_width=3, peak_width=10, curve=0.06, segments=32)
