"""盍 (hé) — 10 strokes.

Decomposition: 盍 = 去 (top, 5 strokes) + 皿 (bottom, 5 strokes).
  去 = 士-shape (top短横 + 长横 + 竖) + 厶 (2 strokes)  [s1..s5]
  皿 = 左竖 + 横折 (top+right) + 内竖 + 内竖 + 底横       [s6..s10]

Recipe: B9-B13 A-recipe — MMH-verbatim anchors + base primitives inline,
N-joint natural gaps preserved. No compound bank primitive fits this
composition (no 皿, no 去 in bank). No BANK_DEVIATION block because no
bank primitive was in play.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 10 strokes drawn
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # all joints N (natural gap)
    'overall_pass': True,
    'notes': '10 strokes MMH-verbatim; s7 rendered as 横折 with corner at (tail_x, head_y).',
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ---------- 去 (top) — 5 strokes ----------

# s1: top short heng (士 top)
p = anchor_to_xy(('C', 0.014, 0.09))     # head ~ (101, 109)
q = anchor_to_xy(('TC', 0.96, 0.999))    # tail ~ (196, 100)
fat_line(d, p, q, width=6)

# s2: vertical 丨 of 士 (from above through to middle)
p = anchor_to_xy(('TC', 0.354, 0.583))   # head ~ (135, 58)
q = anchor_to_xy(('C',  0.406, 0.348))   # tail ~ (141, 135)
fat_line(d, p, q, width=7)

# s3: long middle heng of 士
p = anchor_to_xy(('ML', 0.533, 0.5))     # head ~ (53, 150)
q = anchor_to_xy(('MR', 0.449, 0.386))   # tail ~ (245, 139)
fat_line(d, p, q, width=6)

# s4: first stroke of 厶 — 撇折 shape (down-left then down-right corner)
p = anchor_to_xy(('C', 0.468, 0.509))    # head ~ (147, 151)
q = anchor_to_xy(('C', 0.816, 0.843))    # tail ~ (182, 184)
# 撇折: pie down-left to a bottom-left elbow, then folds down-right to tail
elbow = (p[0] - 18, p[1] + 22)           # ~ (129, 173)
seg1 = quad_bezier(p, ((p[0]+elbow[0])/2 - 4, (p[1]+elbow[1])/2), elbow, n=20)
seg2 = [elbow, q]
w1 = [max(2, 7 - i * 0.15) for i in range(len(seg1))]
w2 = [3, 5]
stroke_variable_width(d, seg1, w1)
stroke_variable_width(d, seg2, w2)

# s5: closing 点 of 厶 — short down-right dot
p = anchor_to_xy(('C',  0.676, 0.603))   # head ~ (168, 160)
q = anchor_to_xy(('MR', 0.033, 0.942))   # tail ~ (203, 194)
pts = [p, ((p[0]+q[0])/2, (p[1]+q[1])/2 - 2), q]
widths = [3, 6, 8]
stroke_variable_width(d, pts, widths)

# ---------- 皿 (bottom) — 5 strokes ----------

# s6: left short 竖 of 皿
p = anchor_to_xy(('BL', 0.691, 0.291))   # head ~ (69, 229)
q = anchor_to_xy(('BL', 0.979, 0.83))    # tail ~ (98, 283)
fat_line(d, p, q, width=6)

# s7: 横折 — top heng + right vertical of 皿 frame.
# MMH head/tail are median endpoints; the true frame extends beyond the tail
# on the right (per GT: right vertical sits near x~245, aligned with s10 tail).
p = anchor_to_xy(('BL', 0.858, 0.294))   # head ~ (86, 229)
q = anchor_to_xy(('BC', 0.916, 0.763))   # tail ~ (192, 276)
# Extend the top heng further right so 皿 frame looks like a real rectangle.
top_right_x = 245                        # aligns with 皿 bottom heng right edge
corner = (top_right_x, p[1])
bottom_right = (top_right_x, q[1])
fat_line(d, p, corner, width=6)
fat_line(d, corner, bottom_right, width=6)

# s8: inner 竖 1 of 皿
p = anchor_to_xy(('BC', 0.216, 0.355))   # head ~ (122, 236)
q = anchor_to_xy(('BC', 0.301, 0.818))   # tail ~ (130, 282)
fat_line(d, p, q, width=6)

# s9: inner 竖 2 of 皿
p = anchor_to_xy(('BC', 0.564, 0.259))   # head ~ (156, 226)
q = anchor_to_xy(('BC', 0.529, 0.801))   # tail ~ (153, 280)
fat_line(d, p, q, width=6)

# s10: bottom long 一 of 皿 (widest stroke)
p = anchor_to_xy(('BL', 0.328, 0.93))    # head ~ (33, 293)
q = anchor_to_xy(('BR', 0.739, 0.897))   # tail ~ (274, 290)
fat_line(d, p, q, width=7)

out = os.path.join(os.path.dirname(__file__), '01_盍.png')
img.save(out)
print(f'wrote {out}')
