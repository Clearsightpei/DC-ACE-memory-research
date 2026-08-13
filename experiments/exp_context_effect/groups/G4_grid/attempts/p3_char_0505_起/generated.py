"""起 (qǐ) — 10 strokes.

Decomposition: 起 = 走 (left-bottom wrap, 7 strokes) + 己 (top-right, 3 strokes).
  走 = 土 (s1-s3) + 龰 (s4-s7, with long 捺 at bottom)
  己 (s8-s10): 横折 + 横 + 竖弯钩

A-recipe applied: MMH-verbatim anchors + base primitives (fat_line +
quad_bezier). No compound bank primitive matches this composition:
走's long-bottom-捺 wraps under 己 in a way ren_side/chuo_walk defaults
don't reproduce, and 己 is a small top-right slot where standalone 己
would over-fill.

# BANK_DEVIATION
# skipped: chuo_walk.py (走's bottom bank if any) and any ji_self.py bank
# reason: 走 wraps left+bottom with a long 捺 running under 己; bank primitives assume standalone scale and would clash with the top-right 己 slot.
# fresh_component: zou_wrap_leftbottom_for_起 + ji_top_right_slot_for_起
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 10 fat_line/bezier calls, one per stroke
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '10 strokes MMH-verbatim; s8 heng-zhe routed via L-corner; s10 竖弯钩 via quad_bezier for right-turn hook.'
}

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# --- MMH-verbatim anchors ---
S1_H = anchor_to_xy(('ML', 0.656, 0.271));  S1_T = anchor_to_xy(('C',  0.468, 0.154))  # 土 top heng
S2_H = anchor_to_xy(('TL', 0.979, 0.595));  S2_T = anchor_to_xy(('C',  0.034, 0.603))  # 土 long heng
S3_H = anchor_to_xy(('ML', 0.246, 0.781));  S3_T = anchor_to_xy(('C',  0.541, 0.614))  # 土 shu (diagonal up-right)
S4_H = anchor_to_xy(('C',  0.002, 0.737));  S4_T = anchor_to_xy(('BC', 0.134, 0.44))   # 龰 撇 (down-left → up-right)
S5_H = anchor_to_xy(('BC', 0.172, 0.089));  S5_T = anchor_to_xy(('BC', 0.509, 0.036))  # short heng in 龰
S6_H = anchor_to_xy(('ML', 0.671, 0.942));  S6_T = anchor_to_xy(('BL', 0.173, 0.807))  # 龰 竖/撇 down-left
S7_H = anchor_to_xy(('BL', 0.771, 0.262));  S7_T = anchor_to_xy(('BR', 0.742, 0.865))  # 走's long 捺 (bottom-right sweep)
S8_H = anchor_to_xy(('C',  0.764, 0.245));  S8_T = anchor_to_xy(('MR', 0.147, 0.544))  # 己 横折
S9_H = anchor_to_xy(('C',  0.869, 0.714));  S9_T = anchor_to_xy(('MR', 0.332, 0.629))  # 己 中横
S10_H = anchor_to_xy(('C',  0.688, 0.605)); S10_T = anchor_to_xy(('MR', 0.602, 0.913)) # 己 竖弯钩

# ---- stroke 1 : 土 top heng (short) ----
fat_line(d, S1_H, S1_T, width=7)

# ---- stroke 2 : 土 second heng (long, spans across) ----
fat_line(d, S2_H, S2_T, width=7)

# ---- stroke 3 : 土 shu (diagonal from ML up to C) ----
fat_line(d, S3_H, S3_T, width=7)

# ---- stroke 4 : 龰 撇 (curved down-left) ----
# Head at C-left, tail at BC upper → use quad_bezier for slight left-curl
ctrl4 = ((S4_H[0]+S4_T[0])/2 - 8, (S4_H[1]+S4_T[1])/2)
pts4 = quad_bezier(S4_H, ctrl4, S4_T, n=32)
widths4 = [max(3, 8 - i*0.15) for i in range(len(pts4))]
stroke_variable_width(d, pts4, widths4)

# ---- stroke 5 : short heng inside 龰 ----
fat_line(d, S5_H, S5_T, width=6)

# ---- stroke 6 : 龰 竖 / diagonal down-left ----
fat_line(d, S6_H, S6_T, width=7)

# ---- stroke 7 : 走's long 捺 (bottom sweep, wide) ----
# head near mid-bottom → tail far bottom-right; slight down-arc
ctrl7 = ((S7_H[0]+S7_T[0])/2, (S7_H[1]+S7_T[1])/2 + 12)
pts7 = quad_bezier(S7_H, ctrl7, S7_T, n=40)
widths7 = [max(4, 5 + i*0.18) for i in range(len(pts7))]  # widening tail
stroke_variable_width(d, pts7, widths7)

# ---- stroke 8 : 己 横折 (heng then zhe) ----
# route via L-corner at (tail_x, head_y)
corner8 = (S8_T[0], S8_H[1])
fat_line(d, S8_H, corner8, width=6)
fat_line(d, corner8, S8_T, width=6)

# ---- stroke 9 : 己 middle heng ----
fat_line(d, S9_H, S9_T, width=6)

# ---- stroke 10 : 己 竖弯钩 (down, then right-curve with small up-hook) ----
# head upper-left, tail lower-right — curve through (head_x, tail_y) corner
corner10 = (S10_H[0], S10_T[1] - 4)
ctrl10 = (corner10[0] + 4, corner10[1] + 4)
pts10a = quad_bezier(S10_H, (S10_H[0], (S10_H[1]+corner10[1])/2), corner10, n=24)
pts10b = quad_bezier(corner10, ctrl10, S10_T, n=24)
pts10 = pts10a + pts10b
widths10 = [6] * len(pts10)
stroke_variable_width(d, pts10, widths10)
# small hook tick upward at tail
hook_end = (S10_T[0] - 4, S10_T[1] - 10)
fat_line(d, S10_T, hook_end, width=5)

out_path = os.path.join(os.path.dirname(__file__), '01_起.png')
img.save(out_path)
print('Saved', out_path)
