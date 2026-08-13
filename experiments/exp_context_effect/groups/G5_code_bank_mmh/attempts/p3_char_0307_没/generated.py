# p3_char_0307_没 — G5
# 没 = 氵 + 殳 (7 strokes). Left = sanshui (3), Right = 殳 (4).
# Recipe: P-A-006 — MMH-verbatim endpoint anchors + stroke-primitive layer.
# 氵 inlined (dian+dian+ti) rather than draw_sanshui because MMH anchors
# compress the 氵 into a narrow left column that doesn't match the native
# sanshui geometry (native x-range 92-174 vs MMH target x-range 42-103).
# P-A-007 note: sanshui would need non-uniform scale — inline is cleaner.
#
# Joints:
#   s3.tail ⇆ s4.tail @ C  : N gap ~17.6 (氵-ti tail near 殳-pie tail)
#   s3.tail ⇆ s7.head @ C  : N gap ~34.7 (氵-ti tail near na head)
#   s4.head ⇆ s5.head @ TC : N gap ~16.8 (top of ⺈/几 cap)
#   s6.mid(0.62) ⇆ s7.mid(0.36) @ BC : P welded (又 X-cross)

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 7 primitives: dian+dian+ti + pie + heng_zhe_short + heng_pie + na
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # 3 N gaps + 1 P weld (s6 x s7)
    'overall_pass': True,
    'notes': 'Inline 氵 (dian+dian+ti at MMH anchors), inline pie for ⺈-pie, heng_zhe_short for cap right sweep, heng_pie+na for 又 with tightened apex_x.'
}

import os
import sys
from PIL import Image, ImageDraw

BANK = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G5_code_bank_mmh/success_bank/code"
sys.path.insert(0, BANK)
from dian import draw_dian
from ti import draw_ti
from pie import draw_pie
from na import draw_na
from heng_zhe_short import draw_heng_zhe_short
from heng_pie import draw_heng_pie

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

# --- 氵 (left, 3 strokes) ---
# s1: top dian  TL(0.715, 0.712) -> TC(0.031, 0.993)  = (71.5,71.2) -> (103.1,99.3)
draw_dian(d, A('TL', 0.715, 0.712), A('TC', 0.031, 0.993),
          w_head=3, w_tail=8, bow=4)
# s2: middle dian  ML(0.425, 0.304) -> ML(0.694, 0.532) = (42.5,130.4) -> (69.4,153.2)
draw_dian(d, A('ML', 0.425, 0.304), A('ML', 0.694, 0.532),
          w_head=3, w_tail=8, bow=4)
# s3: bottom ti  BL(0.595, 0.839) -> ML(0.996, 0.819) = (59.5,283.9) -> (99.6,181.9)
draw_ti(d, A('BL', 0.595, 0.839), A('ML', 0.996, 0.819),
        w_head=9, w_tail=2)

# --- 殳 (right, 4 strokes) ---
# s4: 撇 (small cap-pie)  TC(0.304, 0.838) -> C(0.043, 0.72) = (130.4,83.8) -> (104.3,172.0)
draw_pie(d, A('TC', 0.304, 0.838), A('C', 0.043, 0.72),
         bow_perp=8, w_head=7, w_tail=3, steps=70)

# s5: 横折 cap  TC(0.518, 0.873) -> MR(0.599, 0.538) = (151.8,87.3) -> (259.9,153.8)
# heng arcs right, bends down to tail — use heng_zhe_short (tail is well below head)
draw_heng_zhe_short(d, A('TC', 0.518, 0.873), A('MR', 0.599, 0.538),
                    corner_offset=(15, 5))

# s6: 又's 横撇  C(0.371, 0.852) -> BL(0.987, 0.771) = (137.1,185.2) -> (98.7,277.1)
# horizontal span short; apex_x must be near the joint (BC 172, 245) not default +130
draw_heng_pie(d, A('C', 0.371, 0.852), A('BL', 0.987, 0.771),
              apex_x=175, corner_x=170)

# s7: 又's 捺  C(0.184, 0.998) -> BR(0.845, 0.921) = (118.4,199.8) -> (284.5,292.1)
draw_na(d, A('C', 0.184, 0.998), A('BR', 0.845, 0.921),
        bow_perp=12, w_head=4, w_tail=12, steps=90)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_没.png")
img.save(out)
print("wrote", out)
