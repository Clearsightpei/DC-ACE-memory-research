"""
G5 attempt for p2_radical_134_爪 (4-stroke radical).

MMH structural expectations:
  s1: head TR(0.027, 0.841) → tail C(0.078, 0.204)
      px (203, 84) → (108, 120)  -- short pie-like top stroke, top-right to center
  s2: head ML(0.809, 0.157) → tail BL(0.284, 0.815)
      px (81, 116) → (28, 281)   -- long left 撇 (main body left curve)
  s3: head C(0.327, 0.148) → tail BC(0.43, 1.117)
      px (133, 115) → (143, 312)  -- center 竖 (drops off canvas)
  s4: head C(0.509, 0.339) → tail BR(0.865, 0.651)
      px (151, 134) → (287, 265) -- right 捺
Joints: all N (neighbor / clean gap, ~9–22 px)

Uses bank primitives: pie.py (s1 short + s2 long), shu.py (s3), na.py (s4).
No BANK_DEVIATION — all primitives fit cleanly.
"""

import sys
import os
BANK = '<REPO_ROOT>/experiments/exp_context_effect/groups/G5_code_bank_mmh/success_bank/code'
sys.path.insert(0, BANK)

from PIL import Image, ImageDraw
from pie import draw_pie
from na import draw_na
from shu import draw_shu

SIZE = 300


def cell_to_px(cell, xf, yf):
    """米字格 anchor → pixel (image coords, y grows down)."""
    if cell == 'C':
        col, row = 1, 1
    else:
        col = {'L': 0, 'C': 1, 'R': 2}[cell[1]]
        row = {'T': 0, 'M': 1, 'B': 2}[cell[0]]
    return col * 100 + xf * 100, row * 100 + yf * 100


def render():
    img = Image.new('L', (SIZE, SIZE), 255)
    draw = ImageDraw.Draw(img)

    # s1: short top stroke, TR → C (diagonal down-left, short)
    # 爪 top has a short pie-like flick. Use pie with small bow.
    h1 = cell_to_px('TR', 0.027, 0.841)   # (203, 84)
    t1 = cell_to_px('C',  0.078, 0.204)   # (108, 120)
    draw_pie(draw, h1, t1, bow_perp=4, w_head=6, w_tail=3, steps=50)

    # s2: main left 撇 from ML → BL — long, curves left (bow to the right of
    # travel = bow_perp positive in pie's convention gives curve arching right).
    h2 = cell_to_px('ML', 0.809, 0.157)   # (81, 116)
    t2 = cell_to_px('BL', 0.284, 0.815)   # (28, 281)
    draw_pie(draw, h2, t2, bow_perp=18, w_head=9, w_tail=3, steps=100)

    # s3: center 竖 from C → BC. Tail y=312 exceeds canvas; clamp to 299.
    h3 = cell_to_px('C', 0.327, 0.148)    # (133, 115)
    t3_raw = cell_to_px('BC', 0.43, 1.117)  # (143, 312)
    t3 = (t3_raw[0], min(t3_raw[1], 299))
    draw_shu(draw, h3, t3, width=6)

    # s4: right 捺 from C → BR — thickens toward tail
    h4 = cell_to_px('C',  0.509, 0.339)   # (151, 134)
    t4 = cell_to_px('BR', 0.865, 0.651)   # (287, 265)
    draw_na(draw, h4, t4, bow_perp=10, w_head=4, w_tail=10, steps=80)

    return img


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 4 strokes: s1 pie + s2 pie + s3 shu + s4 na
    'endpoint_mismatches': [],    # endpoints copied verbatim from MMH block
    'joint_class_mismatches': [], # all joints are N (clean gaps preserved by
                                  # keeping s1.tail (108,120), s2.head (81,116),
                                  # s3.head (133,115), s4.head (151,134) distinct)
    'overall_pass': True,
    'notes': 'Bank primitives fit; no deviation. Center 竖 tail clamped from y=312 to 299 (off-canvas MMH y_frac=1.117).',
}


if __name__ == '__main__':
    out = '<REPO_ROOT>/experiments/exp_context_effect/groups/G5_code_bank_mmh/attempts/p2_radical_134_爪/01_爪.png'
    render().save(out)
    print('wrote', out)
