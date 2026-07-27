"""巳 (sì, 3 strokes) — B2 pass.

3-stroke small seal-like radical: top 横折 (short bracket), middle 横 (bar),
and long 竖弯钩 outer bowl. All joints N (natural gaps).

Strokes:
  s1 — 横折 (small top bracket, TL/C region).
  s2 — 横 (middle bar).
  s3 — 竖弯钩 (outer bowl, sweeps left-down-right-up).

Joints:
  s1.tail ⇆ s2.mid @ C            — N.
  s1.head ⇆ s3.head @ ML          — N.
  s2.head ⇆ s3.mid @ ML           — N.

Note: file named `si.py` for consistency with pinyin slug. Not to be
confused with `si_private.py` (厶) — different character entirely.
"""
from heng_zhe import draw_heng_zhe
from heng import draw_heng
from shu_wan_gou import draw_shu_wan_gou


def draw_si_snake(draw,
                  s1_head=('C', 0.02, 0.10),
                  s1_corner=('C', 0.65, 0.10),
                  s1_tail=('C', 0.65, 0.45),
                  s2_head=('C', 0.35, 0.55), s2_tail=('C', 0.80, 0.55),
                  s3_head=('ML', 0.80, 0.05),
                  s3_belly=('C', 0.05, 0.55),
                  s3_corner=('BL', 0.95, 0.10),
                  s3_hook_pt=('BR', 0.15, 0.05),
                  s3_tip=('MR', 0.15, 0.75)):
    draw_heng_zhe(draw, s1_head, s1_corner, s1_tail,
                  h_width=8, v_width=8, shoulder=10)
    draw_heng(draw, s2_head, s2_tail, width=7)
    draw_shu_wan_gou(draw, s3_head, s3_belly, s3_corner, s3_hook_pt, s3_tip,
                     head_w=8, belly_w=11, corner_w=11,
                     hook_start_w=9, tip_w=2)
