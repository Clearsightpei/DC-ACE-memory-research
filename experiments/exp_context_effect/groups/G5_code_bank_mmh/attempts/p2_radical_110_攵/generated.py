# 攵 (pu / rap-radical, 4 strokes)
# All 4 strokes render via bank primitives — no BANK_DEVIATION needed.
#   s1  long pie from top-center down to bottom-left  -> draw_pie
#   s2  short horizontal (slight up-slant) mid-body   -> draw_heng
#   s3  lower pie from center down to bottom-left     -> draw_pie
#   s4  na from mid-left down to bottom-right         -> draw_na
# s3 and s4 cross piercingly (P joint) forming the bottom X of 攵.

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from pie import draw_pie
from na import draw_na
from heng import draw_heng

W = H = 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)


# ---- 米字格 anchor helper (3x3 cells, each 100x100 on 300x300 canvas) ----
_CELL_ORIGINS = {
    'TL': (0,   0), 'TC': (100,  0), 'TR': (200,  0),
    'ML': (0, 100), 'C':  (100,100), 'MC': (100,100), 'MR': (200,100),
    'BL': (0, 200), 'BC': (100,200), 'BR': (200,200),
}

def anchor(cell, xf, yf):
    ox, oy = _CELL_ORIGINS[cell]
    return (ox + xf * 100, oy + yf * 100)


# ---- Stroke 1: long 撇 (upper pie) ----
# MMH: head @ TC(0.172, 0.756) tail @ BL(0.639, 0.039)
s1_head = anchor('TC', 0.172, 0.756)   # ~ (117.2,  75.6)
s1_tail = anchor('BL', 0.639, 0.039)   # ~ ( 63.9, 207.9)
draw_pie(d, s1_head, s1_tail, bow_perp=14, w_head=8, w_tail=3, steps=90)


# ---- Stroke 2: short 横 (slight up-slant) ----
# MMH: head @ C(0.16, 0.436)  tail @ MR(0.188, 0.26)
s2_head = anchor('C',  0.16,  0.436)   # ~ (116.0, 143.6)
s2_tail = anchor('MR', 0.188, 0.26)    # ~ (218.8, 126.0)
draw_heng(d, s2_head, s2_tail, width_head=7, width_tail=8)


# ---- Stroke 3: lower 撇 (pie going down-left, crosses s4) ----
# MMH: head @ C(0.582, 0.471) tail @ BL(0.565, 0.81)
s3_head = anchor('C',  0.582, 0.471)   # ~ (158.2, 147.1)
s3_tail = anchor('BL', 0.565, 0.81)    # ~ ( 56.5, 281.0)
draw_pie(d, s3_head, s3_tail, bow_perp=10, w_head=8, w_tail=3, steps=90)


# ---- Stroke 4: 捺 (na going down-right, crosses s3 at BC — P joint) ----
# MMH: head @ ML(0.952, 0.758) tail @ BR(0.517, 0.9)
s4_head = anchor('ML', 0.952, 0.758)   # ~ ( 95.2, 175.8)
s4_tail = anchor('BR', 0.517, 0.9)     # ~ (251.7, 290.0)
draw_na(d, s4_head, s4_tail, bow_perp=10, w_head=4, w_tail=12, steps=90)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 primitives: pie + heng + pie + na
    'endpoint_mismatches': [], # anchors used verbatim from MMH block
    'joint_class_mismatches': [],  # s3xs4 P join achieved by geometric cross at BC
    'overall_pass': True,
    'notes': 'All 4 strokes from bank primitives (pie x2, heng, na). '
             'No BANK_DEVIATION. s3/s4 form the bottom X (P joint at BC). '
             's1/s2 have small natural gap (N joint, per MMH).',
}


out = pathlib.Path(__file__).parent / '01_攵.png'
img.save(out)
print(f'wrote {out}')
