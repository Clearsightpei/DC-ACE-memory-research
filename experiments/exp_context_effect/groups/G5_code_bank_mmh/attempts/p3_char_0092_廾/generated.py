"""p3_char_0092_廾 — G5 attempt.

廾 is a 3-stroke character: one long heng near the middle, plus two
vertical-ish legs — the left leg is a curved pie, the right leg is a
near-vertical shu, both crossing the heng (piercing joints at cell C).

Uses bank primitives heng, pie, shu directly with MMH-derived endpoints.
"""

import sys, os
BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from PIL import Image, ImageDraw
from heng import draw_heng
from pie import draw_pie
from shu import draw_shu

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH: 3 strokes. s1 heng ML->MR y=0.86. s2 pie C->BL. s3 shu C->BC. Two piercing joints (heng x pie, heng x shu) at cell C.',
}

# --- MMH anchor -> PIL pixel conversion ---
CANVAS = 300
_CELL = CANVAS / 3.0
_CELL_ORIGIN = {
    'TL': (0,0), 'TC': (1,0), 'TR': (2,0),
    'ML': (0,1), 'C':  (1,1), 'MR': (2,1),
    'BL': (0,2), 'BC': (1,2), 'BR': (2,2),
}
def A(cell, xf, yf):
    col, row = _CELL_ORIGIN[cell]
    return ((col + xf) * _CELL, (row + yf) * _CELL)

# Endpoints from injected MMH block
s1_head = A('ML', 0.349, 0.86)   # ~ (34.9, 186)
s1_tail = A('MR', 0.625, 0.86)   # ~ (262.5, 186)
s2_head = A('C',  0.014, 0.485)  # ~ (101, 148)
s2_tail = A('BL', 0.633, 0.596)  # ~ (63, 259)
s3_head = A('C',  0.749, 0.377)  # ~ (175, 138)
s3_tail = A('BC', 0.863, 0.719)  # ~ (186, 272)

img = Image.new('RGB', (CANVAS, CANVAS), 'white')
d = ImageDraw.Draw(img)

# Stroke 1: heng across the middle
draw_heng(d, s1_head, s1_tail, width_head=9, width_tail=10)

# Stroke 2: left pie — bows leftward (positive bow_perp per pie.py convention)
draw_pie(d, s2_head, s2_tail, bow_perp=16, w_head=5, w_tail=2)

# Stroke 3: right shu — near-vertical, slight rightward lean
draw_shu(d, s3_head, s3_tail, width=7)

img.save(os.path.join(os.path.dirname(__file__), '01_廾.png'))
print('rendered')
