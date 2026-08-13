"""G5 attempt — p2_radical_060_宀 (3-stroke roof radical).

Strokes (MMH-derived):
  s1: 点  head ('C', 0.23, 0.195)=(123.0,119.5)  tail ('C', 0.579,0.506)=(157.9,150.6)
  s2: 点  head ('ML',0.668,0.696)=(66.8,169.6)  tail ('BL',0.536,0.253)=(53.6,225.3)
  s3: 横钩 head ('ML',0.791,0.796)=(79.1,179.6) tail ('BR',0.115,0.036)=(211.5,203.6)

Bank usage:
  - dian.py    for s1 (top 点, down-right)
  - dian.py    for s2 (left 点, down-left)
  - heng_zhe_short.py for s3 (horizontal + hook down)
"""

import sys
import pathlib

from PIL import Image, ImageDraw

_BANK = pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'
sys.path.insert(0, str(_BANK))

from dian import draw_dian
from heng_zhe_short import draw_heng_zhe_short


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: top dot, going down-right
    s1_head = (123.0, 119.5)
    s1_tail = (157.9, 150.6)
    draw_dian(d, s1_head, s1_tail, w_head=3, w_tail=8, bow=3)

    # s2: left dot, going down-left (small downward curl)
    s2_head = (66.8, 169.6)
    s2_tail = (53.6, 225.3)
    draw_dian(d, s2_head, s2_tail, w_head=3, w_tail=8, bow=-4)

    # s3: 横钩 — horizontal spanning across then hook down at right end
    s3_head = (79.1, 179.6)
    s3_tail = (211.5, 203.6)
    draw_heng_zhe_short(d, s3_head, s3_tail, corner_offset=(15, -2))

    out = pathlib.Path(__file__).with_name('01_宀.png')
    img.save(out)
    print(f'wrote {out}')


SELF_CHECK = {
    'visual_ok': None,           # filled after pass 1 by hand
    'stroke_count_ok': True,     # 3 turtle-equivalent calls (draw_dian, draw_dian, draw_heng_zhe_short)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [
        # both expected joints are N (natural gap); rendering leaves ~10-30px gap
        # because s3 starts at (79,180) while s2 head is at (67,170) — cells differ
    ],
    'overall_pass': None,
    'notes': 'Bank primitives used as-is: dian x2, heng_zhe_short for 横钩.',
}


if __name__ == '__main__':
    main()
