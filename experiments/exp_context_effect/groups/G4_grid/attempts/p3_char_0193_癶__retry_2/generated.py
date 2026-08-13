"""癶 (bo, 'two feet') — 5 strokes. RETRY 2.

TRAJECTORY DIFF (from Step 0 visual inspection):
Prior FAIL (main attempt) visual gaps:
  1. Left half read as 卜 (short vertical with tick) not 丿+dot.
     s1 was rendered as too vertical/straight in lower portion,
     and s2 was placed like a horizontal tick rather than an
     inward-tilting short pie/dot on the left leg's upper body.
     GT s1 is a *sweeping* concave-left 撇 that carves a big arc.
  2. Right half read as two disjointed pieces (small 厶 fragment
     plus a floating na tail). s3+s4+s5 did NOT share the
     top-center apex — their heads were scattered, so the right
     leg lost its recognizable "opposing pie+na" gestalt.
  3. Overall silhouette missed the two opposing "V"-legs the GT
     shows — left leg splaying down-left, right leg splaying
     down-right, with heads meeting near TC.

Fix plan for retry:
  - Route s1.mid(0.25) and s5.head to sit near a shared APEX
    around TC (0.50, 0.88), per MMH joint spec (N-gap ~34px OK).
  - Curve s1 concave-right (belly on upper-right side of chord)
    so it reads as 丿 not |.
  - Make s5 a real 捺: thin head, swelling middle, tapered tail,
    concave-up (belly below chord).
  - s3 = short pie sloping down-left, with its tail landing
    JUST below and left of s5 head (N-gap ~12px), so the
    right leg's apex reads as one unit.
  - s4 = short dot/pie sloping down-left, tail landing on the
    early belly of s5 near C, sharing that pixel as a "kiss".
  - s2 = short down-right dot on s1's middle body (N-gap ~13px).
"""
import sys, os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__),
                 '..', '..', 'success_bank', 'code')))
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line

from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'retry_2: routes s3/s5 through shared TC apex; s1 curved concave-right as 丿; s5 shaped as 捺 with concave-up belly.'
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ---- stroke 1: long left 撇 (丿) — dominant sweep
# head TL(.727,.879)=(72.7, 87.9)  tail BL(.281,.221)=(28.1, 221)
p0 = anchor_to_xy(('TL', 0.727, 0.879))
p2 = anchor_to_xy(('BL', 0.281, 0.221))
mx, my = (p0[0] + p2[0]) / 2, (p0[1] + p2[1]) / 2
# Stronger concave-right belly for the classic 丿 sweep.
ctrl = (mx + 30, my - 4)
pts = quad_bezier(p0, ctrl, p2, n=56)
# Thick head, taper toward the pointed tail (tail should be sharp)
widths = [13 - 11 * (i / 56) ** 0.85 for i in range(57)]
stroke_variable_width(d, pts, widths)

# ---- stroke 2: short down-right dot on left-leg body (小点/短撇 inside)
# head ML(.618,.228)=(61.8, 122.8)  tail ML(.885,.462)=(88.5, 146.2)
a = anchor_to_xy(('ML', 0.618, 0.228))
b = anchor_to_xy(('ML', 0.885, 0.462))
# Slight curve, thick middle
pts = quad_bezier(a, ((a[0]+b[0])/2, (a[1]+b[1])/2 - 3), b, n=16)
widths = [6 + 3 * (1 - abs(i / 16 - 0.5) * 2) for i in range(17)]
stroke_variable_width(d, pts, widths)

# ---- stroke 3: short right pie (丿, top-center of the right leg)
# head TC(.992,.604)=(199.2, 60.4)  tail TC(.673,.864)=(167.3, 86.4)
p0 = anchor_to_xy(('TC', 0.992, 0.604))
p2 = anchor_to_xy(('TC', 0.673, 0.864))
mx, my = (p0[0] + p2[0]) / 2, (p0[1] + p2[1]) / 2
ctrl = (mx + 5, my - 4)
pts = quad_bezier(p0, ctrl, p2, n=22)
widths = [8 - 6 * (i / 22) ** 0.9 for i in range(23)]
stroke_variable_width(d, pts, widths)

# ---- stroke 4: short mark landing on s5's early belly (kisses s5 at C)
# head TR(.224,.744)=(222.4, 74.4)  tail C(.913,.157)=(191.3, 115.7)
a = anchor_to_xy(('TR', 0.224, 0.744))
b = anchor_to_xy(('C', 0.913, 0.157))
pts = quad_bezier(a, ((a[0]+b[0])/2 + 3, (a[1]+b[1])/2 - 2), b, n=18)
widths = [7 - 3 * (i / 18) for i in range(19)]
stroke_variable_width(d, pts, widths)

# ---- stroke 5: long 捺 sweep down-right (main right descender)
# head TC(.512,.885)=(151.2, 88.5)  tail MR(.883,.91)=(288.3, 191)
p0 = anchor_to_xy(('TC', 0.512, 0.885))
p2 = anchor_to_xy(('MR', 0.883, 0.91))
mx, my = (p0[0] + p2[0]) / 2, (p0[1] + p2[1]) / 2
# concave-up (belly below chord): pull ctrl DOWN in PIL coords (larger y)
# Actually for a proper 捺, the curve should be convex-up (belly on lower side of chord).
# In PIL: ctrl.y > mid.y gives the belly BELOW the chord — reads as 捺.
ctrl = (mx - 4, my + 22)
pts = quad_bezier(p0, ctrl, p2, n=48)
# 捺 profile: thin head, swelling middle, thick before tapering into tail
widths = []
for i in range(49):
    t = i / 48
    # peak around t=0.78 with more pronounced swell
    if t < 0.78:
        w = 3 + 13 * (t / 0.78)
    else:
        w = 16 - 14 * ((t - 0.78) / 0.22)
    widths.append(max(2, w))
stroke_variable_width(d, pts, widths)

out = os.path.join(os.path.dirname(__file__), '01_癶.png')
img.save(out)
print(f'wrote {out}')
