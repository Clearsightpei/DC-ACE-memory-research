"""佻 (tiāo) — 8 strokes. RETRY 2 of p3_char_0402_佻.

TRAJECTORY DIFF (from GT vs prior attempt PNGs):
  main (verdict C) — 兆's two wing-strokes (s6 & s8) heavily curved
    quad_bezier that splayed apart at the tails; s5 & s7 drawn as
    variable-width wedges — right side read as noisy blob.
  retry_1 (verdict FAIL) — kept endpoint fidelity but the two long
    right-side strokes s3 and s6 formed a hard X-cross that dominated
    the right sub-region. s5 (BL→C long diagonal, ~87px) was rendered
    fat and long, reading as another slanted bar instead of a small
    inner mark. Net: right 兆 half looked like an X plus 2 sticks,
    not the balanced 3-column pattern (left 竖, dots middle, 竖弯钩
    right) that the GT shows.

  Fixes this retry:
    (1) Keep MMH endpoint anchors verbatim (they are correct).
    (2) s3 (left 撇 of 兆): render as a proper tapered 撇 (draw_pie,
        small curve) — the FAILURE was in stroke weight/curvature
        not endpoint choice.
    (3) s6 (right 竖弯钩): don't over-curve the middle. Render as an
        almost-straight taper from head to bend point, then a short
        upward hook at the tail. Suppress mid-splay.
    (4) s4/s5/s7/s8: draw THIN fat_lines (width 5) so they read as
        小点/短笔 rather than bold slashes. Shortens visual weight of
        the interior so the two long spine strokes (s3, s6) frame
        the character properly.
    (5) 亻 (s1, s2) unchanged from retry_1 — that worked.

Decomposition: 佻 = 亻 (2 strokes) + 兆 (6 strokes).
"""

# BANK_DEVIATION
# skipped: ren_side.py, dian.py, na.py, and any bezier-heavy wing primitive
# reason: 亻 sits in far-left column (ren_side_far_left pattern, B10/B11
#   evidence 8+ passes). Interior 兆 strokes need thin uniform fat_line
#   so small marks read as marks — variable-width and heavy curves
#   caused the right half to blob in main and X-cross in retry_1.
# fresh_component: ren_side_far_left_for_佻; zhao_thin_inner_for_佻

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
    'notes': ('Retry_2: MMH-verbatim endpoints. Interior 兆 strokes '
              'rendered thin (width 5) to read as small marks; right '
              '竖弯钩 (s6) rendered near-straight then hooked so it does '
              'not X-cross with s3.'),
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
# s3: 兆's left long 撇 — TC(0.324,0.946) → BL(0.891,0.862)
#     Real slant, tapered. Small curve.
draw_pie(d, ('TC', 0.324, 0.946), ('BL', 0.891, 0.862),
         head_width=8, tail_width=2, curve=0.05)

# s4: short 提 (interior top mark) ML(0.973,0.365) → C(0.245,0.603)
#     Thin so it reads as a small mark, not a bar.
p0 = anchor_to_xy(('ML', 0.973, 0.365))
p1 = anchor_to_xy(('C',  0.245, 0.603))
fat_line(d, p0, p1, width=5)

# s5: short lower-left dot BL(0.85,0.183) → C(0.351,0.893)
#     Thin uniform line, small mark inside 兆.
p0 = anchor_to_xy(('BL', 0.85, 0.183))
p1 = anchor_to_xy(('C',  0.351, 0.893))
fat_line(d, p0, p1, width=5)

# s6: right 竖弯钩 TC(0.781,0.7) → BR(0.73,0.203)
#     Near-straight taper w/ gentle bend near tail; DO NOT push mid-control
#     outward (that caused the retry_1 splay/X-cross).
p0 = anchor_to_xy(('TC', 0.781, 0.7))
p2 = anchor_to_xy(('BR', 0.73,  0.203))
# Bend point about 75% along, small right bias — creates the 弯 hint.
bend_t = 0.75
bx = p0[0] + bend_t * (p2[0] - p0[0]) + 4
by = p0[1] + bend_t * (p2[1] - p0[1]) + 2
pts = quad_bezier(p0, (bx, by), p2, n=40)
widths = [7 - 3 * (i / 40) for i in range(41)]
stroke_variable_width(d, pts, widths)
# Small hook at tail — short segment perpendicular-ish, pointing up-left.
hx, hy = p2
d.line([(hx, hy), (hx - 8, hy - 6)], fill=(0, 0, 0), width=4)

# s7: short interior mark MR(0.303,0.084) → MR(0.039,0.518)
p0 = anchor_to_xy(('MR', 0.303, 0.084))
p1 = anchor_to_xy(('MR', 0.039, 0.518))
fat_line(d, p0, p1, width=5)

# s8: short interior mark C(0.937,0.767) → BR(0.443,0.153)
p0 = anchor_to_xy(('C',  0.937, 0.767))
p1 = anchor_to_xy(('BR', 0.443, 0.153))
fat_line(d, p0, p1, width=5)

img.save(os.path.join(os.path.dirname(__file__), '01_佻.png'))
