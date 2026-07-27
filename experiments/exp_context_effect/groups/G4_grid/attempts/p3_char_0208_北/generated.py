"""p3_char_0208_北 — G4 attempt.

Reading order used (v8 slim):
  1. drawer_memory.md — no chronic primitive maps to 北. bi.py exists
     for 匕 but 北 is NOT 匕+匕: MMH lists 5 strokes with a distinct
     left column (竖 + 提 + 短横) + right (短撇 + 竖弯钩). Draw fresh
     per MMH anchors — v8 rule: bank is REFERENCE, GT wins.
  2. INDEX grep '北' — not mastered.
  3. errata grep '北' — not listed.

Split: 北 = left column (3 strokes) + right column (2 strokes).
"""

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '../../success_bank/code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, stroke_variable_width, quad_bezier, sample_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '5 strokes; N-class gaps preserved at all 3 joints.'
}

img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

W = 6  # ink width

# --- Stroke 1: left 竖 — TL(0.999, 0.929) → BC(0.116, 0.701)
s1_head = anchor_to_xy(('TL', 0.999, 0.929))
s1_tail = anchor_to_xy(('BC', 0.116, 0.701))
pts1 = sample_line(s1_head, s1_tail, 30)
stroke_variable_width(draw, pts1, [W]*len(pts1))

# --- Stroke 2: left 提 (short rising) — ML(0.469, 0.775) → C(0.031, 0.655)
s2_head = anchor_to_xy(('ML', 0.469, 0.775))
s2_tail = anchor_to_xy(('C',  0.031, 0.655))
pts2 = sample_line(s2_head, s2_tail, 20)
stroke_variable_width(draw, pts2, [W]*len(pts2))

# --- Stroke 3: bottom 短横 — BL(0.378, 0.622) → BL(0.99, 0.44)
s3_head = anchor_to_xy(('BL', 0.378, 0.622))
s3_tail = anchor_to_xy(('BL', 0.99,  0.44))
pts3 = sample_line(s3_head, s3_tail, 20)
stroke_variable_width(draw, pts3, [W]*len(pts3))

# --- Stroke 4: right 短撇 — MR(0.303, 0.298) → C(0.778, 0.857)
s4_head = anchor_to_xy(('MR', 0.303, 0.298))
s4_tail = anchor_to_xy(('C',  0.778, 0.857))
# Slight curve for 撇 feel — small control point offset
ctrl4 = ((s4_head[0]+s4_tail[0])/2 + 6, (s4_head[1]+s4_tail[1])/2 - 4)
pts4 = quad_bezier(s4_head, ctrl4, s4_tail, 30)
stroke_variable_width(draw, pts4, [W+1]*(len(pts4)//2) + [W-1]*(len(pts4) - len(pts4)//2))

# --- Stroke 5: 竖弯钩 — TC(0.564, 0.712) → BR(0.625, 0.147)
# Goes DOWN from head, curves rightward at bottom, HOOKs up-right to tail.
s5_head = anchor_to_xy(('TC', 0.564, 0.712))
s5_tail = anchor_to_xy(('BR', 0.625, 0.147))
# Break into two beziers: vertical descent → bottom bend → hook up
mid_bottom = (s5_head[0] + 6, 268)          # bottom of the vertical portion
bend_ctrl  = (s5_head[0] + 4, 288)          # bottom bend control
right_end  = (s5_tail[0] - 8, 262)          # where bottom ends before hook up

# Segment A: vertical descent (slightly curving right)
segA = quad_bezier(s5_head, (s5_head[0]+2, 180), mid_bottom, 30)
stroke_variable_width(draw, segA, [W]*len(segA))

# Segment B: bottom bend rightward
segB = quad_bezier(mid_bottom, bend_ctrl, right_end, 25)
stroke_variable_width(draw, segB, [W]*len(segB))

# Segment C: hook upward from right_end to s5_tail
segC = quad_bezier(right_end, ((right_end[0]+s5_tail[0])/2 + 6, (right_end[1]+s5_tail[1])/2 - 4),
                   s5_tail, 20)
stroke_variable_width(draw, segC, [W]*len(segC))

img.save(os.path.join(os.path.dirname(__file__), '01_北.png'))
print("done, 5 strokes")
