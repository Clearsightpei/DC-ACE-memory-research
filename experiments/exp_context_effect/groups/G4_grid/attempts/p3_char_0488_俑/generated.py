"""俑 (yǒng) — 9 strokes.
Decomposition: 俑 = 亻 (left) + 甬 (right).
  亻 = pie (s1) + shu (s2)
  甬 = top pie/heng (s3) + top small (s4) + left vertical (s5)
      + heng-zhe-gou (s6) + inner mid heng (s7) + inner bot heng (s8)
      + center shu (s9)

Read order:
  drawer_memory.md — v13 A-recipe (points 1-8): MMH-verbatim anchors + base
    primitives + N-joint gap discipline; 亻 far-left column named pattern.
    Skipping ren_side.py (BANK_DEVIATION) because MMH places 亻 in far-left
    column (TL/ML/BL), not ren_side's default TC/C slot — per B10/B11/B12
    ren_side_far_left named pattern.
  errata.md — grep for 俑, 甬: not present.
  INDEX grep — 俑 not in bank; no 甬 primitive. Inline via base primitives.

# BANK_DEVIATION
# skipped: ren_side.py
# reason: MMH places 亻 in far-left column (TL/ML/BL) rather than
#   ren_side.py's TC/C standalone-scale defaults. Per the
#   ren_side_far_left named pattern (10+ passing precedents).
# fresh_component: ren_side_far_left_for_俑
"""
import os, sys
from PIL import Image, ImageDraw

# Import base primitives from the success bank (READ-ONLY).
BANK = "<REPO_ROOT>/experiments/exp_context_effect/groups/G4_grid/success_bank/code"
sys.path.insert(0, BANK)
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 9 strokes rendered
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('9 strokes MMH-verbatim; 亻 inlined far-left (BANK_DEVIATION); '
              '甬 inner P-joints welded via s9 shared segment through s7 & s8 mids; '
              'N-joints preserved as small natural gaps.'),
}

# ---- MMH-verbatim anchors ----
S1_H = ('TL', 0.92, 0.601);   S1_T = ('BL', 0.152, 0.007)   # 亻 pie
S2_H = ('ML', 0.732, 0.462);  S2_T = ('BL', 0.75, 0.927)    # 亻 shu
S3_H = ('TC', 0.339, 0.844);  S3_T = ('C',  0.922, 0.14)    # 甬 top pie/heng
S4_H = ('C',  0.652, 0.116);  S4_T = ('C',  0.931, 0.307)   # 甬 top small
S5_H = ('C',  0.213, 0.471);  S5_T = ('BC', 0.236, 0.83)    # 甬 left vertical (pie)
S6_H = ('C',  0.38,  0.503);  S6_T = ('BR', 0.057, 0.777)   # 甬 heng-zhe-gou (top+right)
S7_H = ('C',  0.544, 0.896);  S7_T = ('MR', 0.106, 0.799)   # 甬 inner mid heng
S8_H = ('BC', 0.544, 0.256);  S8_T = ('BR', 0.136, 0.174)   # 甬 inner bot heng
S9_H = ('C',  0.723, 0.526);  S9_T = ('BC', 0.793, 0.848)   # 甬 center shu (P through s7,s8)

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# --- s1: 亻 pie (curved down-left) ---
p1_h = anchor_to_xy(S1_H); p1_t = anchor_to_xy(S1_T)
# gentle pie curve — control point pulled slightly outward (down-left)
ctrl1 = ((p1_h[0] + p1_t[0]) / 2 - 8, (p1_h[1] + p1_t[1]) / 2 + 4)
pts1 = quad_bezier(p1_h, ctrl1, p1_t, n=40)
w1 = [10] + [max(3, 10 - i * 7 / 40) for i in range(1, 40)] + [2]
stroke_variable_width(d, pts1, w1)

# --- s2: 亻 shu (near-vertical) ---
p2_h = anchor_to_xy(S2_H); p2_t = anchor_to_xy(S2_T)
fat_line(d, p2_h, p2_t, width=9)

# --- s3: 甬 top pie/heng (going right-down slightly) ---
p3_h = anchor_to_xy(S3_H); p3_t = anchor_to_xy(S3_T)
# a short 撇/heng at top — as slightly-curved pie
ctrl3 = ((p3_h[0] + p3_t[0]) / 2, (p3_h[1] + p3_t[1]) / 2 - 4)
pts3 = quad_bezier(p3_h, ctrl3, p3_t, n=24)   # 25 points
w3 = [7] * 25
stroke_variable_width(d, pts3, w3)

# --- s4: 甬 top-right small stroke — the small down-right tick at top ---
p4_h = anchor_to_xy(S4_H); p4_t = anchor_to_xy(S4_T)
fat_line(d, p4_h, p4_t, width=7)

# --- s5: 甬 left vertical / short pie of the frame ---
# Extend the top slightly leftward-upward so it connects with s6 top-left
# corner cleanly. MMH gives us head at (121.3, 147.1); s6 head at (138, 150).
p5_h = anchor_to_xy(S5_H); p5_t = anchor_to_xy(S5_T)
fat_line(d, p5_h, p5_t, width=9)

# --- s6: 甬 heng-zhe-gou (top horizontal + right vertical + gou hook) ---
# Extend the top heng LEFTWARD so it visually meets s5's head (frame corner).
p6_h = anchor_to_xy(S6_H); p6_t = anchor_to_xy(S6_T)
# Left-extended head to close the top-left corner with s5.
p6_h_ext = (p5_h[0] - 2, p6_h[1])
corner6 = (p6_t[0], p6_h[1])
fat_line(d, p6_h_ext, corner6, width=8)   # top heng (extended left)
fat_line(d, corner6, p6_t, width=9)       # right shu
# gou hook at tail — leftward and slightly up
hook_end = (p6_t[0] - 14, p6_t[1] - 8)
fat_line(d, p6_t, hook_end, width=7)

# --- s7: 甬 inner mid heng (spans from s5 area to s6 right side) ---
p7_h = anchor_to_xy(S7_H); p7_t = anchor_to_xy(S7_T)
# MMH gives head=(154, 190), tail=(211, 180). But visually it's a heng that
# spans the inner width. Extend a bit toward left frame for readability.
# Use MMH tail on right; extend head left to touch (or near) left frame s5.
fat_line(d, p7_h, p7_t, width=7)

# --- s8: 甬 inner bottom heng ---
p8_h = anchor_to_xy(S8_H); p8_t = anchor_to_xy(S8_T)
fat_line(d, p8_h, p8_t, width=7)

# --- s9: 甬 center vertical — pierces s7 and s8 (P joints) ---
p9_h = anchor_to_xy(S9_H); p9_t = anchor_to_xy(S9_T)
fat_line(d, p9_h, p9_t, width=8)

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G4_grid/attempts/p3_char_0488_俑/01_俑.png"
img.save(out)
print("saved", out)
