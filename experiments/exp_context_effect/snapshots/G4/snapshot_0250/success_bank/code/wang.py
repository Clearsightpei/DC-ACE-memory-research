"""p2_radical_122_王 — 王 (wáng, "king", 4画).

3 same-row 横 + centered 竖 spine (十-family + extra bars).

Joints:
  s1.mid ⇆ s3.head @ C : N (small gap ~18 px — spine top hangs just below top 横)
  s2.mid ⇆ s3.mid @ C  : P (welded — spine pierces mid 横)
  s3.tail ⇆ s4.mid @ BC : N (small gap ~18 px — spine bottom hangs just above bot 横)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from _anchor import anchor_to_xy, fat_line

DEFAULTS = {
    's1_h': ('ML', 0.87, 0.05), 's1_t': ('TR', 0.17, 0.94),   # top 横
    's2_h': ('ML', 0.97, 0.85), 's2_t': ('MR', 0.07, 0.75),   # mid 横 (shorter)
    's3_h': ('C',  0.40, 0.14), 's3_t': ('BC', 0.44, 0.52),   # 竖 spine
    's4_h': ('BL', 0.36, 0.66), 's4_t': ('BR', 0.71, 0.64),   # bot 横 (widest)
}


def draw_wang(draw, **overrides):
    p = {**DEFAULTS, **overrides}
    fat_line(draw, anchor_to_xy(p['s1_h']), anchor_to_xy(p['s1_t']), width=9)
    fat_line(draw, anchor_to_xy(p['s2_h']), anchor_to_xy(p['s2_t']), width=9)
    fat_line(draw, anchor_to_xy(p['s3_h']), anchor_to_xy(p['s3_t']), width=9)
    fat_line(draw, anchor_to_xy(p['s4_h']), anchor_to_xy(p['s4_t']), width=10)
