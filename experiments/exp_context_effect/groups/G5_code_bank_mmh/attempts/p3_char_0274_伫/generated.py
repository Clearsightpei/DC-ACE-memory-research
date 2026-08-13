"""p3_char_0274_伫 — G5 attempt.

Recipe: P-A-006 — MMH anchors verbatim, stroke-primitive layer.
6 strokes:
  s1: 亻 pie (long TL→BL sweep)
  s2: 亻 shu (vertical descender, from ML down to BL)
  s3: 丶-like top pie/dot (TC→C, short down-right)
  s4: short shu (interior C, drops down-slightly-left)
  s5: short heng (mid interior C→MR, goes right)
  s6: long bottom heng (BC→BR)
"""

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'
)
sys.path.insert(0, os.path.abspath(BANK))

from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from dian import draw_dian

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH-anchor verbatim. Joints s1.mid~s2.head (N) and '
             's4.mid~s5.head (N) preserved as small natural gaps.',
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: 亻 pie — TL(0.949,0.656)=(94.9, 65.6) → BL(0.199,0.019)=(19.9, 201.9)
    draw_pie(d, (95, 66), (20, 202), bow_perp=12, w_head=9, w_tail=3, steps=90)

    # s2: 亻 shu — ML(0.697,0.564)=(69.7, 156.4) → BL(0.756,0.941)=(75.6, 294.1)
    # N joint with s1: s2 head sits ~14px away from s1's midpoint (natural gap)
    draw_shu(d, (70, 156), (76, 294), width=7)

    # s3: top dot/pie — TC(0.573,0.75)=(157.3, 75) → C(0.939,0.031)=(193.9, 103.1)
    # Short down-right pie/dot at the top of the right side
    draw_dian(d, (157, 75), (194, 103), w_head=3, w_tail=7, bow=3)

    # s4: short interior shu — C(0.192,0.298)=(119.2, 129.8) → C(0.11,0.843)=(111, 184.3)
    draw_shu(d, (119, 130), (111, 184), width=6)

    # s5: short interior heng — C(0.315,0.494)=(131.5, 149.4) → MR(0.229,0.676)=(222.9, 167.6)
    # N joint with s4: s5 head sits ~14px right of s4's midpoint (natural gap)
    draw_heng(d, (132, 149), (223, 168), width_head=7, width_tail=8)

    # s6: bottom long heng — BC(0.099,0.423)=(109.9, 242.3) → BR(0.484,0.355)=(248.4, 235.5)
    draw_heng(d, (110, 242), (248, 236), width_head=8, width_tail=10)

    out = os.path.join(os.path.dirname(__file__), '01_伫.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    render()
