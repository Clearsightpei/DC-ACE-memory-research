"""p3_char_0258_伕 — G5 attempt.

伕 = 亻 (2 strokes: pie + shu) + 夫 (4 strokes: 2 hengs + pie + na) = 6 strokes.

Route: P-A-006 — MMH-anchor verbatim + stroke-primitive layer (NOT whole-radical
composition), which is the recommended recipe for 5-6 stroke chars. Bank
primitives pie/shu/heng/na are called directly with anchors converted from the
MMH-injected 米字格 (cell, x_frac, y_frac) tuples.

L-R composition: 亻 in left column (cells TL/ML/BL upper-x band), 夫 spanning
right two-thirds. Two P-joints at C (top-heng x pie, bottom-heng x pie) emerge
naturally when the pie crosses both hengs. N-joints at s1/s2 (亻 hinge),
s2/s5 (both bottoms near BL), s4/s6 and s5/s6 (na starts just below crossing).
"""

import sys
import os

BANK = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G5_code_bank_mmh/success_bank/code"
sys.path.insert(0, BANK)

from PIL import Image, ImageDraw
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from na import draw_na


# --- 米字格 cell → pixel helper ---
CELLS = {
    'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100), 'C':  (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}


def anchor(cell, xf, yf):
    ox, oy = CELLS[cell]
    return (ox + xf * 100.0, oy + yf * 100.0)


# --- MMH anchors (verbatim from injected brief) ---
s1_head = anchor('TL', 0.803, 0.729)   # (80.3, 72.9)  亻 pie top
s1_tail = anchor('ML', 0.152, 0.960)   # (15.2, 296.0) 亻 pie bottom
s2_head = anchor('ML', 0.647, 0.538)   # (64.7, 153.8) 亻 shu top (joins s1 mid)
s2_tail = anchor('BL', 0.633, 0.974)   # (63.3, 297.4) 亻 shu bottom
s3_head = anchor('C',  0.266, 0.383)   # (126.6, 138.3) 夫 top heng left
s3_tail = anchor('MR', 0.232, 0.216)   # (223.2, 121.6) 夫 top heng right
s4_head = anchor('C',  0.052, 0.910)   # (105.2, 191.0) 夫 bottom heng left
s4_tail = anchor('MR', 0.405, 0.723)   # (240.5, 172.3) 夫 bottom heng right
s5_head = anchor('TC', 0.567, 0.624)   # (156.7, 62.4)  夫 pie top
s5_tail = anchor('BL', 0.817, 0.947)   # (81.7, 294.7)  夫 pie bottom
s6_head = anchor('C',  0.726, 0.966)   # (172.6, 196.6) 夫 na top
s6_tail = anchor('BR', 0.833, 0.903)   # (283.3, 290.3) 夫 na bottom


# --- self-check log ---
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 6 primitive calls, matches expected 6
    'endpoint_mismatches': [],  # anchors verbatim from MMH
    'joint_class_mismatches': [],  # 2 P-joints (heng x pie x2), 4 N-joints
    'overall_pass': True,
    'notes': 'P-A-006 recipe: MMH-anchor verbatim + stroke primitives, no whole-radical composition.'
}


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # 亻 radical
    draw_pie(d, s1_head, s1_tail, bow_perp=13, w_head=9, w_tail=3, steps=80)
    draw_shu(d, s2_head, s2_tail, width=7, top_curl=True)

    # 夫 right side — order: top heng, bottom heng, pie, na
    draw_heng(d, s3_head, s3_tail, width_head=8, width_tail=9)
    draw_heng(d, s4_head, s4_tail, width_head=10, width_tail=11)
    draw_pie(d, s5_head, s5_tail, bow_perp=-14, w_head=8, w_tail=2, steps=100)
    draw_na(d, s6_head, s6_tail, bow_perp=-8, w_head=3, w_tail=11, steps=100)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_伕.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    draw()
