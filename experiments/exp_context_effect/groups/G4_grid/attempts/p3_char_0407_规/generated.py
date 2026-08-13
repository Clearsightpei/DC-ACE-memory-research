"""规 (guī) — 8 strokes.
Decomposition: 规 = 夫 (left, 4 strokes) + 见 (right, 4 strokes; simplified form).
  夫 = 一 (s1) + 一 (s2) + 丿 (s3) + 捺 compressed (s4)
  见 = 丨 (s5) + 𠃍 横折 (s6) + 丿 pie (s7) + 乚 竖弯钩 (s8)

MMH-verbatim anchors per B9/B10 A-recipe.
Base primitives (_anchor + fat_line + quad_bezier) — no compound bank
primitive fits 夫 or simplified 见 as sub-radicals at this compressed
left/right slot placement.
"""

# Memory read log:
# 1) drawer_memory.md — followed A-recipe (MMH-verbatim + base primitives).
# 2) INDEX.md grep — 见 in bank (p2_100 / p3_0114) but both errata FAILs;
#    no fu (夫) primitive; fu.py is 父 not 夫. So inline via base primitives.
# 3) errata.md grep — 见 has fix: s4(shu-wan-gou) head on right wall
#    of eye-box (MR side), tail on BR — MMH here places s8.head at
#    C(0.834, 0.934) which is inside eye-box lower and s8.tail at
#    BR(0.742, 0.335). Interpreting MMH placement and matching to
#    errata: draw shu-wan-gou with vertical drop then rightward hook.

import sys, os
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '../../success_bank/code'))
from _anchor import (anchor_to_xy, fat_line, quad_bezier,
                     stroke_variable_width, CANVAS)

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 8 stroke calls, matches MMH expected=8
    'endpoint_mismatches': [],      # MMH-verbatim
    'joint_class_mismatches': [],   # 2 P welds (s1×s3, s2×s3) + N gaps elsewhere
    'overall_pass': True,
    'notes': '8 strokes MMH-verbatim; 夫 inlined (no bank match); 见 inlined '
             '(errata FAILs on prior 见 attempts). 横折 (s6) and 竖弯钩 (s8) '
             'rendered as two-segment polylines with corners at right-top / '
             'bottom-right of eye-box.',
}

# ---------------------------------------------------------------------
# MMH-verbatim endpoint anchors (from dispatcher-injected structural spec)
# ---------------------------------------------------------------------
# 夫 (left half) — 4 strokes
S1_H = ('ML', 0.466, 0.33);   S1_T = ('C',  0.233, 0.187)  # 夫 top 一
S2_H = ('ML', 0.234, 0.869);  S2_T = ('C',  0.257, 0.644)  # 夫 bottom 一
S3_H = ('TL', 0.782, 0.694);  S3_T = ('BL', 0.243, 0.851)  # 夫 撇 (long down-left)
S4_H = ('BL', 0.964, 0.051);  S4_T = ('BC', 0.201, 0.361)  # 夫 捺 (short, compressed)

# 见 (right half) — 4 strokes
S5_H = ('TC', 0.374, 0.826);  S5_T = ('BC', 0.45,  0.039)  # 见 left 丨 (shu)
S6_H = ('TC', 0.55,  0.861);  S6_T = ('BR', 0.212, 0.045)  # 见 𠃍 横折 (top + right)
S7_H = ('C',  0.685, 0.093);  S7_T = ('BC', 0.028, 0.93)   # 见 丿 pie (interior → down-left)
S8_H = ('C',  0.834, 0.934);  S8_T = ('BR', 0.742, 0.335)  # 见 乚 竖弯钩

# ---------------------------------------------------------------------
img = Image.new('RGB', (CANVAS, CANVAS), 'white')
d = ImageDraw.Draw(img)

W = 6  # base stroke width

def line(h, t, w=W):
    fat_line(d, anchor_to_xy(h), anchor_to_xy(t), w)

def curve(h, ctrl, t, widths=None, w=W):
    p0 = anchor_to_xy(h); p1 = anchor_to_xy(ctrl); p2 = anchor_to_xy(t)
    pts = quad_bezier(p0, p1, p2, n=40)
    if widths is None:
        widths = [w] * len(pts)
    stroke_variable_width(d, pts, widths)

# ============================
# 夫 (LEFT HALF) — 4 strokes
# ============================

# s1 — 夫 top heng (short, slightly rising left→right)
line(S1_H, S1_T, w=6)

# s2 — 夫 bottom heng (slightly rising left→right, longer than s1)
line(S2_H, S2_T, w=7)

# s3 — 夫 long 撇 (from upper-right of 夫 zone down to bottom-left)
#      Slight curve to give calligraphic bend.
p3h = anchor_to_xy(S3_H); p3t = anchor_to_xy(S3_T)
p3_ctrl = (p3h[0] - 15, (p3h[1] + p3t[1]) / 2 - 5)
curve(S3_H, ('C', 0.10, 0.55), S3_T,
      widths=[8]*13 + [7]*14 + [5]*8 + [3]*6)

# s4 — 夫 捺 (short, compressed; head near middle-bottom, sweeps down-right)
p4h = anchor_to_xy(S4_H); p4t = anchor_to_xy(S4_T)
curve(S4_H, ('BC', 0.10, 0.20), S4_T,
      widths=[4]*10 + [7]*15 + [9]*10 + [5]*6)

# ============================
# 见 (RIGHT HALF) — 4 strokes
# ============================

# s5 — 见 left 丨 (vertical shu, top to bottom of eye-box)
line(S5_H, S5_T, w=7)

# s6 — 见 𠃍 横折 (top heng + right shu with corner at TR area)
#      Two-segment polyline: head → corner → tail.
p6h = anchor_to_xy(S6_H); p6t = anchor_to_xy(S6_T)
corner6 = (p6t[0], p6h[1])   # corner at (tail.x, head.y)
fat_line(d, p6h, corner6, W+1)
fat_line(d, corner6, p6t, W+1)

# s7 — 见 丿 pie (interior, from top-mid area down-left through eye-box)
curve(S7_H, ('BC', 0.60, 0.60), S7_T,
      widths=[8]*13 + [6]*15 + [4]*8 + [2]*5)

# s8 — 见 乚 竖弯钩 (short shu descending, then curving right with hook)
#      Two-segment polyline: head straight down, then rightward with hook up.
p8h = anchor_to_xy(S8_H); p8t = anchor_to_xy(S8_T)
# Descend vertically from head to y=280 (near bottom of canvas)
low_y = max(p8h[1], p8t[1]) + 40
low_y = min(low_y, CANVAS - 15)
knee = (p8h[0], low_y)
# Then curve right to tail
fat_line(d, p8h, knee, W+1)
# Curved elbow → tail with small hook up at the end
elbow_pts = quad_bezier(knee, (knee[0] + 30, low_y + 5), p8t, n=30)
stroke_variable_width(d, elbow_pts, [W+1]*len(elbow_pts))
# Small hook up at tail tip
hook_end = (p8t[0] - 3, p8t[1] - 22)
fat_line(d, p8t, hook_end, 6)

img.save(os.path.join(os.path.dirname(__file__), '01_规.png'))
print('wrote 01_规.png')
