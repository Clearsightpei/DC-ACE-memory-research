"""一 (yī) — Phase-2 radical, 1画. Wrapper for draw_heng.

Anchor plan (米字格, PIL-native):
  stroke 1 (横): head @ ('ML', 0.354, 0.849), tail @ ('MR', 0.695, 0.825)
                 width 10.
Joints: NONE.
"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

from heng import draw_heng


def draw_yi_one(draw,
                head=('ML', 0.354, 0.849),
                tail=('MR', 0.695, 0.825),
                width=10):
    """Render 一. Defaults match MMH anchors for standalone radical."""
    draw_heng(draw, head, tail, width=width)
