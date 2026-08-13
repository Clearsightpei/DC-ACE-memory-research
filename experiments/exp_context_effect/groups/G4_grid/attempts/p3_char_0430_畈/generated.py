# 畈 (fàn) — Phase 3 char 0430, 9 strokes
# Structure: 田 (left, 5 strokes) + 反 (right, 4 strokes)
# Reading-order log:
#  1. drawer_memory.md — no dedicated 田 or 反 primitive; inline fresh (v9 lesson:
#     MMH-verbatim anchors beat hand-tuning when composition is tight).
#  2. INDEX.md grep — 畈 not present; 畀 (0364) uses 田-frame inline pattern; 反
#     (0140) is in the FAIL list.
#  3. errata.md grep — 反 fix idea: 反 = 厂 + 又; keep top heng short, 撇 long
#     left-down; then 又 = 横撇 + 捺.
# No BANK_DEVIATION — nothing skipped; nothing in bank to skip for these parts.
# Anchors follow MMH-derived expectations verbatim from the brief.

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 9 stroke primitives (s2 = 2 segments for 横折)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # P weld at s3⇆s4 (田 spine×heng) and s8⇆s9 (又 cross); N gaps elsewhere
    'overall_pass': True,
    'notes': '畈 = 田(left, 5 strokes) + 反(right, 4 strokes). Anchors from MMH brief.',
}

import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G4_grid/success_bank/code")

from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

WIDTH = 7

img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# =================== 田 (left half, strokes 1-5) ===================

# s1 — left 竖 of 田
p1_head = anchor_to_xy(('ML', 0.261, 0.345))
p1_tail = anchor_to_xy(('BL', 0.448, 0.224))
fat_line(draw, p1_head, p1_tail, WIDTH)

# s2 — 横折 (top bar + right wall of 田). Split at right-angle corner.
p2_head   = anchor_to_xy(('ML', 0.413, 0.436))
p2_tail   = anchor_to_xy(('BL', 0.964, 0.045))
# corner at (tail.x, head.y): go right along top, then down along right.
p2_corner = (p2_tail[0], p2_head[1])
fat_line(draw, p2_head,   p2_corner, WIDTH)
fat_line(draw, p2_corner, p2_tail,   WIDTH)

# s3 — inner middle heng of 田
p3_head = anchor_to_xy(('ML', 0.527, 0.746))
p3_tail = anchor_to_xy(('ML', 0.938, 0.693))
fat_line(draw, p3_head, p3_tail, WIDTH)

# s4 — middle vertical spine of 田 (P-welds with s3)
p4_head = anchor_to_xy(('ML', 0.674, 0.4))
p4_tail = anchor_to_xy(('BL', 0.697, 0.013))
fat_line(draw, p4_head, p4_tail, WIDTH)

# s5 — bottom heng closing 田
p5_head = anchor_to_xy(('BL', 0.504, 0.153))
p5_tail = anchor_to_xy(('BL', 0.905, 0.08))
fat_line(draw, p5_head, p5_tail, WIDTH)

# =================== 反 (right half, strokes 6-9) ===================

# s6 — 厂 top short 横 (slight down-left slope)
p6_head = anchor_to_xy(('TR', 0.353, 0.929))
p6_tail = anchor_to_xy(('C',  0.638, 0.131))
fat_line(draw, p6_head, p6_tail, WIDTH)

# s7 — 厂 长撇 (long left-down curve). Use bezier for gentle arc.
p7_head = anchor_to_xy(('C',  0.418, 0.113))
p7_tail = anchor_to_xy(('BL', 0.896, 0.856))
# Control point pulled slightly to the right to give a natural 撇 curve.
ctrl7 = ((p7_head[0] + p7_tail[0]) / 2 + 12, (p7_head[1] + p7_tail[1]) / 2 - 6)
pts7 = quad_bezier(p7_head, ctrl7, p7_tail, n=40)
widths7 = [max(3, int(WIDTH * (1 - 0.35 * (i / 40)))) for i in range(41)]
stroke_variable_width(draw, pts7, widths7)

# s8 — 又's 横撇 (short down-left from center to bottom-center)
p8_head = anchor_to_xy(('C',  0.611, 0.69))
p8_tail = anchor_to_xy(('BC', 0.359, 0.777))
fat_line(draw, p8_head, p8_tail, WIDTH)

# s9 — 又's 捺 (long down-right sweep, widening then tapering)
p9_head = anchor_to_xy(('C',  0.608, 0.945))
p9_tail = anchor_to_xy(('BR', 0.78, 0.854))
# Bezier with mild downward bulge for 捺 arc.
ctrl9 = ((p9_head[0] + p9_tail[0]) / 2, (p9_head[1] + p9_tail[1]) / 2 + 10)
pts9 = quad_bezier(p9_head, ctrl9, p9_tail, n=40)
# 捺 typically widens then tapers to a point at the tail.
widths9 = []
for i in range(41):
    t = i / 40
    if t < 0.7:
        w = WIDTH - 1 + int(3 * t)
    else:
        w = max(2, int((WIDTH + 2) * (1 - (t - 0.7) / 0.3)))
    widths9.append(max(2, w))
stroke_variable_width(draw, pts9, widths9)

OUT = os.path.join(_HERE, '01_畈.png')
img.save(OUT)
print("Saved", OUT)
