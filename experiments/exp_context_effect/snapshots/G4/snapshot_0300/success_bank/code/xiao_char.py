"""小 (xiǎo, "small", 3画) — Phase-3 char, B4 promotion.

Thin wrapper around mastered `xiao.py` (p2_radical_076_小). Standalone
Phase-3 char is structurally identical to the radical, so the same
TR9-expanded anchors apply directly.

Strokes: 竖钩 spine + 撇 left flank + 点 right flank.
Joints: NONE (S — three separated strokes).
"""
from xiao import draw_xiao


def draw_xiao_char(draw,
                   s1_head=('TC', 0.42, 0.25), s1_belly=('C', 0.42, 0.40),
                   s1_hook_pt=('BC', 0.42, 0.55), s1_tip=('BC', 0.05, 0.40),
                   s2_head=('ML', 0.82, 0.55), s2_tail=('BL', 0.50, 0.20),
                   s3_head=('MR', 0.10, 0.55), s3_tail=('BR', 0.55, 0.10)):
    # OVERRIDE anchors for this composition per TR1 (identical to
    # mastered xiao.py's TR9-expanded PASSed defaults; passed explicitly).
    draw_xiao(draw,
              s1_head=s1_head, s1_belly=s1_belly,
              s1_hook_pt=s1_hook_pt, s1_tip=s1_tip,
              s2_head=s2_head, s2_tail=s2_tail,
              s3_head=s3_head, s3_tail=s3_tail)
