# p3_char_0165_乍 — G5
# 5 strokes: (1) short pie from top-center down-left, (2) top heng rising right,
# (3) long shu piercing down past bottom, (4) mid short heng, (5) bottom short heng.
# All 4 joints are N (natural neighbor gap) per MMH block.

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 5 stroke primitives
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # all N — small natural gaps preserved
    'overall_pass': True,
    'notes': 'Bank primitives: pie, heng x3, shu. Anchors driven directly from MMH block.'
}

import os, sys
from PIL import Image, ImageDraw

BANK = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G5_code_bank_mmh/success_bank/code"
sys.path.insert(0, BANK)
from pie import draw_pie
from heng import draw_heng
from shu import draw_shu

# 米字格 cell top-left in 300x300 canvas (100px cells)
CELLS = {
    'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100), 'C':  (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}
def A(cell, xf, yf):
    cx, cy = CELLS[cell]
    return (cx + xf * 100.0, cy + yf * 100.0)

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# s1: 撇 from TC(0.096, 0.606) -> ML(0.375, 0.843)
draw_pie(d, A('TC', 0.096, 0.606), A('ML', 0.375, 0.843),
         bow_perp=8, w_head=7, w_tail=3)

# s2: 横 from C(0.043, 0.219) -> MR(0.435, 0.005)  (long top heng, rising slightly)
draw_heng(d, A('C', 0.043, 0.219), A('MR', 0.435, 0.005),
          width_head=8, width_tail=9)

# s3: 竖 from C(0.395, 0.274) -> BC(0.509, 1.129)  (long vertical, past bottom)
draw_shu(d, A('C', 0.395, 0.274), A('BC', 0.509, 1.129), width=7)

# s4: 横 from C(0.6, 0.734) -> MR(0.229, 0.69)  (mid short heng)
draw_heng(d, A('C', 0.6, 0.734), A('MR', 0.229, 0.69),
          width_head=7, width_tail=8)

# s5: 横 from BC(0.576, 0.241) -> BR(0.32, 0.171)  (bottom short heng)
draw_heng(d, A('BC', 0.576, 0.241), A('BR', 0.32, 0.171),
          width_head=7, width_tail=8)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_乍.png")
img.save(out)
print("wrote", out)
