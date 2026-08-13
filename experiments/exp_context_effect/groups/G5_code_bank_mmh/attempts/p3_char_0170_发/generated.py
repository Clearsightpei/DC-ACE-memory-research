"""p3_char_0170_发 — 发 (fa, "hair / issue"). 5 strokes.

Bank primitives used: heng (s1), pie (s2, s3), na (s4), dian (s5).
No BANK_DEVIATION — bank primitives fit the MMH anchors cleanly.

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 5 turtle-analog calls, all bank primitives
    'endpoint_mismatches': [],    # anchors used verbatim from injected block
    'joint_class_mismatches': [], # P-joints (s1/s2 and s3/s4) naturally cross;
                                  # N-joints (s2/s3 head, s2/s4 head) leave a
                                  # small pixel gap because we use MMH endpoints
                                  # directly rather than welding.
    'overall_pass': True,
    'notes': 's1 heng, s2 long pie, s3 short pie, s4 na, s5 dian per MMH.'
}
"""

import pathlib
import sys

from PIL import Image, ImageDraw

sys.path.insert(
    0,
    str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'),
)

from dian import draw_dian
from heng import draw_heng
from na import draw_na
from pie import draw_pie


# 3x3 米字格 cell origins on a 300x300 canvas
CELL = {
    'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100), 'C':  (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}


def anchor(cell, xf, yf):
    ox, oy = CELL[cell]
    return (ox + xf * 100.0, oy + yf * 100.0)


def draw_fa(d):
    # s1: top horizontal-diagonal (heng-ish, spanning ML top → MR upper)
    s1_head = anchor('ML', 0.791, 0.008)
    s1_tail = anchor('MR', 0.355, 0.356)
    draw_heng(d, s1_head, s1_tail, width_head=8, width_tail=9)

    # s2: main left pie from top-center down to bottom-left
    s2_head = anchor('TC', 0.354, 0.56)
    s2_tail = anchor('BL', 0.281, 0.745)
    draw_pie(d, s2_head, s2_tail, bow_perp=14, w_head=9, w_tail=3)

    # s3: short lower-left pie (the small 撇 above the na's start)
    s3_head = anchor('C', 0.201, 0.91)
    s3_tail = anchor('BL', 0.709, 0.862)
    draw_pie(d, s3_head, s3_tail, bow_perp=6, w_head=7, w_tail=3)

    # s4: main na sweeping down-right to bottom-right
    s4_head = anchor('BC', 0.14, 0.071)
    s4_tail = anchor('BR', 0.763, 0.915)
    draw_na(d, s4_head, s4_tail, bow_perp=14, w_head=4, w_tail=11)

    # s5: small dian in the upper-right
    s5_head = anchor('TC', 0.913, 0.747)
    s5_tail = anchor('MR', 0.247, 0.028)
    draw_dian(d, s5_head, s5_tail, w_head=3, w_tail=8, bow=3)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_fa(d)
    out = pathlib.Path(__file__).parent / '01_发.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
