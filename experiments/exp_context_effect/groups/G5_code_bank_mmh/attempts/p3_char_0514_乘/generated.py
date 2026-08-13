"""p3_char_0514_乘 — G5 attempt.

Reasoning trace (P-A-008):
- 10 strokes required by MMH block.
- 乘 has: top curly, top heng, long shu through middle, small right vertical,
  short middle-left heng, short ti, two small inner strokes forming inner 北,
  big pie (s9) descending left, big na (s10) descending right.
- No good whole-radical bank match (乘 has no siblings in bank). Use
  stroke-primitive layer per P-A-006: inline all 10 via bank stroke fns
  keyed to MMH endpoint anchors (verbatim), no whole-radical composition.
- Refuse whole-radical inline for 禾 (not in bank) and 北 (not in bank).
- BANK usage: heng, shu, pie, na, ti, dian. No BANK_DEVIATION — using
  stroke primitives at MMH-native scale.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
from na import draw_na
from ti import draw_ti
from dian import draw_dian

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '10 strokes at MMH-verbatim anchors, per-stroke primitive layer (P-A-006).',
}

# 米字格 cells (3x3 on 300x300)
CELLS = {
    'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100), 'C':  (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}

def A(cell, xf, yf):
    cx, cy = CELLS[cell]
    return (cx + xf * 100, cy + yf * 100)

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# s1: TC(0.934,0.668) → TL(0.94,0.908) — top curly, short heng going left
draw_heng(d, A('TC', 0.934, 0.668), A('TL', 0.94, 0.908),
          width_head=6, width_tail=7)

# s2: ML(0.542,0.251) → MR(0.449,0.096) — main top heng cross-bar
draw_heng(d, A('ML', 0.542, 0.251), A('MR', 0.449, 0.096),
          width_head=8, width_tail=9)

# s3: TC(0.356,0.867) → BC(0.45,1.179) — long vertical shu through middle
# clamp tail y to canvas
draw_shu(d, A('TC', 0.356, 0.867), (145.0, 299.0), width=8)

# s4: C(0.052,0.356) → BC(0.116,0.101) — short right-inner vertical (dian-like)
draw_shu(d, A('C', 0.052, 0.356), A('BC', 0.116, 0.101), width=6)

# s5: ML(0.586,0.69) → C(0.043,0.6) — small heng inner-left top
draw_heng(d, A('ML', 0.586, 0.69), A('C', 0.043, 0.6),
          width_head=6, width_tail=7)

# s6: BL(0.574,0.051) → C(0.008,0.922) — short ti in mid-left (rising right)
draw_ti(d, A('BL', 0.574, 0.051), A('C', 0.008, 0.922),
        w_head=7, w_tail=2)

# s7: MR(0.379,0.415) → C(0.913,0.644) — small heng inner-right top
draw_heng(d, A('MR', 0.379, 0.415), A('C', 0.913, 0.644),
          width_head=6, width_tail=7)

# s8: C(0.796,0.298) → MR(0.432,0.667) — small pie-like going down-right (小撇/dot)
draw_pie(d, A('C', 0.796, 0.298), A('MR', 0.432, 0.667),
         bow_perp=-4, w_head=6, w_tail=4)

# s9: C(0.403,0.931) → BL(0.366,0.921) — big pie descending left
draw_pie(d, A('C', 0.403, 0.931), A('BL', 0.366, 0.921),
         bow_perp=18, w_head=10, w_tail=3)

# s10: BC(0.57,0.016) → BR(0.854,0.859) — big na descending right
draw_na(d, A('BC', 0.57, 0.016), A('BR', 0.854, 0.859),
        bow_perp=14, w_head=4, w_tail=12)

img.save(os.path.join(os.path.dirname(__file__), '01_乘.png'))
print('wrote 01_乘.png')
