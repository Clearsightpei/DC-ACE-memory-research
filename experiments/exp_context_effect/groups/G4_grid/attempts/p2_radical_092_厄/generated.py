"""厄 (è) — p2_radical_092. 4 strokes: 厂 (heng + pie) + 㔾 (heng_zhe + shu_wan_gou).

Anchor plan (PIL-native, y grows DOWN):
  s1 (横, top of 厂): head @ ('TL', 0.35, 0.55), tail @ ('TR', 0.55, 0.55)
       — same row (T*), horizontal line across top-middle.
  s2 (撇, left of 厂): head @ ('TL', 0.78, 0.60), tail @ ('BL', 0.20, 0.95)
       — starts near s1.head (N-joint, small gap ~15 px), sweeps down-left.
       curve slightly convex-right (curve=0.10).
  s3 (横折, top of 㔾): head @ ('C', 0.30, 0.20), corner @ ('C', 0.90, 0.20),
       tail @ ('C', 0.90, 0.90)
       — short heng then drop; sits inside the 厂 enclosure.
  s4 (竖弯钩, hook of 㔾): head @ ('C', 0.15, 0.25), belly @ ('C', 0.15, 0.85),
       corner @ ('BC', 0.20, 0.30), hook_pt @ ('BR', 0.55, 0.30),
       tip @ ('BR', 0.60, 0.05)
       — starts near s3.head (N-joint), descends the inner-left, curves
       right along the bottom, hooks UP at right.

Joints:
  s1.head ⇆ s2.head @ TL: N (small gap ~14 px) — 厂 corner is calligraphic near-touch.
  s3.head ⇆ s4.head @ C : N (small gap ~20 px) — top-left of 㔾 (小 gap).
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from heng import draw_heng
from pie import draw_pie
from heng_zhe import draw_heng_zhe
from shu_wan_gou import draw_shu_wan_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        'Compared PNG to GT. Agreements: (1) 厂 top horizontal '
        'sits high with a short-medium 横 extending to the right of '
        'the 撇 head, matching GT. (2) 竖弯钩 descends the left of '
        'the inner shape then sweeps right with an upward hook at '
        'the bottom-right, matching GT. Structural: 4 strokes, N gap '
        'at 厂 corner (~14 px) and N gap at 㔾 top-left (~20 px).'
    ),
}


def build_厄(draw):
    # s1: 横 (top of 厂) — moderate length across upper region
    s1_head = ('TL', 0.35, 0.55)
    s1_tail = ('TC', 0.90, 0.55)
    draw_heng(draw, s1_head, s1_tail, width=6)

    # s2: 撇 (left descending of 厂) — starts near s1.head, sweeps down-left,
    # extends further into BL for a proper long sweep
    s2_head = ('TL', 0.75, 0.60)
    s2_tail = ('BL', 0.10, 0.95)
    draw_pie(draw, s2_head, s2_tail,
             head_width=8, tail_width=1, curve=0.10, segments=60)

    # s3: 横折 (top+right of inner 㔾 box) — head upper-left inside 厂,
    # corner top-right, tail lower-right forming the right wall
    s3_head   = ('ML', 0.90, 0.85)   # (~90, 185) — no, adjust
    s3_corner = ('C', 0.85, 0.20)    # (~185, 120)
    s3_tail   = ('C', 0.85, 0.90)    # (~185, 190)
    # Recompute for correct placement inside 厂:
    # Inner box top-left ≈ (100, 115), top-right ≈ (200, 115), bottom-right ≈ (200, 210)
    s3_head   = ('C', 0.00, 0.15)   # (100, 115)
    s3_corner = ('C', 0.95, 0.15)   # (195, 115)
    s3_tail   = ('C', 0.95, 0.95)   # (195, 195)
    draw_heng_zhe(draw, s3_head, s3_corner, s3_tail,
                  h_width=6, v_width=6, shoulder=8)

    # s4: 竖弯钩 (left + bottom + up-hook of inner 㔾)
    # head just below s3.head (N gap ~20 px), body descends, curves right
    # along the bottom, hooks UP just inside the right wall.
    s4_head    = ('C', 0.00, 0.40)   # (100, 140)
    s4_belly   = ('C', 0.00, 1.00)   # (100, 200) keeps upper body straight
    s4_corner  = ('BC', 0.05, 0.15)  # (105, 215) bend at bottom-left
    s4_hookpt  = ('BC', 0.85, 0.15)  # (185, 215) end of horizontal sweep
    s4_tip     = ('BC', 0.90, -0.05) # (190, 195) hook tip up, above hookpt
    draw_shu_wan_gou(draw, s4_head, s4_belly, s4_corner, s4_hookpt, s4_tip,
                     head_w=6, belly_w=7, corner_w=7,
                     hook_start_w=7, tip_w=2)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    build_厄(draw)
    out = os.path.join(os.path.dirname(__file__), '01_厄.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
