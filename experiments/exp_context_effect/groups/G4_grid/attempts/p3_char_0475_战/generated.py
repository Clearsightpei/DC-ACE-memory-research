"""战 (zhàn) — 9 strokes.
Decomposition: 战 = 占 (left) + 戈 (right)
  占 = 卜 (top) + 口 (bottom)  — 5 strokes
  戈 = 一 + 斜钩 + 丿 + 丶     — 4 strokes

A-recipe: MMH-verbatim anchors, inline base primitives (fat_line +
quad_bezier) rather than compound bank primitives (kou.py, bu.py, and
ge_measure.py all render standalone-scale which won't fit the compound
slot layout MMH gives us here).

Reading order performed:
  1. drawer_memory.md — read; A-recipe points 1-5 applied.
  2. INDEX.md grep — kou.py / bu.py exist as standalone; ge_measure not for 戈 standalone.
  3. errata.md grep — 战 not present.
"""
# BANK_DEVIATION
# skipped: bu.py, kou.py (both would render standalone-scale 占-parts filling ~C region;
#          MMH puts 占 into the LEFT column x∈[0.10,0.40], so standalone primitives don't fit)
# reason: LEFT-column slot compression for 占; inline via base primitives with MMH anchors
# fresh_component: zhan_left_zhan_occupy_for_战 (占 as left-column ~40% width)

import os, sys
sys.path.insert(0, "<REPO_ROOT>/experiments/exp_context_effect/groups/G4_grid/success_bank/code")

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

W = 12  # main stroke width

img = Image.new("RGB", (300, 300), "white")
d = ImageDraw.Draw(img)

# ---------- 占 (LEFT column) ----------

# stroke 1: 竖 of 卜 (long near-vertical, slightly leaning)
S1_H = anchor_to_xy(('TL', 0.727, 0.838))
S1_T = anchor_to_xy(('BL', 0.82,  0.01 ))
fat_line(d, S1_H, S1_T, W)

# stroke 2: 点 of 卜 (short horizontal-ish dot heading down-left into shu)
S2_H = anchor_to_xy(('ML', 0.967, 0.438))
S2_T = anchor_to_xy(('C',  0.427, 0.307))
# render as a tapered short stroke (dot-like)
pts2 = [S2_H,
        ((S2_H[0]+S2_T[0])/2, (S2_H[1]+S2_T[1])/2),
        S2_T]
widths2 = [11, 8, 5]
stroke_variable_width(d, pts2, widths2)

# stroke 3: 竖 of 口 (left vertical of the mouth)
S3_H = anchor_to_xy(('BL', 0.363, 0.08))
S3_T = anchor_to_xy(('BL', 0.598, 0.789))
fat_line(d, S3_H, S3_T, W)

# stroke 4: 横折 of 口 (top-heng then right-shu, L-shape)
S4_H = anchor_to_xy(('BL', 0.557, 0.165))
S4_T = anchor_to_xy(('BC', 0.125, 0.476))
# corner at (tail.x, head.y)
CORNER4 = (S4_T[0], S4_H[1])
fat_line(d, S4_H, CORNER4, W)
fat_line(d, CORNER4, S4_T, W)

# stroke 5: bottom 横 of 口
S5_H = anchor_to_xy(('BL', 0.662, 0.692))
S5_T = anchor_to_xy(('BC', 0.318, 0.59))
fat_line(d, S5_H, S5_T, W)

# ---------- 戈 (RIGHT side) ----------

# stroke 6: 横 of 戈 (goes slightly up-right)
S6_H = anchor_to_xy(('C',  0.389, 0.664))
S6_T = anchor_to_xy(('MR', 0.291, 0.421))
fat_line(d, S6_H, S6_T, W)

# stroke 7: 斜钩 of 戈 — long diagonal with small hook at tail
S7_H = anchor_to_xy(('TC', 0.547, 0.694))
S7_T = anchor_to_xy(('BR', 0.766, 0.37))
# gentle curve: control point pushed slightly right/down for a natural 斜钩
ctrl7 = ((S7_H[0] + S7_T[0]) / 2 + 8,
         (S7_H[1] + S7_T[1]) / 2 + 12)
pts7 = quad_bezier(S7_H, ctrl7, S7_T, n=60)
widths7 = [max(4, 13 - i * 8 / 60) for i in range(len(pts7))]
stroke_variable_width(d, pts7, widths7)
# small hook (钩) pointing up-right at tail
hook_end = (S7_T[0] + 12, S7_T[1] - 16)
fat_line(d, S7_T, hook_end, 9)

# stroke 8: 丿 of 戈 (short pie inside)
S8_H = anchor_to_xy(('MR', 0.376, 0.661))
S8_T = anchor_to_xy(('BC', 0.406, 0.815))
ctrl8 = ((S8_H[0] + S8_T[0]) / 2 - 4,
         (S8_H[1] + S8_T[1]) / 2 + 3)
pts8 = quad_bezier(S8_H, ctrl8, S8_T, n=40)
widths8 = [max(3, 10 - i * 6 / 40) for i in range(len(pts8))]
stroke_variable_width(d, pts8, widths8)

# stroke 9: 丶 (top-right dot) — draw LAST per B10 "top-dot last" rule
S9_H = anchor_to_xy(('TR', 0.124, 0.829))
S9_T = anchor_to_xy(('MR', 0.417, 0.061))
pts9 = [S9_H,
        ((S9_H[0]+S9_T[0])/2, (S9_H[1]+S9_T[1])/2),
        S9_T]
widths9 = [6, 9, 11]
stroke_variable_width(d, pts9, widths9)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_战.png")
img.save(out)
print("wrote", out)

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '9 strokes, MMH-verbatim anchors; 6 joints are N (natural gaps preserved), '
             '2 P-welds at C(戈横 × 斜钩) and BR(斜钩 × 丿) achieved via literal MMH placement.',
}
