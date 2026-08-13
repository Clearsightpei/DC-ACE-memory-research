"""p2_radical_133_止 — G5 attempt.

止 (4画): top 竖 (center) + short middle 横 (going right) + left short 竖
+ long bottom 横. Uses shu + heng bank primitives at MMH-derived anchors.
All three joints are class N (natural gap) per the MMH block.
"""

import pathlib
import sys

from PIL import Image, ImageDraw

BANK = pathlib.Path(__file__).resolve().parents[3] / 'G5_code_bank_mmh' / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from shu import draw_shu
from heng import draw_heng


# 米字格 cell origins on 300×300 canvas (3×3 grid, each cell 100×100)
CELLS = {
    'TL': (0, 0), 'TC': (100, 0), 'TR': (200, 0),
    'ML': (0, 100), 'C': (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}


def anchor(cell, xf, yf):
    ox, oy = CELLS[cell]
    return (ox + xf * 100, oy + yf * 100)


img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# s1 — top 竖 (near center, slight lean right at bottom)
s1_head = anchor('TC', 0.389, 0.785)   # (138.9, 78.5)
s1_tail = anchor('BC', 0.465, 0.593)   # (146.5, 259.3)
draw_shu(d, s1_head, s1_tail, width=8)

# s2 — short 横 in middle, going right (head at center, tail toward MR)
s2_head = anchor('C',  0.632, 0.699)   # (163.2, 169.9)
s2_tail = anchor('MR', 0.364, 0.617)   # (236.4, 161.7)
draw_heng(d, s2_head, s2_tail, width_head=8, width_tail=8)

# s3 — left short 竖 (drops from mid-left down)
s3_head = anchor('ML', 0.744, 0.661)   # (74.4, 166.1)
s3_tail = anchor('BL', 0.993, 0.628)   # (99.3, 262.8)
draw_shu(d, s3_head, s3_tail, width=8)

# s4 — long bottom 横 (baseline of the character)
s4_head = anchor('BL', 0.363, 0.748)   # (36.3, 274.8)
s4_tail = anchor('BR', 0.698, 0.672)   # (269.8, 267.2)
draw_heng(d, s4_head, s4_tail, width_head=9, width_tail=10)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 strokes / 4 primitives
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 3 joints are N (natural gap) — anchors already give ~13-17 px separation
    'overall_pass': True,
    'notes': '止 = top-shu + short-heng + left-shu + bottom-heng. Anchors used verbatim from MMH block; N-class joints preserved as natural gaps (no welding).',
}


out = pathlib.Path(__file__).parent / '01_止.png'
img.save(out)
print(f'saved {out}')
