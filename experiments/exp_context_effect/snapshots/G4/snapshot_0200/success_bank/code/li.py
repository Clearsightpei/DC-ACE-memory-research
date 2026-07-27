"""p2_radical_025_力 — 力 (lì, "strength", 2画). B3 retry PASS.

s1 = 横折钩, s2 = 撇 PIERCING s1's descent (P at C).
Retry-1 that worked: MMH-literal head at TC(0.4, 0.671) — 撇 head
sits ABOVE the 横 top-bar (upper-mid), not welded upper-LEFT as the
old B1 errata guessed. 撇 crosses through the descent naturally.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from heng_zhe_gou import draw_heng_zhe_gou
from pie import draw_pie

DEFAULTS = {
    's1_head': ('ML', 0.668, 0.474),
    's1_corner': ('TR', 0.20, 0.85),
    's1_tail': ('BC', 0.459, 0.596),
    's1_tip': ('BC', 0.05, 0.35),
    's2_head': ('TC', 0.40, 0.671),
    's2_tail': ('BL', 0.372, 0.845),
}


def draw_li(draw, **overrides):
    p = {**DEFAULTS, **overrides}
    draw_heng_zhe_gou(draw, p['s1_head'], p['s1_corner'], p['s1_tail'], p['s1_tip'],
                      h_width=9, v_width=9, shoulder=12, tip_w=2)
    draw_pie(draw, p['s2_head'], p['s2_tail'],
             head_width=10, tail_width=1, curve=0.08)
