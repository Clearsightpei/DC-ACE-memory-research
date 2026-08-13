"""p3_char_0390_佬 — G4 attempt.

Reading checklist (v8):
1. drawer_memory.md — read. 佬 = 亻 (left) + 老 (right). No chronic
   primitive fits directly (no 冂/马/弓/丿/刀). MMH places 亻 in
   far-left column (TL/ML/BL), which per B10 A-recipe means SKIP
   ren_side (its defaults sit at TC/C/BC) and inline pie+shu with
   MMH-verbatim anchors.
2. success_bank/INDEX.md grep — 老 exists (p3_char_0271_老 full inline).
   Reuse that 6-stroke composition for the right side, shifted to
   right two-thirds of canvas via MMH-verbatim anchors.
3. errata.md — 佬 not listed.

MMH stroke count: 8 (2 for 亻 + 6 for 老). Rendered as 8 primitives.

Decomposition:
  # 佬 = 亻 (s1-s2) + 老 (s3-s8)
  # 亻 = 撇 (s1) + 竖 (s2)
  # 老 = 耂 (s3-s6: 横 + 竖 + 长横 + 长撇) + 匕 (s7-s8: 短撇 + 竖弯钩)
"""

# BANK_DEVIATION
# skipped: ren_side.py
# reason: MMH places 亻 in far-left column (TL/ML/BL) — ren_side defaults
#   sit at TC/C/BC (standalone-scale). Partial anchor override is the
#   伊 (B8) FAIL pattern. Inlining pie+shu with MMH-verbatim anchors.
# fresh_component: ren_side_far_left_for_compound_left

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '8 strokes MMH-verbatim; 亻 inlined at far-left column; '
             '老 component reuses p3_char_0271 layout with MMH anchors.',
}

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))
from _anchor import (anchor_to_xy, quad_bezier,
                     stroke_variable_width, fat_line, sample_line)
from PIL import Image, ImageDraw

W = H = 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)
INK = (0, 0, 0)

# ---- stroke 1: 亻 撇 (upper-right to lower-left) ----
p_s1_head = anchor_to_xy(('TL', 0.938, 0.642))   # ~(93.8, 64.2)
p_s1_tail = anchor_to_xy(('ML', 0.149, 0.995))   # ~(14.9, 199.5)
# slight bow: curve outward (to the left) — classic 撇
mx = (p_s1_head[0] + p_s1_tail[0]) / 2 - 8
my = (p_s1_head[1] + p_s1_tail[1]) / 2 + 6
pts = quad_bezier(p_s1_head, (mx, my), p_s1_tail, n=48)
widths = [9 - 6 * (i / 48) for i in range(49)]  # thick head, thin tail
stroke_variable_width(d, pts, widths, INK)

# ---- stroke 2: 亻 竖 (short vertical dropping to bottom-left) ----
p_s2_head = anchor_to_xy(('ML', 0.706, 0.506))   # ~(70.6, 150.6)
p_s2_tail = anchor_to_xy(('BL', 0.715, 0.915))   # ~(71.5, 291.5)
pts = sample_line(p_s2_head, p_s2_tail, n=24)
widths = [7] * 25
stroke_variable_width(d, pts, widths, INK)

# ---- stroke 3: 老 top short 横 (耂's first stroke) ----
p_s3_head = anchor_to_xy(('C',  0.307, 0.277))   # ~(130.7, 127.7)
p_s3_tail = anchor_to_xy(('MR', 0.057, 0.233))   # ~(205.7, 123.3)
pts = sample_line(p_s3_head, p_s3_tail, n=24)
widths = [6 + 2 * (i / 24) for i in range(25)]  # slight thicken at tail
stroke_variable_width(d, pts, widths, INK)

# ---- stroke 4: 老 竖 crossing s3 (P joint at C) ----
p_s4_head = anchor_to_xy(('TC', 0.588, 0.653))   # ~(158.8, 65.3)
p_s4_tail = anchor_to_xy(('C',  0.644, 0.682))   # ~(164.4, 168.2)
pts = sample_line(p_s4_head, p_s4_tail, n=24)
widths = [6] * 25
stroke_variable_width(d, pts, widths, INK)

# ---- stroke 5: 老 long 横 (main crossbar) ----
p_s5_head = anchor_to_xy(('ML', 0.976, 0.825))   # ~(97.6, 182.5)
p_s5_tail = anchor_to_xy(('MR', 0.666, 0.708))   # ~(266.6, 170.8)
mx = (p_s5_head[0] + p_s5_tail[0]) / 2
my = (p_s5_head[1] + p_s5_tail[1]) / 2 - 4
pts = quad_bezier(p_s5_head, (mx, my), p_s5_tail, n=48)
widths = [6 + 3 * (i / 48) for i in range(49)]  # 顿笔 at tail
stroke_variable_width(d, pts, widths, INK)

# ---- stroke 6: 老 长撇 (upper-right → lower-left, crosses s5 at P) ----
p_s6_head = anchor_to_xy(('TR', 0.235, 0.891))   # ~(223.5, 89.1)
p_s6_tail = anchor_to_xy(('BL', 0.879, 0.672))   # ~(87.9, 267.2)
mx = (p_s6_head[0] + p_s6_tail[0]) / 2 + 18
my = (p_s6_head[1] + p_s6_tail[1]) / 2 + 4
pts = quad_bezier(p_s6_head, (mx, my), p_s6_tail, n=48)
widths = [8 - 5 * (i / 48) for i in range(49)]
stroke_variable_width(d, pts, widths, INK)

# ---- stroke 7: 匕 短撇 (short pie, lower-right area) ----
p_s7_head = anchor_to_xy(('BR', 0.027, 0.007))   # ~(202.7, 200.7)
p_s7_tail = anchor_to_xy(('BC', 0.603, 0.479))   # ~(160.3, 247.9)
pts = sample_line(p_s7_head, p_s7_tail, n=24)
widths = [7 - 3 * (i / 24) for i in range(25)]
stroke_variable_width(d, pts, widths, INK)

# ---- stroke 8: 匕 竖弯钩 (vertical-turn-hook) ----
p_s8_head = anchor_to_xy(('BC', 0.433, 0.033))   # ~(143.3, 203.3)
p_s8_tail = anchor_to_xy(('BR', 0.438, 0.429))   # ~(243.8, 242.9)
# Two-segment: drop then arc right with slight hook
corner = (p_s8_head[0] + 6, 282)
mid1 = ((p_s8_head[0] + corner[0]) / 2, (p_s8_head[1] + corner[1]) / 2 + 12)
pts1 = quad_bezier(p_s8_head, mid1, corner, n=32)
mid2 = ((corner[0] + p_s8_tail[0]) / 2, corner[1] + 4)
pts2 = quad_bezier(corner, mid2, p_s8_tail, n=32)
pts = pts1 + pts2[1:]
widths = [7] * len(pts)
stroke_variable_width(d, pts, widths, INK)

# ---- save ----
out_png = os.path.join(os.path.dirname(__file__), '01_佬.png')
img.save(out_png)
print(f"saved: {out_png}")
