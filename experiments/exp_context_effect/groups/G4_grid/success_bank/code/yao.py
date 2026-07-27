"""p2_radical_128_爻 — 爻 (yáo, "yao trigram", 4画).

Two stacked 乂 (each = 撇 + 捺 with P at cross-center).
TR9-expanded so each 乂 fills upper vs lower half of the 米字格.
Joints: 2 × P (welded X at top mid; welded X at bottom mid).
Reuses fu.py X-crossing pattern.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from pie import draw_pie
from na import draw_na

DEFAULTS = {
    # top X
    's1_h': ('TR', 0.30, 0.10), 's1_t': ('C', 0.10, 0.65),
    's2_h': ('TL', 0.60, 0.20), 's2_t': ('C', 0.95, 0.60),
    # bottom X
    's3_h': ('MR', 0.20, 0.60), 's3_t': ('BL', 0.10, 0.95),
    's4_h': ('ML', 0.60, 0.70), 's4_t': ('BR', 0.30, 0.98),
}


def draw_yao(draw, **overrides):
    p = {**DEFAULTS, **overrides}
    draw_pie(draw, p['s1_h'], p['s1_t'], head_width=11, tail_width=1, curve=0.06)
    draw_na(draw, p['s2_h'], p['s2_t'], head_width=3, peak_width=11, tail_width=1,
            peak_t=0.82, curve=0.08)
    draw_pie(draw, p['s3_h'], p['s3_t'], head_width=12, tail_width=1, curve=0.08)
    draw_na(draw, p['s4_h'], p['s4_t'], head_width=3, peak_width=13, tail_width=1,
            peak_t=0.82, curve=0.10)
