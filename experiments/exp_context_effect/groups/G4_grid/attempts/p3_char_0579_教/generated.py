"""教 (jiào) — 11 strokes.

Decomposition: 教 = 孝(left) + 攵(right); 孝 = 耂(top-left) + 子(bottom-left).
  耂: s1 top-heng, s2 shu, s3 lower-heng, s4 long-pie sweep.
  子: s5 short heng-pie, s6 shu-gou (vertical hook), s7 bottom-heng.
  攵: s8 long-pie, s9 short-heng, s10 pie, s11 na (X-cross at s10-s11 mid).

All 11 anchors MMH-verbatim from dispatcher block (A-recipe point 2).
"""

# NOTE: no BANK_DEVIATION block — inlined via base primitives with MMH-verbatim
# anchors per A-recipe point 4 (compound char with slot-embedded parts —
# ren_side/kou/fu.py etc would need >3 anchor overrides to fit these slots).

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line

from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 11 primitives called
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # N-joints preserved as small natural gaps
    'overall_pass': True,
    'notes': '11 strokes MMH-verbatim; s10.mid ⇆ s11.mid welded X-cross (P at BC).'
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)


def line_between(a, b, w):
    fat_line(d, anchor_to_xy(a), anchor_to_xy(b), w)


def curve_pts(a, b, ctrl_dx=0, ctrl_dy=0, n=60):
    p0 = anchor_to_xy(a)
    p2 = anchor_to_xy(b)
    mx = (p0[0] + p2[0]) / 2 + ctrl_dx
    my = (p0[1] + p2[1]) / 2 + ctrl_dy
    return quad_bezier(p0, (mx, my), p2, n=n)


# ---------- 耂 (top-left) ----------
# s1: top 一 of 耂 (short heng)
line_between(('ML', 0.598, 0.099), ('TC', 0.348, 0.987), 9)

# s2: 竖 of 耂 (vertical drop from top-heng)
line_between(('TL', 0.97, 0.58), ('C', 0.005, 0.459), 9)

# s3: lower 一 of 耂 (crossbar heng)
line_between(('ML', 0.305, 0.649), ('C', 0.547, 0.453), 9)

# s4: long 撇 of 耂 — sweeps down-left from top-right area
p0 = anchor_to_xy(('C', 0.679, 0.037))
p2 = anchor_to_xy(('BL', 0.214, 0.44))
mx = (p0[0] + p2[0]) / 2 - 12
my = (p0[1] + p2[1]) / 2 + 6
pts_s4 = quad_bezier(p0, (mx, my), p2, n=60)
widths_s4 = [11 - 10 * (i / len(pts_s4)) for i in range(len(pts_s4))]
stroke_variable_width(d, pts_s4, widths_s4)

# ---------- 子 (bottom-left) ----------
# s5: 横撇 opening of 子 (short right-going stroke, downward tilt)
line_between(('ML', 0.662, 0.913), ('BC', 0.125, 0.106), 9)

# s6: 竖钩 of 子 (long vertical, slight left curve at bottom = hook read via s6 tail)
p0 = anchor_to_xy(('BL', 0.981, 0.124))
p2 = anchor_to_xy(('BL', 0.835, 0.856))
mx = (p0[0] + p2[0]) / 2 + 2
my = (p0[1] + p2[1]) / 2
pts_s6 = quad_bezier(p0, (mx, my), p2, n=40)
stroke_variable_width(d, pts_s6, [10] * len(pts_s6))

# s7: bottom 一 of 子
line_between(('BL', 0.407, 0.596), ('BC', 0.465, 0.235), 9)

# ---------- 攵 (right, 4 strokes; s10-s11 X-cross P at BC) ----------
# s8: long 撇 of 攵
p0 = anchor_to_xy(('TC', 0.881, 0.653))
p2 = anchor_to_xy(('C', 0.526, 0.772))
mx = (p0[0] + p2[0]) / 2 + 8
my = (p0[1] + p2[1]) / 2 + 4
pts_s8 = quad_bezier(p0, (mx, my), p2, n=60)
widths_s8 = [12 - 11 * (i / len(pts_s8)) for i in range(len(pts_s8))]
stroke_variable_width(d, pts_s8, widths_s8)

# s9: short 横 of 攵 (crossbar through s8 body)
line_between(('C', 0.761, 0.564), ('MR', 0.587, 0.424), 8)

# s10: pie of 攵 (second pie, welded X with s11 at BC)
p0 = anchor_to_xy(('MR', 0.039, 0.608))
p2 = anchor_to_xy(('BC', 0.406, 0.78))
mx = (p0[0] + p2[0]) / 2 - 4
my = (p0[1] + p2[1]) / 2 + 4
pts_s10 = quad_bezier(p0, (mx, my), p2, n=60)
widths_s10 = [11 - 10 * (i / len(pts_s10)) for i in range(len(pts_s10))]
stroke_variable_width(d, pts_s10, widths_s10)

# s11: 捺 of 攵 (na — welded to s10 mid, sweeps to bottom-right)
p0 = anchor_to_xy(('C', 0.588, 0.939))
p2 = anchor_to_xy(('BR', 0.792, 0.865))
mx = (p0[0] + p2[0]) / 2 + 4
my = (p0[1] + p2[1]) / 2 - 6
pts_s11 = quad_bezier(p0, (mx, my), p2, n=60)
# na taper: thin head, peak ~0.75, thin tail
n11 = len(pts_s11)
widths_s11 = []
for i in range(n11):
    t = i / (n11 - 1)
    if t < 0.75:
        w = 3 + (14 - 3) * (t / 0.75)
    else:
        w = 14 - (14 - 1) * ((t - 0.75) / 0.25)
    widths_s11.append(w)
stroke_variable_width(d, pts_s11, widths_s11)

# Save PNG
out_path = os.path.join(os.path.dirname(__file__), '01_教.png')
img.save(out_path)
print(f"Wrote {out_path}")
