"""二 (èr) — Phase-2 radical, 2画. Composition: 横 + 横.

Anchor plan (米字格, PIL-native — from passing bootstrap attempt):
  s1 横 (top, short):    head @ ('ML', 0.858, 0.28),  tail @ ('MR', 0.147, 0.157), width 10
  s2 横 (bottom, longer): head @ ('BL', 0.369, 0.358), tail @ ('BR', 0.684, 0.326), width 11

Joints: NONE (S — clear vertical gap between the two horizontals).

Proportion rule: top 横 is SHORTER than bottom 横 (~1/2 to 2/3 the
length). Bottom 横 sits low in the BL/BR cells.

Human PASS (bootstrap batch, 2026-07-17).
"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

from heng import draw_heng


def draw_er(draw,
            s1_head=('ML', 0.858, 0.28),
            s1_tail=('MR', 0.147, 0.157),
            s2_head=('BL', 0.369, 0.358),
            s2_tail=('BR', 0.684, 0.326)):
    """Render 二 as two 横 strokes with clear vertical gap; top shorter than bottom."""
    draw_heng(draw, s1_head, s1_tail, width=10)
    draw_heng(draw, s2_head, s2_tail, width=11)
