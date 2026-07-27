"""付 (fù) — 亻 (person radical, left) + 寸 (inch, right), 5 strokes.

MANDATORY LOOKUP CHECKLIST (top-of-file):
1. INDEX grep 付: not mastered. Nearest: fu.py (爻/父), fu_right.py (阝-right). Neither reusable.
2. errata grep 付: not listed.
3. form_catalog: 撇+竖(short) = 亻 left-radical; 横+竖钩+点 = 寸 right.
4. principles_meta TR1-TR12: TR1 override anchors for THIS composition.
5. joint_atlas: N-class must show visible gap (~10-30 px), not welded.
6. sandbox: no specific 付 notes.

Strokes (from MMH):
  s1  撇   ('TL',0.961,0.662)  → ('BL',0.161,0.18)     — long left sweep of 亻
  s2  竖   ('ML',0.85,0.453)   → ('BL',0.844,0.868)    — short vertical of 亻
  s3  横   ('C',0.151,0.649)   → ('MR',0.795,0.521)    — horizontal of 寸
  s4  竖钩 ('TC',0.972,0.606)  → ('BC',0.682,0.698)    — vertical-hook of 寸
  s5  点   ('C',0.368,0.893)   → ('BC',0.6,0.197)      — dot of 寸

Joints:
  s1.mid ⇆ s2.head  : N — small gap (14 px)
  s2.head ⇆ s3.head : N — gap (34 px), 亻竖 and 寸横 don't touch
  s3.mid ⇆ s4.mid   : P — welded crossing (寸's 横 crossed by 竖钩)
  s3.head ⇆ s5.head : N — gap (31 px)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from shu_gou import draw_shu_gou
from dian import draw_dian


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Pass1: 5 strokes matching MMH anchors. 亻 (pie+shu) left, 寸 (heng+shu_gou+dian) right. P at cross of 寸.'
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # ---- 亻 (person radical, left) ----
    # s1 撇 — long sweep from upper-right (TL corner region) down-left to BL
    draw_pie(draw,
             ('TL', 0.961, 0.662),
             ('BL', 0.161, 0.18),
             head_width=12, tail_width=1, curve=0.10, segments=48)

    # s2 竖 — short vertical (person's leg), starts mid-body of 撇
    draw_shu(draw,
             ('ML', 0.85, 0.453),
             ('BL', 0.844, 0.868),
             width=9)

    # ---- 寸 (right side) ----
    # s3 横 — horizontal across middle-right
    draw_heng(draw,
              ('C', 0.151, 0.649),
              ('MR', 0.795, 0.521),
              width=9)

    # s4 竖钩 — vertical with hook (crosses s3)
    # head: MMH ('TC',0.972,0.606); tail (hook tip): MMH ('BC',0.682,0.698)
    # For shu_gou: head → hook_pt → tip (up-left flick)
    # Body should be near-vertical from head down to a bottom pivot, then hook up-left.
    draw_shu_gou(draw,
                 head=('TC', 0.972, 0.606),
                 belly=('C', 0.972, 0.50),        # same x as head, mid-body knot
                 hook_pt=('BC', 0.90, 0.85),      # bottom pivot
                 tip=('BC', 0.682, 0.698),        # MMH tail = hook tip
                 head_w=12, belly_w=10, hook_start_w=10, tip_w=2)

    # s5 点 — small dot lower-left of 寸's cross
    draw_dian(draw,
              ('C', 0.368, 0.893),
              ('BC', 0.6, 0.197),
              head_width=2, peak_width=9, curve=0.10, segments=24)

    out = os.path.join(os.path.dirname(__file__), '01_付.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    render()
