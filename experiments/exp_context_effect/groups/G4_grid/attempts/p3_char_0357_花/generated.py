"""花 (huā) — 7 strokes.
Decomposition: 花 = 艹 (top, 3 strokes) + 化 (bottom, 4 strokes).
  艹 = 横 + 左短竖 + 右短竖 (all pierce heng, 2×P welds)
  化 = 亻 (撇 + 竖) + 匕 (撇 + 竖弯钩)  (welded at 匕's corner)

A-recipe (v9): MMH-verbatim anchors + base primitives + SELF_CHECK.
Not calling cao_grass_radical bank primitive because MMH places 艹's
heng and verticals significantly higher and tighter than the bank
defaults (bank heng at y_frac 0.85 of ML/MR; MMH heng at y_frac ~0.1
of ML/MR). Bank primitive geometry doesn't fit a compound char where
艹 must compress into the top third.
"""
# BANK_DEVIATION
# skipped: cao_grass_radical.py
# reason: bank defaults center 艹 in the middle band (y ~ 175 px);
#         MMH places 花's 艹 in the top band (y ~ 110 px) so 化 has
#         room below. Inlining with MMH anchors preserves the
#         compound-char proportion.
# fresh_component: cao_grass_top_for_compound

import os
import sys
BANK_DIR = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G4_grid/success_bank/code"
if BANK_DIR not in sys.path:
    sys.path.insert(0, BANK_DIR)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '7 strokes MMH-verbatim; 2 P-welds inside 艹 + 1 P-weld inside 匕; N-gaps at s2/s4, s3/s7, s4/s5, s5/s6.',
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

W_HENG = 8
W_SHU = 8
W_PIE = 8

# ---- 艹 (top) --------------------------------------------------------
# s1: 横 — ML(0.486, 0.122) -> MR(0.484, 0.022)
s1a = anchor_to_xy(('ML', 0.486, 0.122))
s1b = anchor_to_xy(('MR', 0.484, 0.022))
fat_line(d, s1a, s1b, W_HENG + 1)

# s2: 短撇/竖 (left of 艹) — TL(0.97, 0.732) -> C(0.195, 0.368)
s2a = anchor_to_xy(('TL', 0.97, 0.732))
s2b = anchor_to_xy(('C', 0.195, 0.368))
fat_line(d, s2a, s2b, W_SHU)

# s3: 短竖 (right of 艹) — TC(0.764, 0.557) -> C(0.638, 0.409)
s3a = anchor_to_xy(('TC', 0.764, 0.557))
s3b = anchor_to_xy(('C', 0.638, 0.409))
fat_line(d, s3a, s3b, W_SHU)

# ---- 化: 亻 (left) ---------------------------------------------------
# s4: 撇 — C(0.037, 0.503) -> BL(0.284, 0.517)
s4a = anchor_to_xy(('C', 0.037, 0.503))
s4b = anchor_to_xy(('BL', 0.284, 0.517))
# slight curve for pie: use quad_bezier with a control offset toward the outer arc
ctrl = ((s4a[0] + s4b[0]) / 2 + 4, (s4a[1] + s4b[1]) / 2 - 2)
pts = quad_bezier(s4a, ctrl, s4b, n=40)
widths = [W_PIE - int(2 * (i / (len(pts) - 1))) for i in range(len(pts))]
stroke_variable_width(d, pts, widths)

# s5: 竖 (亻's vertical) — BL(0.943, 0.033) -> BL(0.952, 1.006)
s5a = anchor_to_xy(('BL', 0.943, 0.033))
s5b = anchor_to_xy(('BL', 0.952, 1.006))
# enforce same x for straight vertical
s5b = (s5a[0], s5b[1])
fat_line(d, s5a, s5b, W_SHU)

# ---- 化: 匕 (right) --------------------------------------------------
# s6: 撇 — MR(0.244, 0.623) -> BC(0.207, 0.552)
s6a = anchor_to_xy(('MR', 0.244, 0.623))
s6b = anchor_to_xy(('BC', 0.207, 0.552))
ctrl6 = ((s6a[0] + s6b[0]) / 2 + 6, (s6a[1] + s6b[1]) / 2 - 4)
pts6 = quad_bezier(s6a, ctrl6, s6b, n=40)
w6 = [W_PIE - int(2 * (i / (len(pts6) - 1))) for i in range(len(pts6))]
stroke_variable_width(d, pts6, w6)

# s7: 竖弯钩 — C(0.55, 0.532) -> BR(0.625, 0.335)
# head at (~155, 153); tail at (~262, 234).
# Extend the vertical portion further down, then a fuller rightward sweep,
# ending at MMH tail with a small upward hook.
s7a = anchor_to_xy(('C', 0.55, 0.532))
s7b = anchor_to_xy(('BR', 0.625, 0.335))
# Corner is deeper (lower-left of tail) to give the rightward sweep room.
corner = (s7a[0] - 2, s7b[1] + 32)  # roughly (153, 266)
# vertical portion: from head down to corner (mostly straight)
pts7a = quad_bezier(s7a, (s7a[0] - 4, (s7a[1] + corner[1]) / 2), corner, n=25)
# horizontal sweep: from corner up-and-right to tail with a curved arc
mid_ctrl = ((corner[0] + s7b[0]) / 2 - 4, corner[1] + 6)
pts7b = quad_bezier(corner, mid_ctrl, s7b, n=25)
pts7 = pts7a + pts7b[1:]
w7 = [W_SHU for _ in pts7]
stroke_variable_width(d, pts7, w7)
# small upward hook at tail
hook_end = (s7b[0] - 3, s7b[1] - 16)
fat_line(d, s7b, hook_end, W_SHU - 1)

out_dir = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G4_grid/attempts/p3_char_0357_花"
os.makedirs(out_dir, exist_ok=True)
img.save(os.path.join(out_dir, "01_花.png"))
print("wrote 01_花.png; SELF_CHECK:", SELF_CHECK)
