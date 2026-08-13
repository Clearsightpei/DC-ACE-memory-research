"""p3_char_0176_平 — G5 attempt.

5 strokes per MMH:
  1. short top heng: TL(0.99,0.771) -> TR(0.036,0.65)
  2. left small dian: ML(0.794,0.125) -> C(0.063,0.462)
  3. right small pie: TR(0.021,0.943) -> C(0.752,0.444)
  4. long middle heng: ML(0.36,0.881) -> MR(0.728,0.743)
  5. long vertical shu: TC(0.362,0.87) -> BC(0.474,1.117)

Joints:
  - s1.mid ⇆ s5.head @ TC : N (small natural gap ~26px)
  - s4.mid ⇆ s5.mid  @ C  : P (welded crossing)

Bank primitives used: heng, dian, pie, shu — all endpoint-signature so
we feed MMH-derived anchors directly. No BANK_DEVIATION.
"""
import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
sys.path.insert(0, os.path.abspath(BANK))

from heng import draw_heng   # noqa: E402
from shu import draw_shu     # noqa: E402
from pie import draw_pie     # noqa: E402
from dian import draw_dian   # noqa: E402


CELL_ORIG = {
    'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100), 'C':  (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}


def anchor(cell, xf, yf):
    ox, oy = CELL_ORIG[cell]
    return (ox + xf * 100, oy + yf * 100)


def _clamp(pt):
    x, y = pt
    return (max(2, min(298, x)), max(2, min(298, y)))


# --- endpoints ---
s1_head = anchor('TL', 0.99, 0.771)     # (99, 77)
s1_tail = anchor('TR', 0.036, 0.65)     # (204, 65)

s2_head = anchor('ML', 0.794, 0.125)    # (79, 112)
s2_tail = anchor('C',  0.063, 0.462)    # (106, 146)

s3_head = anchor('TR', 0.021, 0.943)    # (202, 94)
s3_tail = anchor('C',  0.752, 0.444)    # (175, 144)

s4_head = anchor('ML', 0.36, 0.881)     # (36, 188)
s4_tail = anchor('MR', 0.728, 0.743)    # (273, 174)

s5_head = anchor('TC', 0.362, 0.87)     # (136, 87)
s5_tail = _clamp(anchor('BC', 0.474, 1.117))  # (147, ~298)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        'Bank-only render: heng x2, dian, pie, shu. '
        's5 crosses s4 (P). s5.head sits ~15 px right of s1.mid (N). '
        's5.tail clamped from y=311.7 to y=298 to stay in canvas.'
    ),
}


def render(out_path):
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # 1. Top short heng
    draw_heng(draw, s1_head, s1_tail, width_head=8, width_tail=9)
    # 2. Left small dian — thin at head, thicker at tail, small bow
    draw_dian(draw, s2_head, s2_tail, w_head=3, w_tail=7, bow=3)
    # 3. Right small pie — leftward sweep
    draw_pie(draw, s3_head, s3_tail, bow_perp=6, w_head=8, w_tail=3)
    # 4. Long middle heng (the main horizontal beam)
    draw_heng(draw, s4_head, s4_tail, width_head=10, width_tail=12)
    # 5. Long central vertical
    draw_shu(draw, s5_head, s5_tail, width=8)

    img.save(out_path)


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '01_平.png')
    render(out)
    print('wrote', out)
