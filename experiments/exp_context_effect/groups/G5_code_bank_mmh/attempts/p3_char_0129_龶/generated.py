"""G5 attempt: p3_char_0129_龶.

龶 = 4 strokes:
  s1 top short heng    TL(87.6, 88.2)  -> TR(203.9, 74.1)
  s2 middle short heng C(100.8,116.3)  -> C(189.8,106.3)
  s3 short vertical    TC(130.7, 49.8) -> C(136.5,137.4)  (pokes above s1; stops short of s4 by ~11px)
  s4 long bottom heng  ML(30.8,156.2)  -> MR(269.2,136.8)

Joints:
  s1.mid X s3.mid @ TC : P (welded, cross)
  s2.mid X s3.mid @ C  : P (welded, cross)
  s3.tail ~ s4.mid @ C : N (natural gap ~11.6 px)

Bank use: heng.py + shu.py stroke primitives (no BANK_DEVIATION).
"""

import os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from heng import draw_heng
from shu import draw_shu


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 4 strokes drawn
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '3 hengs + 1 shu; vertical crosses top two hengs (P/P) and stops ~10 px above bottom heng (N).'
}


def draw(d: ImageDraw.ImageDraw):
    # s1 — top short heng (slight upward slant to right)
    draw_heng(d, head=(87.6, 88.2), tail=(203.9, 74.1),
              width_head=7, width_tail=8)

    # s2 — middle short heng (slight upward slant to right)
    draw_heng(d, head=(100.8, 116.3), tail=(189.8, 106.3),
              width_head=7, width_tail=8)

    # s3 — short vertical (from TC down through both hengs, stops above s4)
    draw_shu(d, head=(130.7, 49.8), tail=(136.5, 137.4),
             width=7, top_curl=False)

    # s4 — long bottom heng (slight upward slant to right)
    draw_heng(d, head=(30.8, 156.2), tail=(269.2, 136.8),
              width_head=9, width_tail=11)


def main():
    im = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(im)
    draw(d)
    out = os.path.join(os.path.dirname(__file__), '01_龶.png')
    im.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
