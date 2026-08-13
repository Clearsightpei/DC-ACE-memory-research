"""亅 (jué) — Phase-2 radical, 1画. Wrapper for draw_shu_gou.

Anchor plan (米字格, PIL-native):
  stroke 1 (竖钩):
    head    @ ('TC', 0.283, 0.674)
    belly   @ ('C',  0.283, 0.35)   internal width-knot; shares head x
    hook_pt @ ('BC', 0.283, 0.85)   bottom of straight vertical
    tip     @ ('BL', 0.973, 0.722)  hook flick to bottom-left
Joints: NONE (single stroke, internal hook is part of the primitive).
"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

from shu_gou import draw_shu_gou


def draw_jue(draw,
             head=('TC', 0.283, 0.674),
             belly=('C',  0.283, 0.35),
             hook_pt=('BC', 0.283, 0.85),
             tip=('BL', 0.973, 0.722),
             head_w=8, belly_w=9, hook_start_w=9, tip_w=2):
    """Render 亅. Defaults match MMH anchors for standalone radical."""
    draw_shu_gou(draw, head, belly, hook_pt, tip,
                 head_w=head_w, belly_w=belly_w,
                 hook_start_w=hook_start_w, tip_w=tip_w)
