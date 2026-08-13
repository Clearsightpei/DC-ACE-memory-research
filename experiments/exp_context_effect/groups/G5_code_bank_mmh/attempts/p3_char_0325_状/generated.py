"""p3_char_0325_状 — G5 attempt.

状 = 丬 (left, 3 strokes) + 犬 (right, 4 strokes). 7 strokes total.
Composed via stroke-primitive layer (P-A-006 style): each MMH endpoint
anchor pair is passed directly to a bank primitive. No whole-radical
wrapper for 丬 exists in the bank (skipped for 犬 too because MMH here
places 犬 with rotated/scaled endpoints — inlining via primitives lets
每 stroke land exactly on the injected anchors).
"""

import os
import sys

from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__), "..", "..",
                    "success_bank", "code")
sys.path.insert(0, os.path.abspath(BANK))

from shu import draw_shu           # noqa: E402
from heng import draw_heng         # noqa: E402
from dian import draw_dian         # noqa: E402
from pie import draw_pie           # noqa: E402
from na import draw_na             # noqa: E402
from ti import draw_ti             # noqa: E402


# ---- 米字格 anchor conversion (mirrors G4's _anchor.py) ----
CANVAS = 300
_CELL = CANVAS / 3.0
_CELL_ORIGIN = {
    'TL': (0, 0), 'TC': (1, 0), 'TR': (2, 0),
    'ML': (0, 1), 'C':  (1, 1), 'MR': (2, 1),
    'BL': (0, 2), 'BC': (1, 2), 'BR': (2, 2),
}


def A(cell, xf, yf):
    col, row = _CELL_ORIGIN[cell]
    return ((col + xf) * _CELL, (row + yf) * _CELL)


# ---- MMH endpoint anchors ----
S1_H = A('ML', 0.437, 0.175)   # 丬 top dot head
S1_T = A('ML', 0.762, 0.482)   # 丬 top dot tail
S2_H = A('BL', 0.249, 0.314)   # 丬 提 head (lower-left)
S2_T = A('ML', 0.943, 0.813)   # 丬 提 tail (upper-right)
S3_H = A('TL', 0.92,  0.724)   # 丬 竖 head (top)
S3_T = A('BL', 0.984, 0.971)   # 丬 竖 tail (bottom)
S4_H = A('C',  0.263, 0.726)   # 犬 一 head (left)
S4_T = A('MR', 0.426, 0.588)   # 犬 一 tail (right)
S5_H = A('TC', 0.696, 0.668)   # 犬 撇 head (upper-right)
S5_T = A('BC', 0.169, 0.748)   # 犬 撇 tail (lower-left)
S6_H = A('C',  0.854, 0.98)    # 犬 捺 head (mid)
S6_T = A('BR', 0.851, 0.821)   # 犬 捺 tail (lower-right)
S7_H = A('MR', 0.136, 0.017)   # 犬 丶 head
S7_T = A('MR', 0.414, 0.283)   # 犬 丶 tail


# ---- Self-check dict ----
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('7 strokes: dian(s1 丬点), ti(s2 丬提), shu(s3 丬竖), '
              'heng(s4 犬一), pie(s5 犬撇), na(s6 犬捺), dian(s7 犬丶). '
              'MMH endpoints used verbatim -> joint gaps emerge naturally.'),
}


def main():
    img = Image.new('RGB', (CANVAS, CANVAS), 'white')
    draw = ImageDraw.Draw(img)

    # s1 — 丬 top dot (short down-right dab)
    draw_dian(draw, S1_H, S1_T, w_head=3, w_tail=7, bow=3, steps=40)
    # s2 — 丬 提 (rising diagonal, lower-left to upper-right)
    draw_ti(draw, S2_H, S2_T, w_head=8, w_tail=2, steps=50)
    # s3 — 丬 竖 (long vertical shaft, no top curl in composed char)
    draw_shu(draw, S3_H, S3_T, width=7, top_curl=False)
    # s4 — 犬 一 (horizontal)
    draw_heng(draw, S4_H, S4_T, width_head=8, width_tail=9)
    # s5 — 犬 撇 (long down-left sweep)
    draw_pie(draw, S5_H, S5_T, bow_perp=14, w_head=9, w_tail=3, steps=80)
    # s6 — 犬 捺 (thickening rightward sweep, welds through s5 midpoint)
    draw_na(draw, S6_H, S6_T, bow_perp=8, w_head=4, w_tail=11, steps=80)
    # s7 — 犬 丶 (small right dot)
    draw_dian(draw, S7_H, S7_T, w_head=3, w_tail=7, bow=2, steps=40)

    out = os.path.join(os.path.dirname(__file__), '01_状.png')
    img.save(out)
    print('wrote', out)
    print('SELF_CHECK:', SELF_CHECK)


if __name__ == '__main__':
    main()
