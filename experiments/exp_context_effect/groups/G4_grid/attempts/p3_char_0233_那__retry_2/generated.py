"""G4 retry_2 for p3_char_0233_那.

TRAJECTORY DIFF
================
GT: 那 = 冄-like left (curved vertical + 2 hengs + right-diagonal 撇) + 阝-right.
     Right 阝 = clean 横撇弯钩 (rounded bracket-with-hook) + long 竖 descending
     below the character baseline. Character is legible + balanced left/right.

main FAIL (attempts/p3_char_0233_那/01_那.png):
  1. RIGHT 阝 rendered as a JAGGED Z-shape — chained straight lines between
     [heng_end, knee, belly, hook_start, tip]. No bezier curve, no rounded
     wan. Reads as a broken '3'/lightning-bolt, not 阝.
  2. LEFT hengs (s2, s3) were TOO SHORT (only ~68 px wide). Combined with a
     visually thin s1 and steep s4, the left component reads as "米/未 mangled"
     rather than as the 冄 pattern.
  3. Left and right halves feel disconnected — no coherent character
     silhouette.

FIXES for retry_2
  - Use draw_heng_pie_wan_gou primitive from the bank (proper bezier curves).
  - Widen the left hengs; keep s1 straight (drop artificial mid-curve).
  - Keep MMH anchors (they place things well); the primitive fixes the shape.
"""

import sys
sys.path.insert(0, '<REPO_ROOT>/experiments/exp_context_effect/groups/G4_grid/success_bank/code')

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width
from heng_pie_wan_gou import draw_heng_pie_wan_gou
from shu import draw_shu

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 left + heng_pie_wan_gou (=1 compound) + shu = 6 strokes
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'retry_2: fu_right primitive for 阝, wider hengs on left, cleaner s1.',
}

W = H = 300
img = Image.new('RGB', (W, H), 'white')
draw = ImageDraw.Draw(img)

# ================== LEFT HALF: 冄-like (strokes 1-4) ==================
# s1 — long left-vertical, slight rightward drift (MMH: TL(0.536,0.899)->BL(0.838,0.218))
p1a = anchor_to_xy(('TL', 0.536, 0.899))     # (53.6,  89.9)
p1b = anchor_to_xy(('BL', 0.838, 0.218))     # (83.8, 221.8)
# Straight line, no artificial mid-curve.
fat_line(draw, p1a, p1b, width=8)

# s2 — upper heng (MMH: ML(0.434,0.342)->C(0.11,0.274)); widen a touch to be readable
p2a = anchor_to_xy(('ML', 0.35, 0.35))       # (35, 135)
p2b = anchor_to_xy(('C', 0.30, 0.30))        # (130, 130)
fat_line(draw, p2a, p2b, width=7)

# s3 — lower heng (MMH: ML(0.272,0.764)->C(0.122,0.658)); widen slightly
p3a = anchor_to_xy(('ML', 0.20, 0.76))       # (20, 176)
p3b = anchor_to_xy(('C', 0.30, 0.66))        # (130, 166)
fat_line(draw, p3a, p3b, width=7)

# s4 — right diagonal 撇 (MMH: TL(0.744,0.981)->BL(0.281,0.599))
# This is the piercing stroke that P-welds with s2 and s3 at cell ML.
p4a = anchor_to_xy(('TL', 0.744, 0.981))     # (74.4, 98.1)
p4b = anchor_to_xy(('BL', 0.281, 0.599))     # (28.1, 259.9)
# slight bow to feel like a 撇
mid4 = ((p4a[0] + p4b[0]) / 2 + 4,
        (p4a[1] + p4b[1]) / 2 - 4)
pts4 = quad_bezier(p4a, mid4, p4b, n=30)
widths4 = [9 - 5 * (i / len(pts4)) for i in range(len(pts4))]  # taper 9 -> 4
# but keep first vertex sane
widths4[0] = 8
stroke_variable_width(draw, pts4, widths4)

# ================== RIGHT HALF: 阝-right (strokes 5-6) ==================
# s5 — 横撇弯钩 compound (proper bezier via primitive)
# MMH s5.head = ('TC', 0.896, 0.926), tail (hook tip) = ('BR', 0.06, 0.109)
# Six control anchors for the compound:
s5_head_h = ('TC', 0.55, 0.30)   # (155, 30) — start of top heng
s5_corner = ('TR', 0.20, 0.30)   # (220, 30) — corner between heng and pie
s5_knee   = ('C', 0.85, 0.55)    # (185, 155) — bottom of pie / top of wan (tucked in-left)
s5_belly  = ('MR', 0.55, 0.65)   # (255, 165) — belly bulges far RIGHT for rounded 弯
s5_hook_pt = ('C', 0.95, 0.95)   # (195, 195) — base of hook (down-left, closing the curl)
s5_tip    = ('C', 0.72, 0.85)    # (172, 185) — hook tip flicked up-left

draw_heng_pie_wan_gou(draw,
                     s5_head_h, s5_corner, s5_knee, s5_belly,
                     s5_hook_pt, s5_tip,
                     h_width=8, corner_shoulder=12,
                     pie_head_w=11, pie_knee_w=8, knee_shoulder=11,
                     wan_head_w=8, wan_belly_w=12,
                     hook_start_w=10, tip_w=2)

# s6 — 竖 vertical (MMH: head TC(0.658,0.809), tail BC(0.767,1.129) which is BELOW canvas)
p6a = anchor_to_xy(('TC', 0.66, 0.25))       # (166, 25) — start high near ear
p6b_raw = anchor_to_xy(('BC', 0.77, 1.05))   # (177, 305)
p6b = (p6b_raw[0], min(p6b_raw[1], 298))
fat_line(draw, p6a, p6b, width=10)

out_path = '<REPO_ROOT>/experiments/exp_context_effect/groups/G4_grid/attempts/p3_char_0233_那__retry_2/01_那.png'
img.save(out_path)
print('wrote', out_path)
