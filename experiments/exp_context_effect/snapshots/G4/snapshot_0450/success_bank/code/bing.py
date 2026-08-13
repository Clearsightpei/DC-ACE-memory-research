"""冫 (bīng) — Phase-2 radical, 2画 ("two-drops water").
Composition: 点 + 提 (upper dot + lower rising flick).

Anchor plan (米字格, PIL-native — from passing bootstrap attempt):
  s1 点: head @ ('TC', 0.245, 0.976), tail @ ('C', 0.638, 0.395)
         head_width 3, peak_width 13, curve 0.10, segments 32
  s2 提: head @ ('BC', 0.315, 0.780), tail @ ('C', 0.734, 0.781)
         head_width 14, tail_width 1, curve 0.10, segments 48

Joints: NONE (S-class — clear vertical gap between strokes).

Human PASS (bootstrap batch, 2026-07-17).
"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

from dian import draw_dian
from ti import draw_ti


def draw_bing(draw,
              s1_head=('TC', 0.245, 0.976),
              s1_tail=('C', 0.638, 0.395),
              s2_head=('BC', 0.315, 0.780),
              s2_tail=('C', 0.734, 0.781)):
    """Render 冫 as 点 (top) + 提 (bottom) with clear gap."""
    draw_dian(draw, s1_head, s1_tail,
              head_width=3, peak_width=13, curve=0.10, segments=32)
    draw_ti(draw, s2_head, s2_tail,
            head_width=14, tail_width=1, curve=0.10, segments=48)
