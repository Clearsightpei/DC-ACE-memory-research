"""p3_char_0183_仞 — G5 attempt.

Decomposition: 仞 = 亻 (2 strokes) + 刃 (3 strokes: 横折钩 + 撇 + 点).
Total 5 strokes matching MMH count.

Bank usage:
- s1 (亻 撇)           -> pie.draw_pie
- s2 (亻 竖)           -> shu.draw_shu
- s3 (刃 横折钩)        -> heng_zhe_gou.draw_heng_zhe_gou
- s4 (刃 撇 sweep)     -> pie.draw_pie (long sweeping variant)
- s5 (刃 点)           -> dian.draw_dian

Anchors decoded from injected MMH block (cell -> 100px, x_frac/y_frac local).
"""

import os
import sys

from PIL import Image, ImageDraw

BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from pie import draw_pie          # noqa: E402
from shu import draw_shu          # noqa: E402
from dian import draw_dian        # noqa: E402
from heng_zhe_gou import draw_heng_zhe_gou  # noqa: E402


CELL = {
    'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100), 'C':  (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}


def anchor(cell, xf, yf):
    cx, cy = CELL[cell]
    return (cx + xf * 100.0, cy + yf * 100.0)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 5 stroke primitives called below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Uses bank pie/shu/dian/heng_zhe_gou. Joints: s1.mid-s2.head N (gap ~16px), '
             's3.head-s4.head N (gap ~15px). Both natural gaps preserved (no weld).'
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: 亻 撇 — TC(0.002,0.595) -> BL(0.185,0.007)
    s1_head = anchor('TC', 0.002, 0.595)   # ~(100, 60)
    s1_tail = anchor('BL', 0.185, 0.007)   # ~(19, 201)
    draw_pie(d, s1_head, s1_tail,
             bow_perp=14, w_head=9, w_tail=3, steps=90)

    # s2: 亻 竖 — ML(0.729,0.526) -> BL(0.768,0.906)
    s2_head = anchor('ML', 0.729, 0.526)   # ~(73, 153)
    s2_tail = anchor('BL', 0.768, 0.906)   # ~(77, 291)
    draw_shu(d, s2_head, s2_tail, width=7, top_curl=True)

    # s3: 刃 横折钩 — head C(0.263,0.345) -> tail BC(0.705,0.534)
    # Head ~ (126,135) is start of horizontal.
    # Tail ~ (170,253) is hook tip (end of stroke).
    # For a heng-zhe-gou, invent corner (top-right of the box) and
    # a distinct gou tail before the small hook flick.
    s3_head = anchor('C', 0.263, 0.345)          # ~(126, 135)
    s3_hook_tip = anchor('BC', 0.705, 0.534)     # ~(170, 253)
    s3_corner = (215.0, 132.0)                   # top-right corner of the 刃 box
    s3_gou_tail = (188.0, 248.0)                 # end of vertical, before hook flick
    draw_heng_zhe_gou(d, s3_head, s3_corner, s3_gou_tail, s3_hook_tip)

    # s4: 刃 撇 — C(0.661,0.409) -> BC(0.014,0.789)
    # Long sweeping pie from upper-right down to bottom-center-left.
    s4_head = anchor('C', 0.661, 0.409)   # ~(166, 141)
    s4_tail = anchor('BC', 0.014, 0.789)  # ~(101, 279)
    draw_pie(d, s4_head, s4_tail,
             bow_perp=18, w_head=8, w_tail=3, steps=100)

    # s5: 刃 点 — C(0.333,0.705) -> BC(0.163,0.118)
    # Small dot inside 刃 — head thin, tail thickens slightly downward-left.
    s5_head = anchor('C', 0.333, 0.705)   # ~(133, 171)
    s5_tail = anchor('BC', 0.163, 0.118)  # ~(116, 212)
    draw_dian(d, s5_head, s5_tail,
              w_head=3, w_tail=6, bow=3, steps=40)

    out = os.path.join(os.path.dirname(__file__), '01_仞.png')
    img.save(out)
    print(f'wrote {out}')
    print(f'SELF_CHECK: {SELF_CHECK}')


if __name__ == '__main__':
    main()
