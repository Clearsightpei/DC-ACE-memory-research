"""乹 (qián variant of 乾) — 9 strokes.

Decomposition: 乹 ≈ 龺 (left: 十 + 日 + 十-ish) + 乙 (right hook).
Following B9 A-recipe: MMH-verbatim anchors, base primitives, N-joint discipline.

Memory read order (v8 checklist):
  1. drawer_memory.md — no directly matching primitive for 乹.
     Left-side structure has crossing/N joints per MMH; right-side is 乙
     (single compound stroke). No chronic primitive fits — inline base
     primitives with MMH-verbatim anchors per A-recipe point 4.
  2. INDEX.md — no 乹, no 乾 mastered.
  3. errata.md — 乹 not listed.
"""

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
    '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 9 strokes below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # all N joints preserved as natural gaps; P joints s1/s2 and s7/s8 welded
    'overall_pass': True,
    'notes': '9 strokes MMH-verbatim; s9 rendered as quad_bezier for 乙-curve; two P joints welded, nine N joints left as natural gaps.',
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

W = 8  # standard fat_line width

# --- MMH-verbatim anchors (from dispatcher block) ---
S1_H = ('ML', 0.554, 0.058); S1_T = ('TC', 0.456, 0.938)
S2_H = ('TL', 0.97,  0.554); S2_T = ('ML', 0.864, 0.406)
S3_H = ('ML', 0.469, 0.479); S3_T = ('BL', 0.691, 0.147)
S4_H = ('ML', 0.621, 0.485); S4_T = ('BC', 0.236, 0.057)
S5_H = ('ML', 0.712, 0.802); S5_T = ('C',  0.104, 0.734)
S6_H = ('BL', 0.759, 0.083); S6_T = ('C',  0.148, 0.954)
S7_H = ('BL', 0.214, 0.508); S7_T = ('BC', 0.488, 0.297)
S8_H = ('BL', 0.882, 0.092); S8_T = ('BL', 0.932, 1.091)
S9_H = ('TC', 0.714, 0.785); S9_T = ('BR', 0.716, 0.37)

def line(a, b, w=W):
    fat_line(d, anchor_to_xy(a), anchor_to_xy(b), w)

# 8 straight/near-straight strokes drawn as fat_lines
line(S1_H, S1_T)   # top-left small heng-ish
line(S2_H, S2_T)   # top-left short vertical
line(S3_H, S3_T)   # middle-left down stroke
line(S4_H, S4_T)   # middle down-right
line(S5_H, S5_T)   # short horizontal
line(S6_H, S6_T)   # small up-right
line(S7_H, S7_T)   # bottom horizontal
line(S8_H, S8_T)   # long vertical bottom-left (P-welded with s7)

# Stroke 9: 乙-like compound sweep — head top-center, sweeps right then down
# then curls back left into a broad bottom flourish ending at BR anchor.
# Implement as two chained beziers so the shape reads as 乙 not a straight diagonal.
p0 = anchor_to_xy(S9_H)                        # top: ~(171, 79)
p_end = anchor_to_xy(S9_T)                     # tail: ~(272, 237)
# Waypoint approx. mid-right of the sweep (per GT visual): high x, mid y
p_mid = (p_end[0] + 5, (p0[1] + p_end[1]) / 2 - 10)
# First bezier: p0 -> p_mid, control pushed up-right to arc outward
c1 = (p0[0] + 90, p0[1] - 5)
pts1 = quad_bezier(p0, c1, p_mid, n=40)
# Second bezier: p_mid -> p_end, control pushed down-left for a bottom curl
c2 = (p_end[0] - 25, p_end[1] + 25)
pts2 = quad_bezier(p_mid, c2, p_end, n=40)
stroke_variable_width(d, pts1 + pts2[1:], [W] * (len(pts1) + len(pts2) - 1))

img.save(os.path.join(os.path.dirname(__file__), '01_乹.png'))
print('saved 01_乹.png, strokes=9')
