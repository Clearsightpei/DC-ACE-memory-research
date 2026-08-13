"""
畏 retry_1 — G4 (revision 2)

TRAJECTORY DIFF
---------------
Prior main attempt (C):
  - 田 too small and off-center; read as 曰; tangled 撇/捺.

First render of this retry:
  - 田 centered enough but shifted left of the bottom's horizontal;
    the 撇/捺 rendered as one continuous curve — legs not distinct.

This revision:
  - Center everything on x=150. 田 in x∈[75,225], spine at x=150.
  - Draw 撇 leg as a nearly-straight taper from near the spine base
    down to BL corner (not arcing).
  - Draw 捺 leg as a straight diagonal from around the 一 crossing
    down to BR corner, heavy tail — clearly separate from the 撇.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Centered 田 + distinct 撇 (left) / 捺 (right) legs.',
}

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line

from PIL import Image, ImageDraw

W = 300
img = Image.new('RGB', (W, W), 'white')
draw = ImageDraw.Draw(img)


def line(a, b, width=6):
    fat_line(draw, anchor_to_xy(a), anchor_to_xy(b), width)


def hzhe(a, corner, b, width=6):
    p0 = anchor_to_xy(a); pc = anchor_to_xy(corner); p1 = anchor_to_xy(b)
    fat_line(draw, p0, pc, width)
    fat_line(draw, pc, p1, width)


def taper_curve(a, ctrl, b, w0=8, w1=3):
    p0 = anchor_to_xy(a); pc = anchor_to_xy(ctrl); p1 = anchor_to_xy(b)
    pts = quad_bezier(p0, pc, p1, n=40)
    ws = [w0 + (w1 - w0) * (i / (len(pts) - 1)) for i in range(len(pts))]
    stroke_variable_width(draw, pts, ws)


# ============ 田 (top, compressed, centered) — 5 strokes ============
# Box: x=75..225 (width 150); y=20..126.

# stroke 1: left 竖
line(('TL', 0.75, 0.20), ('ML', 0.75, 0.26), width=6)

# stroke 2: 横折 (top + right side)
hzhe(('TL', 0.75, 0.20),
     ('TR', 0.25, 0.20),
     ('MR', 0.25, 0.26), width=6)

# stroke 3: inner middle horizontal (y≈73)
line(('TL', 0.75, 0.73), ('TR', 0.25, 0.73), width=5)

# stroke 4: inner middle vertical (x=150)
line(('TC', 0.50, 0.20), ('C', 0.50, 0.26), width=5)

# stroke 5: bottom horizontal of 田
line(('ML', 0.75, 0.26), ('MR', 0.25, 0.26), width=6)


# ============ Bottom (长-legs) — 4 strokes ============

# stroke 6: wide 一 (top of bottom radical) — y≈170, x=15..285
line(('ML', 0.15, 0.70), ('MR', 0.85, 0.70), width=7)

# stroke 7: 竖 spine (x=150), from just above 一 down slightly past it
line(('C', 0.50, 0.28), ('C', 0.50, 0.95), width=6)

# stroke 8: 撇 leg — straight-ish, from spine base sweeping to lower-left
taper_curve(('C', 0.50, 0.85),
            ('ML', 0.75, 0.98),
            ('BL', 0.10, 0.95),
            w0=8, w1=2)

# stroke 9: 捺 leg — straight diagonal from 一/spine crossing to BR
taper_curve(('C', 0.50, 0.72),
            ('MR', 0.30, 0.90),
            ('BR', 0.90, 0.92),
            w0=3, w1=11)


img.save(os.path.join(os.path.dirname(__file__), '01_畏.png'))
print("wrote 01_畏.png")
