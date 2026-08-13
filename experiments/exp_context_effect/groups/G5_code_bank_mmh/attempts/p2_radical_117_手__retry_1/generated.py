"""p2_radical_117_手 — RETRY 1 — 4-stroke radical.

TRAJECTORY DIFF (vs main attempt, verdict C):
  main attempt 01_手.png shows:
    - s1 top stroke: broad flat pie with only mild upward arch (bow_perp=10).
      In the GT the s1 stroke is a much more distinctly arched compact curl,
      with the head clearly higher (curling up) and the tail sweeping down-left.
      Errata explicitly notes: 's1 top hook is a compact curl NOT a pie',
      and 'shu_gou head at TC(139,92) sits INSIDE the top curve loop; ensure
      curve wraps above it'. In main attempt s1's arch was too weak so s4's
      head at (139,92) is essentially co-linear with s1, not tucked under.
    - s4 vertical: hook was subtle, GT hook is clearer leftward curl at tail.

  Fixes this attempt:
    1. bow_perp on s1 increased 10 → 26 so the pie curves noticeably above
       its endpoint midline — the resulting arc will pass well above
       s4.head=(139,92), matching the GT "curve wraps above s4 head" note.
    2. shu_gou hook_start_offset kept generous (48) for a clean hook.
    3. Endpoints unchanged (MMH-derived anchors are correct).

MMH structural expectations:
  s1: TR(0.039, 0.724) -> TL(0.92, 0.979)      (204, 72)  -> (92, 98)   top curl
  s2: ML(0.935, 0.351) -> MR(0.051, 0.213)     (94, 135)  -> (205, 121) upper short heng
  s3: ML(0.325, 0.939) -> MR(0.713, 0.793)     (33, 194)  -> (271, 179) long middle heng
  s4: TC(0.389, 0.92)  -> BC(0.09, 0.763)      (139, 92)  -> (109, 276) shu_gou

Joints:
  s1.mid65 ~ s4.head  @ TC : N (small ~11px gap - natural, no weld)
  s2.mid55 ~ s4.mid17 @ C  : P (piercing — computed intersection ~ (133, 130))
  s3.mid54 ~ s4.mid38 @ C  : P (piercing — computed intersection ~ (123, 188))
"""

import sys
import pathlib

from PIL import Image, ImageDraw

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from pie import draw_pie
from heng import draw_heng
from shu_gou import draw_shu_gou


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- MMH-derived anchors (px) ----
    s1_head, s1_tail = (204, 72), (92, 98)
    s2_head, s2_tail = (94, 135), (205, 121)
    s3_head, s3_tail = (33, 194), (271, 179)
    s4_head, s4_tail = (139, 92), (109, 276)

    # ---- s1: top curled pie — stronger upward arch so the curve wraps
    #        above s4.head=(139,92) (see retry hint).
    draw_pie(d, s1_head, s1_tail, bow_perp=26, w_head=8, w_tail=4, steps=80)

    # ---- s2: upper short heng ----
    draw_heng(d, s2_head, s2_tail, width_head=8, width_tail=9)

    # ---- s3: long middle heng ----
    draw_heng(d, s3_head, s3_tail, width_head=9, width_tail=10)

    # ---- s4: shu_gou (vertical body with clear leftward hook at tail) ----
    draw_shu_gou(d, s4_head, s4_tail, width=8, hook_start_offset=48)

    out = pathlib.Path(__file__).parent / '01_手.png'
    img.save(out)
    return out


SELF_CHECK = {
    'visual_ok': None,           # filled after render/compare
    'stroke_count_ok': True,     # 4 primitives called: pie, heng, heng, shu_gou
    'endpoint_mismatches': [],   # anchors mirror MMH exactly (within ±0.2)
    'joint_class_mismatches': [
        # s1↔s4 N: with bow_perp=26 the arc peaks well above s4.head — natural N gap preserved.
        # s2↔s4 P: piercing intersection near (133, 130), inside cell C.
        # s3↔s4 P: piercing intersection near (123, 188), inside cell C.
    ],
    'overall_pass': None,
    'notes': 'Retry: increased s1 bow_perp 10→26 to make top stroke a compact upward curl (per errata hint).',
}


if __name__ == '__main__':
    p = render()
    print('wrote', p)
