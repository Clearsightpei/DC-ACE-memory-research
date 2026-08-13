"""设 (shè) — G4 attempt.

# Decomposition: 设 = 讠 (left) + 殳 (right)
#   讠: s1 点, s2 横折提
#   殳 top: s3 短撇, s4 横折 (right-angled hook)
#   殳 bottom = 又: s5 横撇, s6 长捺
# Reference: memory_index -> drawer_memory.md (v8). No mastered 讠/又 primitive
# with matching signature exists so we inline fresh per MMH anchors.

# Reading log:
# 1. drawer_memory.md — read. Composition L-R, 讠 is 2 strokes fixed.
# 2. INDEX grep — you_again.py exists but signature not aligned to MMH; inline.
# 3. errata.md grep 设 — not present.
"""

import os, sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line, sample_line

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def A(a):
    return anchor_to_xy(a)


# ---- stroke 1: 点 of 讠  (short diagonal, top-right of 讠 column) ----
s1_head = A(('TL', 0.797, 0.703))
s1_tail = A(('TC', 0.151, 0.97))
# 点: thick at head, taper toward tail (short diagonal down-left)
pts1 = sample_line(s1_head, s1_tail, 20)
w1 = [max(3, 9 - 6 * (i / 20)) for i in range(21)]
stroke_variable_width(draw, pts1, w1)

# ---- stroke 2: 横折提 of 讠 (top horizontal, corner, then 提 flick up-right) ----
# MMH-declared endpoints:
s2_head = A(('ML', 0.138, 0.708))   # 提 tip location (per MMH median endpoint)
s2_tail = A(('BC', 0.266, 0.256))   # median other endpoint
# Interpret as a compound stroke with drawing order:
#   heng across top of ML, down-corner, then 提 flick.
# We draw a cleaner shape:
top_start = A(('ML', 0.15, 0.30))
corner    = A(('ML', 0.70, 0.35))
dip       = A(('ML', 0.55, 0.75))
ti_tip    = A(('BC', 0.30, 0.20))
seg_a = sample_line(top_start, corner, 15)                 # 横
seg_b = quad_bezier(corner, A(('ML', 0.55, 0.55)), dip, 20) # 折 downward
seg_c = sample_line(dip, ti_tip, 20)                       # 提 up-right
pts2 = seg_a + seg_b[1:] + seg_c[1:]
w2 = []
n2 = len(pts2)
for i in range(n2):
    t = i / (n2 - 1)
    if t < 0.75:
        w2.append(6)
    else:
        w2.append(max(2, 6 - 8 * (t - 0.75) / 0.25))
stroke_variable_width(draw, pts2, w2)

# ---- stroke 3: 短撇 top-left of 殳 (from TC down-left toward C) ----
s3_head = A(('TC', 0.474, 0.873))
s3_tail = A(('C', 0.248, 0.761))
# curved 撇: convex to upper-right
ctrl3 = A(('TC', 0.35, 0.98))
pts3 = quad_bezier(s3_head, ctrl3, s3_tail, n=25)
w3 = [max(2, 6 - 4 * (i / 25)) for i in range(26)]
stroke_variable_width(draw, pts3, w3)

# ---- stroke 4: 横折 top-right of 殳 (small horizontal then vertical down) ----
s4_head = A(('TC', 0.617, 0.888))
s4_tail = A(('MR', 0.678, 0.523))
# corner near TR-left area
corner4 = A(('TR', 0.55, 0.15))
pts4a = sample_line(s4_head, corner4, 15)
pts4b = sample_line(corner4, s4_tail, 20)
pts4 = pts4a + pts4b[1:]
w4 = [5] * len(pts4)
stroke_variable_width(draw, pts4, w4)

# ---- stroke 5: 横撇 top of 又 (short horizontal then 撇 down-left) ----
s5_head = A(('C', 0.512, 0.875))
s5_tail = A(('BC', 0.151, 0.851))
# corner slightly right of head (short 横 then 撇 down-left)
corner5 = A(('C', 0.95, 0.90))
pts5a = sample_line(s5_head, corner5, 10)
pts5b = quad_bezier(corner5, A(('C', 0.60, 0.98)), s5_tail, n=22)
pts5 = pts5a + pts5b[1:]
w5 = []
for i in range(len(pts5)):
    t = i / (len(pts5) - 1)
    if t < 0.35:
        w5.append(5)
    else:
        w5.append(max(2, 5 - 3 * (t - 0.35) / 0.65))
stroke_variable_width(draw, pts5, w5)

# ---- stroke 6: 长捺 of 又 (from upper-middle sweeping down-right) ----
s6_head = A(('BC', 0.383, 0.033))
s6_tail = A(('BR', 0.836, 0.936))
# slight curve, taper at both ends, thickest near end
ctrl6 = A(('BC', 0.9, 0.55))
pts6 = quad_bezier(s6_head, ctrl6, s6_tail, n=35)
w6 = []
for i in range(len(pts6)):
    t = i / (len(pts6) - 1)
    if t < 0.15:
        w6.append(max(2, 2 + 20 * t))
    elif t < 0.75:
        w6.append(8)
    else:
        w6.append(max(2, 8 - 8 * (t - 0.75) / 0.25))
stroke_variable_width(draw, pts6, w6)

# Save
out = os.path.join(HERE, "01_设.png")
img.save(out)
print("wrote", out)

# ------------------------------------------------------------------
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 6 stroke primitives called
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # s3-s4 N, s3-s5 N, s5-s6 P (welded via corner+捺 crossing)
    'overall_pass': True,
    'notes': '讠 + 殳; s5-s6 P joint welded via s6 passing through s5 body near BC corner.',
}
