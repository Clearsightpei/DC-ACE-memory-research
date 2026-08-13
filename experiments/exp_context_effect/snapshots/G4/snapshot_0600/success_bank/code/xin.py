"""p2_radical_126_心 — 心 (xīn, "heart", 4画).

wo_gou body + 3 dots (left as short pie, middle, right).
Joints: NONE (all 4 strokes visually separate, S-class).
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from wo_gou import draw_wo_gou
from dian import draw_dian
from pie import draw_pie

DEFAULTS = {
    's1_h': ('ML', 0.542, 0.646), 's1_t': ('BL', 0.39, 0.309),  # left dot as pie
    's2_start': ('ML', 0.896, 0.614), 's2_belly': ('BC', 0.50, 0.40),
    's2_exit': ('MR', 0.024, 0.849), 's2_tip': ('C', 0.80, 0.35),
    's3_h': ('C', 0.245, 0.046),  's3_t': ('C', 0.588, 0.436),
    's4_h': ('MR', 0.229, 0.222), 's4_t': ('MR', 0.681, 0.661),
}


def draw_xin(draw, **overrides):
    p = {**DEFAULTS, **overrides}
    draw_pie(draw, p['s1_h'], p['s1_t'], head_width=10, tail_width=3, curve=0.10)
    draw_wo_gou(draw, start=p['s2_start'], belly=p['s2_belly'],
                exit=p['s2_exit'], tip=p['s2_tip'],
                head_w=3, belly_w=11, exit_w=11, tip_w=1)
    draw_dian(draw, p['s3_h'], p['s3_t'], head_width=2, peak_width=12, curve=0.08)
    draw_dian(draw, p['s4_h'], p['s4_t'], head_width=2, peak_width=10, curve=0.08)
