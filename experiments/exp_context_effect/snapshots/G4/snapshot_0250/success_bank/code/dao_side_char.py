"""刂 (dāo, 2画) — Phase-3 char, B4 promotion.

Thin wrapper around mastered `dao_side.py` (p2_radical). Same composition
as the radical: 短竖 (left, thin partner) + 竖钩 (right, tall, hook up-left).
Post-fix invariant: hook_pt.x == head.x_frac so 竖钩 body stays vertical (TR8).

Joints: NONE (~50 px horizontal gap between the two verticals).
"""
from dao_side import draw_dao_side


def draw_dao_side_char(draw,
                       s1_head=('C', 0.113, 0.16), s1_tail=('C', 0.113, 0.90),
                       s2_head=('TC', 0.614, 0.712),
                       s2_belly=('C', 0.614, 0.50),
                       s2_hook_pt=('BC', 0.614, 0.90),
                       s2_tip=('BC', 0.35, 0.60)):
    # OVERRIDE anchors for this composition per TR1.
    draw_dao_side(draw,
                  s1_head=s1_head, s1_tail=s1_tail,
                  s2_head=s2_head, s2_belly=s2_belly,
                  s2_hook_pt=s2_hook_pt, s2_tip=s2_tip)
