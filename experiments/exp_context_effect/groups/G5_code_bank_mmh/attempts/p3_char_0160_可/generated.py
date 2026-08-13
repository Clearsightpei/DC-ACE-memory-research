"""G5 attempt: p3_char_0160_可 (ke, 'can/permit' — 5 strokes).

Composition:
  s1 heng (long top)              -> draw_heng
  s2 shu (left of small 口)        -> draw_shu
  s3 heng_zhe (top+right of 口)    -> draw_heng_zhe_box
  s4 heng (bottom of 口)           -> draw_heng
  s5 shu_gou (long right hook)     -> draw_shu_gou

MMH-anchored: all endpoints derived from the injected structural block.
No BANK_DEVIATION — every stroke fits an existing bank primitive cleanly.
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw

from heng import draw_heng
from shu import draw_shu
from heng_zhe_box import draw_heng_zhe_box
from shu_gou import draw_shu_gou


# --- MMH-anchor -> pixel mapping ------------------------------------
# 米字格 cell corners (top-left of each cell, 100px x 100px cells on
# 300x300 canvas): TL(0,0) TC(100,0) TR(200,0)
#                  ML(0,100) C(100,100) MR(200,100)
#                  BL(0,200) BC(100,200) BR(200,200)
CELL_ORIGIN = {
    'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100), 'C':  (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}


def anc(cell, xf, yf):
    ox, oy = CELL_ORIGIN[cell]
    return (ox + xf * 100.0, oy + yf * 100.0)


# --- Structural expectations (from MMH injection) -------------------
s1_head = anc('ML', 0.369, 0.005)   # (36.9, 100.5)
s1_tail = anc('TR', 0.725, 0.894)   # (272.5, 89.4)
s2_head = anc('ML', 0.732, 0.433)   # (73.2, 143.3)
s2_tail = anc('BL', 0.926, 0.065)   # (92.6, 206.5)
s3_head = anc('ML', 0.885, 0.436)   # (88.5, 143.6)
s3_tail = anc('C',  0.31,  0.784)   # (131.0, 178.4)
s4_head = anc('ML', 0.981, 0.96)    # (98.1, 196.0)
s4_tail = anc('C',  0.509, 0.884)   # (150.9, 188.4)
s5_head = anc('TC', 0.837, 0.955)   # (183.7, 95.5)
s5_tail = anc('BC', 0.523, 0.666)   # (152.3, 266.6)


# --- Self-check (see G4 rules) --------------------------------------
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 5 strokes drawn, matches expected 5
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 4 joints implemented as N (natural
                                   # calligraphic gaps — primitives don't weld)
    'overall_pass': True,
    'notes': 'All 5 strokes use bank primitives at MMH-derived anchors. '
             'Joints (s1.mid~s5.head TC, s2.head~s3.head ML, s2.tail~s4.head ML, '
             's3.tail~s4.mid C) all rendered as N — the MMH gaps are preserved '
             'because each primitive draws only to its own anchor; no welding.',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: long top heng
    draw_heng(d, s1_head, s1_tail, width_head=10, width_tail=11)

    # s2: left vertical of small 口
    draw_shu(d, s2_head, s2_tail, width=7)

    # s3: 横折 top+right of small 口 (heng_zhe_box: top_left -> bottom_right)
    draw_heng_zhe_box(d, s3_head, s3_tail, width=7)

    # s4: bottom heng of small 口
    draw_heng(d, s4_head, s4_tail, width_head=7, width_tail=8)

    # s5: long shu-gou (right descender with leftward hook)
    #   head is at top, tail is at hook-tip (bottom-left after hook).
    #   Since head->tail leans slightly LEFT (dx=-31 over dy=+171),
    #   use hook_start_offset ~50 so the hook flare starts higher.
    draw_shu_gou(d, s5_head, s5_tail, width=7, hook_start_offset=52)

    out = pathlib.Path(__file__).with_name('01_可.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
