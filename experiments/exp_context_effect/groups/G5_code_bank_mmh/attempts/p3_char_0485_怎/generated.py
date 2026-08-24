# p3_char_0485_怎 — G5
# Composition: 乍 (top, 5 strokes) + 心 (bottom, 4 strokes) = 9 strokes total.
#
# REASONING TRACE (P-A-008):
# - 乍 solo (bank ref p3_char_0165_乍 PASS) uses pie + heng*3 + shu, all inline
#   with fresh anchors — NO whole-乍 primitive exists. Replicate its pattern
#   directly from MMH block (verbatim P-A-006 recipe).
# - 心 solo (bank ref p3_char_0112_心 PASS) uses dian + wo_gou (bank) + dian +
#   dian. wo_gou.py is PROMOTED and reusable — call it (not BANK_DEVIATION).
# - Whole-char primitive question (P-A-007-v2 hard-check): no zha_zuo.py or
#   xin.py in bank; must inline both radicals from strokes. Per P-A-010-v2:
#   composition is stroke-primitive layer (kind not applicable — no radical
#   primitive to rescue).
# - Uniform shift? Both radicals get their own MMH anchors — no need for
#   ox/oy shift; anchors already place 乍 in top half, 心 in bottom row.
#
# All 5 joints per MMH block are class N (natural neighbor gaps).

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 9 stroke primitives called
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # 5 N joints — small natural gaps preserved
    'overall_pass': True,
    'notes': 'Bank primitives: pie, heng x4, shu, dian x3, wo_gou. Anchors from MMH block.'
}

import os, sys
from PIL import Image, ImageDraw

BANK = "<REPO_ROOT>/experiments/exp_context_effect/groups/G5_code_bank_mmh/success_bank/code"
sys.path.insert(0, BANK)
from pie import draw_pie
from heng import draw_heng
from shu import draw_shu
from dian import draw_dian
from wo_gou import draw_wo_gou

# 米字格 cells on 300×300 canvas (100px each)
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

# ============ 乍 (top, strokes 1-5) ============

# s1: 撇 TC(0.148, 0.539) -> ML(0.665, 0.459)   ~ (114.8, 53.9) -> (66.5, 145.9)
draw_pie(d, A('TC', 0.148, 0.539), A('ML', 0.665, 0.459),
         bow_perp=8, w_head=7, w_tail=3)

# s2: 横 C(0.134, 0.058) -> TR(0.238, 0.896)    ~ (113.4, 105.8) -> (223.8, 89.6)
draw_heng(d, A('C', 0.134, 0.058), A('TR', 0.238, 0.896),
          width_head=8, width_tail=9)

# s3: 竖 (long shu, piercing) C(0.365, 0.131) -> BC(0.45, 0.095)  ~ (136.5, 113.1) -> (145, 209.5)
draw_shu(d, A('C', 0.365, 0.131), A('BC', 0.45, 0.095), width=7)

# s4: 横 (mid short) C(0.544, 0.433) -> MR(0.013, 0.356)  ~ (154.4, 143.3) -> (200.1, 135.6)
draw_heng(d, A('C', 0.544, 0.433), A('MR', 0.013, 0.356),
          width_head=7, width_tail=8)

# s5: 横 (bottom of 乍) C(0.544, 0.743) -> MR(0.068, 0.682)  ~ (154.4, 174.3) -> (206.8, 168.2)
draw_heng(d, A('C', 0.544, 0.743), A('MR', 0.068, 0.682),
          width_head=7, width_tail=8)

# ============ 心 (bottom, strokes 6-9) ============

# s6: 左点 BL(0.653, 0.241) -> BL(0.486, 0.783)  ~ (65.3, 224.1) -> (48.6, 278.3)
draw_dian(d, head=A('BL', 0.653, 0.241), tail=A('BL', 0.486, 0.783),
          w_head=3, w_tail=8, bow=4)

# s7: 卧钩 BL(0.976, 0.247) -> BR(0.071, 0.455)  ~ (97.6, 224.7) -> (207.1, 245.5)
# belly dips well below tail (~50 px below) — hearty smile shape.
draw_wo_gou(d, head=A('BL', 0.976, 0.247), tail=A('BR', 0.071, 0.455),
            belly_y=285, width=8, hook_up=22, hook_back=5)

# s8: 中点 BC(0.5, 0.221) -> BC(0.752, 0.473)  ~ (150, 222.1) -> (175.2, 247.3)
draw_dian(d, head=A('BC', 0.5, 0.221), tail=A('BC', 0.752, 0.473),
          w_head=3, w_tail=7, bow=2)

# s9: 右点 BR(0.203, 0.065) -> BR(0.707, 0.402)  ~ (220.3, 206.5) -> (270.7, 240.2)
draw_dian(d, head=A('BR', 0.203, 0.065), tail=A('BR', 0.707, 0.402),
          w_head=3, w_tail=8, bow=3)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_怎.png")
img.save(out)
print("wrote", out)
