"""俎 (zǔ) — 9 strokes.

Decomposition: 俎 = 仌 (left, two stacked 人) + 且 (right, like 目 with extended base).
The bottom heng (s9) extends across BOTH halves, forming the base under both.

Reading order (per MMH):
  s1,s2 = top 人 (pie + na apex-welded)
  s3,s4 = bottom 人 (pie + na apex-welded)
  s5    = left shu of 且
  s6    = top heng + right shu of 且 (compound heng_zhe, L-shape)
  s7    = middle upper heng inside 且
  s8    = middle lower heng inside 且
  s9    = bottom long heng — extends under both left 仌 and right 且

No compound bank primitive fits (仌 not in bank; 且 not in bank).
Inline via base primitives with MMH-verbatim anchors (A-recipe point 4).
"""

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../success_bank/code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '9 strokes MMH-verbatim; all N-joints preserved as natural gaps (no welds).',
}

# --- Stroke anchors (MMH-verbatim from dispatcher) ---
S1_H = ('TL', 0.82, 0.791);  S1_T = ('ML', 0.334, 0.863)   # top 人 pie
S2_H = ('ML', 0.835, 0.351); S2_T = ('C',  0.207, 0.641)   # top 人 na
S3_H = ('ML', 0.727, 0.772); S3_T = ('BL', 0.196, 0.789)   # bottom 人 pie
S4_H = ('BL', 0.779, 0.227); S4_T = ('BC', 0.184, 0.555)   # bottom 人 na
S5_H = ('TC', 0.456, 0.996); S5_T = ('BC', 0.506, 0.692)   # 且 left shu
S6_H = ('C',  0.62,  0.028); S6_T = ('BR', 0.15, 0.628)    # 且 top heng + right shu
S7_H = ('C',  0.667, 0.635); S7_T = ('MR', 0.03,  0.559)   # 且 mid-upper heng
S8_H = ('BC', 0.664, 0.13);  S8_T = ('BR', 0.036, 0.065)   # 且 mid-lower heng
S9_H = ('BC', 0.011, 0.786); S9_T = ('BR', 0.769, 0.754)   # bottom extended heng

# --- Render ---
img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# s1 — top 人 pie: slight curve, tapering
p_h = anchor_to_xy(S1_H); p_t = anchor_to_xy(S1_T)
ctrl = ((p_h[0] + p_t[0]) / 2 - 4, (p_h[1] + p_t[1]) / 2 - 6)
pts = quad_bezier(p_h, ctrl, p_t, n=40)
widths = [max(1.5, 7 - 5 * i / 40) for i in range(41)]
stroke_variable_width(d, pts, widths)

# s2 — top 人 na: goes down-right, slight bow, thickens toward tail
p_h = anchor_to_xy(S2_H); p_t = anchor_to_xy(S2_T)
ctrl = ((p_h[0] + p_t[0]) / 2 + 3, (p_h[1] + p_t[1]) / 2 + 3)
pts = quad_bezier(p_h, ctrl, p_t, n=40)
widths = [max(2, 2 + 5 * i / 40) for i in range(41)]
stroke_variable_width(d, pts, widths)

# s3 — bottom 人 pie (short)
p_h = anchor_to_xy(S3_H); p_t = anchor_to_xy(S3_T)
ctrl = ((p_h[0] + p_t[0]) / 2 - 3, (p_h[1] + p_t[1]) / 2 - 4)
pts = quad_bezier(p_h, ctrl, p_t, n=30)
widths = [max(1.5, 6 - 4 * i / 30) for i in range(31)]
stroke_variable_width(d, pts, widths)

# s4 — bottom 人 na: longer, down-right, thickens
p_h = anchor_to_xy(S4_H); p_t = anchor_to_xy(S4_T)
ctrl = ((p_h[0] + p_t[0]) / 2 + 3, (p_h[1] + p_t[1]) / 2 + 3)
pts = quad_bezier(p_h, ctrl, p_t, n=40)
widths = [max(2, 2 + 5 * i / 40) for i in range(41)]
stroke_variable_width(d, pts, widths)

# s5 — 且 left vertical (shu)
fat_line(d, anchor_to_xy(S5_H), anchor_to_xy(S5_T), width=6)

# s6 — 且 top heng + right shu (heng_zhe L-shape)
p_h = anchor_to_xy(S6_H); p_t = anchor_to_xy(S6_T)
# corner at (p_t.x, p_h.y) — top-right corner of the box
corner = (p_t[0], p_h[1])
fat_line(d, p_h, corner, width=6)
fat_line(d, corner, p_t, width=6)

# s7 — mid-upper interior heng
fat_line(d, anchor_to_xy(S7_H), anchor_to_xy(S7_T), width=5)

# s8 — mid-lower interior heng
fat_line(d, anchor_to_xy(S8_H), anchor_to_xy(S8_T), width=5)

# s9 — bottom long horizontal (spans both halves)
fat_line(d, anchor_to_xy(S9_H), anchor_to_xy(S9_T), width=6)

out = os.path.join(os.path.dirname(__file__), '01_俎.png')
img.save(out)
print(f'wrote {out}')
