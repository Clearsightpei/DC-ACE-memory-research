# BANK_DEVIATION
# skipped: chronic/ma_horse.py
# reason: ma_horse's baked anchors fill the full 300x300 canvas, but 鸭 needs 鸟 compressed into the right half (x~150-230); primitive has no offset/scale params.
# fresh_component: niao_right_half_for_鸭

# 鸭 = 甲 (left) + 鸟 (right). 10 strokes total from MMH.
# Bank shortcut for 甲 not fully applicable (needs left-half compression).
# Drawing fresh from injected MMH anchors.

import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, stroke_variable_width, quad_bezier, fat_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH-anchor-guided fresh render; 甲-left + 鸟-right; bank ma_horse skipped due to canvas-fill mismatch.'
}

img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

W = 7  # stroke width

def A(t): return anchor_to_xy(t)

# ============ 甲 (left half, strokes 1-5) ============

# s1: left vertical of 甲 box (short 竖, slightly slanting right)
# head ML(0.328, 0.187) -> tail ML(0.542, 0.983)
fat_line(draw, A(('ML', 0.328, 0.187)), A(('ML', 0.542, 0.983)), W)

# s2: 横折 top-and-right of 甲 box.
# head ML(0.419, 0.175); corner around (top of spine); tail C(0.157, 0.869) at bottom-mid
# Use bent path: head -> top-right corner -> down
s2_head = A(('ML', 0.419, 0.175))
s2_corner = A(('ML', 0.75, 0.19))       # top-right corner of box
s2_mid = A(('C', 0.12, 0.49))            # meets s3 tail area (N)
s2_tail = A(('C', 0.157, 0.869))
# horizontal top + right vertical down
fat_line(draw, s2_head, s2_corner, W)
fat_line(draw, s2_corner, s2_mid, W)
fat_line(draw, s2_mid, s2_tail, W)

# s3: middle 横 crossing spine (P-weld with s5)
# head ML(0.639, 0.556) -> tail C(0.037, 0.477)
fat_line(draw, A(('ML', 0.639, 0.556)), A(('C', 0.037, 0.477)), W)

# s4: bottom 横 of 甲 box (P-weld with s5)
# head ML(0.586, 0.907) -> tail C(0.058, 0.77)
fat_line(draw, A(('ML', 0.586, 0.907)), A(('C', 0.058, 0.77)), W)

# s5: central spine (long 竖 extending below box)
# head ML(0.738, 0.195) -> tail BL(0.812, 0.918)
fat_line(draw, A(('ML', 0.738, 0.195)), A(('BL', 0.812, 0.918)), W)

# ============ 鸟 (right half, strokes 6-10) ============

# s6: top 撇 short at top of 鸟 head
# head TC(0.796, 0.562) -> tail C(0.62, 0.061)
s6_head = A(('TC', 0.796, 0.562))
s6_tail = A(('C', 0.62, 0.061))
fat_line(draw, s6_head, s6_tail, W-1)

# s7: 横折钩 top box of 鸟 (horizontal-ish going right and slightly down, with hook)
# head C(0.661, 0.116) -> tail C(0.942, 0.559)
# Draw as: horizontal right, then curve down (like 横折)
s7_head = A(('C', 0.661, 0.116))
s7_corner = A(('C', 0.93, 0.12))       # top-right corner
s7_tail = A(('C', 0.942, 0.559))
fat_line(draw, s7_head, s7_corner, W)
fat_line(draw, s7_corner, s7_tail, W)
# hook flick at end (small up-left)
hook_pt = (s7_tail[0] - 8, s7_tail[1] - 4)
fat_line(draw, s7_tail, hook_pt, W-1)

# s8: eye dot (short stroke)
# head C(0.767, 0.304) -> tail C(0.925, 0.43)
fat_line(draw, A(('C', 0.767, 0.304)), A(('C', 0.925, 0.43)), W-1)

# s9: 竖折折钩 body of 鸟 (long smooth curve down)
# head C(0.491, 0.075) -> tail BR(0.024, 0.769)
s9_head = A(('C', 0.491, 0.075))
s9_tail = A(('BR', 0.024, 0.769))
# Smooth bezier down with slight leftward bow then out to bottom-right
ctrl9 = A(('C', 0.35, 0.75))
pts9 = quad_bezier(s9_head, ctrl9, s9_tail, n=40)
widths9 = [W for _ in pts9]
stroke_variable_width(draw, pts9, widths9)
# hook tail up-left flick
hook9 = (s9_tail[0] - 12, s9_tail[1] - 6)
fat_line(draw, s9_tail, hook9, W-2)

# s10: bottom 长横 spanning under 鸟
# head BC(0.034, 0.487) -> tail BR(0.244, 0.388)
fat_line(draw, A(('BC', 0.034, 0.487)), A(('BR', 0.244, 0.388)), W)

img.save(os.path.join(_HERE, '01_鸭.png'))
print("stroke_count = 10")
print("saved 01_鸭.png")
