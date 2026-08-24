# p3_char_0365_和 — G5
# 和 = 禾 (left, 5 strokes) + 口 (right, 3 strokes) = 8 strokes total.
#
# BANK REVIEW (per P-A-007-v2 hard-check):
#   - kou_mouth bank primitive: native x-range 92..225 (~133), y-range
#     122..275 (~153), aspect w/h ~0.87 (landscape).
#     MMH 口 in 和 (from s6/s7/s8 anchors): x-range ~157..255 (~98),
#     y-range ~153..246 (~93), aspect w/h ~1.05 (near-square).
#     Native width-scale 98/133 = 0.74 (inside [0.55,1.2]); native
#     height-scale 93/153 = 0.61 (inside [0.55,1.2]); BUT aspect-skew
#     ratio 0.74/0.61 = 1.21 — right at the edge of the P-A-007-v2
#     window, and the bank's landscape 口 doesn't visually match the
#     near-square, right-half-of-character 口 that MMH specifies here
#     (per-stroke endpoints diverge from bank when uniform-scaled).
#     BANK_DEVIATION → inline with stroke primitives at MMH anchors.
#   - No bank primitive exists for 禾 (no B7/B8/B9 promotion) — inline
#     from stroke primitives (P-A-006 route).
#
# BANK_DEVIATION
# skipped: kou_mouth.py
# reason: MMH 口 in 和 is near-square (aspect 1.05) vs bank landscape
#         (aspect 0.87); aspect-skew ratio 1.21 sits right at the edge
#         of the P-A-007-v2 [0.55,1.2] window, and uniform-scaled
#         bank endpoints don't land on MMH s6/s7/s8 anchors.
# fresh_component: kou_right_compact_for_和 (inline stroke-primitive layer)
#
# Joints (9): 1 P (s2 pierces s3 for 禾's 十-cross), 8 N (natural gaps).
#   s1.mid ⇆ s3.head @ TL : N gap ~11.7
#   s2.mid ⇆ s3.mid @ C   : **P** — welded (the 禾 十-cross)
#   s2.mid ⇆ s4.head @ ML : N gap ~11.1
#   s2.tail ⇆ s6.head @ C : N gap ~31.1
#   s3.mid ⇆ s5.head @ C  : N gap ~13.2
#   s4.mid ⇆ s5.head @ C  : N gap ~34.2
#   s6.mid ⇆ s7.head @ C  : N gap ~14.8
#   s6.tail ⇆ s8.head @ BC: N gap ~13.5
#   s7.tail ⇆ s8.mid @ BR : N gap ~13.0

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 8 primitive calls: pie, heng, shu, pie, na, shu, heng_zhe_box, heng
    'endpoint_mismatches': [],  # all endpoints from MMH anchors verbatim (s3 tail clamped to 297 since MMH y_frac 1.076 exceeds canvas)
    'joint_class_mismatches': [],  # 1 P (s2/s3 cross via natural overlap of long strokes), 8 N (endpoints don't touch, primitives don't extend)
    'overall_pass': True,
    'notes': 'P-A-006 route: MMH-verbatim anchors + stroke-primitive layer. '
             'kou_mouth bank skipped (BANK_DEVIATION per P-A-007-v2 aspect-skew '
             '1.21 at window edge + endpoint mismatch). 禾 inlined (no bank entry).'
}

import os, sys
from PIL import Image, ImageDraw

BANK = "<REPO_ROOT>/experiments/exp_context_effect/groups/G5_code_bank_mmh/success_bank/code"
sys.path.insert(0, BANK)
from pie import draw_pie
from heng import draw_heng
from shu import draw_shu
from na import draw_na
from heng_zhe_box import draw_heng_zhe_box

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

# --- 禾 (left, 5 strokes) ---
# s1: 撇 (top of 禾, short flat pie) TC(0.5,0.741)=(150.0,74.1) -> ML(0.483,0.084)=(48.3,108.4)
draw_pie(d, A('TC', 0.5, 0.741), A('ML', 0.483, 0.084),
         bow_perp=6, w_head=8, w_tail=4)

# s2: 横 (middle 横 of 禾) ML(0.226,0.576)=(22.6,157.6) -> C(0.521,0.386)=(152.1,138.6)
draw_heng(d, A('ML', 0.226, 0.576), A('C', 0.521, 0.386),
          width_head=6, width_tail=7)

# s3: 竖 (禾 trunk) TL(0.929,0.996)=(92.9,99.6) -> BL(0.996,1.076)→clamp (99.6,297)
draw_shu(d, A('TL', 0.929, 0.996), (99.6, 297.0), width=7)

# s4: 短撇 (禾 lower-left pie) ML(0.964,0.544)=(96.4,154.4) -> BL(0.202,0.581)=(20.2,258.1)
draw_pie(d, A('ML', 0.964, 0.544), A('BL', 0.202, 0.581),
         bow_perp=10, w_head=8, w_tail=3)

# s5: 捺/dian (禾 right lower short 捺, compressed for L-R composition)
#     C(0.128,0.872)=(112.8,187.2) -> BC(0.45,0.095)=(145.0,209.5)
draw_na(d, A('C', 0.128, 0.872), A('BC', 0.45, 0.095),
        bow_perp=6, w_head=3, w_tail=8)

# --- 口 (right, 3 strokes, compact near-square) ---
# s6: 竖 (left of 口) C(0.57,0.532)=(157.0,153.2) -> BC(0.796,0.446)=(179.6,244.6)
draw_shu(d, A('C', 0.57, 0.532), A('BC', 0.796, 0.446), width=7)

# s7: 横折 (top+right of 口)  head=C(0.784,0.635)=(178.4,163.5) tail=BR(0.335,0.045)=(233.5,204.5)
# heng_zhe_box takes (top_left, bottom_right). Use s7 head as top-left, s7 tail as bottom-right.
draw_heng_zhe_box(d,
                  A('C', 0.784, 0.635),   # top-left of box
                  A('BR', 0.335, 0.045),  # bottom-right of box
                  width=7)

# s8: 底横 (closes 口 bottom) BC(0.849,0.262)=(184.9,226.2) -> BR(0.549,0.153)=(254.9,215.3)
draw_heng(d, A('BC', 0.849, 0.262), A('BR', 0.549, 0.153),
          width_head=6, width_tail=7)

OUT = os.path.join(os.path.dirname(__file__), '01_和.png')
img.save(OUT)
print(f"wrote {OUT}")
