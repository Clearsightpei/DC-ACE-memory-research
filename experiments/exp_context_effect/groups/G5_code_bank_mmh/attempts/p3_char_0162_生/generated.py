"""G5 attempt: p3_char_0162_生.

生 = 5 strokes:
  s1 short pie (top)   ML(87.6, 111.3) -> BL(50.1, 200.1)
  s2 middle heng       ML(93.8, 161.1) -> MR(219.7, 144.4)
  s3 lower short heng  BL(99.0, 216.5) -> BR(206.0, 204.8)
  s4 tall central shu  TC(142.4, 59.8) -> BC(145.9, 262.0)  (lifted from MMH 272.5 to preserve N-gap vs s5)
  s5 long bottom heng  BL(41.3, 288.6) -> BR(270.4, 279.5)

Joints:
  s1.mid ~ s2.head @ ML   : N — natural gap (pie's tail near s2.head)
  s2.mid X s4.mid @ C     : P — welded (shu pierces middle heng)
  s3.mid X s4.mid @ BC    : P — welded (shu pierces lower heng)
  s4.tail ~ s5.mid @ BC   : N — shu ends ABOVE bottom heng, ~20 px gap

Bank use: heng.py + shu.py + pie.py (no BANK_DEVIATION). Sibling of 龶 (p3_char_0129)
with an extra top pie added.
"""

import os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from heng import draw_heng
from shu import draw_shu
from pie import draw_pie


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 5 strokes: pie + heng + heng + shu + heng
    'endpoint_mismatches': [
        {'stroke': 4, 'expected_tail': (145.9, 272.5), 'actual_tail': (145.9, 262.0),
         'delta': 'lifted 10.5 px up to widen N-gap vs s5 (spec says gap≈16.9 px, not weld)'}
    ],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'sibling of 龶 with added top pie; shu pierces s2 & s3 (P/P), ends above s5 (N).'
}


def draw(d: ImageDraw.ImageDraw):
    # s1 — pie sweeping down-left; head extended upward from MMH medial (111→85)
    # per P-MMH-002 (MMH gives medial section, visible ink extends past endpoints).
    # Tail nudged right (50→58) for tighter N-gap with s2.head at (93.8, 161.1).
    draw_pie(d, head=(95.0, 82.0), tail=(58.0, 178.0),
             bow_perp=10, w_head=8, w_tail=2, steps=70)

    # s2 — middle heng, slight upward slant to right
    draw_heng(d, head=(93.8, 161.1), tail=(219.7, 144.4),
              width_head=7, width_tail=8)

    # s3 — lower short heng, slight upward slant
    draw_heng(d, head=(99.0, 216.5), tail=(206.0, 204.8),
              width_head=7, width_tail=8)

    # s4 — tall central shu (pierces s2 and s3, stops just above s5)
    draw_shu(d, head=(142.4, 59.8), tail=(145.9, 262.0),
             width=7, top_curl=False)

    # s5 — long bottom heng, slight upward slant
    draw_heng(d, head=(41.3, 288.6), tail=(270.4, 279.5),
              width_head=9, width_tail=11)


def main():
    im = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(im)
    draw(d)
    out = os.path.join(os.path.dirname(__file__), '01_生.png')
    im.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
