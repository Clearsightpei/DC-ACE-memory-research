"""匕 (bǐ) — Phase-2 radical, 2画. Composition: 撇 + 竖弯钩.

Anchor plan (米字格, PIL-native — from passing bootstrap attempt):
  s1 撇:       head @ ('MR', 0.183, 0.254), tail @ ('C', 0.031, 0.931)
               head_width 10, tail_width 2, curve 0.10 (upward bow)
  s2 竖弯钩:   head    @ ('ML', 0.776, 0.005)   — top-left of body
               belly   @ ('C', 0.30, 0.95)      — control (Bezier),
                                                  opens the N-gap with s1
               corner  @ ('BC', 0.35, 0.30)     — round bottom bend
               hook_pt @ ('BR', 0.55, 0.28)     — right side of base
               tip     @ ('BR', 0.496, 0.036)   — up-flick tip
               head_w 8, belly_w 11, corner_w 11, hook_start_w 10, tip_w 2

Joints:
  s1.tail ⇆ s2.body-midpoint — N-class (~15-25 px). Body of s2 arcs to
  the right of s1.tail; visible crossing but not welded.

Human PASS (bootstrap batch, 2026-07-17).
"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

from pie import draw_pie
from shu_wan_gou import draw_shu_wan_gou


def draw_bi(draw,
            s1_head=('MR', 0.183, 0.254),
            s1_tail=('C', 0.031, 0.931),
            s2_head=('ML', 0.776, 0.005),
            s2_belly=('C', 0.30, 0.95),
            s2_corner=('BC', 0.35, 0.30),
            s2_hook_pt=('BR', 0.55, 0.28),
            s2_tip=('BR', 0.496, 0.036)):
    """Render 匕 as 撇 + 竖弯钩 with N-class crossing joint."""
    draw_pie(draw, s1_head, s1_tail,
             head_width=10, tail_width=2, curve=0.10, segments=48)
    draw_shu_wan_gou(draw,
                     head=s2_head, belly=s2_belly, corner=s2_corner,
                     hook_pt=s2_hook_pt, tip=s2_tip,
                     head_w=8, belly_w=11, corner_w=11,
                     hook_start_w=10, tip_w=2)
