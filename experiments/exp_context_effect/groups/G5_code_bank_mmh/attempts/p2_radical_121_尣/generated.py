"""G5 attempt: p2_radical_121_尣 (4-stroke radical, variant of 尢).

MMH structural block:
  s1 (small pie top-left):   TL(0.762, 0.756) -> ML(0.542, 0.271)
                             px (76.2, 75.6) -> (54.2, 127.1)
  s2 (small dian top-right): TC(0.746, 0.677) -> MR(0.156, 0.075)
                             px (174.6, 67.7) -> (215.6, 107.5)
  s3 (long pie down-left):   ML(0.914, 0.356) -> BL(0.311, 0.903)
                             px (91.4, 135.6) -> (31.1, 290.3)
  s4 (shu-wan-gou):          C(0.491, 0.113) -> BR(0.704, 0.265)
                             px (149.1, 111.3) -> (270.4, 226.5)

Joints: NONE (all four strokes visually separate; N-class throughout).

Bank use:
  s1 -> pie.py::draw_pie (short, mild bow)
  s2 -> dian.py::draw_dian (short down-right tapered)
  s3 -> pie.py::draw_pie (long left-sweeping)
  s4 -> shu_wan_gou.py::draw_shu_wan_gou (tuned so tail lands at BR anchor,
        not a huge upward hook — 尢-family right stroke curls right and
        finishes going up only slightly)
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from pie import draw_pie
from dian import draw_dian
from shu_wan_gou import draw_shu_wan_gou

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 strokes drawn matches expected 4
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '4 strokes: small pie TL, small dian TC->MR, long pie ML->BL, shu-wan-gou C->BR',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: small top-left pie, mostly vertical, slight left-ward drift
    draw_pie(d, head=(76, 76), tail=(54, 127),
             bow_perp=6, w_head=7, w_tail=3, steps=50)

    # s2: small top dian-like stroke going down-right (TC -> MR)
    draw_dian(d, head=(175, 68), tail=(216, 108),
              w_head=3, w_tail=7, bow=3, steps=48)

    # s3: long left-sweeping pie from ML down to BL
    draw_pie(d, head=(91, 136), tail=(31, 290),
             bow_perp=20, w_head=9, w_tail=3, steps=100)

    # s4: shu-wan-gou from C down and to BR (small hook-up, tail at BR)
    draw_shu_wan_gou(d, head=(149, 111), tail=(270, 226),
                     width=8, bottom_extra=65, knee_ratio=0.72)

    out = os.path.join(os.path.dirname(__file__), '01_尣.png')
    img.save(out)
    print(f'saved {out}')


if __name__ == '__main__':
    main()
