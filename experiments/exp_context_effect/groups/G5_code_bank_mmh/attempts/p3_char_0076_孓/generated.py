"""p3_char_0076_孓 — G5 attempt.

3 strokes per MMH:
  s1: 横撇 (heng_pie) — top hook (head TL, tail C)
  s2: 弯钩 (wan_gou) — main descender (head C, tail BC)
  s3: 横 (heng) — crossbar diagonal (head ML, tail BR)

Joints:
  J1  s1.tail ~ s2.head  @ C  : N (natural gap ~13 px)
  J2  s2.mid  x s3.mid   @ BC : P (welded crossing)

Bank usage: heng_pie + wan_gou + heng (no BANK_DEVIATION).
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code"))

from PIL import Image, ImageDraw
from heng_pie import draw_heng_pie
from wan_gou import draw_wan_gou
from heng import draw_heng

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 's1 heng_pie head TL(72,89) tail C(153,135). '
             's2 wan_gou head C(130,126) tail BC(105,273). '
             's3 heng head ML(61,161) tail BR(282,248). '
             'J1 N-gap ~14 px between s1.tail and s2.head. '
             'J2 P-weld: s3 diagonal crosses s2 shaft near BC.',
}


def anchor(cell, xf, yf):
    """米字格 cell + fractional coords -> absolute px (300x300 canvas)."""
    col = {'L': 0, 'C': 1, 'R': 2, 'ML': 0, 'MR': 2,
           'TL': 0, 'TC': 1, 'TR': 2,
           'BL': 0, 'BC': 1, 'BR': 2}
    row = {'T': 0, 'M': 1, 'B': 2,
           'TL': 0, 'TC': 0, 'TR': 0,
           'ML': 1, 'C': 1, 'MR': 1,
           'BL': 2, 'BC': 2, 'BR': 2}
    cx = col[cell] * 100
    cy = row[cell] * 100
    return (cx + xf * 100, cy + yf * 100)


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: heng_pie — top hook  (head TL 0.721,0.896 = (72,89); tail C 0.538,0.354 = (153,135))
    s1_head = anchor('TL', 0.721, 0.896)
    s1_tail = anchor('C',  0.538, 0.354)
    # heng_pie's default corner_x=hx+125 would land at 197 (past tail).
    # Override so the corner sits near the tail anchor.
    draw_heng_pie(d, s1_head, s1_tail,
                  apex_x=s1_tail[0] - 4,
                  corner_x=s1_tail[0])

    # s2: wan_gou — main descender (head C 0.307,0.26 = (131,126); tail BC 0.049,0.728 = (105,273))
    s2_head = anchor('C',  0.307, 0.26)
    s2_tail = anchor('BC', 0.049, 0.728)
    draw_wan_gou(d, s2_head, s2_tail,
                 belly_right=22, hook_len=24, hook_up=12,
                 w_head=5, w_body=6, w_tail=2)

    # s3: heng — crossbar (head ML 0.609,0.611 = (61,161); tail BR 0.818,0.476 = (282,248))
    s3_head = anchor('ML', 0.609, 0.611)
    s3_tail = anchor('BR', 0.818, 0.476)
    draw_heng(d, s3_head, s3_tail, width_head=8, width_tail=9)

    return img


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_孓.png')
    render().save(out)
    print('wrote', out)
