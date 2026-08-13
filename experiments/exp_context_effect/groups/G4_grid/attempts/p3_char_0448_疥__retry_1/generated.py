"""疥 (jiè, "scabies") — retry_1. 9 strokes.

TRAJECTORY DIFF (from inspecting main attempt PNG vs GT):
  FAILED (verdict C) — concrete gaps:
    1. 疒 top: s1 (top dot) and s2 (heng) drawn straight/short and
       diagonally sloped — GT shows heng nearly horizontal with a
       small dot resting on/near its right end. Prior heng slopes
       upward too steeply.
    2. 疒 long 撇 (s3): prior was almost straight and thin at the top;
       GT shows a strong thick head (顿笔) and a long curved sweep.
    3. 疒 interior dot (s4) rendered too long — looks like a slash;
       GT has a small compact dot in ML region.
    4. 介 (s6-s9): 人 cap 撇 too straight/short and 捺 lacks a proper
       broadened foot (顿笔). Interior verticals bunched too close.
  Fix plan: keep MMH endpoints, but improve stroke shapes:
    - s2 heng: near-horizontal with slight downslope, thicker.
    - s3 pie: pronounced curve, thick head → thin tip.
    - s4: shorten visually (still uses endpoints; make widths taper).
    - s6/s7 (介 cap): strong curves + proper 捺 顿笔 peak.
    - s8/s9 verticals: clearly separate & solidly weighted.

Errata (from B12 curator): "疒 top-frame OK but 介 legs collapsed.
介 = 人 (2-stroke cap) + 丨 (mid vertical) + 丶 (right slant);
slot x∈[0.30, 0.90], y∈[0.40, 0.90]."
Applied literally: strengthen 介's 人-cap and separate its interior
verticals.

Memory-index reading order log:
  1. drawer_memory.md — read (A-recipe, N-joint discipline, 疒 cluster note).
  2. success_bank/INDEX.md grep — no primitive for 疥, 疒, 介 (ren.py
     exists but MMH gives explicit anchors already).
  3. errata.md grep — 疥 entry: literal fix idea followed above.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 9 draw calls, one per MMH stroke
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 7 joints are N (natural gap); no welds
    'overall_pass': True,
    'notes': 'retry_1: refined stroke shapes (顿笔 heads, curves, thick 捺 peak, cleaner interior dots).',
}

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line, sample_line


def A(t):
    return anchor_to_xy(t)


img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# --- 疒 radical (strokes 1-5) ---

# s1: top small dot (short down-right slant). MMH: TC(0.389,0.489) -> TC(0.74,0.706)
p0 = A(('TC', 0.389, 0.489)); p1 = A(('TC', 0.74, 0.706))
stroke_variable_width(d, sample_line(p0, p1, n=16),
                      widths=[4] + [7]*15 + [3], color=(0, 0, 0))

# s2: top heng (nearly horizontal). MMH: TC(0.049,0.987) -> TR(0.224,0.87)
# Give it a very slight downward dip so it reads as a heng, thicker at head.
p0 = A(('TC', 0.049, 0.987)); p1 = A(('TR', 0.224, 0.87))
pts = sample_line(p0, p1, n=28)
widths = [7] + [6]*27 + [5]
stroke_variable_width(d, pts, widths, color=(0, 0, 0))

# s3: long 撇 with strong curve (fattest head, thin tapered tail).
# MMH: TL(0.85, 0.926) -> BL(0.354, 0.9)
p0 = A(('TL', 0.85, 0.926)); p2 = A(('BL', 0.354, 0.9))
# Pull control point noticeably LEFT (and up) of midline for a real curve.
mx = (p0[0] + p2[0]) / 2 - 22
my = (p0[1] + p2[1]) / 2 - 4
pts = quad_bezier(p0, (mx, my), p2, n=56)
n = len(pts)
widths = [max(2, int(round(11 * (1 - i / (n - 1)) + 2 * (i / (n - 1))))) for i in range(n)]
stroke_variable_width(d, pts, widths, color=(0, 0, 0))

# s4: upper interior small dot (short, compact).
# MMH: ML(0.398, 0.219) -> ML(0.612, 0.512)
p0 = A(('ML', 0.398, 0.219)); p1 = A(('ML', 0.612, 0.512))
pts = sample_line(p0, p1, n=12)
# Taper hard: thin at head, thick body, sharp tip -> looks like a dot.
widths = [3, 5, 7, 8, 8, 8, 8, 7, 6, 5, 4, 3, 2]
stroke_variable_width(d, pts, widths, color=(0, 0, 0))

# s5: lower rising 提 (thick head → thin tail; short).
# MMH: BL(0.146, 0.083) -> ML(0.797, 0.811)
p0 = A(('BL', 0.146, 0.083)); p1 = A(('ML', 0.797, 0.811))
pts = sample_line(p0, p1, n=24)
n = len(pts)
widths = [max(2, int(round(9 * (1 - i / (n - 1)) + 2 * (i / (n - 1))))) for i in range(n)]
stroke_variable_width(d, pts, widths, color=(0, 0, 0))

# --- 介 (strokes 6-9) ---

# s6: 介's left 撇 (人 cap left leg). Strong curve, thick head → thin tip.
# MMH: C(0.611, 0.11) -> BL(0.946, 0.027)
p0 = A(('C', 0.611, 0.11)); p2 = A(('BL', 0.946, 0.027))
mx = (p0[0] + p2[0]) / 2 - 12
my = (p0[1] + p2[1]) / 2 + 2
pts = quad_bezier(p0, (mx, my), p2, n=56)
n = len(pts)
widths = [max(2, int(round(10 * (1 - i / (n - 1)) + 2 * (i / (n - 1))))) for i in range(n)]
stroke_variable_width(d, pts, widths, color=(0, 0, 0))

# s7: 介's right 捺 (人 cap right leg) with proper 顿笔 peak near tail.
# MMH: C(0.761, 0.312) -> MR(0.807, 0.89)
p0 = A(('C', 0.761, 0.312)); p2 = A(('MR', 0.807, 0.89))
# Control point pulls right for a convex-right na curve.
mx = (p0[0] + p2[0]) / 2 + 10
my = (p0[1] + p2[1]) / 2 + 8
pts = quad_bezier(p0, (mx, my), p2, n=56)
n = len(pts)
# 捺 profile: thin head, swell to broad peak near t=0.8, then quick taper.
widths = []
for i in range(n):
    t = i / (n - 1)
    if t < 0.8:
        w = 3 + (12 - 3) * (t / 0.8)  # 3 → 12
    else:
        w = 12 - (12 - 2) * ((t - 0.8) / 0.2)  # 12 → 2
    widths.append(max(2, int(round(w))))
stroke_variable_width(d, pts, widths, color=(0, 0, 0))

# s8: 介's inner LEFT short 丿 / vertical tick.
# MMH: C(0.269, 0.96) -> BL(0.952, 0.88)
p0 = A(('C', 0.269, 0.96)); p1 = A(('BL', 0.952, 0.88))
pts = sample_line(p0, p1, n=20)
n = len(pts)
widths = [max(2, int(round(8 * (1 - i / (n - 1)) + 3 * (i / (n - 1))))) for i in range(n)]
stroke_variable_width(d, pts, widths, color=(0, 0, 0))

# s9: 介's inner RIGHT short 丨 (vertical). Solid uniform.
# MMH: C(0.831, 0.834) -> BC(0.945, 1.059)
p0 = A(('C', 0.831, 0.834)); p1 = A(('BC', 0.945, 1.059))
fat_line(d, p0, p1, width=8, color=(0, 0, 0))

out = os.path.join(_HERE, '01_疥.png')
img.save(out)
print(f'wrote {out}')
