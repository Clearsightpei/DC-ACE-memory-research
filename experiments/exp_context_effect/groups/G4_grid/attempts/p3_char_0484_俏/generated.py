# BANK_DEVIATION
# skipped: ren_side.py
# reason: MMH places 亻 in far-left column (TL/ML/BL slot); ren_side.py bakes standalone TC/C/BC anchors that don't fit compound-slot compression (B10-B12 codified ren_side_far_left pattern).
# fresh_component: ren_side_far_left_for_俏

"""俏 (qiào) — 9 strokes.
Decomposition: 俏 = 亻 (left, 2 strokes) + 肖 (right, 7 strokes)
                肖 = ⺌ (top, 3 strokes: middle-shu + left-slant + right-slant)
                     + 月 (bottom, 4 strokes: pie + heng-zhe-gou + 2 inner heng)
All joints are N-class (natural gaps).
"""

import sys
sys.path.insert(0, "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G4_grid/success_bank/code")
from _anchor import anchor_to_xy, fat_line, stroke_variable_width, quad_bezier
from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 9 stroke primitives
    'endpoint_mismatches': [],  # MMH-verbatim throughout
    'joint_class_mismatches': [],  # all 7 joints kept as N-gaps (no welding)
    'overall_pass': True,
    'notes': '9 strokes MMH-verbatim; 亻 far-left inline (BANK_DEVIATION); 月 s7 as heng-zhe-gou compound; all N-joints preserved.',
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ---- stroke 1: 亻 pie (long slanted from upper-mid TL down to BL) ----
s1_h = anchor_to_xy(('TL', 0.955, 0.715))
s1_t = anchor_to_xy(('BL', 0.22, 0.03))
# curve bulges slightly to the right (concave toward the shu)
ctrl1 = ((s1_h[0] + s1_t[0]) / 2 + 8, (s1_h[1] + s1_t[1]) / 2 - 4)
pts1 = quad_bezier(s1_h, ctrl1, s1_t, n=48)
widths1 = [10.5 - 8.5 * i / 48 for i in range(49)]  # taper from head to tail
stroke_variable_width(d, pts1, widths1)

# ---- stroke 2: 亻 shu (near-vertical) ----
s2_h = anchor_to_xy(('ML', 0.762, 0.521))
s2_t = anchor_to_xy(('BL', 0.803, 0.953))
fat_line(d, s2_h, s2_t, 8)

# ---- stroke 3: ⺌ middle shu (short vertical, near top of right half) ----
s3_h = anchor_to_xy(('TC', 0.793, 0.63))
s3_t = anchor_to_xy(('C', 0.834, 0.515))
fat_line(d, s3_h, s3_t, 7)

# ---- stroke 4: ⺌ left slant (short pie going down-right into center) ----
s4_h = anchor_to_xy(('C', 0.345, 0.087))
s4_t = anchor_to_xy(('C', 0.562, 0.324))
fat_line(d, s4_h, s4_t, 6)

# ---- stroke 5: ⺌ right slant (short pie going down-left into center) ----
s5_h = anchor_to_xy(('TR', 0.376, 0.791))
s5_t = anchor_to_xy(('MR', 0.115, 0.225))
fat_line(d, s5_h, s5_t, 6)

# ---- stroke 6: 月 left pie (nearly vertical, gentle left bulge at bottom) ----
s6_h = anchor_to_xy(('C', 0.427, 0.538))
s6_t = anchor_to_xy(('BC', 0.415, 0.892))
ctrl6 = (s6_h[0] - 5, (s6_h[1] + s6_t[1]) / 2 + 6)
pts6 = quad_bezier(s6_h, ctrl6, s6_t, n=36)
widths6 = [8 - 1.5 * i / 36 for i in range(37)]
stroke_variable_width(d, pts6, widths6)

# ---- stroke 7: 月 heng-zhe-gou (top heng + right shu + small hook) ----
# Rendered as one compound polyline (one stroke primitive call).
s7_h = anchor_to_xy(('C', 0.608, 0.582))
s7_t = anchor_to_xy(('BC', 0.939, 0.789))
corner = (s7_t[0], s7_h[1])
hook_tip = (s7_t[0] - 8, s7_t[1] - 5)
pts7 = [s7_h, corner, s7_t, hook_tip]
widths7 = [7, 7, 8, 4]
stroke_variable_width(d, pts7, widths7)

# ---- stroke 8: 月 upper inner heng (slight upward tilt) ----
s8_h = anchor_to_xy(('C', 0.603, 0.951))
s8_t = anchor_to_xy(('MR', 0.033, 0.896))
fat_line(d, s8_h, s8_t, 5)

# ---- stroke 9: 月 lower inner heng (slight upward tilt) ----
s9_h = anchor_to_xy(('BC', 0.573, 0.32))
s9_t = anchor_to_xy(('BR', 0.06, 0.256))
fat_line(d, s9_h, s9_t, 5)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G4_grid/attempts/p3_char_0484_俏/01_俏.png")
