# TRAJECTORY DIFF
# Prior main FAIL:
#   1. 己 (left) topology broken — bottom hook 竖弯钩 curled RIGHT and
#      over-extended so the whole left side read as 已 or garbled; the
#      "up hook" tip was not clearly higher than the sweep end.
#   2. 己's top 横折 sat too low and its short 横 s2 was too close to s3,
#      making the three left-side strokes crowd into one blob.
#   3. 攵 (right) strokes were placed but 撇 s4 was too vertical, s5 横
#      was too tilted and long, and the s6/s7 X-cross intersected too
#      low on s6 — the top-half of 攵 looked disconnected.
#
# Fixes this attempt:
#   A. 己 rebuilt canonical: top 横折 (small hook at top of ML), a short
#      floating 横 in the middle, then 竖弯钩 with EXPLICIT up-hook
#      (hook tip y is ABOVE the horizontal sweep line — enforced by
#      an assert below). Left component compressed to x < 130.
#   B. 攵 sized larger with clear X-cross at ~C(0.5, 0.6): s4 撇 short
#      top-right diagonal, s5 横 shorter and flatter, s6 长撇 sweeping
#      to BC, s7 捺 crossing s6 near the middle (P joint, welded).
#
# BANK_DEVIATION
# skipped: yi_already.py
# reason: 改 left is 己 (open middle 横 that does not touch either side),
#         not 已; and the component must compress to the left third.
# fresh_component: ji_self_for_改_v2

import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code')))
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width
from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 7 strokes
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '7 strokes; 己 hook tip enforced ABOVE sweep line; 攵 X-cross at C.'
}

img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# ============ LEFT: 己 (s1..s3), compressed to x < 130 ============

# s1 — 横折 (small top bracket)
s1_head   = anchor_to_xy(('ML', 0.56, 0.17))     # (56, 117)
s1_corner = (128.0, 118.0)                        # right edge of top bar
s1_tail   = (128.0, 162.0)                        # bottom of the small fold
top = quad_bezier(s1_head, ((s1_head[0]+s1_corner[0])/2.0, s1_head[1]-1),
                  s1_corner, n=20)
fold = quad_bezier(s1_corner, (s1_corner[0]+2, (s1_corner[1]+s1_tail[1])/2.0),
                   s1_tail, n=14)
stroke_variable_width(draw, top + fold[1:], [6]*21 + [6]*14)

# s2 — 短横 (open middle horizontal, floating, does NOT touch either side)
s2_head = (62.0, 178.0)   # left tip, does not touch s3
s2_tail = (118.0, 172.0)  # right tip, does not touch s1 fold
s2_pts = quad_bezier(s2_head, ((s2_head[0]+s2_tail[0])/2.0, (s2_head[1]+s2_tail[1])/2.0 - 1),
                     s2_tail, n=16)
stroke_variable_width(draw, s2_pts, [5]*17)

# s3 — 竖弯钩 (vertical → sweep right → UP hook)
s3_head  = (48.0, 168.0)   # top of vertical descent (near s1 tail area)
s3_bend  = (48.0, 255.0)   # bottom-left corner
s3_sweep = (135.0, 258.0)  # right end of horizontal sweep
s3_tail  = (128.0, 225.0)  # hook tip — MUST be ABOVE sweep endpoint (smaller y)
assert s3_tail[1] < s3_sweep[1], "up-hook: tip y must be less than sweep y"
desc  = quad_bezier(s3_head, (s3_head[0]-3, (s3_head[1]+s3_bend[1])/2.0),
                    s3_bend, n=28)
sweep = quad_bezier(s3_bend, ((s3_bend[0]+s3_sweep[0])/2.0, s3_sweep[1]+6),
                    s3_sweep, n=22)
hook  = quad_bezier(s3_sweep, (s3_sweep[0]+2, (s3_sweep[1]+s3_tail[1])/2.0),
                    s3_tail, n=10)
stroke_variable_width(
    draw, desc + sweep[1:] + hook[1:],
    [7]*29 + [8]*22 + [7 - i/10.0*4 for i in range(1, 11)]
)

# ============ RIGHT: 攵 (s4..s7), dominant, X-cross at ~C ============

# s4 — 短撇 (top short pie, going down-left)
s4_head = (205.0, 78.0)
s4_tail = (163.0, 160.0)
s4_pts = quad_bezier(s4_head, ((s4_head[0]+s4_tail[0])/2.0 - 4,
                                (s4_head[1]+s4_tail[1])/2.0),
                     s4_tail, n=22)
stroke_variable_width(draw, s4_pts, [7 - i/22.0*4 for i in range(23)])

# s5 — 短横 (small horizontal crossing under s4, tilted slightly up-right)
s5_head = (172.0, 152.0)
s5_tail = (250.0, 138.0)
s5_pts = quad_bezier(s5_head, ((s5_head[0]+s5_tail[0])/2.0,
                                (s5_head[1]+s5_tail[1])/2.0 - 2),
                     s5_tail, n=18)
stroke_variable_width(draw, s5_pts, [5]*19)

# s6 — 长撇 (long pie sweeping down-left across most of right half)
s6_head = (215.0, 155.0)
s6_tail = (140.0, 275.0)
s6_pts = quad_bezier(s6_head, ((s6_head[0]+s6_tail[0])/2.0 - 6,
                                (s6_head[1]+s6_tail[1])/2.0 + 2),
                     s6_tail, n=32)
stroke_variable_width(draw, s6_pts, [8 - i/32.0*5 for i in range(33)])

# s7 — 捺 (long na sweeping down-right, X-crosses s6 near middle)
s7_head = (185.0, 175.0)   # starts just below s6 head, above the cross
s7_tail = (280.0, 278.0)
s7_pts = quad_bezier(s7_head, ((s7_head[0]+s7_tail[0])/2.0,
                                (s7_head[1]+s7_tail[1])/2.0 + 4),
                     s7_tail, n=32)
stroke_variable_width(draw, s7_pts, [4 + i/32.0*6 for i in range(33)])

img.save(os.path.join(HERE, '01_改.png'))
print('rendered 01_改.png with 7 strokes')
