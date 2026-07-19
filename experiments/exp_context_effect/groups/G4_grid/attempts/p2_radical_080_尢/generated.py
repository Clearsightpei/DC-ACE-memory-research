"""尢 (yóu) — 3-stroke radical.

Composition plan (per MMH-derived expectations):
  stroke 1 (横): head @ ('ML', 0.571, 0.482) → tail @ ('MR', 0.273, 0.295)
      Same row (M-row) → true horizontal (slight upward tilt is fine because
      MMH pixel coords span the same cell-row).
  stroke 2 (撇): head @ ('TC', 0.225, 0.691) → tail @ ('BL', 0.275, 0.915)
      Long diagonal sweep from upper-mid down to lower-left, thick-to-thin.
  stroke 3 (竖弯钩): 4-anchor primitive.
      head    @ ('C', 0.465, 0.652)  — top of vertical descent, MMH s3.head.
      belly   @ inline (kept on the vertical column so upper body is straight).
      corner  @ inline (bottom bend, BC/BR row).
      hook_pt @ inline (end of horizontal sweep at right side).
      tip     @ ('BR', 0.657, 0.259) — MMH s3.tail (hook flick UP).

Joints:
  s1.mid(0.43) ⇆ s2.mid(0.29) @ cell C → P (welded piercing).
  s2.mid(0.34) ⇆ s3.head       @ cell C → N (small gap ≈ 29 px, expected).

TR notes:
  TR2/TR9: standalone radical; anchors span full 米字格 (M-row across, TC→BL
           diagonal, C→BR hook) — occupies the full grid.
  TR4: joint P (s1×s2) enforced by 撇 curve control — the pie's bow places
       it near ('C', 0.30, 0.41) which is also s1's mid-band. Rendered as
       overlapping ink, no ellipse cheat needed (natural pixel overlap
       where line-width 10 × line-width ~7 both cover the crossing point).
  TR10: s2/s3 joint is N-class ≈ 29 px — verified acceptable natural gap;
        do NOT weld.
  TR12: s1 (横) head & tail both in M-row (ML, MR) ✓ true horizontal.
"""

SELF_CHECK = {
    # Visual agreements between attempt-1 PNG and GT:
    #   (a) both have a long 撇 sweep from upper-mid down to lower-left,
    #       crossing the top 横 near the heng's left third.
    #   (b) both have a 竖弯钩 that descends from the middle, curves right
    #       across the bottom, and hooks UP at the far right.
    # Attempt-1 defects fixed in this revision:
    #   - Pie was nearly straight (curve=0.06); GT shows a more pronounced
    #     convex-right bow. Bumped curve to 0.09.
    #   - Shu_wan_gou corner was very angular; softened bend by moving
    #     `belly` down and `corner` a touch lower/inward for smoother arc.
    'visual_ok': True,
    'stroke_count_ok': True,     # 3 primitive calls == 3 MMH strokes
    'endpoint_mismatches': [],   # anchors match MMH within tolerance
    'joint_class_mismatches': [], # s1×s2 P (natural overlap at C),
                                   # s2/s3 N (~30px gap at C) — implemented
    'overall_pass': True,
    'notes': 'revision 1: bumped pie curve, softened shu_wan_gou knee',
}

import os
import sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width  # noqa
from heng import draw_heng  # noqa
from pie import draw_pie   # noqa
from shu_wan_gou import draw_shu_wan_gou  # noqa


def draw_you_lame(draw):
    # --- stroke 1: 横 ---
    draw_heng(draw,
              from_anchor=('ML', 0.571, 0.482),
              to_anchor=('MR', 0.273, 0.295),
              width=7)

    # --- stroke 2: 撇 ---
    # Long sweep from upper-mid down to bottom-left. Slight curve so mid
    # passes near ('C', 0.304, 0.41) to weld with heng.
    draw_pie(draw,
             from_anchor=('TC', 0.225, 0.691),
             to_anchor=('BL', 0.275, 0.915),
             head_width=10, tail_width=2,
             curve=0.09, segments=60)

    # --- stroke 3: 竖弯钩 ---
    # 4-anchor primitive: head, belly, corner, hook_pt, tip.
    # Start at ('C', 0.465, 0.652) — near s2 body but slightly right & down (N-gap).
    # Descend vertically on the column near x = 146 px, bend at bottom, sweep
    # right, hook up to ('BR', 0.657, 0.259).
    draw_shu_wan_gou(draw,
                     head=('C', 0.465, 0.652),
                     belly=('C', 0.50, 0.98),           # keep vertical column ~150px, bend low
                     corner=('BC', 0.62, 0.70),         # smoother bend at (162, 270)
                     hook_pt=('BR', 0.55, 0.60),        # (255, 260) end of horizontal
                     tip=('BR', 0.657, 0.259),          # MMH tail — hook flick up
                     head_w=9, belly_w=11, corner_w=10,
                     hook_start_w=9, tip_w=2)


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_you_lame(draw)
    out = os.path.join(HERE, '01_尢.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
