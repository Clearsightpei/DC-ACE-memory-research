# p3_char_0251_当 — G5
# 6 strokes: 当 = 3 top marks (小-like) + 彐 bottom bracket.
#   s1: center small 竖 (short vertical), TC->C
#   s2: left small 点/pie, ML->C
#   s3: right small 撇, TR->C
#   s4: 横折 (big fold — top+right of bracket), ML->BC
#   s5: interior 横 (middle horizontal), BL->BC
#   s6: bottom 横 (closes bracket left→right), BL->BR
# 3 joints: all N (natural gaps per MMH block).
# P-A-006: MMH-anchor verbatim + stroke-primitive layer.

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 6 stroke primitives
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all N — small natural gaps preserved
    'overall_pass': True,
    'notes': 'Bank primitives: shu, dian, pie, heng_zhe_gou (as 横折), heng x2. Anchors verbatim from MMH block.'
}

import os, sys
from PIL import Image, ImageDraw

BANK = "<REPO_ROOT>/experiments/exp_context_effect/groups/G5_code_bank_mmh/success_bank/code"
sys.path.insert(0, BANK)
from shu import draw_shu
from dian import draw_dian
from pie import draw_pie
from heng import draw_heng
from heng_zhe_short import draw_heng_zhe_short

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

# --- TOP THREE MARKS (小-like) ---
# s1: center 竖 (small vertical): TC(0.371,0.7)=(137.1,70) -> C(0.418,0.658)=(141.8,165.8)
draw_shu(d, A('TC', 0.371, 0.7), A('C', 0.418, 0.658), width=6)

# s2: left small 点 (leaning): ML(0.773,0.104)=(77.3,110.4) -> C(0.069,0.4)=(106.9,140.0)
draw_dian(d, A('ML', 0.773, 0.104), A('C', 0.069, 0.4),
          w_head=3, w_tail=7, bow=2)

# s3: right small 撇: TR(0.057,0.82)=(205.7,82.0) -> C(0.731,0.345)=(173.1,134.5)
draw_pie(d, A('TR', 0.057, 0.82), A('C', 0.731, 0.345),
         bow_perp=5, w_head=8, w_tail=3)

# --- 彐 BOTTOM BRACKET ---
# s4: 横折 (no hook — clean right-angle bracket top+right): ML(0.797,0.77)=(79.7,177.0) -> BC(0.925,0.578)=(192.5,257.8)
h_head = A('ML', 0.797, 0.77)      # (79.7, 177.0)
h_tail = A('BC', 0.925, 0.578)     # (192.5, 257.8)
draw_heng_zhe_short(d, h_head, h_tail, corner_offset=(0, 4))

# s5: interior 横: BL(0.715,0.247)=(71.5,224.7) -> BC(0.866,0.188)=(186.6,218.8)
draw_heng(d, A('BL', 0.715, 0.247), A('BC', 0.866, 0.188),
          width_head=7, width_tail=8)

# s6: bottom 横: BL(0.753,0.777)=(75.3,277.7) -> BR(0.18,0.719)=(218.0,271.9)
draw_heng(d, A('BL', 0.753, 0.777), A('BR', 0.18, 0.719),
          width_head=8, width_tail=9)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_当.png")
img.save(out)
print("wrote", out)
