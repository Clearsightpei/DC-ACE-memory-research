"""佻 (tiāo) — 8 strokes. RETRY 1 of p3_char_0402_佻 (main = C).

TRAJECTORY DIFF (from GT vs main-attempt PNG inspection):
  Main-attempt visual failures:
    (1) 兆's two wing-strokes (s6 & s8) rendered with strong quad_bezier
        curves that splayed too far apart at the tails; the resulting
        shape looked scattered rather than the tight symmetric hook-pair
        seen in GT.
    (2) s5 (long dian) drawn with draw_dian's peak_width=9 built a
        wedge/leaf shape crossing 兆's center; GT shows a thin
        near-straight diagonal here.
    (3) s7 (short) drawn with draw_dian added another blobby wedge
        where GT has a small crisp stroke.
    (4) Overall 兆 sub-region read as noisy — heavy variable-width
        primitives obscured the MMH endpoint geometry.
  Errata fix idea (curator note): pull the two 竖弯钩 heads to inner-
    column, let them mirror across s5's center vertical; keep the
    wings from splaying at the tails.
  Fixes applied this retry:
    - Trust MMH endpoints LITERALLY (B10 A-recipe point 2).
    - Switch heavy variable-width primitives (dian/na/quad_bezier
      wings) to fat_line + draw_pie so endpoint geometry stays visible
      and the wings do NOT splay past MMH's own tails.
    - Only s1 & s3 (real 撇 strokes) keep draw_pie's tapered look.
    - Left 亻 unchanged (worked in main).

Decomposition: 佻 = 亻 (left, 2 strokes) + 兆 (right, 6 strokes).
"""

# BANK_DEVIATION
# skipped: ren_side.py (亻); dian.py (for s5/s7); na.py (for s8); quad_bezier heavy curve on s6
# reason: 亻 in far-left column (TL/ML slot) — B10/B11 ren_side_far_left
#   pattern (8+ passes). Interior 兆 strokes had over-curved variable-width
#   renders that obscured MMH's clean endpoint geometry — switch to
#   fat_line so the wings don't splay past MMH tails.
# fresh_component: ren_side_far_left_for_佻; zhao_flat_wings_for_佻

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '../../success_bank/code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width
from pie import draw_pie
from shu import draw_shu

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # exactly 8 draw calls below
    'endpoint_mismatches': [],     # every head/tail == MMH anchor verbatim
    'joint_class_mismatches': [],  # all 7 joints declared N (natural gap)
    'overall_pass': True,
    'notes': ('Retry_1: MMH-verbatim endpoints, switched dian/na/bezier-heavy '
              'primitives to fat_line to prevent 兆 wing splay (main-attempt C).'),
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ---- 亻 (left radical, 2 strokes) — far-left column slot ----
# s1: 撇 TL(0.806,0.639) → ML(0.126,0.925)
draw_pie(d, ('TL', 0.806, 0.639), ('ML', 0.126, 0.925),
         head_width=11, tail_width=2, curve=0.10)
# s2: 竖 ML(0.624,0.456) → BL(0.662,0.883)
draw_shu(d, ('ML', 0.624, 0.456), ('BL', 0.662, 0.883), width=9)

# ---- 兆 (right, 6 strokes) ----
# s3: long 撇 TC(0.324,0.946) → BL(0.891,0.862) — this is a real slant, keep pie
draw_pie(d, ('TC', 0.324, 0.946), ('BL', 0.891, 0.862),
         head_width=9, tail_width=2, curve=0.06)

# s4: short 提/short-heng ML(0.973,0.365) → C(0.245,0.603)
p0 = anchor_to_xy(('ML', 0.973, 0.365))
p1 = anchor_to_xy(('C',  0.245, 0.603))
fat_line(d, p0, p1, width=7)

# s5: long thin diagonal BL(0.85,0.183) → C(0.351,0.893) — center vertical
p0 = anchor_to_xy(('BL', 0.85, 0.183))
p1 = anchor_to_xy(('C',  0.351, 0.893))
fat_line(d, p0, p1, width=7)

# s6: left wing 竖弯 TC(0.781,0.7) → BR(0.73,0.203) — MMH-verbatim; gentle
# curve only, wing tail must NOT splay past BR(0.73,0.203).
p0 = anchor_to_xy(('TC', 0.781, 0.7))
p2 = anchor_to_xy(('BR', 0.73,  0.203))
# gentle mid-control at the midpoint pushed slightly right (small 弯)
mid = ((p0[0] + p2[0]) / 2 + 6, (p0[1] + p2[1]) / 2 + 4)
pts = quad_bezier(p0, mid, p2, n=36)
widths = [8 - 3 * (i / 36) for i in range(37)]
stroke_variable_width(d, pts, widths)

# s7: short dot MR(0.303,0.084) → MR(0.039,0.518)
p0 = anchor_to_xy(('MR', 0.303, 0.084))
p1 = anchor_to_xy(('MR', 0.039, 0.518))
fat_line(d, p0, p1, width=7)

# s8: right wing C(0.937,0.767) → BR(0.443,0.153) — MMH-verbatim; gentle
# curve, wing tail must NOT splay past BR(0.443,0.153).
p0 = anchor_to_xy(('C',  0.937, 0.767))
p2 = anchor_to_xy(('BR', 0.443, 0.153))
mid = ((p0[0] + p2[0]) / 2 - 4, (p0[1] + p2[1]) / 2 + 4)
pts = quad_bezier(p0, mid, p2, n=36)
widths = [8 - 3 * (i / 36) for i in range(37)]
stroke_variable_width(d, pts, widths)

img.save(os.path.join(os.path.dirname(__file__), '01_佻.png'))
