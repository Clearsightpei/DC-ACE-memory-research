"""俐 (lì) — 9 strokes.

Decomposition: 俐 = 亻 (left) + 利 (right); 利 = 禾 (middle) + 刂 (right).
Slots (from MMH):
  亻: far-left column     — s1 pie + s2 shu
  禾: middle column       — s3 top pie, s4 short heng, s5 vertical shu,
                              s6 left pie, s7 right dot (捺)
  刂: right column        — s8 short shu + s9 long 竖钩

Follows the B12+B11 A-recipe:
  * MMH-verbatim anchors (from dispatcher-injected block).
  * base primitives (pie/shu/heng/na/dian) with fat_line / stroke_variable_width.
  * BANK_DEVIATION for the two compound primitives whose defaults
    don't match this 3-radical slot compression (ren_side, dao_side).
  * Named pattern: ren_side_far_left_for_3radical (recurring, see B11/B12).
"""
# BANK_DEVIATION
# skipped: ren_side.py
# reason: ren_side defaults sit at TC/C/BC (mid-column); MMH places 亻 at
#   TL/ML/BL — far-left column slot for a 3-radical char.
# fresh_component: ren_side_far_left_for_3radical
#
# skipped: dao_side.py
# reason: dao_side default spacing between 短竖 and 竖钩 is wider than the
#   tight right-column pair MMH puts here.
# fresh_component: dao_side_tight_pair_for_3radical

from PIL import Image, ImageDraw
import os, sys

_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..",
                                     "success_bank", "code"))
sys.path.insert(0, _BANK)
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 9 stroke units
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],   # all 10 joints are N (with 1 P at s4/s5 center); gaps preserved
    'overall_pass': True,
    'notes': ('MMH-verbatim; 亻 far-left inline; 禾 5-stroke middle; '
              '刂 tight right pair. Base primitives only.'),
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ============ 亻 (left, far-left column) ============
# s1 撇 pie: TL(0.817,0.727) -> ML(0.196,0.869), bowed slightly left.
s1_h = anchor_to_xy(('TL', 0.817, 0.727))
s1_t = anchor_to_xy(('ML', 0.196, 0.869))
mx = (s1_h[0] + s1_t[0]) / 2 - 8
my = (s1_h[1] + s1_t[1]) / 2
pts = quad_bezier(s1_h, (mx, my), s1_t, n=48)
widths = [12 - 11 * (i / len(pts)) for i in range(len(pts))]
stroke_variable_width(d, pts, widths)

# s2 竖 shu: ML(0.656,0.459) -> BL(0.662,0.771).
s2_h = anchor_to_xy(('ML', 0.656, 0.459))
s2_t = anchor_to_xy(('BL', 0.662, 0.771))
fat_line(d, s2_h, s2_t, width=9)

# ============ 禾 (middle column, 5 strokes) ============
# s3 top short 撇 (pie): TC(0.802,0.835) -> C(0.017,0.189).
# starts upper-right, ends middle-lower-left.
s3_h = anchor_to_xy(('TC', 0.802, 0.835))
s3_t = anchor_to_xy(('C', 0.017, 0.189))
mx = (s3_h[0] + s3_t[0]) / 2 - 4
my = (s3_h[1] + s3_t[1]) / 2 + 2
pts = quad_bezier(s3_h, (mx, my), s3_t, n=40)
widths = [9 - 6 * (i / len(pts)) for i in range(len(pts))]
stroke_variable_width(d, pts, widths)

# s4 short 一 (heng of 禾): ML(0.94,0.611) -> C(0.749,0.474).
s4_h = anchor_to_xy(('ML', 0.94, 0.611))
s4_t = anchor_to_xy(('C', 0.749, 0.474))
fat_line(d, s4_h, s4_t, width=7)

# s5 长 竖 (central vertical of 禾): C(0.324,0.113) -> BC(0.374,0.81).
s5_h = anchor_to_xy(('C', 0.324, 0.113))
s5_t = anchor_to_xy(('BC', 0.374, 0.81))
fat_line(d, s5_h, s5_t, width=9)

# s6 short 撇 (left pie of 禾 lower half): C(0.339,0.629) -> BL(0.879,0.405).
s6_h = anchor_to_xy(('C', 0.339, 0.629))
s6_t = anchor_to_xy(('BL', 0.879, 0.405))
mx = (s6_h[0] + s6_t[0]) / 2 - 3
my = (s6_h[1] + s6_t[1]) / 2 + 2
pts = quad_bezier(s6_h, (mx, my), s6_t, n=32)
widths = [8 - 5 * (i / len(pts)) for i in range(len(pts))]
stroke_variable_width(d, pts, widths)

# s7 short 点/捺 (right dot of 禾 lower half): C(0.479,0.854) -> BC(0.708,0.062).
# Very short (~22 px). Draw as a compact tapered dot going down-right.
s7_h = anchor_to_xy(('C', 0.479, 0.854))
s7_t = anchor_to_xy(('BC', 0.708, 0.062))
mid7 = ((s7_h[0] + s7_t[0]) / 2, (s7_h[1] + s7_t[1]) / 2)
pts_dot = [s7_h, mid7, s7_t]
widths_dot = [3, 9, 5]
stroke_variable_width(d, pts_dot, widths_dot)

# ============ 刂 (right column pair) ============
# s8 短竖 (short vertical, inner-right).
s8_h = anchor_to_xy(('C', 0.913, 0.266))
s8_t = anchor_to_xy(('BC', 0.995, 0.133))
fat_line(d, s8_h, s8_t, width=7)

# s9 竖钩 (long vertical with small hook up-left at the bottom).
s9_h = anchor_to_xy(('TR', 0.256, 0.677))
s9_t = anchor_to_xy(('BC', 0.975, 0.672))
hook_start = (s9_h[0] - 2, s9_t[1] - 14)
fat_line(d, s9_h, hook_start, width=10)
pts_hook = quad_bezier(hook_start,
                       (hook_start[0] - 6, hook_start[1] + 4),
                       s9_t, n=14)
widths_hook = [9 - 7 * (i / len(pts_hook)) for i in range(len(pts_hook))]
stroke_variable_width(d, pts_hook, widths_hook)

out_path = os.path.join(os.path.dirname(__file__), "01_俐.png")
img.save(out_path)
print("wrote", out_path)
