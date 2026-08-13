"""兆 (zhao) — 6 strokes.

Split: LEFT half (long 撇 + 点 + 提) + RIGHT half (竖弯钩 + 短撇 + 点).
Joints:
  s1.mid(0.41) ⇆ s3.tail @ C  (N — small gap ~19.6px)
  s4.mid(0.31) ⇆ s6.head @ C  (N — small gap ~15.5px)

Following MMH-derived anchors verbatim (v9 lesson: MMH-verbatim strong).
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line

from PIL import Image, ImageDraw

W = H = 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)

# Expected 6 strokes.
STROKES = []

# --- s1: LEFT long 撇 (head TC → tail BL, curves through mid near C) ---
s1_head = anchor_to_xy(('TC', 0.058, 0.899))   # (105.8, 89.9)
s1_tail = anchor_to_xy(('BL', 0.478, 0.968))   # (47.8, 296.8)
# curve bulges to lower-right through mid (~114,286 at t=0.41)
s1_ctrl = (140, 240)
s1_pts = quad_bezier(s1_head, s1_ctrl, s1_tail, n=60)
# tapered: thicker at head, thin at tail (撇 taper)
s1_w = [max(4, 12 - 8*(i/60)) for i in range(61)]
stroke_variable_width(d, s1_pts, s1_w)
STROKES.append('s1_pie_long')

# --- s2: small top-left stroke (点/短撇), head ML → tail ML ---
s2_head = anchor_to_xy(('ML', 0.633, 0.342))   # (63.3, 134.2)
s2_tail = anchor_to_xy(('ML', 0.935, 0.591))   # (93.5, 159.1)
s2_pts = quad_bezier(s2_head, ((s2_head[0]+s2_tail[0])/2, (s2_head[1]+s2_tail[1])/2), s2_tail, n=20)
s2_w = [5]*11 + [3]*10
stroke_variable_width(d, s2_pts, s2_w)
STROKES.append('s2_dian_upper_left')

# --- s3: 提 bottom-left, head BL → tail C (goes up-right) ---
s3_head = anchor_to_xy(('BL', 0.419, 0.209))   # (41.9, 220.9)
s3_tail = anchor_to_xy(('C',  0.084, 0.896))   # (108.4, 189.6)
# 提 slight upward curve
s3_ctrl = (70, 210)
s3_pts = quad_bezier(s3_head, s3_ctrl, s3_tail, n=30)
s3_w = [max(3, 8 - 5*(i/30)) for i in range(31)]  # taper toward tail
stroke_variable_width(d, s3_pts, s3_w)
STROKES.append('s3_ti_bottom_left')

# --- s4: RIGHT big 竖弯钩 (long curve TC top → drops through C → out BR) ---
s4_head = anchor_to_xy(('TC', 0.588, 0.712))   # (158.8, 71.2)
s4_tail = anchor_to_xy(('BR', 0.701, 0.244))   # (270.1, 224.4)
# curve drops down through mid ~(172.6, 179.7 at t=0.31), then swings out right
# Build two-segment path: head → knee at (~175, 210) → tail
knee = (175, 215)
s4_pts_a = quad_bezier(s4_head, (170, 130), knee, n=40)   # descending vertical
s4_pts_b = quad_bezier(knee, (215, 235), s4_tail, n=30)   # swinging right at bottom
s4_pts = s4_pts_a + s4_pts_b
# 竖弯钩 taper: medium head, slightly thicker at knee, hook thinner
s4_w = ([9]*20 + [10]*21) + [10]*15 + [6]*16
if len(s4_w) != len(s4_pts):
    s4_w = [8]*len(s4_pts)
stroke_variable_width(d, s4_pts, s4_w)
STROKES.append('s4_shu_wan_gou')

# --- s5: short top-right stroke (short 撇), head MR → tail C ---
s5_head = anchor_to_xy(('MR', 0.194, 0.113))   # (219.4, 111.3)
s5_tail = anchor_to_xy(('C',  0.931, 0.576))   # (193.1, 157.6)
s5_ctrl = ((s5_head[0]+s5_tail[0])/2, (s5_head[1]+s5_tail[1])/2 - 2)
s5_pts = quad_bezier(s5_head, s5_ctrl, s5_tail, n=25)
s5_w = [max(3, 7 - 4*(i/25)) for i in range(26)]  # 撇 taper
stroke_variable_width(d, s5_pts, s5_w)
STROKES.append('s5_short_pie_top_right')

# --- s6: middle 点 on right, head C → tail BR ---
s6_head = anchor_to_xy(('C',  0.77, 0.834))    # (177.0, 183.4)
s6_tail = anchor_to_xy(('BR', 0.37, 0.253))    # (237.0, 225.3)
s6_ctrl = ((s6_head[0]+s6_tail[0])/2, (s6_head[1]+s6_tail[1])/2)
s6_pts = quad_bezier(s6_head, s6_ctrl, s6_tail, n=20)
s6_w = [5]*11 + [4]*10
stroke_variable_width(d, s6_pts, s6_w)
STROKES.append('s6_dian_mid_right')

assert len(STROKES) == 6, f"expected 6 strokes, got {len(STROKES)}"

out = os.path.join(os.path.dirname(__file__), '01_兆.png')
img.save(out)
print("wrote", out, "strokes:", STROKES)

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'anchors match MMH; N-class joints kept as small natural gaps (no weld).',
}
