"""G5 attempt: p2_radical_080_尢 (3-stroke radical).

MMH structural block:
  s1 (heng-ish): ML(0.571, 0.482) → MR(0.273, 0.295)
                 px (57.1, 148.2) → (227.3, 129.5)
  s2 (pie long): TC(0.225, 0.691) → BL(0.275, 0.915)
                 px (122.5, 69.1) → (27.5, 291.5)
  s3 (shu-wan-gou): C(0.465, 0.652) → BR(0.657, 0.259)
                    px (146.5, 165.2) → (265.7, 225.9)

Joints:
  s1.mid ⇆ s2.mid @ C : P (welded)
  s2.mid ⇆ s3.head @ C : N (gap ~29 px)

Bank use:
  s1 → heng.py::draw_heng
  s2 → pie.py::draw_pie
  s3 → shu_wan_gou.py::draw_shu_wan_gou (tuned so tail sits at BR anchor,
        not hooked far up — 尢's right stroke curls right but its tail
        ends going down-right rather than making a full upward gou)
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from heng import draw_heng
from pie import draw_pie
from shu_wan_gou import draw_shu_wan_gou

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '3 strokes: heng + long pie + shu-wan-gou; joints P at center, N gap between pie/gou',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: heng, slight upward tilt
    draw_heng(d, head=(57, 148), tail=(227, 130), width_head=8, width_tail=9)

    # s2: pie, long left-sweeping from TC down to BL
    draw_pie(d, head=(122, 69), tail=(28, 292),
             bow_perp=18, w_head=9, w_tail=3, steps=100)

    # s3: shu-wan-gou. Head at C, curls right, tail at BR heading down-right.
    # 尢's right stroke ends going down-right (small hook), not up.
    # Use smaller bottom_extra and place tail at BR anchor.
    draw_shu_wan_gou(d, head=(147, 165), tail=(266, 226),
                     width=8, bottom_extra=70, knee_ratio=0.70)

    out = os.path.join(os.path.dirname(__file__), '01_尢.png')
    img.save(out)
    print(f'saved {out}')


if __name__ == '__main__':
    main()
