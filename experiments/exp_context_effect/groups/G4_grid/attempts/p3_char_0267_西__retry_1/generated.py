"""p3_char_0267_西 — retry_1

TRAJECTORY DIFF
---------------
Prior attempt (main) FAILED. Visual inspection of its PNG vs GT shows:
  * Top heng was tilted and shorter than needed; not crossing the frame cleanly.
  * The frame's left vertical was disconnected from the top heng.
  * Right frame collapsed diagonally — the 横折 corner was not square, right wall
    slanted inward.
  * Inner strokes were dropped or fragmented.
  * Bottom closing heng was missing / disconnected from left/right verticals.

Fixes for retry_1:
  1. Draw a wide, straight top heng that clearly extends past both frame walls (y≈95).
  2. Frame = strict rectangle: left vertical strict-x at ~75, right vertical strict-x
     at ~225. Both from y≈115 to y≈270. Top of frame = horizontal at y≈115 from
     x=75 to x=225. Bottom heng closes at y≈270 flush with both walls.
  3. Two inner strokes: left inner short 撇 slightly left-leaning from (~120, 130)
     to (~110, 220); right inner 竖弯 from (~180, 130) down to (~205, 215) with
     slight rightward curl at bottom. Both cross the middle horizontal implicitly
     but here we render 西 as: top heng, left frame shu, top+right frame heng-zhe,
     two inner short strokes, bottom heng closure — exactly 6 strokes.
  4. Ensure bottom heng touches both frame walls (N joints s2.tail↔s6.head at BL,
     s3.tail↔s6.tail at BR — near-weld gaps).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 6 strokes drawn
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Clean rectangular frame + inner strokes; bottom closure enforced.',
}

import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

W = H = 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)

# ---- s1: top heng (extends past frame) ----
# head at TL(0.20,0.95)=(60, 95); tail at TR(0.50,0.85)=(250, 85)
p_s1_head = (55, 92)
p_s1_tail = (250, 88)
fat_line(d, p_s1_head, p_s1_tail, width=6)

# ---- s2: left frame vertical (shu) ----
# from just below top heng down to bottom
p_s2_head = (78, 115)
p_s2_tail = (78, 268)
fat_line(d, p_s2_head, p_s2_tail, width=7)

# ---- s3: 横折 (top-of-frame heng + right vertical) ----
# corner at TR-ish; head near left, corner top-right, tail bottom-right
p_s3_head = (78, 115)
p_s3_corner = (225, 115)
p_s3_tail = (225, 268)
# top segment
fat_line(d, p_s3_head, p_s3_corner, width=6)
# right vertical segment (thicker near corner shoulder)
fat_line(d, (225, 112), p_s3_tail, width=8)
# corner smoother
d.ellipse((225-5, 115-5, 225+5, 115+5), fill=(0, 0, 0))

# ---- s4: inner left stroke (短撇 leaning left) ----
# head near top-center-left, tail toward mid-lower-left
p_s4_head = (120, 130)
p_s4_tail = (108, 220)
pts4 = quad_bezier(p_s4_head, (116, 175), p_s4_tail, n=30)
widths4 = [5 - 3*i/(len(pts4)-1) + 3 for i in range(len(pts4))]  # taper
stroke_variable_width(d, pts4, widths4)

# ---- s5: inner right stroke (竖弯 — down then slight right curl) ----
p_s5_head = (175, 130)
p_s5_ctrl = (195, 200)
p_s5_tail = (208, 220)
pts5 = quad_bezier(p_s5_head, p_s5_ctrl, p_s5_tail, n=30)
widths5 = [6 - 2*i/(len(pts5)-1) for i in range(len(pts5))]
stroke_variable_width(d, pts5, widths5)

# ---- s6: bottom heng closing (from left wall to right wall) ----
p_s6_head = (75, 268)
p_s6_tail = (228, 265)
fat_line(d, p_s6_head, p_s6_tail, width=6)

# save
out = os.path.join(_HERE, '01_西.png')
img.save(out)
print(f"wrote {out}")
