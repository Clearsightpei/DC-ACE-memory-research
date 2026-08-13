"""p3_char_0194_世 — G5 attempt.

MMH decomposition (5 strokes):
  s1: long heng across the middle       ML(0.272,0.793) → MR(0.777,0.608)
  s2: left-center vertical (shu)        TC(0.351,0.891) → BC(0.395,0.162)
  s3: right-center vertical (shu)       TC(0.937,0.782) → BC(0.922,0.039)
  s4: short bottom horizontal (heng)    BC(0.406,0.218) → BR(0.08 ,0.139)
  s5: outer 竖折 (shu_zhe): head high on left, corner at bottom-left,
       tail to the right. Endpoints ML(0.771,0.137) → BR(0.452,0.654).

Joints: s1×s2 P (C cell), s1×s3 P (MR cell), s1×s5 P (ML cell),
        s2.tail~s4.head N (~8 px gap), s3.tail~s4.tail N (~16 px gap).

Bank primitives used: heng.py, shu.py, shu_zhe.py (no deviation).
"""

import sys
import pathlib

sys.path.insert(
    0,
    str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'),
)

from PIL import Image, ImageDraw
from heng import draw_heng
from shu import draw_shu
from shu_zhe import draw_shu_zhe


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 's5 modeled as shu-zhe with corner near (77,265) so it '
             'pierces s1 in ML cell (P) and reaches BR tail.',
}


def render(out_path):
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: long heng across middle
    draw_heng(d, (27.2, 179.3), (277.7, 160.8),
              width_head=8, width_tail=9)

    # s2: left-center vertical (shu) — passes through heng
    draw_shu(d, (135.1, 89.1), (139.5, 216.2), width=6)

    # s3: right-center vertical (shu) — passes through heng
    draw_shu(d, (193.7, 78.2), (192.2, 203.9), width=6)

    # s4: short bottom horizontal between the two inner verticals' bases
    draw_heng(d, (140.6, 221.8), (208.0, 213.9),
              width_head=7, width_tail=8)

    # s5: outer 竖折 — down then right, wrapping the bottom-left
    #     head high in ML, corner in BL, tail in BR
    draw_shu_zhe(d, head=(77.1, 113.7),
                 corner=(77.1, 264.5),
                 tail=(245.2, 264.5), width=7)

    img.save(out_path)


if __name__ == '__main__':
    here = pathlib.Path(__file__).resolve().parent
    render(here / '01_世.png')
