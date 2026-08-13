"""乚 (yǐ-hook, 1画 radical, 竖弯钩 family with subtle up-tick).

RETRY 1 pass (bootstrap batch failed with plain 竖弯; the up-tick was
the fix). Uses draw_shu_wan_gou with tip mapped to MMH tail so the
tick reads intentional, not truncated.

Stroke: single compound (head → belly → corner → hook_pt → tip).
Joints: none (single continuous stroke).
"""
from shu_wan_gou import draw_shu_wan_gou


def draw_yi_hook(draw,
                 head=('TL', 0.636, 0.867),
                 belly=('ML', 0.65, 0.90),
                 corner=('BL', 0.75, 0.30),
                 hook_pt=('BR', 0.55, 0.30),
                 tip=('BR', 0.552, 0.124)):
    draw_shu_wan_gou(draw, head=head, belly=belly, corner=corner,
                     hook_pt=hook_pt, tip=tip,
                     head_w=8, belly_w=11, corner_w=11,
                     hook_start_w=9, tip_w=2)
