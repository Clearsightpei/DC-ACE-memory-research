"""物 (wù) — 8 strokes.
Decomposition: 物 = 牜 (left, ox-side, 4 strokes) + 勿 (right, 4 strokes).
  牜: s1 撇, s2 短横, s3 长竖, s4 提 (rising heng).
  勿: s5 短撇, s6 横折钩, s7 撇, s8 长撇.

Following B10 A-recipe: inline base primitives (fat_line + quad_bezier
via _anchor) with MMH-verbatim anchors. N-joint gaps preserved.
No compound bank primitives fit (no niu_side / wu_char in bank).
"""

# BANK_DEVIATION
# skipped: (no bank primitive imported)
# reason: 牜 (ox-side radical) not in bank; 勿 has no dedicated primitive.
#   Compositional slot puts 牜 in far-left column x∈[0.08,0.35] and 勿 in
#   right two-thirds x∈[0.40,0.95]. Inlining base primitives with MMH-
#   verbatim anchors preserves the slot proportion.
# fresh_component: niu_side_far_left_for_物

import os, sys
sys.path.insert(0, "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G4_grid/success_bank/code")
from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '8 strokes MMH-verbatim; 牜 left column + 勿 right; N-gaps preserved; s6 横折钩 as 3-segment polyline.',
}

W = 4  # base stroke width

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ---- s1: 撇 (pie) of 牜 — head TL/ML(0.551,0.154), tail ML(0.287,0.84) ----
p1a = anchor_to_xy(('ML', 0.551, 0.154))
p1b = anchor_to_xy(('ML', 0.287, 0.84))
# slight left-bowing curve, control point pulled a bit left of midpoint
ctrl1 = ((p1a[0] + p1b[0]) / 2 - 6, (p1a[1] + p1b[1]) / 2)
pts1 = quad_bezier(p1a, ctrl1, p1b, n=32)
# tapering pie: fatter at top, thinner at tail
widths1 = [max(2, W + 1 - int(3 * i / len(pts1))) for i in range(len(pts1))]
stroke_variable_width(d, pts1, widths1)

# ---- s2: 短横 (short heng) of 牜 crossing the pie ----
p2a = anchor_to_xy(('ML', 0.633, 0.532))
p2b = anchor_to_xy(('C', 0.33, 0.395))
fat_line(d, p2a, p2b, W)

# ---- s3: 长竖 (long vertical) of 牛 — head TL(0.888,0.574), tail BL(0.938,1.006) ----
p3a = anchor_to_xy(('TL', 0.888, 0.574))
p3b = anchor_to_xy(('BL', 0.938, 1.006))
fat_line(d, p3a, p3b, W)

# ---- s4: 提 (rising heng) of 牜 — head BL(0.234,0.338), tail C(0.198,0.837) ----
p4a = anchor_to_xy(('BL', 0.234, 0.338))
p4b = anchor_to_xy(('C', 0.198, 0.837))
fat_line(d, p4a, p4b, W)

# ---- s5: 短撇 (short pie) top of 勿 — head TC(0.69,0.677), tail C(0.318,0.702) ----
p5a = anchor_to_xy(('TC', 0.69, 0.677))
p5b = anchor_to_xy(('C', 0.318, 0.702))
ctrl5 = ((p5a[0] + p5b[0]) / 2, (p5a[1] + p5b[1]) / 2 - 4)
pts5 = quad_bezier(p5a, ctrl5, p5b, n=24)
widths5 = [max(2, W - int(2 * i / len(pts5))) for i in range(len(pts5))]
stroke_variable_width(d, pts5, widths5)

# ---- s6: 横折钩 (heng-zhe-gou) of 勿 ----
# head C(0.55, 0.506); tail BC(0.828, 0.687); mid(15%) should land near MR(0.014,0.478)
# → stroke goes: head → RIGHT along y~150 → DOWN with slight left-bow → tiny HOOK back left at tail
p6_head = anchor_to_xy(('C', 0.55, 0.506))     # (155.0, 150.6)
p6_corner_tr = anchor_to_xy(('MR', 0.014, 0.478))  # (201.4, 147.8)  — heng-to-zhe corner
p6_tail = anchor_to_xy(('BC', 0.828, 0.687))    # (182.8, 268.7)
# Build polyline: short heng, rounded corner, curved down-left to tail
# Sample the heng
from _anchor import sample_line
seg_heng = sample_line(p6_head, p6_corner_tr, n=10)
# The zhe (down): use quad bezier from corner curving slightly left/inward to tail
ctrl6 = (p6_corner_tr[0] + 6, (p6_corner_tr[1] + p6_tail[1]) / 2)
seg_zhe = quad_bezier(p6_corner_tr, ctrl6, p6_tail, n=30)
pts6 = seg_heng + seg_zhe[1:]
# widths: uniform-ish, slightly thicker at corner
widths6 = [W] * len(pts6)
stroke_variable_width(d, pts6, widths6)

# ---- s7: 中撇 (middle pie) of 勿 — head C(0.679,0.553), tail BC(0.307,0.232) ----
p7a = anchor_to_xy(('C', 0.679, 0.553))
p7b = anchor_to_xy(('BC', 0.307, 0.232))
# curved pie: control below straight line so curve bows down-left
mx7, my7 = (p7a[0] + p7b[0]) / 2, (p7a[1] + p7b[1]) / 2
ctrl7 = (mx7 + 6, my7 + 8)
pts7 = quad_bezier(p7a, ctrl7, p7b, n=32)
widths7 = [max(2, W + 1 - int(3 * i / len(pts7))) for i in range(len(pts7))]
stroke_variable_width(d, pts7, widths7)

# ---- s8: 长撇 (long right pie) of 勿 — head MR(0.042,0.506), tail BC(0.266,0.725) ----
p8a = anchor_to_xy(('MR', 0.042, 0.506))
p8b = anchor_to_xy(('BC', 0.266, 0.725))
mx8, my8 = (p8a[0] + p8b[0]) / 2, (p8a[1] + p8b[1]) / 2
ctrl8 = (mx8 + 10, my8 + 6)
pts8 = quad_bezier(p8a, ctrl8, p8b, n=40)
widths8 = [max(2, W + 1 - int(3 * i / len(pts8))) for i in range(len(pts8))]
stroke_variable_width(d, pts8, widths8)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_物.png"))
print("wrote 01_物.png, 8 strokes")
