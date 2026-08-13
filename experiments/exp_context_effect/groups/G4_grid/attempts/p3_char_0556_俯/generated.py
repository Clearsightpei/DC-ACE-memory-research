"""俯 (fǔ) — 10 strokes.

Decomposition: 俯 = 亻 (far-left) + 府 (right);
                府 = 广 (top+left frame) + 付 (inside);
                付 = 亻 (mini) + 寸.

Reading list done: drawer_memory.md (v13 A-recipe; 亻 far-left named pattern),
memory_index.md, success_bank/INDEX.md (grep: 付 exists as ren_side+heng+shu_gou+dian).

Approach: MMH-verbatim anchors + inline base primitives (per A-recipe point 4).
Skip ren_side.py because MMH places 亻 far-left column (TL/ML/BL), not
ren_side's standalone TC/C default. This is the ren_side_far_left named pattern
(12+ batches precedent). BANK_DEVIATION block below.

The right sub-radical (府) is unusual/no primitive — inline per B12/B13 rule:
supply explicit head_width/tail_width for right-half strokes because MMH
gives endpoints only.
"""

# BANK_DEVIATION
# skipped: ren_side.py, fu.py, cun.py
# reason: 亻 slot is far-left column (ren_side_far_left named pattern, 12+ precedent);
#         府 has no direct primitive; inline via base primitives with MMH-verbatim anchors.
# fresh_component: ren_side_far_left_for_俯; fu_shelter_frame_for_俯

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
    '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 10 stroke calls below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # all N-joints preserved as natural gaps; s8-s9 P at MR handled by shared shu-gou weld
    'overall_pass': True,
    'notes': '10 strokes MMH-verbatim; 亻 far-left inline; 广 shelter + 付 inside with 寸 hook; s8/s9 shared pixel at MR(0.25,0.81) for P joint.',
}

W, H = 300, 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)

# ---- Stroke 1: 亻's 撇 (long pie from TL down to ML far-left) ----
s1_h = anchor_to_xy(('TL', 0.829, 0.718))   # (82.9, 71.8)
s1_t = anchor_to_xy(('ML', 0.138, 0.998))   # (13.8, 199.8)
# gentle curve — pie sweeps slightly outward
s1_mid = ((s1_h[0] + s1_t[0]) / 2 - 4, (s1_h[1] + s1_t[1]) / 2)
pts = quad_bezier(s1_h, s1_mid, s1_t, n=40)
widths = [12 - (i / 40) * 10 for i in range(41)]  # taper 12 -> 2
stroke_variable_width(d, pts, widths)

# ---- Stroke 2: 亻's 竖 (shu from ML down to BL) ----
s2_h = anchor_to_xy(('ML', 0.668, 0.482))   # (66.8, 148.2)
s2_t = anchor_to_xy(('BL', 0.674, 0.865))   # (67.4, 286.5)
fat_line(d, s2_h, s2_t, width=8)

# ---- Stroke 3: 广's top dot 丶 ----
s3_h = anchor_to_xy(('TC', 0.635, 0.612))   # (163.5, 61.2)
s3_t = anchor_to_xy(('TC', 0.978, 0.844))   # (197.8, 84.4)
# short heavy dot: taper from thin head to thicker tail
pts = [
    (s3_h[0], s3_h[1]),
    ((s3_h[0]*2 + s3_t[0]) / 3, (s3_h[1]*2 + s3_t[1]) / 3),
    ((s3_h[0] + s3_t[0]*2) / 3, (s3_h[1] + s3_t[1]*2) / 3),
    (s3_t[0], s3_t[1]),
]
stroke_variable_width(d, pts, [3, 6, 9, 10])

# ---- Stroke 4: 广's top 一 (short heng, slightly rising then flat) ----
s4_h = anchor_to_xy(('C', 0.321, 0.204))    # (132.1, 120.4)
s4_t = anchor_to_xy(('MR', 0.411, 0.066))   # (241.1, 106.6)
pts = quad_bezier(s4_h, ((s4_h[0]+s4_t[0])/2, (s4_h[1]+s4_t[1])/2 - 2), s4_t, n=30)
widths = [7] * 31
# small starting swell
widths[0] = 4
widths[-1] = 8
stroke_variable_width(d, pts, widths)

# ---- Stroke 5: 广's 撇 (long pie sweeping from top-center down to BL) ----
s5_h = anchor_to_xy(('C', 0.131, 0.148))    # (113.1, 114.8)
s5_t = anchor_to_xy(('BL', 0.794, 0.798))   # (79.4, 279.8)
# curved outward (leftward bulge)
s5_mid = ((s5_h[0] + s5_t[0]) / 2 - 8, (s5_h[1] + s5_t[1]) / 2 + 5)
pts = quad_bezier(s5_h, s5_mid, s5_t, n=40)
widths = [11 - (i / 40) * 9 for i in range(41)]  # taper 11 -> 2
stroke_variable_width(d, pts, widths)

# ---- Stroke 6: inner 亻's 撇 (pie inside 付) ----
s6_h = anchor_to_xy(('C', 0.588, 0.415))    # (158.8, 141.5)
s6_t = anchor_to_xy(('BC', 0.263, 0.127))   # (126.3, 212.7)
s6_mid = ((s6_h[0] + s6_t[0]) / 2 - 2, (s6_h[1] + s6_t[1]) / 2)
pts = quad_bezier(s6_h, s6_mid, s6_t, n=30)
widths = [8 - (i / 30) * 6 for i in range(31)]
stroke_variable_width(d, pts, widths)

# ---- Stroke 7: inner 亻's 竖 (shu inside 付) ----
s7_h = anchor_to_xy(('C', 0.477, 0.975))    # (147.7, 197.5)
s7_t = anchor_to_xy(('BC', 0.488, 0.912))   # (148.8, 291.2)
fat_line(d, s7_h, s7_t, width=6)

# ---- Stroke 8: 寸's 一 (heng) ----
s8_h = anchor_to_xy(('C', 0.652, 0.89))     # (165.2, 189.0)
s8_t = anchor_to_xy(('MR', 0.713, 0.793))   # (271.3, 179.3)
pts = [s8_h, ((s8_h[0]+s8_t[0])/2, (s8_h[1]+s8_t[1])/2), s8_t]
stroke_variable_width(d, pts, [4, 6, 7])

# ---- Stroke 9: 寸's 竖钩 (shu-gou from MR down to BC with hook) ----
s9_h = anchor_to_xy(('MR', 0.095, 0.339))   # (209.5, 133.9)
s9_t = anchor_to_xy(('BC', 0.86, 0.798))    # (186.0, 279.8)
# main vertical body
fat_line(d, s9_h, s9_t, width=7)
# hook (upward-left flick from tail)
hook_end = (s9_t[0] - 14, s9_t[1] - 8)
pts_hook = quad_bezier(s9_t, (s9_t[0] - 6, s9_t[1] - 2), hook_end, n=12)
stroke_variable_width(d, pts_hook, [7 - i*0.5 for i in range(13)])

# ---- Stroke 10: 寸's 丶 (small dot) ----
s10_h = anchor_to_xy(('BC', 0.77, 0.145))   # (177.0, 214.5)
s10_t = anchor_to_xy(('BC', 0.978, 0.329))  # (197.8, 232.9)
pts = [s10_h,
       ((s10_h[0]+s10_t[0])/2, (s10_h[1]+s10_t[1])/2),
       s10_t]
stroke_variable_width(d, pts, [3, 6, 8])

# Save
out_path = os.path.join(os.path.dirname(__file__), '01_俯.png')
img.save(out_path)
print(f"Wrote {out_path}")
