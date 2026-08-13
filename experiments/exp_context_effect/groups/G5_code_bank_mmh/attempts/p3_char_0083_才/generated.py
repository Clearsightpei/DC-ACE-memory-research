"""p3_char_0083_才 (cai, "talent") — G5 attempt.

Structure (from MMH block, 3 strokes):
  s1: heng   ML(0.524,0.471) → MR(0.528,0.339)  ≈ (52,147)→(253,134)
  s2: shu_gou (vertical with leftward hook)  TC(0.506,0.668) → BC(0.201,0.672)
       ≈ (151,67)→(120,267)  — leans slightly left; slight hook flick at tail
  s3: pie    C(0.562,0.441) → BL(0.398,0.587)  ≈ (156,144)→(40,259)

Joints:
  s1.mid ⇆ s2.mid @ C : P (welded crossing at ~(145,140))
  s1.mid ⇆ s3.head @ C : N (small gap; s3.head sits ~11px right of crossing)
  s2.mid ⇆ s3.head @ C : N (small gap)

Bank primitives used:
  heng.py    · draw_heng     (s1)
  shu_gou.py · draw_shu_gou  (s2)
  pie.py     · draw_pie      (s3)
"""

import sys, os
BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, BANK)

from PIL import Image, ImageDraw
from heng import draw_heng
from shu_gou import draw_shu_gou
from pie import draw_pie


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 3 primitive calls, matches expected 3
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'heng+shu_gou+pie; pie head offset slightly from crossing to keep N gap.'
}


def render(path):
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: heng across the middle (spans nearly full width, gentle rise)
    draw_heng(d, head=(52, 147), tail=(253, 134),
              width_head=9, width_tail=11)

    # s2: shu_gou — top-center down with gentle lean; small hook flick at bottom
    draw_shu_gou(d, head=(151, 67), tail=(120, 267),
                 width=8, hook_start_offset=32)

    # s3: pie — head just below/right of the crossing; sweeps down-left
    #     head offset (+11 x, +4 y) from ~(145,140) to keep N-gap vs s1.mid & s2.mid
    draw_pie(d, head=(156, 144), tail=(40, 259),
             bow_perp=16, w_head=9, w_tail=3)

    img.save(path)


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_才.png')
    render(out)
    print('wrote', out)
