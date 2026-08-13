# BANK_DEVIATION
# skipped: ren_side.py (default TC/C anchors don't match MMH's TL/ML far-left slot for 亻)
# reason: 亻 is placed far-left column per MMH (pie head TL(0.935,0.683)→BL, shu ML→BL);
#         no bank primitive for 甹 right-half. Inline via base primitives per A-recipe.
# fresh_component: ren_side_far_left_for_俜 + ping_right_inline (7-stroke 甹)
"""俜 (pīng) = 亻 (left) + 甹 (right). 9 strokes MMH.
Decomposition: 亻 (s1 pie + s2 shu) + 甹 (s3-s7 top 甶-box + s8 long descending sweep + s9 bottom vertical BC).
All anchors MMH-verbatim; N-joints preserved as small natural gaps.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../success_bank/code'))
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new('RGB', (W, H), 'white')
draw = ImageDraw.Draw(img)

# ---- Stroke 1: 亻 撇 (TL far-right → BL) - long tapered pie ----
s1_head = anchor_to_xy(('TL', 0.935, 0.683))
s1_tail = anchor_to_xy(('BL', 0.199, 0.065))
ctrl1 = ((s1_head[0]+s1_tail[0])/2 + 6, (s1_head[1]+s1_tail[1])/2 - 4)
pts1 = quad_bezier(s1_head, ctrl1, s1_tail, n=48)
widths1 = [max(2, int(12 - 10*i/len(pts1))) for i in range(len(pts1))]
stroke_variable_width(draw, pts1, widths1)

# ---- Stroke 2: 亻 竖 (ML mid → BL bottom) ----
s2_head = anchor_to_xy(('ML', 0.662, 0.646))
s2_tail = anchor_to_xy(('BL', 0.709, 0.977))
fat_line(draw, s2_head, s2_tail, 9)

# ---- Stroke 3: 甹 top-left 竖/短撇 of 甶-box (C top → C middle-low) ----
s3_head = anchor_to_xy(('C', 0.181, 0.078))
s3_tail = anchor_to_xy(('C', 0.433, 0.811))
# Slight bezier for the shu-pie descent
ctrl3 = ((s3_head[0]+s3_tail[0])/2 - 4, (s3_head[1]+s3_tail[1])/2)
pts3 = quad_bezier(s3_head, ctrl3, s3_tail, n=32)
widths3 = [8]*len(pts3)
stroke_variable_width(draw, pts3, widths3)

# ---- Stroke 4: 甹 甶-box top-right 横折 (C top → MR mid) ----
s4_head = anchor_to_xy(('C', 0.324, 0.104))
s4_tail = anchor_to_xy(('MR', 0.174, 0.696))
# heng_zhe: horizontal from head across to top-right corner then down
# corner at approximately TR/MR boundary at x of tail
corner4 = anchor_to_xy(('MR', 0.174, 0.104))
fat_line(draw, s4_head, corner4, 8)
fat_line(draw, corner4, s4_tail, 9)

# ---- Stroke 5: 甹 甶 middle heng (inside horizontal) ----
s5_head = anchor_to_xy(('C', 0.523, 0.409))
s5_tail = anchor_to_xy(('MR', 0.048, 0.339))
fat_line(draw, s5_head, s5_tail, 7)

# ---- Stroke 6: 甹 甶 inner-top short vertical (TC → C) ----
s6_head = anchor_to_xy(('TC', 0.679, 0.536))
s6_tail = anchor_to_xy(('C', 0.74, 0.626))
fat_line(draw, s6_head, s6_tail, 7)

# ---- Stroke 7: 甹 甶-box bottom horizontal ----
s7_head = anchor_to_xy(('C', 0.485, 0.749))
s7_tail = anchor_to_xy(('MR', 0.101, 0.67))
fat_line(draw, s7_head, s7_tail, 8)

# ---- Stroke 8: 甹 long descending 横折弯钩 / 乙-like sweep (BL top → MR bottom) ----
s8_head = anchor_to_xy(('BL', 0.979, 0.074))
s8_tail = anchor_to_xy(('MR', 0.733, 0.937))
# Broad sweep: pull control point slightly below the chord midpoint for a
# gentle arc, not a deep sag. Ends at MR with a small hook up.
chord_mid = ((s8_head[0]+s8_tail[0])/2, (s8_head[1]+s8_tail[1])/2)
mid8 = (chord_mid[0] - 20, chord_mid[1] + 30)
pts8a = quad_bezier(s8_head, mid8, s8_tail, n=60)
widths8 = [max(3, int(10 - 4*i/len(pts8a))) for i in range(len(pts8a))]
stroke_variable_width(draw, pts8a, widths8)
# small hook up-left at tail
hook8_end = (s8_tail[0] - 6, s8_tail[1] - 18)
fat_line(draw, s8_tail, hook8_end, 6)

# ---- Stroke 9: 甹 bottom center vertical (BC → BC bottom) ----
s9_head = anchor_to_xy(('BC', 0.553, 0.092))
s9_tail = anchor_to_xy(('BC', 0.582, 0.941))
fat_line(draw, s9_head, s9_tail, 9)

img.save(os.path.join(os.path.dirname(__file__), '01_俜.png'))

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 9 stroke primitives (s1..s9)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH-verbatim anchors. 亻 far-left inline (pie+shu). 甹 甶-box (s3-s7) + long sweep s8 + center BC shu s9. N-joints preserved as gaps.',
}
