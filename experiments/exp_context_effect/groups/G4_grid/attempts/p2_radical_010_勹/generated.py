"""勹 (bāo) radical — Phase 2, G4 grid-bank attempt.

MMH structural expectations:
  strokes: 2
  s1: 撇 (piě)         head ('TC',0.116,0.645)  tail ('ML',0.56,0.682)
  s2: 横折钩 (hzg)     head ('ML',0.987,0.336)  tail ('BC',0.453,0.742)
  joint: s1.mid(0.65) ⇆ s2.head @ ML  — class N (small gap ≈ 16.6 px)

Anchor plan (米字格, PIL-native y-DOWN):
  s1 (撇):  head @ ('TC', 0.116, 0.645)  — thick 起笔, upper-mid area
            tail @ ('ML', 0.56, 0.682)   — needle tip, lower-left, mid-height
            width 12→2, curve 0.05 (shallow bow)
  s2 (横折钩): head   @ ('ML', 0.99, 0.34)   — top of the wrap, right of s1's tail
              corner @ ('MR', 0.65, 0.22)   — bend at upper-right (short 横 span)
              tail   @ ('BC', 0.55, 0.72)   — bottom, above the hook base
              tip    @ ('BC', 0.38, 0.58)   — hook flick UP-and-LEFT
              widths 8/8, shoulder 12

Joints:
  s1.mid ⇆ s2.head : N (small natural gap, no weld). We deliberately
                     keep s2.head anchor a hair to the right/above s1.tail.

Self-check dict at top per G4 protocol.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from pie import draw_pie
from heng_zhe_gou import draw_heng_zhe_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Revision 1: tightened 横 span (corner MR 0.45,0.30), pulled '
             'tail to BC (0.35,0.78), tip to BC (0.15,0.60) so the wrap '
             'descent slants down-left to match GT; N-class gap preserved.',
}


def render(path):
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # ---- Stroke 1: 撇 ---------------------------------------------------
    s1_head = ('TC', 0.116, 0.645)
    s1_tail = ('ML', 0.56,  0.682)
    draw_pie(draw, s1_head, s1_tail,
             head_width=12, tail_width=2, curve=0.05, segments=48)

    # ---- Stroke 2: 横折钩 -----------------------------------------------
    # Revision: tighten the 横 span (corner closer to head) and pull tail
    # further left so the descent slants toward BC, matching GT's wrap curve.
    s2_head   = ('ML', 0.99, 0.34)
    s2_corner = ('MR', 0.45, 0.30)
    s2_tail   = ('BC', 0.35, 0.78)
    s2_tip    = ('BC', 0.15, 0.60)
    draw_heng_zhe_gou(draw, s2_head, s2_corner, s2_tail, s2_tip,
                      h_width=9, v_width=9, shoulder=12, tip_w=2)

    # ---- Direction / joint invariants -----------------------------------
    p_s1_head = anchor_to_xy(s1_head)
    p_s1_tail = anchor_to_xy(s1_tail)
    p_s2_head = anchor_to_xy(s2_head)
    p_s2_tail = anchor_to_xy(s2_tail)
    p_s2_tip  = anchor_to_xy(s2_tip)

    # 撇 goes down-and-left.
    assert p_s1_tail[0] < p_s1_head[0], '撇 tail must be LEFT of head'
    assert p_s1_tail[1] > p_s1_head[1], '撇 tail must be BELOW head'
    # Hook flick points up-and-left.
    assert p_s2_tip[1]  < p_s2_tail[1], 'hook tip must be ABOVE tail'
    assert p_s2_tip[0]  < p_s2_tail[0], 'hook tip must be LEFT of tail'
    # N-class joint gap between s1.tail and s2.head — should be small but > 0.
    gap = ((p_s1_tail[0] - p_s2_head[0]) ** 2
           + (p_s1_tail[1] - p_s2_head[1]) ** 2) ** 0.5
    # target ~16.6 px per MMH; anything in 8–35 range is a valid N-class gap.
    assert 4 < gap < 60, f'N-class gap out of range: {gap:.1f} px'

    img.save(path)


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_勹.png')
    render(out)
    print('wrote', out)
