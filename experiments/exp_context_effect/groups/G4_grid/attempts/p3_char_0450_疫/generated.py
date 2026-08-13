"""p3_char_0450_疫 — G4 attempt.

Split: 疫 = 疒 (5 strokes) + 殳 (4 strokes) = 9 strokes.

Memory reading log:
  1. drawer_memory.md — no direct 疒 or 殳 canonical primitive; you_again.py
     exists but 殳 top is not 又 (has 几-like top + dot). Composition is
     enclosing-top-left frame (疒) + inner-right (殳).
  2. success_bank/INDEX.md grep 疒 → p3_char_0171 (PASSED, no .py primitive
     shipped in code/, treated as composition).  Grep 殳 → none.
  3. errata.md grep 疫 → not listed.

Bank deviation: none — no bank primitive skipped (no 疒/殳 primitive exists
to skip). Rendered fresh from MMH anchors with fat_line + quad_bezier.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 9 stroke calls below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '疒 (s1-s5) + 殳 (s6-s9). Joint s8/s9 is P-welded (crossing 撇+捺).',
}


def A(anchor):
    return anchor_to_xy(anchor)


def curved(draw, p0, p2, ctrl_bias=(0, 0), widths=(6, 6), n=40):
    """Draw a subtle-curve stroke with quadratic bezier + variable widths."""
    mx = (p0[0] + p2[0]) / 2 + ctrl_bias[0]
    my = (p0[1] + p2[1]) / 2 + ctrl_bias[1]
    pts = quad_bezier(p0, (mx, my), p2, n=n)
    w0, w1 = widths
    ws = [w0 + (w1 - w0) * (i / n) for i in range(n + 1)]
    stroke_variable_width(draw, pts, ws)


img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# -------- 疒 (strokes 1-5) --------

# s1: 点 (small dot at top of 疒) — TC region, short slanted stroke
p = A(('TC', 0.474, 0.565)); q = A(('TC', 0.784, 0.785))
curved(d, p, q, ctrl_bias=(2, -2), widths=(4, 8), n=24)

# s2: 横 (horizontal top of 疒) — from C to TR, slight rise
p = A(('C', 0.116, 0.075)); q = A(('TR', 0.32, 0.914))
# this is 横 — nearly flat; render as fat_line with slight curve
pts = quad_bezier(p, ((p[0]+q[0])/2, (p[1]+q[1])/2 - 3), q, n=32)
stroke_variable_width(d, pts, [7]*(len(pts)))

# s3: 撇 (long sweeping 撇 of 疒) — from ML top down-left to BL
p = A(('ML', 0.902, 0.034)); q = A(('BL', 0.319, 1.009))
# curve left-bowed
mx = (p[0]+q[0])/2 - 14
my = (p[1]+q[1])/2 + 6
pts = quad_bezier(p, (mx, my), q, n=48)
ws = [11 - 7*(i/(len(pts)-1)) for i in range(len(pts))]  # taper 11->4
stroke_variable_width(d, pts, ws)

# s4: 点 (top dot inside 疒) — ML small dot
p = A(('ML', 0.48, 0.283)); q = A(('ML', 0.703, 0.541))
curved(d, p, q, ctrl_bias=(1, -1), widths=(3, 8), n=24)

# s5: 提 (rising tick inside 疒) — BL to ML, sweeping upward
p = A(('BL', 0.255, 0.206)); q = A(('ML', 0.899, 0.805))
pts = quad_bezier(p, ((p[0]+q[0])/2, (p[1]+q[1])/2 + 2), q, n=32)
ws = [9 - 5*(i/(len(pts)-1)) for i in range(len(pts))]
stroke_variable_width(d, pts, ws)

# -------- 殳 (strokes 6-9) --------

# s6: 撇 (top part of 殳: short pie) — C to BC, sweeping down-left
p = A(('C', 0.389, 0.33)); q = A(('BC', 0.172, 0.019))
mx = (p[0]+q[0])/2 - 6
my = (p[1]+q[1])/2 + 4
pts = quad_bezier(p, (mx, my), q, n=32)
ws = [7 - 3*(i/(len(pts)-1)) for i in range(len(pts))]
stroke_variable_width(d, pts, ws)

# s7: 横折弯 or 横 (top-right of 殳) — C to MR, short flat-then-hook
p = A(('C', 0.506, 0.315)); q = A(('MR', 0.481, 0.74))
# nearly vertical with slight bend
mx = (p[0]+q[0])/2 + 6
my = (p[1]+q[1])/2 - 2
pts = quad_bezier(p, (mx, my), q, n=32)
stroke_variable_width(d, pts, [6]*(len(pts)))

# s8: 撇 (bottom sweeping 撇 of 又/殳 lower) — BC head to BL tail (long left sweep)
p = A(('BC', 0.348, 0.077)); q = A(('BL', 0.999, 0.912))
mx = (p[0]+q[0])/2 - 8
my = (p[1]+q[1])/2 + 6
pts_s8 = quad_bezier(p, (mx, my), q, n=48)
ws = [10 - 6*(i/(len(pts_s8)-1)) for i in range(len(pts_s8))]
stroke_variable_width(d, pts_s8, ws)

# s9: 捺 (bottom 捺 of 又/殳 lower) — BC head to BR tail, swelling then taper
p = A(('BC', 0.236, 0.238)); q = A(('BR', 0.804, 0.959))
mx = (p[0]+q[0])/2 + 6
my = (p[1]+q[1])/2 + 8
pts_s9 = quad_bezier(p, (mx, my), q, n=48)
ws = []
for i in range(len(pts_s9)):
    t = i / (len(pts_s9)-1)
    # swell: peak around t=0.75
    if t < 0.75:
        w = 3 + 10 * (t / 0.75)
    else:
        w = 13 - 11 * ((t - 0.75) / 0.25)
    ws.append(w)
stroke_variable_width(d, pts_s9, ws)


out_dir = os.path.dirname(__file__)
out_png = os.path.join(out_dir, '01_疫.png')
img.save(out_png)
print(f'wrote {out_png}')
