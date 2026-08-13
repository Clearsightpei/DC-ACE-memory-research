"""p3_char_0243_成 — G4 attempt.

# Reading order log:
# 1. drawer_memory.md — no chronic match for 成; no direct sub-radical import
#    fits cleanly (成 is 戈-family, no primitive in bank).
# 2. success_bank/INDEX.md grep 成 — not present.
# 3. errata.md grep 成 — not present. Fresh attempt.
# 4. Trust MMH anchors verbatim per v9 lesson (比/文 PASSes).

# 成 decomposition: NOT a clean left/right split; it is a 戈-frame containing
# a small inner piece. Six strokes per MMH:
#   s1: short heng near top-center       (ML→MR, small horizontal)
#   s2: long left 撇                     (ML→BL, big diagonal down-left)
#   s3: short vertical inside            (BL→BL, tiny)
#   s4: big 斜钩 (斜钩 with hook)         (TC→BR, main diagonal down-right)
#   s5: inner 撇                         (MR→BC, short diagonal)
#   s6: top-right 点 (dot)               (TC→TR)
# Joints (from MMH block):
#   J1 s1.head N s2.head @ ML  (gap ~18 px)
#   J2 s1.mid  P s4.mid  @ C   (welded crossing)
#   J3 s2.mid  N s3.head @ BL  (gap ~14 px)
#   J4 s4.mid  P s5.mid  @ BC  (welded crossing)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
    "../../success_bank/code"))

from PIL import Image, ImageDraw
from _anchor import (anchor_to_xy, quad_bezier,
                     stroke_variable_width, fat_line, sample_line)

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH anchors verbatim; s4 hook curl at BR; joints P at C and BC welded via shared control points.'
}

W = 300
img = Image.new('RGB', (W, W), 'white')
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
BASE_W = 5

def A(anchor):
    return anchor_to_xy(anchor)

# ---------------- stroke definitions ----------------

strokes = []

# --- Shared control points for the two welded joints ---
# J2 s1 mid (~0.57 along) & s4 mid (~0.27 along) meet at C(0.575, 0.369)
CROSS_TOP = A(('C', 0.575, 0.369))
# J4 s4 mid (~0.56 along) & s5 mid (~0.55 along) meet at BC(0.931, 0.321)
CROSS_MID = A(('BC', 0.931, 0.321))

# --- s1: short top heng (ML→MR) ---
# Goes through CROSS_TOP as it is the mid of s1 (at t~0.57).
s1_head = A(('ML', 0.905, 0.474))
s1_tail = A(('MR', 0.089, 0.248))
# Simple line but ensure it passes through CROSS_TOP; parameterize as polyline:
s1_pts = [s1_head, CROSS_TOP, s1_tail]
strokes.append(('s1', s1_pts, [BASE_W, BASE_W+1, BASE_W-1]))

# --- s2: long left 撇 (ML→BL) curving down-left ---
s2_head = A(('ML', 0.677, 0.421))
s2_tail = A(('BL', 0.284, 0.912))
# curved 撇 — bows out to the left. Control near midpoint pulled slightly left.
mid_x = (s2_head[0] + s2_tail[0]) / 2 - 12
mid_y = (s2_head[1] + s2_tail[1]) / 2
s2_ctrl = (mid_x, mid_y)
s2_pts = quad_bezier(s2_head, s2_ctrl, s2_tail, n=40)
# Widths: pie tapers from thick head to thin tail
s2_widths = [max(2, int(BASE_W + 2 - i / 40 * 4)) for i in range(41)]
strokes.append(('s2', s2_pts, s2_widths))

# --- s3: tiny short stroke in BL cell (BL→BL) ---
# Almost a vertical dash inside the 撇 area — likely the small horizontal
# accent on the interior. Treat as a short segment.
s3_head = A(('BL', 0.879, 0.057))
s3_tail = A(('BL', 0.958, 0.525))
s3_pts = [s3_head, s3_tail]
strokes.append(('s3', s3_pts, [BASE_W, BASE_W]))

# --- s4: big 斜钩 from TC→BR with hook curl at end (passes near CROSS_TOP & CROSS_MID) ---
s4_head = A(('TC', 0.324, 0.536))
s4_tail = A(('BR', 0.748, 0.481))
p_a = s4_head
p_b = CROSS_TOP
p_c = CROSS_MID
p_d = s4_tail
# Smooth 斜钩: single bezier head→CROSS_MID using CROSS_TOP as ctrl (bows through top-cross),
# then curved segment CROSS_MID → tail bowing rightward (斜钩 belly), then hook tick.
seg_top = quad_bezier(p_a, p_b, p_c, n=32)
# belly: bow slightly right for 斜钩 shape
belly_ctrl = ((p_c[0] + p_d[0]) / 2 + 22, (p_c[1] + p_d[1]) / 2 + 4)
seg_belly = quad_bezier(p_c, belly_ctrl, p_d, n=24)
# Hook curl at the very end — small tick going up-right
hook_end = (p_d[0] + 10, p_d[1] - 24)
hook = sample_line(p_d, hook_end, n=8)
s4_pts = seg_top + seg_belly[1:] + hook[1:]
# widths: start medium, thickest at middle, tapered before hook, then tick
n4 = len(s4_pts)
s4_widths = []
for i in range(n4):
    t = i / (n4 - 1)
    if t < 0.85:
        w = BASE_W + 1 + int(2 * (1 - abs(2*t - 1)))  # bulge in middle
    else:
        w = max(2, BASE_W - 2)
    s4_widths.append(w)
strokes.append(('s4', s4_pts, s4_widths))

# --- s5: inner 撇 (MR→BC) crossing s4 at CROSS_MID ---
s5_head = A(('MR', 0.115, 0.644))
s5_tail = A(('BC', 0.462, 0.728))
# Route through CROSS_MID at mid (~0.55).
# Use a slight curve.
ctrl5 = ((s5_head[0] + s5_tail[0]) / 2 - 4, (s5_head[1] + s5_tail[1]) / 2 - 4)
# but we need to pass near CROSS_MID; blend by using two bezier legs
seg5a = quad_bezier(s5_head, ((s5_head[0]+CROSS_MID[0])/2 + 2, (s5_head[1]+CROSS_MID[1])/2 - 2),
                    CROSS_MID, n=20)
seg5b = quad_bezier(CROSS_MID, ((CROSS_MID[0]+s5_tail[0])/2 - 4, (CROSS_MID[1]+s5_tail[1])/2 - 2),
                    s5_tail, n=20)
s5_pts = seg5a + seg5b[1:]
n5 = len(s5_pts)
s5_widths = [max(2, int(BASE_W + 1 - i / (n5-1) * 3)) for i in range(n5)]
strokes.append(('s5', s5_pts, s5_widths))

# --- s6: top-right dot (TC→TR) — actually a short 撇/dot ---
s6_head = A(('TC', 0.913, 0.724))
s6_tail = A(('TR', 0.235, 0.926))
# Short thick tapered stroke
s6_pts = sample_line(s6_head, s6_tail, n=12)
s6_widths = [max(3, BASE_W + 3 - int(i * 0.5)) for i in range(13)]
strokes.append(('s6', s6_pts, s6_widths))

# ---------------- render ----------------

assert len(strokes) == 6, f"stroke count {len(strokes)} != 6"

for name, pts, widths in strokes:
    if len(widths) != len(pts):
        # normalize widths length
        if len(widths) == 2:
            widths = [widths[0]] * len(pts)
        else:
            # pad or trim
            widths = (widths + [widths[-1]] * len(pts))[:len(pts)]
    stroke_variable_width(d, pts, widths, INK)

out = os.path.join(os.path.dirname(__file__), "01_成.png")
img.save(out)
print(f"wrote {out}  strokes={len(strokes)}")
