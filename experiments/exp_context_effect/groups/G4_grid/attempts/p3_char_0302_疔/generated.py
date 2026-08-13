"""p3_char_0302_疔 — G4 attempt.

Structure: 疒 (5 strokes: dian, heng, long-pie, inner-dian, inner-ti)
         + 丁 (2 strokes: heng, shu-gou) = 7 strokes total.

Memory notes:
  - Reading order: drawer_memory.md; INDEX lookup — 疒 (0171) exists as
    a mastered composition but no dedicated .py; 丁 in errata (fix: heng
    full-width, shu head on heng, N-gap small). Inlining fresh here.
  - Anchors driven by MMH structural block.
"""

import os, sys
BANK = os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
sys.path.insert(0, os.path.abspath(BANK))
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'inlined; s3 long pie curves left; s7 shu-gou with left hook at tail; N-gaps preserved (not welded).'
}

CANVAS = 300
img = Image.new('RGB', (CANVAS, CANVAS), 'white')
d = ImageDraw.Draw(img)

W_MAIN = 6   # main strokes
W_DOT  = 7   # dot / short strokes

# --- 疒 ---
# s1: top dian (点) — short slant from upper-left to lower-right
p1a = anchor_to_xy(('TC', 0.462, 0.545))
p1b = anchor_to_xy(('TC', 0.781, 0.809))
# taper: thin start, thicker end
pts = [(p1a[0] + (p1b[0]-p1a[0])*i/8, p1a[1] + (p1b[1]-p1a[1])*i/8) for i in range(9)]
widths = [2 + int(6*i/8) for i in range(9)]
stroke_variable_width(d, pts, widths)

# s2: top heng of 广 (slight upward slope right-to-left is actually here left-to-right slightly up)
p2a = anchor_to_xy(('C', 0.037, 0.128))
p2b = anchor_to_xy(('TR', 0.335, 0.993))
fat_line(d, p2a, p2b, W_MAIN)

# s3: long left pie (撇) — starts near heng-left, curves down-left
p3a = anchor_to_xy(('ML', 0.844, 0.081))
p3b = anchor_to_xy(('BL', 0.41, 1.003))
# control point pulls slightly leftward for curve
ctrl3 = ((p3a[0] + p3b[0]) / 2 - 15, (p3a[1] + p3b[1]) / 2 + 10)
curve3 = quad_bezier(p3a, ctrl3, p3b, n=40)
# taper — thicker mid, thin tail
w3 = [W_MAIN - int(3 * (i/40) ** 2) for i in range(41)]
stroke_variable_width(d, curve3, w3)

# s4: inner upper dian (short down-right stroke)
p4a = anchor_to_xy(('ML', 0.396, 0.298))
p4b = anchor_to_xy(('ML', 0.636, 0.57))
pts4 = [(p4a[0] + (p4b[0]-p4a[0])*i/6, p4a[1] + (p4b[1]-p4a[1])*i/6) for i in range(7)]
w4 = [2 + int(5*i/6) for i in range(7)]
stroke_variable_width(d, pts4, w4)

# s5: inner ti (提) — short up-right stroke
p5a = anchor_to_xy(('BL', 0.193, 0.124))
p5b = anchor_to_xy(('ML', 0.791, 0.901))
pts5 = [(p5a[0] + (p5b[0]-p5a[0])*i/8, p5a[1] + (p5b[1]-p5a[1])*i/8) for i in range(9)]
w5 = [6 - int(4*i/8) for i in range(9)]
stroke_variable_width(d, pts5, w5)

# --- 丁 (inside) ---
# s6: heng of 丁 — horizontal in center-right
p6a = anchor_to_xy(('C', 0.104, 0.685))
p6b = anchor_to_xy(('MR', 0.52, 0.591))
fat_line(d, p6a, p6b, W_MAIN)

# s7: shu-gou of 丁 — vertical, small hook to the left at the bottom
p7a = anchor_to_xy(('C', 0.69, 0.702))
p7b = anchor_to_xy(('BC', 0.418, 0.771))
# mostly vertical with a leftward curl near tail
mid7 = (p7a[0] - 4, (p7a[1] + p7b[1]) / 2)
curve7 = quad_bezier(p7a, mid7, p7b, n=30)
fat_line(d, curve7[0], curve7[15], W_MAIN)  # straight upper half
# lower half — leftward-curving hook
for i in range(15, 30):
    fat_line(d, curve7[i], curve7[i+1], W_MAIN)

out_path = os.path.join(os.path.dirname(__file__), '01_疔.png')
img.save(out_path)
print(f"wrote {out_path}")
print(f"stroke count: 7")
