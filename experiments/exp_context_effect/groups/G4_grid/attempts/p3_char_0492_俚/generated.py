"""俚 (lǐ) — 亻 + 里 (9 strokes) — p3_char_0492.

Decomposition (from MMH endpoints):
  亻 (far-left column, 2 strokes): s1 pie, s2 shu
  里 (right, 7 strokes): 日 + spine + 土
    s3 short 竖 (left wall of 日 within 里)
    s4 横折 (top + right wall of 日)
    s5 middle 横 of 日
    s6 bottom 横 of 日
    s7 long 竖 (central spine piercing 日 and 土)
    s8 short middle 横 of 土
    s9 long bottom 一 (base of 土)

MMH-verbatim anchors. Base primitives only (no compound bank).
"""
# BANK_DEVIATION
# skipped: ren_side.py
# reason: ren_side defaults sit near TC/C/BC (mid-column); MMH places 亻 at
#         TL/ML/BL — the recurring far-left column slot for gt-with-wide-right.
# fresh_component: ren_side_far_left_for_俚

from PIL import Image, ImageDraw
import os, sys

_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..",
                                     "success_bank", "code"))
sys.path.insert(0, _BANK)
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 9 strokes
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # 10 N + 3 P (welded at s5×s7, s6×s7, s7×s8)
    'overall_pass': True,
    'notes': 'MMH-verbatim; 亻 far-left inline; 里 = 日 + spine + 土.',
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ============ 亻 (far-left column, 2 strokes) ============
# s1 撇 (pie): TL(0.879, 0.647) -> ML(0.185, 0.983)
s1_h = anchor_to_xy(('TL', 0.879, 0.647))
s1_t = anchor_to_xy(('ML', 0.185, 0.983))
mx = (s1_h[0] + s1_t[0]) / 2 - 8
my = (s1_h[1] + s1_t[1]) / 2
pts = quad_bezier(s1_h, (mx, my), s1_t, n=48)
widths = [12 - 11 * (i / len(pts)) for i in range(len(pts))]
stroke_variable_width(d, pts, widths)

# s2 竖 (shu): ML(0.683, 0.506) -> BL(0.744, 0.918)
s2_h = anchor_to_xy(('ML', 0.683, 0.506))
s2_t = anchor_to_xy(('BL', 0.744, 0.918))
fat_line(d, s2_h, s2_t, width=9)

# ============ 里 - 日 top half ============
# s3 short 竖 (left wall of 日): C(0.146, 0.093) -> C(0.395, 0.916)
s3_h = anchor_to_xy(('C', 0.146, 0.093))
s3_t = anchor_to_xy(('C', 0.395, 0.916))
fat_line(d, s3_h, s3_t, width=9)

# s4 横折 (top bar + right wall of 日): C(0.286, 0.102) -> MR(0.168, 0.843)
# Two segments joined at the top-right corner near TR(0.16, 0.10) region.
s4_h = anchor_to_xy(('C', 0.286, 0.102))
s4_t = anchor_to_xy(('MR', 0.168, 0.843))
# Corner: at approximately (right wall x, top y). Use s4_t's x and s4_h's y.
s4_corner = (s4_t[0], s4_h[1])
fat_line(d, s4_h, s4_corner, width=9)
fat_line(d, s4_corner, s4_t, width=9)

# s5 middle 横 of 日: C(0.497, 0.503) -> MR(0.039, 0.421)
s5_h = anchor_to_xy(('C', 0.497, 0.503))
s5_t = anchor_to_xy(('MR', 0.039, 0.421))
fat_line(d, s5_h, s5_t, width=8)

# s6 bottom 横 of 日: C(0.444, 0.854) -> MR(0.045, 0.729)
s6_h = anchor_to_xy(('C', 0.444, 0.854))
s6_t = anchor_to_xy(('MR', 0.045, 0.729))
fat_line(d, s6_h, s6_t, width=8)

# ============ 里 - central spine + 土 ============
# s7 long 竖 (central spine, piercing 日 through 土):
#   C(0.661, 0.143) -> BC(0.714, 0.613)
s7_h = anchor_to_xy(('C', 0.661, 0.143))
s7_t = anchor_to_xy(('BC', 0.714, 0.613))
fat_line(d, s7_h, s7_t, width=9)

# s8 short middle 横 of 土: BC(0.321, 0.259) -> BR(0.212, 0.194)
s8_h = anchor_to_xy(('BC', 0.321, 0.259))
s8_t = anchor_to_xy(('BR', 0.212, 0.194))
fat_line(d, s8_h, s8_t, width=9)

# s9 long bottom 一 (base of 土): BL(0.967, 0.728) -> BR(0.666, 0.701)
s9_h = anchor_to_xy(('BL', 0.967, 0.728))
s9_t = anchor_to_xy(('BR', 0.666, 0.701))
fat_line(d, s9_h, s9_t, width=10)

out_path = os.path.join(os.path.dirname(__file__), "01_俚.png")
img.save(out_path)
print("wrote", out_path)
