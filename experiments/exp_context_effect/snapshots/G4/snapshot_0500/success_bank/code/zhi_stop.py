"""p2_radical_133_止 — 止 (zhǐ, "stop", 4画).

Main 竖 center + short 横 right + short 竖 left + long 横 bottom.
Every 横/竖 endpoint pair shares same row/col (TR8 rules 5/6).

Joints (all N ~15-20 px):
  s1.mid ⇆ s2.head @ C
  s1.tail ⇆ s4.mid(~.43) @ BC
  s3.tail ⇆ s4.mid(~.25) @ BL
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from heng import draw_heng
from shu import draw_shu

DEFAULTS = {
    's1_h': ('TC', 0.40, 0.75), 's1_t': ('BC', 0.40, 0.60),
    's2_h': ('C',  0.60, 0.65), 's2_t': ('MR', 0.40, 0.65),
    's3_h': ('ML', 0.75, 0.65), 's3_t': ('BL', 0.75, 0.65),
    's4_h': ('BL', 0.15, 0.75), 's4_t': ('BR', 0.85, 0.75),
}


def draw_zhi_stop(draw, **overrides):
    p = {**DEFAULTS, **overrides}
    draw_shu(draw, p['s1_h'], p['s1_t'], width=10)
    draw_heng(draw, p['s2_h'], p['s2_t'], width=9)
    draw_shu(draw, p['s3_h'], p['s3_t'], width=9)
    draw_heng(draw, p['s4_h'], p['s4_t'], width=10)
