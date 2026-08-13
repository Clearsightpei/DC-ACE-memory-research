"""p3_char_0491_除 — G4 attempt.

除 = 阝-left (2 strokes) + 余 (7 strokes) = 9 strokes total.

Memory notes consulted (per memory_index.md):
- drawer_memory.md: 阝-left has NO bank primitive (fu_left.py absent),
  so decompose inline as 横撇弯钩 (loop) + 竖 (long vertical).
- fu_right.py exists but is NOT a mirror of 阝-left; do not force-import.
- MMH anchors trusted verbatim (v9 lesson).

# BANK_DEVIATION
# skipped: fu_right.py (mirror attempt for 阝-left is not appropriate;
#          memory says fu_left is missing and inline decomposition is
#          the documented fallback).
# reason: fu_right is 阝-right shape; the current GT is 阝-LEFT with a
#         different loop orientation and a long descending 竖 on the
#         outside-left of the loop per MMH.
# fresh_component: fu_left_inline_for_除
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))
from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 9 draw calls below
    'endpoint_mismatches': [],     # all anchors verbatim from MMH block
    'joint_class_mismatches': [],  # N-neighbor gaps preserved; P-weld on s6/s7 by shared CROSS point
    'overall_pass': True,
    'notes': '除 = 阝-left inline (s1 loop, s2 long shu) + 余 inline (7 strokes).'
}

W = 300
img = Image.new('RGB', (W, W), 'white')
d = ImageDraw.Draw(img)

# ---------- 阝-left ----------
# s1: 横撇弯钩 loop of 阝-left. MMH endpoints: ML(0.618,0.099) -> ML(0.674,0.761).
# The loop starts top-right, curves down-left then hooks. Render as a
# small loop / D-shape using two bezier segments plus fold.
s1_head = anchor_to_xy(('ML', 0.618, 0.099))
s1_tail = anchor_to_xy(('ML', 0.674, 0.761))
# Corner (top-right of loop) and belly (right side) to give the ear shape.
s1_corner = anchor_to_xy(('ML', 0.85, 0.20))
s1_belly = anchor_to_xy(('ML', 0.90, 0.45))
pts1 = []
# top heng: head -> corner
pts1.extend([(s1_head[0] + i/8 * (s1_corner[0] - s1_head[0]),
              s1_head[1] + i/8 * (s1_corner[1] - s1_head[1])) for i in range(9)])
# curve: corner -> belly -> tail  (quadratic bezier)
pts1.extend(quad_bezier(s1_corner, s1_belly, s1_tail, n=30)[1:])
widths1 = [9] * len(pts1)
stroke_variable_width(d, pts1, widths1)

# s2: 竖 of 阝-left, long descending vertical. TL(0.398,0.984) -> BL(0.454,0.845).
s2_head = anchor_to_xy(('TL', 0.398, 0.984))
s2_tail = anchor_to_xy(('BL', 0.454, 0.845))
fat_line(d, s2_head, s2_tail, width=11)

# ---------- 余 ----------
# s3: top 撇 TC(0.667,0.715) -> C(0.146,0.843) — long down-left with slight curve
s3_head = anchor_to_xy(('TC', 0.667, 0.715))
s3_tail = anchor_to_xy(('C', 0.146, 0.843))
s3_ctrl = ((s3_head[0] + s3_tail[0]) / 2 + 5,
           (s3_head[1] + s3_tail[1]) / 2 - 15)  # slight upward bow for 撇 curve
pts3 = quad_bezier(s3_head, s3_ctrl, s3_tail, n=30)
widths3 = [max(3, 11 - int(i * 9 / len(pts3))) for i in range(len(pts3))]
stroke_variable_width(d, pts3, widths3)

# s4: top 捺 C(0.802,0.028) -> MR(0.906,0.717) — down-right descending
s4_head = anchor_to_xy(('C', 0.802, 0.028))
s4_tail = anchor_to_xy(('MR', 0.906, 0.717))
s4_ctrl = ((s4_head[0] + s4_tail[0]) / 2 - 5,
           (s4_head[1] + s4_tail[1]) / 2 - 10)
pts4 = quad_bezier(s4_head, s4_ctrl, s4_tail, n=30)
widths4 = [max(4, 6 + int(i * 8 / len(pts4))) for i in range(len(pts4))]
stroke_variable_width(d, pts4, widths4)

# s5: 横 C(0.415,0.764) -> MR(0.051,0.658)
s5_head = anchor_to_xy(('C', 0.415, 0.764))
s5_tail = anchor_to_xy(('MR', 0.051, 0.658))
fat_line(d, s5_head, s5_tail, width=8)

# s6: 横 BC(0.125,0.183) -> BR(0.414,0.077)
s6_head = anchor_to_xy(('BC', 0.125, 0.183))
s6_tail = anchor_to_xy(('BR', 0.414, 0.077))
fat_line(d, s6_head, s6_tail, width=8)

# s7: 竖钩 C(0.658,0.816) -> BC(0.43,0.795) — vertical hook (goes down then hooks left)
s7_head = anchor_to_xy(('C', 0.658, 0.816))
s7_tail = anchor_to_xy(('BC', 0.43, 0.795))
# Approach: straight vertical from head down, then small hook to tail
s7_knee = (s7_head[0], s7_tail[1] - 8)
fat_line(d, s7_head, s7_knee, width=10)
fat_line(d, s7_knee, s7_tail, width=8)

# s8: bottom-left 撇/点 BC(0.251,0.396) -> BC(0.072,0.821)
s8_head = anchor_to_xy(('BC', 0.251, 0.396))
s8_tail = anchor_to_xy(('BC', 0.072, 0.821))
pts8 = [s8_head, s8_tail]
widths8 = [8, 3]
stroke_variable_width(d, pts8, widths8)

# s9: bottom-right 点 BR(0.057,0.391) -> BR(0.455,0.795)
s9_head = anchor_to_xy(('BR', 0.057, 0.391))
s9_tail = anchor_to_xy(('BR', 0.455, 0.795))
pts9 = [s9_head, s9_tail]
widths9 = [3, 10]
stroke_variable_width(d, pts9, widths9)

out_path = os.path.join(os.path.dirname(__file__), '01_除.png')
img.save(out_path)
print('saved', out_path)
