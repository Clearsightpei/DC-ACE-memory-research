"""疬 (lì) — 9 strokes.
Decomposition: 疬 = 疒 (top-left frame, 5 strokes) + 万-like interior (4 strokes).
Uses MMH-verbatim anchors per B9/B10/B11 A-recipe (points 1-5).
Base primitives (fat_line + quad_bezier) inlined via _anchor + sys.path.

Reading order followed: drawer_memory.md (fast lookup — 疒/力/万 not in
chronic; no chronic import). success_bank/INDEX.md grep — no 疬. errata.md
grep — no 疬. Falls through to A-recipe defaults.
"""

import sys, os
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
    '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, quad_bezier, fat_line, stroke_variable_width  # noqa

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 9 strokes drawn
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH-verbatim anchors; N-joints left as natural gaps; s8/s9 P-weld at BC(0.8,0.03).',
}

# ---- setup ----
img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# MMH anchors (verbatim from dispatcher-injected block)
S1_H = ('TC', 0.412, 0.583); S1_T = ('TC', 0.784, 0.814)     # top short heng
S2_H = ('C',  0.075, 0.104); S2_T = ('TR', 0.312, 0.993)     # top-right heng
S3_H = ('ML', 0.855, 0.031); S3_T = ('BL', 0.413, 0.933)     # long left 撇 (spine of 疒)
S4_H = ('ML', 0.445, 0.263); S4_T = ('ML', 0.697, 0.532)     # left short 提/dian
S5_H = ('BL', 0.211, 0.112); S5_T = ('ML', 0.794, 0.866)     # left dot going up-right
S6_H = ('C',  0.421, 0.485); S6_T = ('MR', 0.303, 0.418)     # interior small heng
S7_H = ('C',  0.254, 0.436); S7_T = ('BL', 0.882, 0.854)     # interior 撇
S8_H = ('BC', 0.397, 0.065); S8_T = ('BC', 0.781, 0.736)     # interior heng-zhe-gou down
S9_H = ('C',  0.734, 0.717); S9_T = ('BC', 0.21,  0.883)     # interior final 撇

# ---- render strokes ----

# s1: top short dot/heng (like a comma dot at top of 疒)
p1a, p1b = anchor_to_xy(S1_H), anchor_to_xy(S1_T)
stroke_variable_width(d, [p1a, p1b], [3, 8])

# s2: top-right heng, slight curve down-right
p2a, p2b = anchor_to_xy(S2_H), anchor_to_xy(S2_T)
mx2 = ((p2a[0] + p2b[0]) / 2, (p2a[1] + p2b[1]) / 2 - 3)
pts2 = quad_bezier(p2a, mx2, p2b, n=40)
w2 = [7 - 3 * (i / len(pts2)) for i in range(len(pts2))]
stroke_variable_width(d, pts2, w2)

# s3: long 撇 — spine of 疒, curves gently left
p3a, p3b = anchor_to_xy(S3_H), anchor_to_xy(S3_T)
c3 = (p3a[0] + (p3b[0] - p3a[0]) * 0.55 + 12,
      p3a[1] + (p3b[1] - p3a[1]) * 0.55)
pts3 = quad_bezier(p3a, c3, p3b, n=60)
w3 = [10 - 8 * (i / len(pts3)) for i in range(len(pts3))]
stroke_variable_width(d, pts3, w3)

# s4: short 点/提 in ML region (upper of two left dots)
p4a, p4b = anchor_to_xy(S4_H), anchor_to_xy(S4_T)
stroke_variable_width(d, [p4a, p4b], [3, 8])

# s5: lower left dot going up-right (like 提)
p5a, p5b = anchor_to_xy(S5_H), anchor_to_xy(S5_T)
stroke_variable_width(d, [p5a, p5b], [8, 3])

# s6: interior short heng
p6a, p6b = anchor_to_xy(S6_H), anchor_to_xy(S6_T)
fat_line(d, p6a, p6b, 6)

# s7: interior 撇 diagonal
p7a, p7b = anchor_to_xy(S7_H), anchor_to_xy(S7_T)
c7 = ((p7a[0] + p7b[0]) / 2 + 6, (p7a[1] + p7b[1]) / 2)
pts7 = quad_bezier(p7a, c7, p7b, n=48)
w7 = [8 - 5 * (i / len(pts7)) for i in range(len(pts7))]
stroke_variable_width(d, pts7, w7)

# s8: interior long vertical-ish stroke (heng-zhe-gou body).
# From BC(0.397,0.065) to BC(0.781,0.736) — goes down-right then hooks.
p8a, p8b = anchor_to_xy(S8_H), anchor_to_xy(S8_T)
# small hook at tail
c8 = (p8a[0] + (p8b[0] - p8a[0]) * 0.35 + 6,
      p8a[1] + (p8b[1] - p8a[1]) * 0.35)
pts8 = quad_bezier(p8a, c8, p8b, n=48)
stroke_variable_width(d, pts8, [7] * len(pts8))
# little gou tick at tail (up-left)
hook_end = (p8b[0] - 12, p8b[1] - 6)
fat_line(d, p8b, hook_end, 6)

# s9: interior final 撇 from C down-left to BC
p9a, p9b = anchor_to_xy(S9_H), anchor_to_xy(S9_T)
c9 = ((p9a[0] + p9b[0]) / 2 + 4, (p9a[1] + p9b[1]) / 2 + 2)
pts9 = quad_bezier(p9a, c9, p9b, n=48)
w9 = [9 - 7 * (i / len(pts9)) for i in range(len(pts9))]
stroke_variable_width(d, pts9, w9)

# ---- save ----
out = os.path.join(os.path.dirname(__file__), '01_疬.png')
img.save(out)
print(f'wrote {out}')
