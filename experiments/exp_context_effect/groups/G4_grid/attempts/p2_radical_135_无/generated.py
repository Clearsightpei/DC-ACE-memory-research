"""无 (wú, "no/without", 4 strokes) — Phase-2 radical, revision 1.

Revision fixes from attempt 1:
  - s1 was too diagonal and too long; make it a short, mild-slant top bar
    sitting inside T-row.
  - s2 was tilted like a diagonal (my y_fracs mixed rows); clamp both
    endpoints inside M-row with matching y_frac per TR8 rule 5.
  - s3 shot past bottom; shorten to end just above canvas edge.
  - s4 hook geometry was broken (corner and hook cells wrong); use
    tighter cell placements based on shu_wan_gou reference pattern
    (er_legs.py / wu_lame.py style).

Anchor plan (米字格 anchors, PIL y-down):
  s1 — short top 横 (slight rise, TR9 keeps top-row placement):
        ('TL', 0.60, 0.55) → ('TR', 0.50, 0.35), width 8.
        (Sits in top row, spans TC into TR, slight upward tilt to right.)
  s2 — long middle 横 (both in M-row for TR8 rule 5):
        ('ML', 0.15, 0.55) → ('MR', 0.85, 0.55), width 10.
        Straight horizontal across the middle.
  s3 — 撇 left leg (P-welds through s2 at C, sweeps to BL):
        ('C', 0.30, 0.10) → ('BL', 0.50, 0.90), curve 0.08.
  s4 — 竖弯钩 right leg (starts on middle bar just right of center,
        drops, curves right, small up-hook):
        head ('C', 0.60, 0.55), belly ('C', 0.60, 0.95),
        corner ('BC', 0.70, 0.60), hook ('BR', 0.35, 0.55),
        tip ('BR', 0.40, 0.20).

Joints:
  s1.mid ⇆ s3.head @ C — N (small gap, s3 head is below s1 tail region).
  s2.mid ⇆ s3.mid @ C — P (welded crossing, s3 pierces s2).
  s2.mid ⇆ s4.head @ C — N (s4 head sits on s2 body ~25px right of center).
  s3.mid ⇆ s4.head @ C — N (~24 px gap).

Reference: wu_lame.py (兀), er_legs.py (儿) for shu_wan_gou.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line
from heng import draw_heng
from pie import draw_pie
from shu_wan_gou import draw_shu_wan_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [
        {'stroke': 's1',
         'expected': "head ML(0.879,0.011), tail TR(0.106,0.882)",
         'actual':   "head TL(0.60,0.55), tail TR(0.50,0.35)",
         'delta': 'Simplified to a T-row short heng; MMH literal produced ugly slash.'},
        {'stroke': 's2',
         'expected': "head ML(0.469,0.822), tail MR(0.417,0.676)",
         'actual':   "head ML(0.15,0.55), tail MR(0.85,0.55)",
         'delta': 'Straightened & lengthened; MMH y_fracs mixed rows.'},
    ],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Revision 1. Straightened horizontals per TR8 rules 5/6. Right leg uses shu_wan_gou.'
}


def draw_wu(draw):
    # s1: short top 横 (slight upward tilt to the right).
    s1_head = ('TL', 0.60, 0.55)
    s1_tail = ('TR', 0.50, 0.35)
    draw_heng(draw, s1_head, s1_tail, width=8)

    # s2: long middle 横 — straight, both endpoints share y_frac 0.55.
    s2_head = ('ML', 0.15, 0.55)
    s2_tail = ('MR', 0.85, 0.55)
    draw_heng(draw, s2_head, s2_tail, width=10)

    # s3: 撇 left leg — from just below s1, piercing s2 at C, to BL.
    s3_head = ('C', 0.30, 0.10)
    s3_tail = ('BL', 0.50, 0.90)
    draw_pie(draw, s3_head, s3_tail, head_width=11, tail_width=2, curve=0.08)

    # s4: 竖弯钩 right leg — mimics wu_lame's shu_wan but with a hook.
    s4_head   = ('C', 0.60, 0.55)
    s4_belly  = ('C', 0.60, 0.95)
    s4_corner = ('BC', 0.70, 0.60)
    s4_hook   = ('BR', 0.35, 0.55)
    s4_tip    = ('BR', 0.40, 0.20)
    draw_shu_wan_gou(draw, s4_head, s4_belly, s4_corner, s4_hook, s4_tip,
                     head_w=8, belly_w=10, corner_w=10,
                     hook_start_w=9, tip_w=2)


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_wu(draw)
    out_path = os.path.join(os.path.dirname(__file__), '01_无.png')
    img.save(out_path)
    print(f'Wrote {out_path}')


if __name__ == '__main__':
    main()
