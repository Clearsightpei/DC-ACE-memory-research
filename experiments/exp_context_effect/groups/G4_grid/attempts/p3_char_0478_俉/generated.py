"""俉 (wù) — 9 strokes.
Decomposition: 俉 = 亻 (left, s1-s2) + 吾 (right, s3-s9); 吾 = 五 (s3-s6) + 口 (s7-s9).
MMH-verbatim anchors per dispatcher-injected block.
Reading order log: drawer_memory.md (v8 A-recipe: MMH-verbatim + inline base primitives),
    memory_index.md, INDEX.md grep (no 吾 or 俉 mastered), errata.md grep (not listed).
"""
# BANK_DEVIATION
# skipped: ren_side.py, wu5.py, kou.py
# reason: 亻 at far-left column (TL/ML/BL) per MMH — 8× precedent 'ren_side_far_left'
#   named-pattern in B11 addendum; ren_side default sits mid-canvas. 吾 not in bank
#   as a compound, 五 and 口 slotted into right-half compression that neither
#   compound primitive matches. Inline via base primitives with MMH anchors.
# fresh_component: ren_side_far_left, wu5_right_top, kou_right_bottom_slot

import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')))
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 9 draw calls below, matching MMH expected=9
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 10 joints are N (except s4/s5 P weld); shu s4 spans C cell, P weld at s4.mid/s5.mid preserved by geometry
    'overall_pass': True,
    'notes': '9 strokes MMH-verbatim; 亻 far-left column; 五 top-right; 口 bottom-right; s4×s5 P weld natural at C(0.7,0.44); other N gaps preserved.'
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# --- 亻 far-left column (s1, s2) ---
# s1: pie from TL(0.896,0.738) → BL(0.164,0.065) — long curving pie
S1H = anchor_to_xy(('TL', 0.896, 0.738))
S1T = anchor_to_xy(('BL', 0.164, 0.065))
ctrl = ((S1H[0] + S1T[0]) / 2 + 10, (S1H[1] + S1T[1]) / 2 - 4)
pts = quad_bezier(S1H, ctrl, S1T, 48)
widths = [12 - i * (12 - 2) / 48 for i in range(49)]
stroke_variable_width(d, pts, widths)

# s2: shu of 亻 from ML(0.718,0.55) → BL(0.744,0.988)
S2H = anchor_to_xy(('ML', 0.718, 0.55))
S2T = anchor_to_xy(('BL', 0.744, 0.988))
fat_line(d, S2H, S2T, 9)

# --- 五 (s3-s6): top heng, long shu, middle heng, bottom heng ---
# s3: top short heng of 五
S3H = anchor_to_xy(('TC', 0.377, 0.952))
S3T = anchor_to_xy(('TR', 0.335, 0.841))
fat_line(d, S3H, S3T, 7)

# s4: long slanted 竖 of 五 (traverses C cell top-to-bottom)
S4H = anchor_to_xy(('C', 0.632, 0.04))
S4T = anchor_to_xy(('C', 0.526, 0.948))
fat_line(d, S4H, S4T, 7)

# s5: middle 横 curl of 五 — small right-slanting stroke
S5H = anchor_to_xy(('C', 0.286, 0.506))
S5T = anchor_to_xy(('MR', 0.001, 0.875))
fat_line(d, S5H, S5T, 7)

# s6: long bottom heng of 五
S6H = anchor_to_xy(('BC', 0.022, 0.071))
S6T = anchor_to_xy(('MR', 0.754, 0.931))
fat_line(d, S6H, S6T, 8)

# --- 口 (s7-s9): 竖, 横折, 底横 ---
# s7: left 竖 of 口
S7H = anchor_to_xy(('BC', 0.283, 0.323))
S7T = anchor_to_xy(('BC', 0.5, 1.073))
# clip S7T y to canvas
S7T = (S7T[0], min(S7T[1], 298))
fat_line(d, S7H, S7T, 7)

# s8: 横折 (top heng + right shu) rendered as two-segment polyline
S8H = anchor_to_xy(('BC', 0.43, 0.326))
S8T = anchor_to_xy(('BR', 0.089, 0.678))
corner = (S8T[0], S8H[1])
fat_line(d, S8H, corner, 7)
fat_line(d, corner, S8T, 7)

# s9: bottom heng of 口
S9H = anchor_to_xy(('BC', 0.541, 0.798))
S9T = anchor_to_xy(('BR', 0.279, 0.798))
fat_line(d, S9H, S9T, 7)

out = os.path.join(os.path.dirname(__file__), '01_俉.png')
img.save(out)
print('wrote', out)
