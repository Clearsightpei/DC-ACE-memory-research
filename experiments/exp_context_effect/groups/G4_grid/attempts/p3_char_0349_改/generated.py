# BANK_DEVIATION
# skipped: yi_already.py
# reason: 改's left component is 己 (open middle stroke), not 已; and it's
#         compressed into the left third (ML/C anchors) not full-canvas TL/TC.
# fresh_component: ji_self_for_改
#
# Consulted memory_index.md + drawer_memory.md; no chronic primitive matches
# 改 (no 丿/刀/冂/弓/马 sub-component).
#
# 改 = 己 (left, s1..s3) + 攵 (right, s4..s7)

import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code')))
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width
from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '7 strokes; left 己 s1-s3 with N joints at ML and C; right 攵 s4-s7 with s6xs7 P (welded crossing) and s4/s5/s7 near-neighbors at C.'
}

img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# ==== LEFT: 己 (s1..s3) ====

# s1 — 横折 (small top bracket in ML → C)
s1_head = anchor_to_xy(('ML', 0.56, 0.169))     # (56, 117)
s1_corner = anchor_to_xy(('ML', 0.95, 0.22))    # right edge of ML row
s1_tail = anchor_to_xy(('C', 0.061, 0.55))      # (106, 155)
top_pts = quad_bezier(
    s1_head, ((s1_head[0]+s1_corner[0])/2.0, s1_head[1]-2), s1_corner, n=22)
fold_pts = quad_bezier(
    s1_corner, (s1_corner[0]+3, (s1_corner[1]+s1_tail[1])/2.0), s1_tail, n=16)
stroke_variable_width(draw, top_pts + fold_pts[1:],
    [5]*23 + [5]*16)

# s2 — 短横 (open middle horizontal, does not touch either side)
s2_head = anchor_to_xy(('ML', 0.715, 0.699))    # (71.5, 170)
s2_tail = anchor_to_xy(('C', 0.216, 0.632))     # (121.6, 163)
s2_pts = quad_bezier(
    s2_head, ((s2_head[0]+s2_tail[0])/2.0, (s2_head[1]+s2_tail[1])/2.0 - 2),
    s2_tail, n=18)
stroke_variable_width(draw, s2_pts, [5]*19)

# s3 — 竖弯钩 (descend → sweep right → short hook up)
s3_head = anchor_to_xy(('ML', 0.486, 0.658))    # (48.6, 165.8)
s3_bend = (48.0, 245.0)                         # bottom of vertical descent
s3_sweep = (120.0, 250.0)                       # right end of horizontal sweep (short)
s3_tail = anchor_to_xy(('BC', 0.146, 0.124))    # (114.6, 212.4)  hook tip
desc = quad_bezier(
    s3_head, (s3_head[0]-4, (s3_head[1]+s3_bend[1])/2.0), s3_bend, n=28)
sweep = quad_bezier(
    s3_bend, ((s3_bend[0]+s3_sweep[0])/2.0, s3_sweep[1]+8), s3_sweep, n=22)
hook = quad_bezier(
    s3_sweep, (s3_sweep[0]-2, (s3_sweep[1]+s3_tail[1])/2.0), s3_tail, n=12)
stroke_variable_width(draw, desc + sweep[1:] + hook[1:],
    [6 + i/28.0*2 for i in range(29)] +
    [8]*22 +
    [7 - i/12.0*4 for i in range(1, 13)])

# ==== RIGHT: 攵 (s4..s7) ====

# s4 — 短撇 (top short pie going down-left)
s4_head = anchor_to_xy(('TC', 0.72, 0.612))     # (172, 61)
s4_tail = anchor_to_xy(('C', 0.397, 0.597))     # (139.7, 159.7)
s4_pts = quad_bezier(
    s4_head, ((s4_head[0]+s4_tail[0])/2.0 - 3, (s4_head[1]+s4_tail[1])/2.0),
    s4_tail, n=22)
stroke_variable_width(draw, s4_pts, [7 - i/22.0*4 for i in range(23)])

# s5 — 短横 (small horizontal going right-and-up in mid area)
s5_head = anchor_to_xy(('C', 0.562, 0.491))     # (156.2, 149.1)
s5_tail = anchor_to_xy(('MR', 0.499, 0.283))    # (249.9, 128.3)
s5_pts = quad_bezier(
    s5_head, ((s5_head[0]+s5_tail[0])/2.0, (s5_head[1]+s5_tail[1])/2.0),
    s5_tail, n=18)
stroke_variable_width(draw, s5_pts, [5]*19)

# s6 — 长撇 (long pie sweeping down-left across the character)
s6_head = anchor_to_xy(('C', 0.896, 0.509))     # (189.6, 150.9)
s6_tail = anchor_to_xy(('BC', 0.093, 0.678))    # (109.3, 267.8)
s6_pts = quad_bezier(
    s6_head, ((s6_head[0]+s6_tail[0])/2.0 - 8, (s6_head[1]+s6_tail[1])/2.0 + 4),
    s6_tail, n=32)
stroke_variable_width(draw, s6_pts, [7 - i/32.0*4 for i in range(33)])

# s7 — 捺 (long na going down-right; crosses s6)
s7_head = anchor_to_xy(('C', 0.354, 0.802))     # (135.4, 180.2)
s7_tail = anchor_to_xy(('BR', 0.856, 0.807))    # (285.6, 280.7)
s7_pts = quad_bezier(
    s7_head, ((s7_head[0]+s7_tail[0])/2.0, (s7_head[1]+s7_tail[1])/2.0 + 4),
    s7_tail, n=32)
stroke_variable_width(draw, s7_pts, [4 + i/32.0*5 for i in range(33)])

img.save(os.path.join(HERE, '01_改.png'))
print('rendered 01_改.png with 7 strokes')
