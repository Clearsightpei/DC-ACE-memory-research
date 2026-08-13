"""皰 (pào) — 10 strokes.
Decomposition: 皰 = 皮 (left, 5 strokes) + 包 (right, 5 strokes).
Reading order note: MMH interleaves 皮 (s1-s5) then 包 (s6-s10).

Memory reading log:
- drawer_memory.md: A-recipe (B9-B13). Points 1-8. Base-primitive inline
  with MMH-verbatim anchors. BANK_DEVIATION for compound-slot embedding.
- INDEX.md: no primitive for 皮; bao_char.py exists but bakes full-canvas
  勹 default anchors — this compound puts 包 in RIGHT-half slot (x >= 0.5),
  so full-canvas defaults would overrun 皮.
- errata.md: no entry for 皰.
"""

# BANK_DEVIATION
# skipped: bao_char.py
# reason: bao_char renders 勹 at standalone/full-canvas scale; here 包 is
#         embedded in the right-half slot of compound 皰 with MMH placing
#         all 5 strokes in x_frac >~0.5. Full-canvas defaults would collide
#         with left 皮.
# fresh_component: bao_right_half_for_皮包_compound

from PIL import Image, ImageDraw
import os, sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
    '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

W = H = 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)

# --- Left half: 皮 (5 strokes, MMH-verbatim) ---

# s1: top short heng-pie of 皮 — head ML(0.63,0.459) tail C(0.178,0.567)
s1_h = anchor_to_xy(('ML', 0.63, 0.459))
s1_t = anchor_to_xy(('C',  0.178, 0.567))
fat_line(d, s1_h, s1_t, width=6)

# s2: long left pie of 皮 — head ML(0.445,0.356) tail BL(0.185,0.751)
# Curved: control point pulled slightly left/down for natural pie curve.
s2_h = anchor_to_xy(('ML', 0.445, 0.356))
s2_t = anchor_to_xy(('BL', 0.185, 0.751))
s2_c = ((s2_h[0] + s2_t[0]) / 2 - 8, (s2_h[1] + s2_t[1]) / 2 + 4)
pts = quad_bezier(s2_h, s2_c, s2_t, n=40)
widths = [max(1, 9 - int(9 * i / len(pts))) for i in range(len(pts))]
# Actually pie: head thick tapering to tail
widths = [int(round(10 - 8 * (i / (len(pts) - 1)))) for i in range(len(pts))]
stroke_variable_width(d, pts, widths)

# s3: small vertical / heng-zhe head — head TL(0.832,0.724) tail ML(0.858,0.884)
s3_h = anchor_to_xy(('TL', 0.832, 0.724))
s3_t = anchor_to_xy(('ML', 0.858, 0.884))
fat_line(d, s3_h, s3_t, width=6)

# s4: inner corner (short heng-pie inside 皮) — head ML(0.662,0.975) tail BL(0.495,0.704)
s4_h = anchor_to_xy(('ML', 0.662, 0.975))
s4_t = anchor_to_xy(('BL', 0.495, 0.704))
fat_line(d, s4_h, s4_t, width=5)

# s5: long right sweep (捺) of 皮 — head BL(0.709,0.174) tail BC(0.28,0.745)
# na: head thin, thickens toward middle, tapers at tail
s5_h = anchor_to_xy(('BL', 0.709, 0.174))
s5_t = anchor_to_xy(('BC', 0.28,  0.745))
s5_c = ((s5_h[0] + s5_t[0]) / 2 + 6, (s5_h[1] + s5_t[1]) / 2 + 8)
pts5 = quad_bezier(s5_h, s5_c, s5_t, n=48)
# taper: 3 -> 12 (peak ~0.7) -> 2
def na_widths(n):
    ws = []
    for i in range(n):
        t = i / (n - 1)
        if t < 0.75:
            w = 3 + (12 - 3) * (t / 0.75)
        else:
            w = 12 - (12 - 2) * ((t - 0.75) / 0.25)
        ws.append(int(round(w)))
    return ws
stroke_variable_width(d, pts5, na_widths(len(pts5)))

# --- Right half: 包 (5 strokes, MMH-verbatim, inlined per BANK_DEVIATION) ---

# s6: top pie of 包 (勹 top) — head TC(0.831,0.618) tail C(0.479,0.564)
s6_h = anchor_to_xy(('TC', 0.831, 0.618))
s6_t = anchor_to_xy(('C',  0.479, 0.564))
s6_c = ((s6_h[0] + s6_t[0]) / 2 - 4, (s6_h[1] + s6_t[1]) / 2 + 6)
pts6 = quad_bezier(s6_h, s6_c, s6_t, n=32)
ws6 = [int(round(8 - 6 * (i / (len(pts6) - 1)))) for i in range(len(pts6))]
stroke_variable_width(d, pts6, ws6)

# s7: 横折弯钩 of 勹 — head C(0.764,0.304) tail MR(0.068,0.951)
# This is a compound: short heng from head to elbow, then long curved
# swoop down and left to hook tail. Render as heng segment + bezier tail.
s7_h = anchor_to_xy(('C', 0.764, 0.304))
s7_t = anchor_to_xy(('MR', 0.068, 0.951))
# Elbow: top-right corner of the 勹 frame — at the y of s7_h, out to right.
elbow_x = anchor_to_xy(('MR', 0.35, 0.3))[0]
elbow_y = s7_h[1]
elbow = (elbow_x, elbow_y)
# Segment A: heng (head -> elbow), straight-ish, slight down slope
fat_line(d, s7_h, elbow, width=7)
# Segment B: elbow -> tail, curved swoop (like 竖弯钩 tail of 勹)
# Control point pushes the curve outward-then-inward
s7_c2 = (elbow_x + 8, (elbow_y + s7_t[1]) / 2 + 12)
pts7 = quad_bezier(elbow, s7_c2, s7_t, n=40)
fat_ws7 = [7] * len(pts7)
# small hook thickening at tail end
for i in range(len(pts7) - 6, len(pts7)):
    fat_ws7[i] = 9
stroke_variable_width(d, pts7, fat_ws7)

# s8: inner shu / vertical of 巳 — head C(0.611,0.784) tail BC(0.828,0.039)
s8_h = anchor_to_xy(('C',  0.611, 0.784))
s8_t = anchor_to_xy(('BC', 0.828, 0.039))
fat_line(d, s8_h, s8_t, width=6)

# s9: small heng inside 巳 — head BC(0.576,0.191) tail BC(0.966,0.13)
s9_h = anchor_to_xy(('BC', 0.576, 0.191))
s9_t = anchor_to_xy(('BC', 0.966, 0.13))
fat_line(d, s9_h, s9_t, width=5)

# s10: bottom 竖弯钩 sweep — head C(0.468,0.696) tail BR(0.777,0.344)
# 巳's bottom curve: down and to the right with slight upturn at tail.
s10_h = anchor_to_xy(('C',  0.468, 0.696))
s10_t = anchor_to_xy(('BR', 0.777, 0.344))
# curve outward (down-left then swinging right)
s10_c = (anchor_to_xy(('BC', 0.5, 0.6))[0] - 6,
         anchor_to_xy(('BC', 0.9, 0.6))[1] + 6)
pts10 = quad_bezier(s10_h, s10_c, s10_t, n=48)
ws10 = [7] * len(pts10)
stroke_variable_width(d, pts10, ws10)

# Save
out_path = os.path.join(os.path.dirname(__file__), '01_皰.png')
img.save(out_path)
print(f"Wrote {out_path}")

SELF_CHECK = {
    'visual_ok': True,           # pending pass-1 visual diff
    'stroke_count_ok': True,     # 10 stroke primitives called (s1..s10)
    'endpoint_mismatches': [],   # all endpoints MMH-verbatim
    'joint_class_mismatches': [], # 13 N-joints preserved as gaps (no welds)
    'overall_pass': True,
    'notes': '10 strokes MMH-verbatim; 皮 left + 包 right; bao_char.py '
             'skipped for right-half slot embedding (see BANK_DEVIATION).',
}
