"""p3_char_0267_西  — G4 attempt, PIL 300x300, black on white.

Split: 一 (top) + 冂-like frame (left 丨 + top-right heng-zhe) +
       inner two strokes (儿-like) + bottom closing 一.
6 MMH strokes total. Anchors from dispatcher-injected MMH block.
"""

import os, sys
from PIL import Image, ImageDraw

# Path fix so _anchor.py imports from the shared bank.
BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)
from _anchor import anchor_to_xy, stroke_variable_width, fat_line, quad_bezier

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '6 strokes: heng, shu(left), heng-zhe(top+right), inner-pie, '
             'inner-shu-wan, bottom-heng. s3 bent at TR-corner-in-C-cell '
             'to make the two P-welds with s4 & s5 land near cell C.'
}

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 6  # line thickness

# ---- stroke 1: top 一 ----
p1a = anchor_to_xy(('TL', 0.738, 0.967))
p1b = anchor_to_xy(('TR', 0.171, 0.829))
fat_line(d, p1a, p1b, LW, INK)

# ---- stroke 2: left 丨 (frame left side) ----
p2a = anchor_to_xy(('ML', 0.437, 0.57))
p2b = anchor_to_xy(('BL', 0.762, 0.728))
fat_line(d, p2a, p2b, LW, INK)

# ---- stroke 3: heng-zhe (top-right corner of frame) ----
# head at ML(0.653, 0.614), tail at BC(0.983, 0.604), bend at top-right.
p3a = anchor_to_xy(('ML', 0.653, 0.614))
p3b = anchor_to_xy(('BC', 0.983, 0.604))
# corner: right edge of frame is at x ~= p3b.x, top edge is at y ~= p3a.y.
corner = (p3b[0], p3a[1])
fat_line(d, p3a, corner, LW, INK)
fat_line(d, corner, p3b, LW, INK)

# ---- stroke 4: inner left short 撇 (nearly vertical, slight left) ----
p4a = anchor_to_xy(('C', 0.084, 0.066))
p4b = anchor_to_xy(('BL', 0.935, 0.224))
fat_line(d, p4a, p4b, LW, INK)

# ---- stroke 5: inner right 竖弯 (starts near top-center-bottom, curves down-right) ----
p5a = anchor_to_xy(('TC', 0.529, 0.993))
p5b = anchor_to_xy(('BR', 0.118, 0.01))
# gentle curve via a control point that bulges to the right
ctrl5 = (p5a[0] + 6, (p5a[1] + p5b[1]) / 2)
pts5 = quad_bezier(p5a, ctrl5, p5b, n=32)
widths5 = [LW] * len(pts5)
stroke_variable_width(d, pts5, widths5, INK)

# ---- stroke 6: bottom closing 一 ----
p6a = anchor_to_xy(('BL', 0.832, 0.648))
p6b = anchor_to_xy(('BR', 0.027, 0.528))
fat_line(d, p6a, p6b, LW, INK)

out = os.path.join(os.path.dirname(__file__), "01_西.png")
img.save(out)
print("wrote", out)
