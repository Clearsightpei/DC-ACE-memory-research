"""小 (xiǎo, "small", 3 strokes) — B2 pass.

Strokes:
  s1 — 竖钩 (center spine + up-left hook).
  s2 — 撇 (left flank).
  s3 — 点 (right flank, sloping down-right).

Joints: NONE (S — all three separated).

TR9 note: MMH under-spans the spine; head raised to TC(0.42,0.25),
hook to BC(0.42,0.55) so the hook flick reads clearly.
"""
from shu_gou import draw_shu_gou
from pie import draw_pie
from dian import draw_dian


def draw_xiao(draw,
              s1_head=('TC', 0.42, 0.25), s1_belly=('C', 0.42, 0.40),
              s1_hook_pt=('BC', 0.42, 0.55), s1_tip=('BC', 0.05, 0.40),
              s2_head=('ML', 0.82, 0.55), s2_tail=('BL', 0.50, 0.20),
              s3_head=('MR', 0.10, 0.55), s3_tail=('BR', 0.55, 0.10)):
    draw_shu_gou(draw, s1_head, s1_belly, s1_hook_pt, s1_tip,
                 head_w=11, belly_w=13, hook_start_w=11, tip_w=2)
    draw_pie(draw, s2_head, s2_tail, head_width=10, tail_width=1, curve=0.10)
    draw_dian(draw, s3_head, s3_tail, head_width=2, peak_width=10, curve=0.06)
