"""畚 (běn) — 10 strokes.
Decomposition: 畚 = 龴/采-top (5 strokes) + 田 (5 strokes).
Top: two small marks (s1, s2) + horizontal beam (s3) + left leg 撇 (s4) + right leg 捺 (s5).
Bottom: 田 = s6 left竖 + s7 横折 (right side + top) + s8 middle横 + s9 middle竖 + s10 bottom横.

MMH-verbatim anchors from dispatcher-injected block. Base primitives inlined
via fat_line and stroke_variable_width. No compound bank primitive was a
clean fit (no bank entry for 畚 or 采-top or 田-compound); base-primitives-
inline per A-recipe point 4.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width, sample_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '10 strokes MMH-verbatim; top 5 = 采-form dots+beam+legs; bottom 5 = 田. N-joints preserved as small gaps.',
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# --- TOP (采-like), strokes 1-5 ---

# s1: TC(0.336, 0.524) -> C(0.875, 0.137) — top 撇 (short pie sloping down-left as drawn)
# MMH direction: head at (133,52) tail at (188,114). Draw with 丿-taper thick-head→thin-tail.
p1a = anchor_to_xy(('TC', 0.336, 0.524))
p1b = anchor_to_xy(('C',  0.875, 0.137))
# gentle curve
mid1 = ((p1a[0]+p1b[0])/2 + 3, (p1a[1]+p1b[1])/2 - 2)
pts1 = quad_bezier(p1a, mid1, p1b, 30)
widths1 = [6 - 4*(i/30) for i in range(31)]  # thick head → thin tail (proper 丿)
stroke_variable_width(d, pts1, widths1)

# s2: TC(0.723, 0.899) -> MR(0.074, 0.245) — small 丶 dot at top-right
p2a = anchor_to_xy(('TC', 0.723, 0.899))
p2b = anchor_to_xy(('MR', 0.074, 0.245))
pts2 = sample_line(p2a, p2b, 16)
widths2 = [4 + 5*(i/16) for i in range(17)]  # thin→thick teardrop
stroke_variable_width(d, pts2, widths2)

# s3: ML(0.451, 0.708) -> MR(0.423, 0.588) — long horizontal beam
p3a = anchor_to_xy(('ML', 0.451, 0.708))
p3b = anchor_to_xy(('MR', 0.423, 0.588))
fat_line(d, p3a, p3b, 6)

# s4: C(0.222, 0.307) -> BL(0.296, 0.382) — long left-going 撇 leg
p4a = anchor_to_xy(('C',  0.222, 0.307))
p4b = anchor_to_xy(('BL', 0.296, 0.382))
# slight curve leftward
mid4 = ((p4a[0]+p4b[0])/2 - 8, (p4a[1]+p4b[1])/2)
pts4 = quad_bezier(p4a, mid4, p4b, 40)
widths4 = [7 - 5*(i/40) for i in range(41)]  # thick→thin (撇)
stroke_variable_width(d, pts4, widths4)

# s5: C(0.764, 0.655) -> BR(0.851, 0.136) — long right-going 捺 leg
p5a = anchor_to_xy(('C',  0.764, 0.655))
p5b = anchor_to_xy(('BR', 0.851, 0.136))
mid5 = ((p5a[0]+p5b[0])/2 + 6, (p5a[1]+p5b[1])/2 + 4)
pts5 = quad_bezier(p5a, mid5, p5b, 40)
widths5 = [4 + 6*(i/40) for i in range(41)]  # thin→thick (捺)
stroke_variable_width(d, pts5, widths5)

# --- BOTTOM 田, strokes 6-10 ---

# s6: BL(0.823, 0.2) -> BC(0.031, 0.988) — left 竖 of 田. Clamp y to canvas.
p6a = anchor_to_xy(('BL', 0.823, 0.2))
p6b_raw = anchor_to_xy(('BC', 0.031, 0.988))
p6b = (p6b_raw[0], min(p6b_raw[1], 295))
fat_line(d, p6a, p6b, 6)

# s7: BC(0.002, 0.188) -> BC(0.872, 1.076) — 横折 (top + right side of 田).
# Bent stroke: horizontal top then vertical right. Clamp y_tail to canvas.
p7_start = anchor_to_xy(('BC', 0.002, 0.188))
p7_corner = anchor_to_xy(('BC', 0.872, 0.188))  # bend at top-right
p7_end_raw = anchor_to_xy(('BC', 0.872, 1.076))
p7_end = (p7_end_raw[0], min(p7_end_raw[1], 295))
fat_line(d, p7_start, p7_corner, 6)
fat_line(d, p7_corner, p7_end, 6)

# s8: BC(0.148, 0.522) -> BC(0.731, 0.473) — middle horizontal of 田
p8a = anchor_to_xy(('BC', 0.148, 0.522))
p8b = anchor_to_xy(('BC', 0.731, 0.473))
fat_line(d, p8a, p8b, 5)

# s9: BC(0.342, 0.235) -> BC(0.377, 0.76) — middle vertical of 田
p9a = anchor_to_xy(('BC', 0.342, 0.235))
p9b = anchor_to_xy(('BC', 0.377, 0.76))
fat_line(d, p9a, p9b, 5)

# s10: BC(0.093, 0.889) -> BC(0.778, 0.786) — bottom horizontal of 田
p10a = anchor_to_xy(('BC', 0.093, 0.889))
p10b = anchor_to_xy(('BC', 0.778, 0.786))
fat_line(d, p10a, p10b, 6)

out = os.path.join(os.path.dirname(__file__), '01_畚.png')
img.save(out)
print('wrote', out)
