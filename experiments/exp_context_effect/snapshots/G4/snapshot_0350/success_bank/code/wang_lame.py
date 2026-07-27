"""p2_radical_121_尣 — 尣 (wāng, "lame", 4画).

Bank entry promoted after B3 human PASS.

Composition (per B3 attempt):
  s1 — 短撇 upper-left "hair"
  s2 — 短撇/dian upper-right "hair"
  s3 — 长撇 left leg (ML → BL)
  s4 — 竖弯 right leg (C → BR)

Joints: NONE (all four visually separate — S-class).
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from pie import draw_pie
from shu_wan import draw_shu_wan

DEFAULTS = {
    's1_head': ('TL', 0.75, 0.55), 's1_tail': ('ML', 0.55, 0.30),
    's2_head': ('TC', 0.75, 0.60), 's2_tail': ('MR', 0.20, 0.10),
    's3_head': ('ML', 0.90, 0.35), 's3_tail': ('BL', 0.30, 0.90),
    's4_head': ('C',  0.50, 0.15), 's4_belly': ('C', 0.50, 0.80),
    's4_corner': ('BC', 0.55, 0.85), 's4_tail': ('BR', 0.45, 0.75),
}


def draw_wang_lame(draw, **overrides):
    p = {**DEFAULTS, **overrides}
    draw_pie(draw, p['s1_head'], p['s1_tail'], head_width=8, tail_width=2, curve=0.12)
    draw_pie(draw, p['s2_head'], p['s2_tail'], head_width=8, tail_width=2, curve=0.15)
    draw_pie(draw, p['s3_head'], p['s3_tail'], head_width=11, tail_width=2, curve=0.10)
    draw_shu_wan(draw, p['s4_head'], p['s4_belly'], p['s4_corner'], p['s4_tail'],
                 head_w=8, belly_w=10, corner_w=10, tail_w=8)
