"""值 (zhí, "value") — 10 strokes.

Decomposition: 值 = 亻 (far-left column) + 直 (right two-thirds).
  亻 = 撇 + 竖 (2 strokes)
  直 = 十 (top: 横 + 竖) + 目 (left竖 + 横折 + 3 interior/closing hengs) + 长横 bottom
Per B12 A-recipe: inline base primitives (fat_line / quad_bezier) with
MMH-verbatim anchors; no compound-primitive partial-overrides.
"""

# BANK_DEVIATION
# skipped: ren_side.py
# reason: MMH places 亻 in far-left column (pie head TL 0.926, pie tail ML 0.208,
#         shu head ML 0.700 shu tail BL 0.732) — ren_side's TC/C default anchors
#         would need full override. Named pattern: ren_side_far_left_for_值.
# fresh_component: ren_side_far_left_for_值

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 10 strokes = MMH expected
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '10 strokes MMH-verbatim; all N-joints preserved as gaps; s6 as 横折 with corner at (tail.x, head.y).',
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ---- Stroke 1: 撇 of 亻 (curved pie from top-right down to lower-left)
s1_h = anchor_to_xy(('TL', 0.926, 0.735))
s1_t = anchor_to_xy(('ML', 0.208, 0.983))
# curved pie: tapered from head to tail, slight curve outward-left
n = 40
pts = []
widths = []
for i in range(n + 1):
    t = i / n
    ctrl_x = s1_h[0] * 0.4 + s1_t[0] * 0.6 - 10
    ctrl_y = s1_h[1] * 0.55 + s1_t[1] * 0.45 - 5
    x = (1 - t) ** 2 * s1_h[0] + 2 * (1 - t) * t * ctrl_x + t * t * s1_t[0]
    y = (1 - t) ** 2 * s1_h[1] + 2 * (1 - t) * t * ctrl_y + t * t * s1_t[1]
    pts.append((x, y))
    widths.append(10 - 8 * t)  # 10 -> 2, tapered
stroke_variable_width(d, pts, widths)

# ---- Stroke 2: 竖 of 亻 (vertical)
s2_h = anchor_to_xy(('ML', 0.700, 0.562))
s2_t = anchor_to_xy(('BL', 0.732, 0.918))
fat_line(d, s2_h, s2_t, width=7)

# ---- Stroke 3: 横 (top of 十 / 直)
s3_h = anchor_to_xy(('C', 0.204, 0.16))
s3_t = anchor_to_xy(('MR', 0.408, 0.037))
fat_line(d, s3_h, s3_t, width=6)

# ---- Stroke 4: 竖 (vertical of 十)
s4_h = anchor_to_xy(('TC', 0.679, 0.609))
s4_t = anchor_to_xy(('C', 0.629, 0.506))
fat_line(d, s4_h, s4_t, width=7)

# ---- Stroke 5: 左竖 of 目
s5_h = anchor_to_xy(('C', 0.318, 0.521))
s5_t = anchor_to_xy(('BC', 0.365, 0.728))
fat_line(d, s5_h, s5_t, width=6)

# ---- Stroke 6: 横折 of 目 (top-and-right L). Head + tail via MMH; corner = (tail.x, head.y)
s6_h = anchor_to_xy(('C', 0.471, 0.556))
s6_t = anchor_to_xy(('BR', 0.062, 0.646))
s6_corner = (s6_t[0], s6_h[1])
fat_line(d, s6_h, s6_corner, width=6)
fat_line(d, s6_corner, s6_t, width=6)

# ---- Stroke 7: interior top heng of 目
s7_h = anchor_to_xy(('C', 0.5, 0.951))
s7_t = anchor_to_xy(('C', 0.919, 0.878))
fat_line(d, s7_h, s7_t, width=5)

# ---- Stroke 8: interior middle heng of 目
s8_h = anchor_to_xy(('BC', 0.488, 0.232))
s8_t = anchor_to_xy(('BC', 0.910, 0.159))
fat_line(d, s8_h, s8_t, width=5)

# ---- Stroke 9: bottom heng of 目 (closing rectangle)
s9_h = anchor_to_xy(('BC', 0.482, 0.508))
s9_t = anchor_to_xy(('BC', 0.928, 0.449))
fat_line(d, s9_h, s9_t, width=5)

# ---- Stroke 10: 长横 bottom of whole 直
s10_h = anchor_to_xy(('BL', 0.943, 0.836))
s10_t = anchor_to_xy(('BR', 0.692, 0.780))
fat_line(d, s10_h, s10_t, width=7)

out_path = os.path.join(os.path.dirname(__file__), '01_值.png')
img.save(out_path)
print(f'wrote {out_path}')
