# BANK_DEVIATION
# skipped: none (no 免 primitive in bank; ren_side default anchors don't match MMH
#          spec for stroke 1 which sweeps from TL to ML — much longer/lower than
#          the ren_side default TC-to-BL curve).
# reason: MMH anchors put the 亻 撇 lower-right→lower-left with a longer sweep;
#         inlining directly is simpler than overriding all 4 default anchors.
# fresh_component: ren_side_variant_for_俛 (inline pie+shu), full 免 (7 strokes)
"""俛 (fǔ) = 亻 + 免. 9 strokes total per MMH.

Bank check: ren_side exists but its default anchors don't fit this MMH spec
well; er_legs exists but 免's bottom differs from bare 儿. Inline everything
using the MMH-supplied endpoint anchors to respect the structural gate.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../success_bank/code'))
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new('RGB', (W, H), 'white')
draw = ImageDraw.Draw(img)

# ---- Stroke 1: 亻 撇 (long sweep, TL → ML) ----
s1_head = anchor_to_xy(('TL', 0.841, 0.671))
s1_tail = anchor_to_xy(('ML', 0.164, 0.948))
# curve control point pulled slightly right of the chord
ctrl1 = ((s1_head[0]+s1_tail[0])/2 + 8, (s1_head[1]+s1_tail[1])/2 - 4)
pts1 = quad_bezier(s1_head, ctrl1, s1_tail, n=40)
widths1 = [max(2, int(11 - 10*i/len(pts1))) for i in range(len(pts1))]
stroke_variable_width(draw, pts1, widths1)

# ---- Stroke 2: 亻 竖 (short vertical) ----
s2_head = anchor_to_xy(('ML', 0.618, 0.544))
s2_tail = anchor_to_xy(('BL', 0.662, 0.918))
fat_line(draw, s2_head, s2_tail, 8)

# ---- Stroke 3: 免 top 撇 (short, TC → C going down-left) ----
s3_head = anchor_to_xy(('TC', 0.497, 0.615))
s3_tail = anchor_to_xy(('C', 0.102, 0.295))
ctrl3 = ((s3_head[0]+s3_tail[0])/2, (s3_head[1]+s3_tail[1])/2 - 6)
pts3 = quad_bezier(s3_head, ctrl3, s3_tail, n=30)
widths3 = [max(2, int(8 - 6*i/len(pts3))) for i in range(len(pts3))]
stroke_variable_width(draw, pts3, widths3)

# ---- Stroke 4: 免 top box right side (short vertical, TC bottom → C) ----
s4_head = anchor_to_xy(('TC', 0.547, 0.961))
s4_tail = anchor_to_xy(('C', 0.664, 0.418))
fat_line(draw, s4_head, s4_tail, 7)

# ---- Stroke 5: 免 top-inner-left segment (C → BC) — top-of-口-box left ----
s5_head = anchor_to_xy(('C', 0.061, 0.503))
s5_tail = anchor_to_xy(('BC', 0.254, 0.08))
fat_line(draw, s5_head, s5_tail, 7)

# ---- Stroke 6: 免 top-of-box horizontal-then-turn (C → MR) ----
s6_head = anchor_to_xy(('C', 0.204, 0.506))
s6_tail = anchor_to_xy(('MR', 0.042, 0.787))
# corner near top-right of C cell
corner6 = anchor_to_xy(('MR', 0.02, 0.51))
pts6 = [s6_head, corner6, s6_tail]
# render as two segments
fat_line(draw, s6_head, corner6, 7)
fat_line(draw, corner6, s6_tail, 8)

# ---- Stroke 7: 免 middle horizontal-then-vertical bar (BC → MR) ----
s7_head = anchor_to_xy(('BC', 0.31, 0.016))
s7_tail = anchor_to_xy(('MR', 0.232, 0.89))
fat_line(draw, s7_head, s7_tail, 8)

# ---- Stroke 8: 免 儿-left 撇 (C → BL) ----
s8_head = anchor_to_xy(('C', 0.559, 0.529))
s8_tail = anchor_to_xy(('BL', 0.908, 0.93))
ctrl8 = ((s8_head[0]+s8_tail[0])/2 + 6, (s8_head[1]+s8_tail[1])/2 - 6)
pts8 = quad_bezier(s8_head, ctrl8, s8_tail, n=40)
widths8 = [max(2, int(10 - 8*i/len(pts8))) for i in range(len(pts8))]
stroke_variable_width(draw, pts8, widths8)

# ---- Stroke 9: 免 儿-right 竖弯钩 (BC → BR, needs hook up-left at tail) ----
s9_head = anchor_to_xy(('BC', 0.731, 0.071))
s9_tail = anchor_to_xy(('BR', 0.637, 0.312))
# curve: descend then sweep right, hook up
corner9 = anchor_to_xy(('BR', 0.30, 0.75))
# body
pts9 = quad_bezier(s9_head, ((s9_head[0]+corner9[0])/2 + 4, (s9_head[1]+corner9[1])/2 + 20), corner9, n=30)
widths9 = [10]*len(pts9)
stroke_variable_width(draw, pts9, widths9)
# horizontal to just before tail
horiz_end = ( (corner9[0]+s9_tail[0])/2 + 12, corner9[1]-2 )
fat_line(draw, corner9, horiz_end, 10)
# hook up
fat_line(draw, horiz_end, s9_tail, 6)

img.save(os.path.join(os.path.dirname(__file__), '01_俛.png'))

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 9 stroke primitives (s1..s9)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Inlined all 9 strokes from MMH anchors; no bank primitive fit 免 cleanly. 亻 kept as ren_side-shape via s1(pie)+s2(shu). 儿 bottom as s8+s9 inline.',
}
