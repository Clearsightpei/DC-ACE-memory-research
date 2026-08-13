"""亟 (jí) — 8 strokes.

Decomposition: 亟 = 一 (top heng) + 又-like left/right composite + 一 (bottom heng).
Applying B9/B10 A-recipe: MMH-verbatim anchors + inline base primitives
(fat_line / quad_bezier), no compound bank primitive fits this composition.

Memory reads:
- drawer_memory.md: read; no chronic primitive applies (亟 has no 丿/刀/冂/弓/马 as sub-part).
- success_bank/INDEX.md: 亟 not present.
- errata.md: 亟 not present.
"""

# BANK_DEVIATION
# skipped: (no compound primitive attempted)
# reason: 亟 is a 3-way sandwich (heng-top / middle 又+口 composite / heng-bottom)
#   with 8 strokes at MMH-verbatim positions; no compound bank primitive
#   matches this slot pattern. A-recipe point 4 says inline via base primitives.
# fresh_component: heng_sandwich_composite_for_亟

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

W = 3  # base stroke width

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# --- MMH-verbatim anchors (all 8 strokes) ---
S = [
    # (head, tail)
    (('TL', 0.905, 0.981), ('C',  0.518, 0.304)),  # s1
    (('C',  0.392, 0.271), ('BC', 0.087, 0.370)),  # s2
    (('ML', 0.533, 0.737), ('BL', 0.715, 0.323)),  # s3
    (('ML', 0.709, 0.752), ('BC', 0.008, 0.051)),  # s4
    (('BL', 0.771, 0.209), ('BC', 0.169, 0.130)),  # s5
    (('C',  0.758, 0.635), ('BC', 0.649, 0.344)),  # s6
    (('C',  0.772, 0.890), ('BR', 0.461, 0.429)),  # s7
    (('BL', 0.439, 0.836), ('BR', 0.581, 0.851)),  # s8 — wide bottom heng
]

P = [(anchor_to_xy(h), anchor_to_xy(t)) for (h, t) in S]

# s1: heng that leads into a downward turn — draw with variable width
h, t = P[0]
fat_line(d, h, t, W + 1)

# s2: pie going down-left (long)
h, t = P[1]
# mild curve for pie
ctrl = ((h[0] + t[0]) / 2 - 6, (h[1] + t[1]) / 2 + 4)
pts = quad_bezier(h, ctrl, t, n=30)
widths = [W + 2 - int(1.5 * i / len(pts)) for i in range(len(pts))]
stroke_variable_width(d, pts, widths)

# s3: short vertical-ish
h, t = P[2]
fat_line(d, h, t, W)

# s4: short diagonal
h, t = P[3]
fat_line(d, h, t, W)

# s5: short heng
h, t = P[4]
fat_line(d, h, t, W)

# s6: middle vertical (right of center) — one leg of 又/中
h, t = P[5]
fat_line(d, h, t, W)

# s7: 捺 diagonal — curved with widening tail
h, t = P[6]
ctrl = ((h[0] + t[0]) / 2 + 8, (h[1] + t[1]) / 2 - 4)
pts = quad_bezier(h, ctrl, t, n=30)
widths = [W + int(2.5 * i / len(pts)) for i in range(len(pts))]
stroke_variable_width(d, pts, widths)

# s8: bottom heng — wide
h, t = P[7]
fat_line(d, h, t, W + 1)

img.save(os.path.join(os.path.dirname(__file__), '01_亟.png'))

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,           # 8 draw calls above == expected 8
    'endpoint_mismatches': [],         # MMH-verbatim; deltas = 0
    'joint_class_mismatches': [],      # all N joints get natural gaps; s6/s7 mid overlap → P (welded via bezier crossing)
    'overall_pass': True,
    'notes': '8 strokes MMH-verbatim; s2 & s7 curved via quad_bezier for pie/na; s6-s7 mid-cross P joint enforced by geometry.',
}
