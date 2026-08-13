"""佼 (jiǎo, handsome) — 8 strokes. 亻 + 交.

P-A-006 stroke-primitive layer + P-A-008 per-sub-component reasoning
+ P-A-009 quantitative BANK_DEVIATION reasoning.

Decomposition:
- 亻 (s1+s2): use ren_left bank primitive.
- 交 (s3-s8): no bank primitive; inline with MMH anchors verbatim.

--- P-A-007-v2 quantitative check for 亻 bank use ---
Bank ren_left native (s1 head→tail): (158.8, 73.8) → (80.6, 211.2)
  native dx=-78.2, dy=137.4, aspect=|dx|/dy=0.569
MMH target for 佼's 亻 (s1 head→tail): TL(0.867,0.659)→ML(0.141,0.983)
  cell-local abs: (86.7, 65.9) → (14.1, 198.3)
  target dx=-72.6, dy=132.4, aspect=0.548
Ratios: scale_y = 132.4/137.4 = 0.964; aspect ratio = 0.548/0.569 = 0.963
Both within [0.55, 1.2] tolerance → USE ren_left bank primitive.
Solve: (158.8*s + ox, 73.8*s + oy) = (86.7, 65.9) at s=0.964
  → ox = 86.7 - 153.09 = -66.4, oy = 65.9 - 71.14 = -5.2

--- 交 sub-component reasoning (P-A-008) ---
- s3 top dian: (153.8, 67.7) → (188.4, 92.0), short slanted dot.
- s4 long heng: (118.9, 123.9) → (229.7, 109.0), spans width ~111 px.
- s5 short pie: (129.8, 153.2) → (97.6, 201.6), small tilted 撇 under
  heng-left.
- s6 short dian: (194.8, 139.7) → (242.0, 176.1), small tilted 点 under
  heng-right.
- s7 big pie (X-cross left): (182.8, 172.9) → (104.0, 281.5), long 撇
  sweeping down-left. Joint P (welded) at BC with s8.
- s8 big na (X-cross right): (131.8, 198.3) → (273.3, 294.7), long 捺
  sweeping down-right. P-welded to s7 at (BC).

# BANK_DEVIATION
# skipped: (no bank primitive for 交 whole-radical; only stroke-primitives available)
# reason: 交 not in bank; per P-A-006 use stroke-primitive layer with MMH-verbatim anchors
# fresh_component: jiao_right_verbatim (inlined dian+heng+pie+dian+pie+na)
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 2 (ren_left inline) + 6 = 8
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # s7/s8 welded at BC (P), Ns via natural spacing
    'overall_pass': True,
    'notes': 'ren_left @ scale 0.964, ox=-66.4 oy=-5.2 for 亻; 交 inlined verbatim.',
}

import os
import sys

_BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
)
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw

from ren_left import draw_ren_left
from dian import draw_dian
from heng import draw_heng
from pie import draw_pie
from na import draw_na

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ------ 亻 (s1 + s2) via bank ren_left -----------------------------------
draw_ren_left(d, ox=-66.4, oy=-5.2, scale=0.964)

# ------ 交 (s3..s8) inlined per MMH anchors ------------------------------
# s3: top dian (short, slanting down-right)
draw_dian(d, (153.8, 67.7), (188.4, 92.0),
          w_head=3, w_tail=7, bow=3, steps=40)

# s4: long heng (slight upward slope)
draw_heng(d, (118.9, 123.9), (229.7, 109.0),
          width_head=6, width_tail=7)

# s5: short pie (under heng, left side)
draw_pie(d, (129.8, 153.2), (97.6, 201.6),
         bow_perp=5, w_head=5, w_tail=2, steps=50)

# s6: short dian (under heng, right side)
draw_dian(d, (194.8, 139.7), (242.0, 176.1),
          w_head=3, w_tail=7, bow=3, steps=40)

# s7: big pie (X-cross left arm)
draw_pie(d, (182.8, 172.9), (104.0, 281.5),
         bow_perp=14, w_head=8, w_tail=2, steps=90)

# s8: big na (X-cross right arm), P-welded to s7 at ~(BC)
draw_na(d, (131.8, 198.3), (273.3, 294.7),
        bow_perp=12, w_head=4, w_tail=13, steps=100)

_OUT = os.path.join(os.path.dirname(__file__), '01_佼.png')
img.save(_OUT)
print('WROTE', _OUT)
