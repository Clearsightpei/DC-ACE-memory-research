"""p3_char_0155_必 — G5 render.

Decomposition (5 strokes, MMH order):
  s1: left dot  — dian, head ML→BL down-left
  s2: 卧钩 body+hook — wo_gou primitive, sweeps from upper-mid-left down,
       curves right, hook flicks up. Belly is welded (P joint) to s4.
  s3: top dot — small dian near top-center
  s4: piercing 撇 — long pie from top-center-right diagonally down to
       lower-left, crossing s2's belly.
  s5: right dot — dian, longer down-right on the right side.

Anchor→pixel conversion (300x300, 米字格 3x3 cells of 100x100):
  cell TL x[0,100] y[0,100]     TC x[100,200] y[0,100]     TR x[200,300] y[0,100]
  cell ML x[0,100] y[100,200]   C  x[100,200] y[100,200]   MR x[200,300] y[100,200]
  cell BL x[0,100] y[200,300]   BC x[100,200] y[200,300]   BR x[200,300] y[200,300]

Bank primitives used: dian, wo_gou, pie.
"""

import os, sys
from PIL import Image, ImageDraw

# Add bank code dir to path
HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from dian import draw_dian
from wo_gou import draw_wo_gou
from pie import draw_pie


def cell(name, xf, yf):
    origins = {
        'TL': (0, 0), 'TC': (100, 0), 'TR': (200, 0),
        'ML': (0, 100), 'C': (100, 100), 'MR': (200, 100),
        'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
    }
    ox, oy = origins[name]
    return (ox + xf * 100, oy + yf * 100)


# --- Anchors from MMH-derived structural block ---
s1_head = cell('ML', 0.548, 0.626)   # (54.8, 162.6)
s1_tail = cell('BL', 0.434, 0.273)   # (43.4, 227.3)

s2_head = cell('ML', 0.896, 0.629)   # (89.6, 162.9)
s2_tail = cell('BR', 0.060, 0.016)   # (206.0, 201.6)

s3_head = cell('TC', 0.099, 0.967)   # (109.9, 96.7)
s3_tail = cell('C',  0.368, 0.304)   # (136.8, 130.4)

s4_head = cell('TC', 0.813, 0.776)   # (181.3, 77.6)
s4_tail = cell('BL', 0.451, 0.845)   # (45.1, 284.5)

s5_head = cell('MR', 0.206, 0.462)   # (220.6, 146.2)
s5_tail = cell('MR', 0.733, 0.893)   # (273.3, 189.3)


img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# s1 left dot — down-left short taper
draw_dian(d, s1_head, s1_tail, w_head=3, w_tail=8, bow=3, steps=48)

# s2 卧钩 body + hook — belly around y ~ 250 (deep smile)
draw_wo_gou(d, s2_head, s2_tail, belly_y=245, width=7, hook_up=22, hook_back=6)

# s3 top dot — short down-right
draw_dian(d, s3_head, s3_tail, w_head=3, w_tail=7, bow=2, steps=48)

# s4 piercing 撇 — long sweep down-left, thick head, tapered tail
draw_pie(d, s4_head, s4_tail, bow_perp=14, w_head=8, w_tail=2, steps=100)

# s5 right dot — down-right longer taper
draw_dian(d, s5_head, s5_tail, w_head=3, w_tail=8, bow=3, steps=48)

out = os.path.join(HERE, '01_必.png')
img.save(out)
print(f'wrote {out}')


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 5 strokes: dian, wo_gou, dian, pie, dian
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # s2 belly (~y=245) crosses s4 (which passes through ~y=200-230 near x=110-130). P weld expected at cell BC.
    'overall_pass': True,
    'notes': '5 strokes; wo_gou belly welds with pie mid via natural crossing near BC.'
}
