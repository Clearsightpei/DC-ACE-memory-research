# p3_char_0301_作 — G5
# 作 = 亻 + 乍 (7 strokes, all straight — P-COMP-011 friendly).
# Recipe: P-A-006 — MMH-verbatim endpoint anchors + stroke-primitive layer.
# NOT calling ren_left whole-radical: MMH anchors compress 亻 tighter to
# the extreme left than the native primitive geometry, so inline stroke
# primitives at MMH anchors match GT better (P-A-006 vs P-A-007 tradeoff).
#
# Joints (all N — natural neighbor gaps, no welding):
#   s1.mid ⇆ s2.head at ML : N gap ~11.7
#   s3.mid ⇆ s4.head at C  : N gap ~13.7
#   s4.head ⇆ s5.head at C : N gap ~14.6
#   s5.mid ⇆ s6.head at C  : N gap ~13.6
#   s5.mid ⇆ s7.head at BC : N gap ~19.6

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 7 primitives: pie + shu + pie + heng + shu + heng + heng
    'endpoint_mismatches': [],       # all endpoints placed directly from MMH block
    'joint_class_mismatches': [],    # all 5 joints implemented as N (no welding)
    'overall_pass': True,
    'notes': 'P-A-006: inline stroke primitives at MMH anchors. Right-half 乍 straight strokes; left 亻 pie+shu with N gap between s1.mid and s2.head.'
}

import os, sys
from PIL import Image, ImageDraw

BANK = "<REPO_ROOT>/experiments/exp_context_effect/groups/G5_code_bank_mmh/success_bank/code"
sys.path.insert(0, BANK)
from pie import draw_pie
from heng import draw_heng
from shu import draw_shu

# 米字格 cell top-left in 300×300 canvas (100 px cells)
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

# --- 亻 (left) ---
# s1: 撇 TL(0.973, 0.653)=(97.3, 65.3) -> ML(0.22, 0.972)=(22.0, 197.2)
draw_pie(d, A('TL', 0.973, 0.653), A('ML', 0.22, 0.972),
         bow_perp=14, w_head=9, w_tail=3)

# s2: 竖 ML(0.812, 0.43)=(81.2, 143.0) -> BL(0.873, 0.865)=(87.3, 286.5)
draw_shu(d, A('ML', 0.812, 0.43), A('BL', 0.873, 0.865), width=7)

# --- 乍 (right) ---
# s3: 撇 TC(0.729, 0.577)=(172.9, 57.7) -> C(0.14, 0.796)=(114.0, 179.6)
draw_pie(d, A('TC', 0.729, 0.577), A('C', 0.14, 0.796),
         bow_perp=8, w_head=8, w_tail=3)

# s4: 横 C(0.617, 0.371)=(161.7, 137.1) -> MR(0.695, 0.201)=(269.5, 120.1)
#     (top heng, rising slightly right)
draw_heng(d, A('C', 0.617, 0.371), A('MR', 0.695, 0.201),
          width_head=8, width_tail=9)

# s5: 竖 C(0.805, 0.433)=(180.5, 143.3) -> BC(0.919, 1.144)=(191.9, 314.4)
#     (long vertical descender, extends past bottom edge)
draw_shu(d, A('C', 0.805, 0.433), A('BC', 0.919, 1.144), width=7)

# s6: 横 C(0.978, 0.945)=(197.8, 194.5) -> MR(0.505, 0.84)=(250.5, 184.0)
#     (mid short heng)
draw_heng(d, A('C', 0.978, 0.945), A('MR', 0.505, 0.84),
          width_head=7, width_tail=8)

# s7: 横 BC(0.998, 0.405)=(199.8, 240.5) -> BR(0.561, 0.3)=(256.1, 230.0)
#     (bottom short heng)
draw_heng(d, A('BC', 0.998, 0.405), A('BR', 0.561, 0.3),
          width_head=7, width_tail=8)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_作.png")
img.save(out)
print("wrote", out)
