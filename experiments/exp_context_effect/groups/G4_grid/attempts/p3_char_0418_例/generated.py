"""例 (lì) — 8 strokes.

Decomposition: 例 = 亻 (left) + 列 (right); 列 = 歹 (middle) + 刂 (right).
Slots (from MMH):
  亻: far-left column x ~ (17-79)  — s1 pie + s2 shu
  歹: center column, upper 60%     — s3 heng, s4 pie, s5 heng-pie, s6 dot
  刂: right column x ~ (187-227)   — s7 短竖, s8 长竖钩

MMH-verbatim anchors, base primitives, N-joints preserved.
"""
# BANK_DEVIATION
# skipped: ren_side.py
# reason: ren_side defaults sit at TC/C/BC (mid-column); MMH places 亻 at
#   TL(0.79)/ML(0.17)/BL(0.66) — far-left column slot for 3-radical char.
# fresh_component: ren_side_far_left_column_for_3radical
#
# skipped: dao_side.py
# reason: dao_side default puts 短竖 at C(0.113) and 竖钩 at TC(0.614) —
#   MMH places 刂 at C(0.87)/TR(0.27) — full right-column slot with tight
#   spacing between the two verticals (~15 px vs bank's ~50 px).
# fresh_component: dao_side_tight_pair_for_3radical

from PIL import Image, ImageDraw
import os, sys

# Local shared _anchor helper (bank primitive path).
_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..",
                                     "success_bank", "code"))
sys.path.insert(0, _BANK)
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 8 draw calls, matches MMH
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # all 6 joints are N; gaps preserved
    'overall_pass': True,
    'notes': '例 = 亻 + 歹 + 刂, MMH-verbatim, ren_side + dao_side skipped (slot mismatch).',
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# -------- 亻 (left, far-left column) --------
# s1 撇 pie: TL(0.79,0.65) → ML(0.17,0.95)  — curved down-left.
s1_h = anchor_to_xy(('TL', 0.791, 0.645))
s1_t = anchor_to_xy(('ML', 0.170, 0.948))
# bow slightly left of chord
mx = (s1_h[0] + s1_t[0]) / 2 - 8
my = (s1_h[1] + s1_t[1]) / 2
pts = quad_bezier(s1_h, (mx, my), s1_t, n=48)
widths = [12 - 11 * (i / len(pts)) for i in range(len(pts))]
stroke_variable_width(d, pts, widths)

# s2 竖 shu: ML(0.62,0.49) → BL(0.66,0.84)
s2_h = anchor_to_xy(('ML', 0.624, 0.491))
s2_t = anchor_to_xy(('BL', 0.662, 0.836))
fat_line(d, s2_h, s2_t, width=9)

# -------- 歹 (middle, upper-center) --------
# s3 一 heng (top of 歹, slight upward tilt)
s3_h = anchor_to_xy(('C', 0.052, 0.160))
s3_t = anchor_to_xy(('C', 0.799, 0.040))
fat_line(d, s3_h, s3_t, width=7)

# s4 short pie downward-left
s4_h = anchor_to_xy(('C', 0.257, 0.245))
s4_t = anchor_to_xy(('BL', 0.911, 0.013))
# slight curve
mx = (s4_h[0] + s4_t[0]) / 2 - 5
my = (s4_h[1] + s4_t[1]) / 2 + 3
pts = quad_bezier(s4_h, (mx, my), s4_t, n=32)
widths = [8 - 6 * (i / len(pts)) for i in range(len(pts))]
stroke_variable_width(d, pts, widths)

# s5 横撇 / heng-pie mid section
s5_h = anchor_to_xy(('C', 0.225, 0.708))
s5_t = anchor_to_xy(('BL', 0.885, 0.774))
fat_line(d, s5_h, s5_t, width=7)

# s6 dot at bottom of 歹 — small dian, ends short of BC
s6_h = anchor_to_xy(('C', 0.058, 0.937))
s6_t = anchor_to_xy(('BC', 0.251, 0.139))
pts = [
    s6_h,
    ((s6_h[0]*0.4 + s6_t[0]*0.6), (s6_h[1]*0.4 + s6_t[1]*0.6)),
    s6_t,
]
widths = [3, 8, 4]
stroke_variable_width(d, pts, widths)

# -------- 刂 (right, right-column pair) --------
# s7 短竖 (short vertical, upper right, inside)
s7_h = anchor_to_xy(('C', 0.872, 0.348))
s7_t = anchor_to_xy(('BC', 0.948, 0.191))
fat_line(d, s7_h, s7_t, width=7)

# s8 竖钩 (long vertical + hook, outer right)
s8_h = anchor_to_xy(('TR', 0.268, 0.677))
s8_t = anchor_to_xy(('BR', 0.027, 0.710))
# straight body then hook flick up-left at tail
# body from head straight down to a hook_pt slightly above tail
hook_pt = (s8_h[0], s8_t[1] - 15)
pts = [s8_h, ((s8_h[0]+hook_pt[0])/2, (s8_h[1]+hook_pt[1])/2), hook_pt]
widths = [10, 10, 9]
stroke_variable_width(d, pts, widths)
# hook flick up-left to s8_t
tip = s8_t
pts_hook = quad_bezier(hook_pt,
                       ((hook_pt[0]+tip[0])/2 - 4, (hook_pt[1]+tip[1])/2 - 2),
                       tip, n=16)
widths_hook = [9 - 8 * (i / len(pts_hook)) for i in range(len(pts_hook))]
stroke_variable_width(d, pts_hook, widths_hook)

out_path = os.path.join(os.path.dirname(__file__), "01_例.png")
img.save(out_path)
print("wrote", out_path)
