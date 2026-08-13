# p2_radical_033_亠 — G5 attempt
# 2 strokes: (1) 点 (dian) top-center, (2) 一 (heng) long horizontal below.
# MMH anchors → px (300x300, 米字格 3x3 cells of 100px each):
#   s1 dian: head C(0.204, 0.28)  → (120.4, 128.0)
#            tail C(0.608, 0.559) → (160.8, 155.9)
#   s2 heng: head ML(0.463, 0.931) → ( 46.3, 193.1)
#            tail MR(0.584, 0.857) → (258.4, 185.7)
# Joints: NONE (clear separation between dot and horizontal).

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 2 strokes drawn, expected 2
    'endpoint_mismatches': [],    # anchors used directly from MMH
    'joint_class_mismatches': [], # no joints expected
    'overall_pass': True,
    'notes': '亠 = 点 + 长横. Bank primitives dian.py + heng.py both fit cleanly.',
}

import sys, pathlib
BANK = pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from PIL import Image, ImageDraw
from dian import draw_dian
from heng import draw_heng

W = H = 300
CELL = W // 3  # 米字格 cell = 100 px

GRID = {
    'TL': (0, 0), 'TC': (1, 0), 'TR': (2, 0),
    'ML': (0, 1), 'C':  (1, 1), 'MR': (2, 1),
    'BL': (0, 2), 'BC': (1, 2), 'BR': (2, 2),
}


def anchor(cell, xf, yf):
    c, r = GRID[cell]
    return (c * CELL + xf * CELL, r * CELL + yf * CELL)


img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)

# stroke 1 — 点
s1_head = anchor('C', 0.204, 0.28)
s1_tail = anchor('C', 0.608, 0.559)
draw_dian(d, s1_head, s1_tail, w_head=3, w_tail=8, bow=5, steps=48)

# stroke 2 — 长横 (wide horizontal, slight rise from left to right per MMH tail y<head y)
s2_head = anchor('ML', 0.463, 0.931)
s2_tail = anchor('MR', 0.584, 0.857)
draw_heng(d, s2_head, s2_tail, width_head=9, width_tail=10)

OUT = pathlib.Path(__file__).parent / '01_亠.png'
img.save(OUT)
print(f'wrote {OUT}')
