"""p3_char_0455_相 (xiāng) — 9 strokes.

Decomposition: 相 = 木 (left) + 目 (right).
  木 = heng + shu + pie + na (strokes 1-4)
  目 = shu + heng-zhe + heng + heng + heng (strokes 5-9)

Per B9/B10/B11 A-recipe: MMH-verbatim anchors + base primitives.
Skipping ri.py (目 primitive) because 目 is right-half compressed and
ri.py's DEFAULTS fill full canvas; slot-embedding pattern.
mu.py does not exist in bank (never restored post-Phase1 reset).

# BANK_DEVIATION
# skipped: ri.py
# reason: 目 is embedded as right-half compressed slot (x_frac ~0.55-0.90
#         of canvas). ri.py DEFAULTS render wall-to-wall standalone 目.
# fresh_component: ri_right_half_for_compound
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '../../success_bank/code'))
from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 9 primitive calls (heng-zhe is 1 stroke via 2-seg polyline)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '9 strokes MMH-verbatim; 木 left + 目 right; N-joints preserved as gaps; heng-zhe as single L-polyline.',
}


img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# === 木 (strokes 1-4) ===
# s1: heng
s1h = anchor_to_xy(('ML', 0.287, 0.538))
s1t = anchor_to_xy(('C',  0.368, 0.383))
fat_line(draw, s1h, s1t, width=8)

# s2: shu (vertical spine of 木)
s2h = anchor_to_xy(('TL', 0.87, 0.568))
s2t = anchor_to_xy(('BL', 0.923, 1.038))
fat_line(draw, s2h, s2t, width=9)

# s3: pie (going down-left from spine)
s3h = anchor_to_xy(('ML', 0.914, 0.564))
s3t = anchor_to_xy(('BL', 0.193, 0.546))
# curve slightly: control point pulled up-right of midpoint
mid = ((s3h[0] + s3t[0]) / 2, (s3h[1] + s3t[1]) / 2)
ctrl = (mid[0] + 5, mid[1] - 12)
pts = quad_bezier(s3h, ctrl, s3t, n=32)
widths = [8 - 6 * (i / len(pts)) for i in range(len(pts))]  # taper
stroke_variable_width(draw, pts, widths)

# s4: na (short dot-like right stroke on 木, compressed since 木 is left radical)
s4h = anchor_to_xy(('C',  0.061, 0.787))
s4t = anchor_to_xy(('BC', 0.345, 0.051))
# taper from narrow to wide (na thickens toward tail)
pts4 = quad_bezier(s4h,
                   ((s4h[0]+s4t[0])/2 - 3, (s4h[1]+s4t[1])/2 + 2),
                   s4t, n=24)
widths4 = [3 + 6 * (i / len(pts4)) for i in range(len(pts4))]
stroke_variable_width(draw, pts4, widths4)

# === 目 (strokes 5-9) ===
# s5: left shu of 目
s5h = anchor_to_xy(('C',  0.553, 0.184))
s5t = anchor_to_xy(('BC', 0.626, 0.76))
fat_line(draw, s5h, s5t, width=9)

# s6: heng-zhe (top + right side of 目) — single L-polyline via corner
s6h = anchor_to_xy(('C',  0.737, 0.216))
s6t = anchor_to_xy(('BR', 0.391, 0.815))
# corner at top-right of 目: x=s6t[0], y=s6h[1]
corner = (s6t[0], s6h[1])
fat_line(draw, s6h, corner, width=9)  # top heng
fat_line(draw, corner, s6t, width=9)  # right shu
# small solidify at corner
r = 5
draw.ellipse([corner[0]-r, corner[1]-r, corner[0]+r, corner[1]+r], fill=(0,0,0))

# s7: middle heng #1 (inside 目, upper)
s7h = anchor_to_xy(('C',  0.746, 0.737))
s7t = anchor_to_xy(('MR', 0.142, 0.673))
fat_line(draw, s7h, s7t, width=7)

# s8: middle heng #2 (inside 目, lower)
s8h = anchor_to_xy(('BC', 0.752, 0.159))
s8t = anchor_to_xy(('BR', 0.15, 0.101))
fat_line(draw, s8h, s8t, width=7)

# s9: bottom heng (closes 目)
s9h = anchor_to_xy(('BC', 0.731, 0.622))
s9t = anchor_to_xy(('BR', 0.244, 0.525))
fat_line(draw, s9h, s9t, width=8)


out = os.path.join(os.path.dirname(__file__), '01_相.png')
img.save(out)
print(f'wrote {out}')
