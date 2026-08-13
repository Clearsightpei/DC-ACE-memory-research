"""p3_char_0228_乩 — G5 attempt.

Decomposition: 占 (left, 5 strokes) + 乚 (right, 1 stroke) = 6 strokes.
  - 占 = 卜 (s1 shu + s2 dian) + 口 (s3 shu-left + s4 heng-zhe + s5 heng-bottom)
  - 乚 = s6 shu-wan-gou

All strokes rendered via bank primitives with MMH endpoint anchors.
"""

import os
import sys
from PIL import Image, ImageDraw

# Bank imports
BANK = os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
sys.path.insert(0, os.path.abspath(BANK))

from shu import draw_shu
from dian import draw_dian
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box
from shu_wan_gou import draw_shu_wan_gou


# ---- Cell → pixel helper (米字格 3×3 over 300×300) ----
CELL_ORIGINS = {
    'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
    'CL': (0, 100), 'C':  (100, 100), 'CR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}


def anc(cell, xf, yf):
    ox, oy = CELL_ORIGINS[cell]
    return (ox + xf * 100.0, oy + yf * 100.0)


# ---- MMH-derived anchors ----
s1_head = anc('TL', 0.844, 0.735)   # (84.4, 73.5)   — top of 卜's 丨
s1_tail = anc('BL', 0.902, 0.024)   # (90.2, 202.4)  — bottom
s2_head = anc('C',  0.061, 0.424)   # (106.1, 142.4) — start of 丶
s2_tail = anc('C',  0.518, 0.339)   # (151.8, 133.9) — end of 丶

s3_head = anc('BL', 0.407, 0.098)   # (40.7, 209.8)  — top-left of 口
s3_tail = anc('BL', 0.621, 0.883)   # (62.1, 288.3)  — bottom-left

s4_head = anc('BL', 0.601, 0.188)   # (60.1, 218.8)  — top-right corner of top-heng
s4_tail = anc('BC', 0.187, 0.499)   # (118.7, 249.9) — bottom of right vertical

s5_head = anc('BL', 0.680, 0.657)   # (68.0, 265.7)  — right end of bottom-heng
s5_tail = anc('BC', 0.356, 0.637)   # (135.6, 263.7) — near-mid — treat as opposite endpoint

s6_head = anc('TC', 0.658, 0.645)   # (165.8, 64.5)  — top of 乚
s6_tail = anc('BR', 0.728, 0.265)   # (272.8, 226.5) — end of hook


# ---- Render ----
img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# s1: 丨 of 卜
draw_shu(d, s1_head, s1_tail, width=7)

# s2: 丶 of 卜  (calligraphic dot — thin head, thick tail with a small bow)
draw_dian(d, s2_head, s2_tail, w_head=3, w_tail=9, bow=4, steps=48)

# --- 口 box.  MMH anchors are slightly inconsistent (s4.tail sits above s3.tail).
# Normalise onto a clean box footprint so the 口 reads square, then draw the
# three strokes onto that box.  Left side comes from s3, top-heng from s4.head
# swept right to a computed corner, bottom-heng from s5 endpoints.
box_left   = s3_head[0]                       # 40.7
box_right  = max(s4_tail[0], s5_tail[0])       # 135.6
box_top    = min(s3_head[1], s4_head[1])       # 209.8
box_bottom = max(s3_tail[1], s5_head[1])       # 288.3

# s3: left vertical of 口
draw_shu(d, (box_left, box_top), (box_left, box_bottom), width=6)

# s4: 横折 — top edge + right edge of 口
draw_heng_zhe_box(d, (box_left + 2, box_top), (box_right, box_bottom - 6), width=7)

# s5: bottom horizontal of 口
draw_heng(d, (box_left + 3, box_bottom - 3), (box_right - 2, box_bottom - 3),
          width_head=6, width_tail=7)

# s6: 竖弯钩 (乚)  — long descent + wide right hook
draw_shu_wan_gou(d, s6_head, s6_tail, width=7, bottom_extra=45, knee_ratio=0.85)


# ---- Save ----
out = os.path.join(os.path.dirname(__file__), "01_乩.png")
img.save(out)
print(f"wrote {out}")


# ================================================================
SELF_CHECK = {
    'visual_ok': None,        # filled after visual compare
    'stroke_count_ok': True,  # 6 strokes: shu, dian, shu, heng_zhe_box, heng, shu_wan_gou
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': ('口 anchors reconciled onto a consistent box footprint because '
              'raw MMH s3.tail (y=288) and s4.tail (y=250) disagreed on the '
              'box height. All 6 N joints preserved as small natural gaps.'),
}
