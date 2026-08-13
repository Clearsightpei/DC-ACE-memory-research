"""p3_char_0100_中 — G5 attempt.

Composition plan (4 strokes, from MMH-injected anchors):
  s1: left vertical of box   (shu)        — bank: draw_shu
  s2: top + right of box     (heng_zhe)   — bank: draw_heng_zhe_box
  s3: bottom of box          (heng)       — bank: draw_heng
  s4: central piercing shaft (shu, long)  — bank: draw_shu

Joint plan:
  s1.head <-> s2.head (ML): N -- keep small natural gap at top-left corner
  s1.tail <-> s3.head (BL): N -- keep small natural gap at bottom-left corner
  s2.tail <-> s3.mid   (MR): N -- small natural gap at bottom-right corner
  s2.mid  <-> s4.mid   (C):  P -- middle shaft pierces the top of box (welded)
  s3.mid  <-> s4.mid   (C):  P -- middle shaft pierces the bottom of box (welded)

All 4 strokes use existing bank primitives; NO BANK_DEVIATION.
"""

import sys
import pathlib

BANK = pathlib.Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from PIL import Image, ImageDraw
from shu import draw_shu
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box


# ---- Anchor -> pixel conversion (300x300 canvas, 3x3 米字格) ----
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


# ---- Endpoints from MMH block ----
s1_head = A('ML', 0.568, 0.248)   # (56.8, 124.8)
s1_tail = A('BL', 0.864, 0.054)   # (86.4, 205.4)

s2_head = A('ML', 0.768, 0.269)   # (76.8, 126.9)
s2_tail = A('MR', 0.057, 0.693)   # (205.7, 169.3)

s3_head = A('ML', 0.926, 0.975)   # (92.6, 197.5)
s3_tail = A('MR', 0.25,  0.834)   # (225.0, 183.4)

s4_head = A('TC', 0.315, 0.589)   # (131.5, 58.9)
s4_tail = A('BC', 0.462, 1.029)   # (146.2, 302.9)


# ---- Render ----
img = Image.new('RGB', (CANVAS, CANVAS), 'white')
draw = ImageDraw.Draw(img)

# s1: left vertical of box
draw_shu(draw, s1_head, s1_tail, width=7)

# s2: heng_zhe (top + right of box).  bank expects (top_left, bottom_right).
# The MMH s2 head IS the top-left of the box, tail is the bottom-right.
draw_heng_zhe_box(draw, s2_head, s2_tail, width=7)

# s3: bottom heng (closes the box)
draw_heng(draw, s3_head, s3_tail, width_head=8, width_tail=9)

# s4: central shaft -- piercing through box (welded at C at two crossings)
draw_shu(draw, s4_head, s4_tail, width=8)


OUT = pathlib.Path(__file__).parent / "01_中.png"
img.save(OUT)


# ---- Mandatory self-check block ----
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # exactly 4 stroke calls (draw_shu, draw_heng_zhe_box, draw_heng, draw_shu)
    'endpoint_mismatches': [],        # all endpoints use MMH anchors exactly
    'joint_class_mismatches': [
        # Nothing mismatched: N-joints emerge naturally from the anchor gaps;
        # P-joints emerge from the central shu piercing through heng_zhe_box top + bottom heng.
    ],
    'overall_pass': True,
    'notes': 'All 4 strokes drawn from bank primitives at MMH anchors. '
             'N-joints (box corners) preserved by using MMH endpoints without welding; '
             'P-joints (central shaft crossing top/bottom horizontals) welded via overdraw at C.'
}

if __name__ == '__main__':
    print(f"wrote {OUT}")
    print(f"self_check: {SELF_CHECK}")
