"""尢 (yóu, "lame" as Phase-3 CHAR, 3画) — B4 main promotion.

Thin wrapper: char-context reuse of you.py (Phase-2 radical). MMH
Phase-3 anchors match the radical defaults exactly (bank was built
from this MMH profile); pass them explicitly per TR1.

Strokes: 横 + 撇 + 竖弯钩.
Joints:
  s1.mid ⇆ s2.mid  @ C — P (natural ink overlap, welded).
  s2.mid ⇆ s3.head @ C — N (~29 px gap; do NOT weld).
"""
from you import draw_you


def draw_you_lame(draw,
                  s1_head=('ML', 0.571, 0.482), s1_tail=('MR', 0.273, 0.295),
                  s2_head=('TC', 0.225, 0.691), s2_tail=('BL', 0.275, 0.915),
                  s3_head=('C', 0.465, 0.652),
                  s3_belly=('C', 0.50, 0.98),
                  s3_corner=('BC', 0.62, 0.70),
                  s3_hook_pt=('BR', 0.55, 0.60),
                  s3_tip=('BR', 0.657, 0.259)):
    draw_you(draw,
             s1_head=s1_head, s1_tail=s1_tail,
             s2_head=s2_head, s2_tail=s2_tail,
             s3_head=s3_head, s3_belly=s3_belly,
             s3_corner=s3_corner, s3_hook_pt=s3_hook_pt, s3_tip=s3_tip)
