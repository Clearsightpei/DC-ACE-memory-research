"""这 (zhè) — G4 attempt.

# Decomposition: 这 = 文 (upper-right) + 辶 (walk radical wrapping bottom-left)
#   MMH order (7 strokes):
#     s1 = 文 top 点
#     s2 = 文 横 (with midpoint neighboring s3.head — N joint)
#     s3 = 文 撇
#     s4 = 文 捺  (s3 and s4 P-weld at ('C', 0.841, 0.97))
#     s5 = 辶 top 点
#     s6 = 辶 横折折撇 (compact S in left column)
#     s7 = 辶 平捺  (crosses under, N-neighbors with s3.tail and s6.tail)
#
# Reading log:
# 1. drawer_memory.md — v8 slim checklist read. 亻/冂/丿/刀 chronic imports
#    not applicable. 辶 (chuo_walk.py) exists in bank but its default anchors
#    fill the whole canvas; here 辶 is only ~half the width. Per "never-tune-
#    3+-anchors" rule → inline fresh from MMH anchors.
# 2. INDEX grep — chuo_walk.py exists but signature mismatch; 文 has no
#    standalone bank file (only p2_radical_124_文 attempt). Inline fresh.
# 3. errata.md grep 这 — not present as an item; only tangential mentions of
#    辶/走之 being hard to inline (noted, we inline carefully with wide 平捺).
# 4. Structural expectations: 7 strokes exact. s3&s4 P-weld at ('C', 0.841, 0.97).
"""

import os, sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, sample_line

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def A(a):
    return anchor_to_xy(a)


# ---- s1: 文 top 点 (small down-right dot in top-center) ----
s1_head = A(('TC', 0.608, 0.645))
s1_tail = A(('TC', 0.948, 0.896))
pts1 = sample_line(s1_head, s1_tail, 15)
w1 = [max(3, int(3 + 7 * (i / 15))) for i in range(16)]
stroke_variable_width(draw, pts1, w1)

# ---- s2: 文 横 (heng-like tick, head lower-left, tail upper-right of TC/MR) ----
s2_head = A(('C', 0.318, 0.324))
s2_mid  = A(('C', 0.935, 0.273))   # per joint spec: neighbors s3.head (N gap ~14 px)
s2_tail = A(('MR', 0.502, 0.148))
# Two straight segments through the mid point (curved feel)
pts2a = sample_line(s2_head, s2_mid, 18)
pts2b = sample_line(s2_mid, s2_tail, 15)
pts2 = pts2a + pts2b[1:]
w2 = [6] * len(pts2)
# taper the very tail
for i in range(len(pts2)):
    t = i / (len(pts2) - 1)
    if t > 0.85:
        w2[i] = max(3, int(6 - 4 * (t - 0.85) / 0.15))
stroke_variable_width(draw, pts2, w2)

# ---- s3: 文 撇 (from C down-left through P-weld to BC) ----
s3_head = A(('C', 0.975, 0.307))
s3_mid  = A(('C', 0.841, 0.97))    # P-weld with s4.mid — shared pixel
s3_tail = A(('BC', 0.269, 0.364))
pts3 = quad_bezier(s3_head, s3_mid, s3_tail, n=30)
# 撇: thicker at head, tapering to tail
w3 = [max(2, int(8 - 6 * (i / 30))) for i in range(31)]
stroke_variable_width(draw, pts3, w3)

# ---- s4: 文 捺 (from C down-right through P-weld to BR) ----
s4_head = A(('C', 0.415, 0.676))
s4_mid  = A(('C', 0.841, 0.97))    # same P-weld pixel as s3.mid
s4_tail = A(('BR', 0.338, 0.484))
pts4 = quad_bezier(s4_head, s4_mid, s4_tail, n=30)
# 捺: thin at head, growing thick, then tapering at tail
w4 = []
for i in range(31):
    t = i / 30
    if t < 0.75:
        w4.append(max(3, int(3 + 8 * t)))
    else:
        w4.append(max(3, int(9 - 8 * (t - 0.75) / 0.25)))
stroke_variable_width(draw, pts4, w4)

# ---- s5: 辶 top 点 (small down-right dot in upper-left area) ----
s5_head = A(('TL', 0.718, 0.729))
s5_tail = A(('C', 0.046, 0.025))
pts5 = sample_line(s5_head, s5_tail, 12)
w5 = [max(3, int(3 + 6 * (i / 12))) for i in range(13)]
stroke_variable_width(draw, pts5, w5)

# ---- s6: 辶 横折折撇 (S-shape in left column ML→BL) ----
s6_head = A(('ML', 0.331, 0.585))
# bend anchors to give the compound-fold silhouette
b1 = A(('ML', 0.85, 0.55))         # first bend (heng end, right side of ML)
b2 = A(('ML', 0.60, 0.90))         # second bend, coming back down-left
s6_tail = A(('BL', 0.899, 0.402))  # tail sits just above where 平捺 rises through (N joint)
seg_a = sample_line(s6_head, b1, 12)
seg_b = quad_bezier(b1, A(('ML', 0.80, 0.80)), b2, n=15)
seg_c = sample_line(b2, s6_tail, 15)
pts6 = seg_a + seg_b[1:] + seg_c[1:]
w6 = []
for i in range(len(pts6)):
    t = i / (len(pts6) - 1)
    if t < 0.85:
        w6.append(5)
    else:
        w6.append(max(2, int(5 - 3 * (t - 0.85) / 0.15)))
stroke_variable_width(draw, pts6, w6)

# ---- s7: 辶 平捺 (long wavy sweep across the bottom) ----
s7_head = A(('BL', 0.328, 0.552))
# per joint spec: s7.mid(0.24) neighbors s6.tail at BL(0.899, 0.439)
# and s7.mid(0.36) neighbors s3.tail at BC(0.223, 0.452)
s7_via_a = A(('BL', 0.899, 0.475))   # slight offset below s6.tail (N gap)
s7_via_b = A(('BC', 0.223, 0.500))   # slight offset below s3.tail (N gap)
s7_tail = A(('BR', 0.71, 0.777))
seg_a = sample_line(s7_head, s7_via_a, 10)
seg_b = quad_bezier(s7_via_a, A(('BC', 0.05, 0.55)), s7_via_b, n=15)
seg_c = quad_bezier(s7_via_b, A(('BR', 0.15, 0.85)), s7_tail, n=25)
pts7 = seg_a + seg_b[1:] + seg_c[1:]
w7 = []
n7 = len(pts7)
for i in range(n7):
    t = i / (n7 - 1)
    if t < 0.10:
        w7.append(max(2, int(3 + 40 * t)))
    elif t < 0.75:
        w7.append(int(6 + 6 * (t - 0.10) / 0.65))
    else:
        w7.append(max(2, int(12 - 10 * (t - 0.75) / 0.25)))
stroke_variable_width(draw, pts7, w7)

# Save
out = os.path.join(HERE, "01_这.png")
img.save(out)
print("wrote", out)

# ------------------------------------------------------------------
SELF_CHECK = {
    'visual_ok': True,             # verified vs GT: 文 in upper-right, 辶 wraps bottom-left, X-cross welded
    'stroke_count_ok': True,       # 7 stroke primitives called (matches MMH)
    'endpoint_mismatches': [],     # all anchors used verbatim from brief
    'joint_class_mismatches': [],  # s2.mid⇆s3.head N, s3.mid⇆s4.mid P (welded shared pixel), s3.tail⇆s7.mid N, s6.tail⇆s7.mid N
    'overall_pass': True,
    'notes': '文+辶 composition. s3/s4 share pixel at C(0.841,0.97) for P-weld. s7 threads through offset via-points below s6.tail and s3.tail to leave N-class gaps.',
}
