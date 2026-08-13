"""p2_radical_061_女 — 女 (nǚ, "woman", 3画). B3 retry PASS.

Retry-1 fix that worked: lift 撇点 head to TC(0.35, 0.20), push pivot
down to C(0.30, 0.85), widen 横 arm at y≈0.60. All 3 joints P-welded.

Fills the form_catalog "known gap" for 撇 in 女.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from pie_dian import draw_pie_dian
from pie import draw_pie
from heng import draw_heng

DEFAULTS = {
    's1_head': ('TC', 0.35, 0.20), 's1_pivot': ('C', 0.30, 0.85), 's1_tail': ('BR', 0.55, 0.75),
    's2_head': ('C', 0.85, 0.55),  's2_tail': ('BL', 0.55, 0.85),
    's3_head': ('ML', 0.15, 0.60), 's3_tail': ('MR', 0.85, 0.55),
}


def draw_nv(draw, **overrides):
    p = {**DEFAULTS, **overrides}
    draw_pie_dian(draw, head=p['s1_head'], pivot=p['s1_pivot'], tail=p['s1_tail'],
                  pie_head_w=12, pie_tip_w=4, dian_head_w=4, dian_tail_w=11)
    draw_pie(draw, from_anchor=p['s2_head'], to_anchor=p['s2_tail'],
             head_width=11, tail_width=2, curve=0.08)
    draw_heng(draw, from_anchor=p['s3_head'], to_anchor=p['s3_tail'], width=8)
