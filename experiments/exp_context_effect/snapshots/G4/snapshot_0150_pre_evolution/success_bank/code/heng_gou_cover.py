"""乛 — Phase-2 radical, 1画. Wrapper for draw_heng_gou.

Anchor plan (米字格, PIL-native):
  stroke 1 (横钩):
    head     @ ('ML', 0.782, 0.342)  MMH head
    shoulder @ ('MR', 0.40,  0.25)   internal bend point (required by primitive)
    tip      @ ('C',  0.89,  0.623)  MMH tail = hook tip
Joints: NONE.

The shoulder is an internal anchor (bend location) of heng_gou;
MMH only reports head + tail. Shoulder chosen so hook flicks DOWN-LEFT
per canonical 横钩 direction.
"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

from heng_gou import draw_heng_gou


def draw_heng_gou_cover(draw,
                        head=('ML', 0.782, 0.342),
                        shoulder=('MR', 0.40, 0.25),
                        tip=('C', 0.89, 0.623),
                        head_w=8, mid_w=6, shoulder_w=11, tip_w=2):
    """Render 乛. Defaults match MMH anchors for standalone radical."""
    draw_heng_gou(draw, head, shoulder, tip,
                  head_w=head_w, mid_w=mid_w,
                  shoulder_w=shoulder_w, tip_w=tip_w)
