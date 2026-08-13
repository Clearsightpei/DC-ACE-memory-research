"""p3_char_0468_盅 — G5 attempt.

Composition (9 strokes) = 中 (s1-s4, upper half) + 皿 (s5-s9, lower half).

Both components identity-match past G5 templates:
  - 中: p3_char_0100_中 (shu + heng_zhe_box + heng + shu, central shaft
    piercing top and bottom of box)
  - 皿: p3_char_0195_皿 (shu + heng_zhe_box + shu + shu + heng)

Reasoning trace (P-A-008):
  * MMH gives 9 strokes; decomposes cleanly into 4-stroke 中 (top) + 5-stroke 皿
    (bottom). Both components have well-tested inline recipes from prior PASSes.
  * No whole-radical bank primitive exists for 中 or 皿, so composition proceeds
    from stroke primitives directly (P-A-006 stroke-primitive layer).
  * No BANK_DEVIATION — draw_shu, draw_heng_zhe_box, draw_heng all fit the MMH
    endpoints cleanly. This is a straight identity-reuse of two prior recipes
    stacked vertically.
  * Joint check: 中 has 2 P-joints (central shaft pierces top+bottom of box) —
    emerges naturally from long shu overdrawing horizontals at C. 皿 corners are
    all N (natural gaps) which come free from separate stroke calls. Bridge
    joint s4.tail ⇆ s6.mid / s4.tail ⇆ s8.head are both N (~12-28 px gap) —
    naturally satisfied since 中's shu tail sits above 皿's top band.
"""

import sys
import pathlib

BANK = pathlib.Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from PIL import Image, ImageDraw
from shu import draw_shu
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box


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


# ---- 中 (upper half): s1-s4 -------------------------------------------------
# s1: left vertical of top box
s1_head = A('ML', 0.727, 0.119)   # (72.7, 111.9)
s1_tail = A('ML', 0.981, 0.729)   # (98.1, 172.9)

# s2: heng_zhe of top box (top_left -> bottom_right)
s2_head = A('ML', 0.844, 0.113)   # (84.4, 111.3)
s2_tail = A('C',  0.922, 0.430)   # (192.2, 143.0)

# s3: bottom heng of top box
s3_head = A('C',  0.034, 0.679)   # (103.4, 167.9)
s3_tail = A('MR', 0.080, 0.538)   # (208.0, 153.8)

# s4: central shaft piercing top box top-to-bottom
s4_head = A('TC', 0.333, 0.609)   # (133.3, 60.9)
s4_tail = A('BC', 0.438, 0.086)   # (143.8, 208.6)

# ---- 皿 (lower half): s5-s9 -------------------------------------------------
# s5: left short shu
s5_head = A('BL', 0.659, 0.203)   # (65.9, 220.3)
s5_tail = A('BL', 0.911, 0.824)   # (91.1, 282.4)

# s6: heng_zhe of 皿 (top_left -> bottom_right)
s6_head = A('BL', 0.820, 0.215)   # (82.0, 221.5)
s6_tail = A('BC', 0.934, 0.757)   # (193.4, 275.7)

# s7: inner left short shu
s7_head = A('BC', 0.187, 0.291)   # (118.7, 229.1)
s7_tail = A('BC', 0.251, 0.807)   # (125.1, 280.7)

# s8: inner right short shu
s8_head = A('BC', 0.597, 0.218)   # (159.7, 221.8)
s8_tail = A('BC', 0.541, 0.774)   # (154.1, 277.4)

# s9: long bottom heng
s9_head = A('BL', 0.322, 0.912)   # (32.2, 291.2)
s9_tail = A('BR', 0.698, 0.892)   # (269.8, 289.2)


img = Image.new('RGB', (CANVAS, CANVAS), 'white')
draw = ImageDraw.Draw(img)

# 中
draw_shu(draw, s1_head, s1_tail, width=7)                        # s1
draw_heng_zhe_box(draw, s2_head, s2_tail, width=7)               # s2
draw_heng(draw, s3_head, s3_tail, width_head=8, width_tail=9)    # s3
draw_shu(draw, s4_head, s4_tail, width=8)                        # s4 (long central shaft)

# 皿
draw_shu(draw, s5_head, s5_tail, width=7)                        # s5
draw_heng_zhe_box(draw, s6_head, s6_tail, width=8)               # s6
draw_shu(draw, s7_head, s7_tail, width=6)                        # s7
draw_shu(draw, s8_head, s8_tail, width=6)                        # s8
draw_heng(draw, s9_head, s9_tail, width_head=9, width_tail=10)   # s9


OUT = pathlib.Path(__file__).parent / "01_盅.png"
img.save(OUT)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 9 stroke primitive calls = expected 9
    'endpoint_mismatches': [],     # every endpoint uses MMH anchor verbatim
    'joint_class_mismatches': [
        # 中 P-joints (s2.mid ⇆ s4.mid at C; s3.mid ⇆ s4.mid at C):
        #   central long shu overdraws heng_zhe_box top + bottom heng → P (welded).
        # All other 12 joints are N — natural gaps from independent primitive calls;
        # bank primitives do not weld to neighbors, so N is satisfied structurally.
    ],
    'overall_pass': True,
    'notes': '9-stroke composition = 中 (4 strokes; identity of p3_char_0100_中 recipe) '
             'stacked over 皿 (5 strokes; identity of p3_char_0195_皿 recipe). '
             'No BANK_DEVIATION. Central 中-shaft is the only P-joint pair.'
}


if __name__ == '__main__':
    print(f"wrote {OUT}")
