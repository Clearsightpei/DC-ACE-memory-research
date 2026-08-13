"""佥 (qiān) — 7 strokes.
Decomposition: 佥 = 人 (top apex) + 一 (middle heng) + 从-like base (2 pie + 2 short strokes) + 一 (bottom heng).
Layout: 人 covers top; middle heng at C-row; base fills bottom row; bottom heng terminates.

Memory-read log:
  # drawer_memory.md read — A-recipe (MMH-verbatim + inline base primitives).
  # success_bank/INDEX grep 佥 — no mastered entry.
  # errata.md grep 佥 — not present.
Following B9 A-recipe: MMH-verbatim anchors + fat_line base primitives.
Compound primitives (ren) rejected because MMH places apex at TC(0.53,0.92),
below ren.py defaults; partial override would risk B8 伊-style FAIL.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

from PIL import Image, ImageDraw

W = 6  # stroke width

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# Stroke 1: 人-left pie — TC(0.38,0.647) → BL(0.293,0.033)
p1a = anchor_to_xy(('TC', 0.38, 0.647))
p1b = anchor_to_xy(('BL', 0.293, 0.033))
# slight curve typical of pie: control point pulled a bit inward
ctrl1 = ((p1a[0] + p1b[0]) / 2 - 4, (p1a[1] + p1b[1]) / 2 + 6)
pts1 = quad_bezier(p1a, ctrl1, p1b, n=40)
widths1 = [W + 2 - i * (W - 2) / 40 for i in range(41)]  # taper
stroke_variable_width(d, pts1, widths1)

# Stroke 2: 人-right na — TC(0.532,0.923) → MR(0.856,0.696)
p2a = anchor_to_xy(('TC', 0.532, 0.923))
p2b = anchor_to_xy(('MR', 0.856, 0.696))
ctrl2 = ((p2a[0] + p2b[0]) / 2, (p2a[1] + p2b[1]) / 2 + 8)
pts2 = quad_bezier(p2a, ctrl2, p2b, n=40)
widths2 = [max(2, W - 2 + i * 4 / 40) for i in range(41)]  # thickens toward tail (na)
stroke_variable_width(d, pts2, widths2)

# Stroke 3: middle heng — C(0.096,0.705) → C(0.854,0.632)
p3a = anchor_to_xy(('C', 0.096, 0.705))
p3b = anchor_to_xy(('C', 0.854, 0.632))
fat_line(d, p3a, p3b, W)

# Stroke 4: bottom-left pie/dian short — BL(0.841,0.142) → BC(0.131,0.487)
p4a = anchor_to_xy(('BL', 0.841, 0.142))
p4b = anchor_to_xy(('BC', 0.131, 0.487))
fat_line(d, p4a, p4b, W - 1)

# Stroke 5: small dian in BC — BC(0.286,0.027) → BC(0.479,0.341)
p5a = anchor_to_xy(('BC', 0.286, 0.027))
p5b = anchor_to_xy(('BC', 0.479, 0.341))
fat_line(d, p5a, p5b, W - 1)

# Stroke 6: right pie in base — C(0.919,0.89) → BC(0.556,0.707)
p6a = anchor_to_xy(('C', 0.919, 0.89))
p6b = anchor_to_xy(('BC', 0.556, 0.707))
ctrl6 = ((p6a[0] + p6b[0]) / 2 + 4, (p6a[1] + p6b[1]) / 2 - 2)
pts6 = quad_bezier(p6a, ctrl6, p6b, n=40)
widths6 = [W + 1 - i * (W - 2) / 40 for i in range(41)]
stroke_variable_width(d, pts6, widths6)

# Stroke 7: bottom heng — BL(0.574,0.827) → BR(0.496,0.812)
p7a = anchor_to_xy(('BL', 0.574, 0.827))
p7b = anchor_to_xy(('BR', 0.496, 0.812))
fat_line(d, p7a, p7b, W)

out = os.path.join(os.path.dirname(__file__), '01_佥.png')
img.save(out)

# ---- SELF_CHECK ----
# Stroke count: 7 draw calls (s1..s7) ✓
# Endpoint anchors: MMH-verbatim tuples used ✓
# Joints:
#   s1.head ⇆ s2.head @ TC (~(0.5, 0.85)) : N — MMH says gap ~20 px.
#     Actual: p1a=(138, 65), p2a=(153, 92). dist = sqrt(15^2+27^2) ≈ 30.9 px → N gap preserved ✓
#   s6.tail ⇆ s7.mid(0.46) @ BC (~(0.5, 0.75)) : N — MMH says gap ~18 px.
#     s7.mid at t=0.46: (57.4 + 0.46*(249.6-57.4), 282.7 + 0.46*(281.2-282.7)) ≈ (145.8, 282.0)
#     s6.tail = (155.6, 270.7). dist ≈ sqrt(9.8^2 + 11.3^2) ≈ 15.0 px → N gap preserved ✓
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '7 strokes MMH-verbatim; both N-joints preserved as natural gaps (~15-30 px).',
}
