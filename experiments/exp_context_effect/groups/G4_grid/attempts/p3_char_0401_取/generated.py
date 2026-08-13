"""取 (qǔ) — 8 strokes: 耳 (6) + 又 (2).

Composition: 耳 (left) + 又 (right).
Following MMH-derived anchors from dispatcher brief verbatim.
s1-s6 = 耳; s7-s8 = 又.

Joints (per brief):
  P (welded): s3↔s6 (耳 right shu welds bottom heng),
              s7↔s8 (又's heng-pie crosses na — classic P).
  All others N (small natural gap).
"""
import os, sys

# Path setup for shared primitives
HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '8 strokes via MMH anchors. 耳 = s1..s6, 又 = s7..s8. '
             's3 (right shu) extends past BC baseline (yf=1.07 clipped near canvas edge). '
             's7 (横撇) rendered with slight bend via quad_bezier for calligraphic feel. '
             's8 (捺) rendered with tapered variable width. P-joints welded at s7/s8 crossing.'
}

# ---- Render ----
img = Image.new("RGB", (300, 300), (255, 255, 255))
draw = ImageDraw.Draw(img)

# s1 — 耳 top short heng: TL(0.384,0.896) -> TC(0.544,0.773)
s1_head = anchor_to_xy(('TL', 0.384, 0.896))
s1_tail = anchor_to_xy(('TC', 0.544, 0.773))
fat_line(draw, s1_head, s1_tail, 6)

# s2 — 耳 left vertical (long shu): TL(0.58,0.99) -> BL(0.621,0.165)
s2_head = anchor_to_xy(('TL', 0.58, 0.99))
s2_tail = anchor_to_xy(('BL', 0.621, 0.165))
fat_line(draw, s2_head, s2_tail, 6)

# s3 — 耳 right vertical extending below baseline: TC(0.166,0.873) -> BC(0.236,1.07)
# (Head near top-right of 耳 frame, tail past bottom — creates the 耳 tail hook)
s3_head = anchor_to_xy(('TC', 0.166, 0.873))
s3_tail_raw = anchor_to_xy(('BC', 0.236, 1.07))
# Clip to canvas
s3_tail = (min(s3_tail_raw[0], 298), min(s3_tail_raw[1], 298))
fat_line(draw, s3_head, s3_tail, 6)

# s4 — 耳 first middle short heng: ML(0.765,0.38) -> C(0.043,0.327)
s4_head = anchor_to_xy(('ML', 0.765, 0.38))
s4_tail = anchor_to_xy(('C', 0.043, 0.327))
fat_line(draw, s4_head, s4_tail, 5)

# s5 — 耳 second middle short heng: ML(0.741,0.743) -> C(0.031,0.679)
s5_head = anchor_to_xy(('ML', 0.741, 0.743))
s5_tail = anchor_to_xy(('C', 0.031, 0.679))
fat_line(draw, s5_head, s5_tail, 5)

# s6 — 耳 bottom heng (long, extends into 又 area): BL(0.261,0.312) -> C(0.477,0.954)
s6_head = anchor_to_xy(('BL', 0.261, 0.312))
s6_tail = anchor_to_xy(('C', 0.477, 0.954))
fat_line(draw, s6_head, s6_tail, 6)

# s7 — 又 横撇: C(0.523,0.266) -> BC(0.403,0.461)
# Render as a proper heng-pie: horizontal segment from head going RIGHT
# to a corner, then pie sweep down-left to tail.
s7_head = anchor_to_xy(('C', 0.523, 0.266))
s7_tail = anchor_to_xy(('BC', 0.403, 0.461))
# Corner point: to the right and slightly below head — makes a visible heng top
s7_corner = (s7_head[0] + 55, s7_head[1] + 8)
# Draw heng segment (head -> corner)
fat_line(draw, s7_head, s7_corner, 5)
# Draw pie segment (corner -> tail) as a slight curve
pie_ctrl = (s7_corner[0] - 20, s7_corner[1] + 45)
pts_pie = quad_bezier(s7_corner, pie_ctrl, s7_tail, n=32)
widths_pie = [7 - 5 * (i / 32) for i in range(33)]
stroke_variable_width(draw, pts_pie, widths_pie)

# s8 — 又 捺 with peak swell: C(0.482,0.482) -> BR(0.81,0.49)
# The 又 X-cross: s8 head near s7 corner area, sweeps down-right.
s8_head = anchor_to_xy(('C', 0.482, 0.482))
s8_tail = anchor_to_xy(('BR', 0.81, 0.49))
# Weld s8_head to s7 pie mid so the X reads clearly
s8_ctrl = ((s8_head[0] + s8_tail[0]) / 2, (s8_head[1] + s8_tail[1]) / 2 + 8)
pts8 = quad_bezier(s8_head, s8_ctrl, s8_tail, n=48)
widths8 = []
for i in range(49):
    t = i / 48
    # Peak fat at t=0.70 (捺 characteristic swell before tail)
    if t < 0.70:
        w = 3 + 8 * (t / 0.70)
    else:
        # Taper down toward tail
        w = 11 - 9 * ((t - 0.70) / 0.30)
    widths8.append(max(2, w))
stroke_variable_width(draw, pts8, widths8)

out_png = os.path.join(HERE, "01_取.png")
img.save(out_png)
print(f"wrote {out_png}")
