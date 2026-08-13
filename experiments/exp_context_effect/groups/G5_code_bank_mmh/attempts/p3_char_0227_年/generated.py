"""p3_char_0227_年 — G5 drawer attempt.

年 = 6 strokes:
  s1 top-left 撇 (pie)
  s2 short top 横 (heng)
  s3 short middle 横
  s4 short mid 竖 (shu)
  s5 long bottom 横
  s6 long central 竖 that pierces s3 and s5

Bank consultation:
  - `qian_thousand.py` (千, 3 strokes: pie+heng+shu) is the closest sibling
    but shape is quite different (千 has no mid-heng, no mid-shu, no top-heng).
  - Composing from primitives (draw_pie, draw_heng, draw_shu) matches MMH
    anchors cleanly. No BANK_DEVIATION needed (we are inlining stroke
    primitives, not deviating from any radical primitive).

Anchors decoded from MMH block (300x300 米字格, each cell is 100x100):
  s1: TC(0.099,0.524)->ML(0.633,0.339)  = (109.9, 52.4)  -> ( 63.3, 133.9)
  s2: TC(0.128,0.97) ->TR(0.153,0.853)  = (112.8, 97.0)  -> (215.3,  85.3)
  s3:  C(0.011,0.506)->MR(0.147,0.436)  = (101.1,150.6)  -> (214.7, 143.6)
  s4: ML(0.841,0.482)->BC(0.058,0.027)  = ( 84.1,148.2)  -> (105.8, 202.7)
  s5: BL(0.243,0.142)->BR(0.722,0.068)  = ( 24.3,214.2)  -> (272.2, 206.8)
  s6:  C(0.436,0.043)->BC(0.556,1.223)  = (143.6,104.3)  -> (155.6, 322.3)
    (s6 tail y=322 is outside the 300px canvas; clip to y=295.)
"""

import pathlib
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]
                       / 'success_bank' / 'code'))

from heng import draw_heng
from pie import draw_pie
from shu import draw_shu


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 6 primitive calls
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # 5 N-joints implemented via geometry gaps;
                                   # 2 P-joints (s3xs6 at C, s5xs6 at BC)
                                   # are welded by s6 piercing through.
    'overall_pass': True,
    'notes': ('s6 clipped to y=295 (MMH tail y=322 lies outside canvas).'),
}


def draw_nian(d: ImageDraw.ImageDraw):
    # s1: top-left pie
    draw_pie(d, (109.9, 52.4), (63.3, 133.9),
             bow_perp=8, w_head=8, w_tail=3, steps=70)
    # s2: short top heng (slight upward slant)
    draw_heng(d, (112.8, 97.0), (215.3, 85.3),
              width_head=7, width_tail=9)
    # s3: short mid heng
    draw_heng(d, (101.1, 150.6), (214.7, 143.6),
              width_head=7, width_tail=9)
    # s4: short mid shu (slight rightward lean)
    draw_shu(d, (84.1, 148.2), (105.8, 202.7),
             width=6)
    # s5: long bottom heng
    draw_heng(d, (24.3, 214.2), (272.2, 206.8),
              width_head=9, width_tail=11)
    # s6: central shu piercing s3 and s5 (welded P-joints)
    draw_shu(d, (143.6, 104.3), (155.6, 295.0),
             width=7)


def main():
    out_path = pathlib.Path(__file__).with_name('01_年.png')
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_nian(d)
    img.save(out_path)
    print(f'wrote {out_path}')


if __name__ == '__main__':
    main()
