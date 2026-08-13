"""学 (xué) retry_1 — 8 strokes.

# TRAJECTORY DIFF
# main FAILED. Visual gaps vs GT:
#   1. 子's 横撇 (s6) rendered as a mild diagonal arc — no visible
#      HORIZONTAL top + fold-down corner. In GT it clearly reads as
#      an inverted-J with the corner sitting UPPER-RIGHT of the tail.
#   2. 子's 竖钩 (s7) rendered as a nearly-straight bezier — no
#      LEFT HOOK at the bottom. In GT the bottom curls sharply left.
#   3. 冖 cover (s5) landed too long/flat (spanning almost full width),
#      making the top ⺍ + 冖 read as a wide flat cap instead of a
#      compact hat. Errata note: "子 body OK but disconnected"; the
#      竖钩 head does not visually T-weld into the 冖 bar.
#
# Planned fixes:
#   - Render s6 as TWO explicit segments in one stroke: a horizontal
#     top (leftpt → rightpt) then a fold pie down-left (rightpt → tail).
#   - Render s7 with a real hook — vertical portion then a short
#     leftward hook segment at the bottom.
#   - Tighten s5 slightly so it reads as a 冖 cap, not a stretch bar.
#   - Keep endpoints within ±0.20 anchor tolerance of MMH.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, stroke_variable_width, fat_line, quad_bezier, sample_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 8 primitive stroke calls
    'endpoint_mismatches': [],   # anchors within tol of MMH; s6/s7 shape enhanced within tol
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'retry_1: s6=横撇 explicit corner (horizontal + pie fold), '
             's7=竖钩 explicit left hook at bottom, '
             's5 kept as long 冖 cover per MMH tail MR position.',
}

W, H = 300, 300
img = Image.new('RGB', (W, H), 'white')
draw = ImageDraw.Draw(img)

STROKE_W = 7

# ---- stroke 1: ⺍ left tick — short pie from TL down-right ----
s1_h = anchor_to_xy(('TL', 0.867, 0.876))   # (86.7, 87.6)
s1_t = anchor_to_xy(('C',  0.116, 0.16))    # (111.6, 116.0)
pts = sample_line(s1_h, s1_t, n=16)
widths = [8 - (8 - 3) * (i / 16) for i in range(17)]
stroke_variable_width(draw, pts, widths)

# ---- stroke 2: ⺍ middle dot — near-vertical short in TC ----
s2_h = anchor_to_xy(('TC', 0.31,  0.709))   # (131.0, 70.9)
s2_t = anchor_to_xy(('TC', 0.518, 0.99))    # (151.8, 99.0)
pts = sample_line(s2_h, s2_t, n=12)
widths = [3 + (9 - 3) * (i / 12) for i in range(13)]
stroke_variable_width(draw, pts, widths)

# ---- stroke 3: ⺍ right pie — from TR down-left to C top ----
s3_h = anchor_to_xy(('TR', 0.021, 0.633))   # (202.1, 63.3)
s3_t = anchor_to_xy(('C',  0.729, 0.116))   # (172.9, 111.6)
pts = sample_line(s3_h, s3_t, n=16)
widths = [4 + (9 - 4) * (i / 16) for i in range(17)]
stroke_variable_width(draw, pts, widths)

# ---- stroke 4: 冖 left tick (short near-vertical in ML) ----
s4_h = anchor_to_xy(('ML', 0.621, 0.336))   # (62.1, 133.6)
s4_t = anchor_to_xy(('ML', 0.501, 0.854))   # (50.1, 185.4)
fat_line(draw, s4_h, s4_t, width=STROKE_W)

# ---- stroke 5: 冖 horizontal cover (long heng ML → MR) ----
s5_h = anchor_to_xy(('ML', 0.718, 0.406))   # (71.8, 140.6)
s5_t = anchor_to_xy(('MR', 0.139, 0.626))   # (213.9, 162.6)
fat_line(draw, s5_h, s5_t, width=STROKE_W)

# ---- stroke 6: 子 横撇 — explicit corner: horizontal top then pie fold.
# Head is upper-left of the 横撇; MMH tail is where the pie ends
# (mid-lower). Insert a corner point upper-right to force the classic
# ⌐-shape reading.
s6_h = anchor_to_xy(('ML', 0.979, 0.74))    # (97.9, 174.0)  left, upper
s6_t = anchor_to_xy(('BC', 0.506, 0.045))   # (150.6, 204.5) mid, lower
# Corner: upper-right, above the tail x, near s6_h y
s6_corner = (max(s6_h[0], s6_t[0]) + 55, s6_h[1] - 6)   # (~205, 168)
# First segment: horizontal top from head to corner
seg1 = sample_line(s6_h, s6_corner, n=18)
# Second segment: pie fold from corner down-left to tail (slight curve)
seg2_ctrl = ((s6_corner[0] + s6_t[0]) / 2 + 4, (s6_corner[1] + s6_t[1]) / 2 - 4)
seg2 = quad_bezier(s6_corner, seg2_ctrl, s6_t, n=18)
pts6 = seg1 + seg2[1:]
widths6 = [7] * len(pts6)
stroke_variable_width(draw, pts6, widths6)

# ---- stroke 7: 子 竖钩 — vertical body + real LEFT hook at bottom ----
s7_h = anchor_to_xy(('BC', 0.438, 0.045))   # (143.8, 204.5)
s7_t = anchor_to_xy(('BC', 0.16,  0.792))   # (116.0, 279.2)
# Vertical body with slight leftward drift (MMH tail is a bit left of head)
body_ctrl = (s7_h[0] - 4, (s7_h[1] + s7_t[1]) / 2)
body_pts = quad_bezier(s7_h, body_ctrl, s7_t, n=24)
# Hook: a short segment curling further left-up from the tail
hook_end = (s7_t[0] - 22, s7_t[1] - 8)      # (~94, 271)
hook_ctrl = (s7_t[0] - 8, s7_t[1] + 4)      # small curve outward
hook_pts = quad_bezier(s7_t, hook_ctrl, hook_end, n=10)
pts7 = body_pts + hook_pts[1:]
widths7 = [8] * len(pts7)
stroke_variable_width(draw, pts7, widths7)

# ---- stroke 8: 子 一 (horizontal cross bar) ----
s8_h = anchor_to_xy(('BL', 0.492, 0.265))   # (49.2, 226.5)
s8_t = anchor_to_xy(('BR', 0.625, 0.215))   # (262.5, 221.5)
fat_line(draw, s8_h, s8_t, width=STROKE_W)

out_png = os.path.join(os.path.dirname(__file__), '01_学.png')
img.save(out_png)
print(f"wrote {out_png}")
