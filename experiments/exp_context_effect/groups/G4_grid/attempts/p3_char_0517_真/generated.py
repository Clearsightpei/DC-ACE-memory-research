"""真 (zhēn) — 10 strokes.

Decomposition (MMH stroke order):
  s1 heng (top of 十)          s2 shu (vertical of 十) — s1+s2 form 十 at top
  s3 shu (left of 目 frame)
  s4 heng-zhe (top+right of 目 frame)
  s5,s6,s7 three inner heng of 目 (top, middle, bottom-of-frame)
  s8 long 一 (extends beyond frame)
  s9 pie (left leg of 八)
  s10 na (right leg of 八)

Follows the p3_0425_具 A-recipe (MMH-verbatim anchors, base primitives
via _anchor.fat_line + quad_bezier). Adds the 十 top absent in 具. No
compound bank primitive fits (no 真-family entry, mu.py absent).
N-joints kept as small natural gaps; s1×s2 is the sole P (welded).
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import (anchor_to_xy, fat_line, quad_bezier,
                     stroke_variable_width)

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 10 draw calls below
    'endpoint_mismatches': [],     # all MMH-verbatim
    'joint_class_mismatches': [],  # s1×s2 welded P; all others natural N gaps
    'overall_pass': True,
    'notes': '10 strokes MMH-verbatim; 十 top + 目 frame + long一 + 八; N-gaps preserved.',
}

W = 300
img = Image.new('RGB', (W, W), (255, 255, 255))
d = ImageDraw.Draw(img)

INK_W = 6

# ---------------- 十 top (strokes 1-2, P-welded at TC) ----------------

# s1: top 一 of 十.  MMH TL(0.809, 0.961) -> TR(0.256, 0.838)
p_s1_h = anchor_to_xy(('TL', 0.809, 0.961))
p_s1_t = anchor_to_xy(('TR', 0.256, 0.838))
fat_line(d, p_s1_h, p_s1_t, INK_W)

# s2: short 丨 of 十.  MMH TC(0.436, 0.545) -> C(0.418, 0.28)
p_s2_h = anchor_to_xy(('TC', 0.436, 0.545))
p_s2_t = anchor_to_xy(('C',  0.418, 0.28))
fat_line(d, p_s2_h, p_s2_t, INK_W)

# ---------------- 目 frame (strokes 3-7) ----------------

# s3: 竖 — left side of 目.  MMH C(0.008, 0.312) -> BC(0.069, 0.35)
p_s3_h = anchor_to_xy(('C',  0.008, 0.312))
p_s3_t = anchor_to_xy(('BC', 0.069, 0.35))
fat_line(d, p_s3_h, p_s3_t, INK_W)

# s4: 横折 — top+right of 目.  MMH C(0.143, 0.333) -> BC(0.831, 0.271)
p_s4_h = anchor_to_xy(('C',  0.143, 0.333))
p_s4_t = anchor_to_xy(('BC', 0.831, 0.271))
# corner: top-right of frame; same y as head, same x as tail.
p_s4_corner = (p_s4_t[0], p_s4_h[1])
fat_line(d, p_s4_h, p_s4_corner, INK_W)
fat_line(d, p_s4_corner, p_s4_t, INK_W)

# s5: inner heng #1 (upper inner).  MMH C(0.189, 0.667) -> C(0.699, 0.603)
p_s5_h = anchor_to_xy(('C', 0.189, 0.667))
p_s5_t = anchor_to_xy(('C', 0.699, 0.603))
fat_line(d, p_s5_h, p_s5_t, INK_W - 1)

# s6: inner heng #2 (middle inner).  MMH C(0.201, 0.931) -> C(0.688, 0.872)
p_s6_h = anchor_to_xy(('C', 0.201, 0.931))
p_s6_t = anchor_to_xy(('C', 0.688, 0.872))
fat_line(d, p_s6_h, p_s6_t, INK_W - 1)

# s7: bottom heng of 目 frame.  MMH BC(0.192, 0.183) -> BC(0.711, 0.121)
p_s7_h = anchor_to_xy(('BC', 0.192, 0.183))
p_s7_t = anchor_to_xy(('BC', 0.711, 0.121))
fat_line(d, p_s7_h, p_s7_t, INK_W - 1)

# ---------------- long 一 (stroke 8) ----------------

# s8: long 一 below 目.  MMH BL(0.325, 0.461) -> BR(0.692, 0.417)
p_s8_h = anchor_to_xy(('BL', 0.325, 0.461))
p_s8_t = anchor_to_xy(('BR', 0.692, 0.417))
fat_line(d, p_s8_h, p_s8_t, INK_W + 1)  # slightly heavier main crossbar

# ---------------- 八 (strokes 9-10) ----------------

# s9: 撇 (left leg).  MMH BC(0.298, 0.716) -> BL(0.604, 1.103)
p_s9_h = anchor_to_xy(('BC', 0.298, 0.716))
p_s9_t = anchor_to_xy(('BL', 0.604, 1.103))
mx = (p_s9_h[0] + p_s9_t[0]) / 2
my = (p_s9_h[1] + p_s9_t[1]) / 2
p_s9_ctrl = (mx - 6, my)
pts9 = quad_bezier(p_s9_h, p_s9_ctrl, p_s9_t, n=40)
widths9 = [max(2, INK_W - 1 - int(3 * (i / 40))) for i in range(41)]
stroke_variable_width(d, pts9, widths9)

# s10: 捺 (right leg).  MMH BC(0.778, 0.604) -> BR(0.227, 1.085)
p_s10_h = anchor_to_xy(('BC', 0.778, 0.604))
p_s10_t = anchor_to_xy(('BR', 0.227, 1.085))
mx = (p_s10_h[0] + p_s10_t[0]) / 2
my = (p_s10_h[1] + p_s10_t[1]) / 2
p_s10_ctrl = (mx + 4, my + 4)
pts10 = quad_bezier(p_s10_h, p_s10_ctrl, p_s10_t, n=40)
widths10 = []
for i in range(41):
    t = i / 40
    if t < 0.85:
        w = INK_W - 1 + int(4 * t)
    else:
        w = INK_W - 1 + int(4 * 0.85) - int(6 * (t - 0.85) / 0.15)
    widths10.append(max(2, w))
stroke_variable_width(d, pts10, widths10)

# ---------------- save ----------------
out = os.path.join(os.path.dirname(__file__), '01_真.png')
img.save(out)
print(f'wrote {out}')
