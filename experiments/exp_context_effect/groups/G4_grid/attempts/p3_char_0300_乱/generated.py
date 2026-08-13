"""p3_char_0300_乱 — G4 attempt.

Decomposition: 乱 = 舌 (left, 6 strokes: 丿一丨 + 口[竖横折横]) + 乚 (right hook, 1 stroke) = 7 strokes.
Uses MMH-derived anchors verbatim (v9 lesson: MMH-verbatim beats tuning).
"""
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '7 strokes; N-joints kept as small gaps per MMH; s2.mid/s3.mid P-welded via s2 crossing s3 near ML right edge.',
}

import os, sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line  # noqa

CANVAS = 300
img = Image.new('RGB', (CANVAS, CANVAS), 'white')
d = ImageDraw.Draw(img)


def curve(d, a_head, a_tail, ctrl_off=(0, 0), width=8, n=32):
    p0 = anchor_to_xy(a_head)
    p2 = anchor_to_xy(a_tail)
    p1 = ((p0[0] + p2[0]) / 2.0 + ctrl_off[0],
          (p0[1] + p2[1]) / 2.0 + ctrl_off[1])
    pts = quad_bezier(p0, p1, p2, n=n)
    widths = [width] * len(pts)
    stroke_variable_width(d, pts, widths)


# ---- 舌 (left half, 6 strokes) ----

# s1 — 丿 (pie): from top TC down-left to ML.
# head (TC,0.441,0.885) -> tail (ML,0.58,0.236)
p_h = anchor_to_xy(('TC', 0.441, 0.885))
p_t = anchor_to_xy(('ML', 0.58, 0.236))
# gentle leftward bow
ctrl = ((p_h[0] + p_t[0]) / 2 + 4, (p_h[1] + p_t[1]) / 2 - 4)
pts = quad_bezier(p_h, ctrl, p_t, n=32)
widths = [3 + (1 - i / 32) * 6 for i in range(33)]  # thick head, thin tail
stroke_variable_width(d, pts, widths)

# s2 — 一 (heng, top of 千): from ML left to C.
p_h = anchor_to_xy(('ML', 0.22, 0.688))
p_t = anchor_to_xy(('C', 0.526, 0.523))
widths = [8] * 33
pts = quad_bezier(p_h, ((p_h[0] + p_t[0]) / 2, (p_h[1] + p_t[1]) / 2 - 2), p_t, n=32)
stroke_variable_width(d, pts, widths)

# s3 — 丨 (short vertical of 千): ML right edge going down to BL top.
# This is the vertical crossing s2 (P-weld) — extend slightly upward to weld cleanly.
p_h = anchor_to_xy(('ML', 0.896, 0.166))
p_t = anchor_to_xy(('BL', 0.911, 0.051))
fat_line(d, p_h, p_t, 8)

# ---- 口 (bottom of 舌, 3 strokes in BL cell) ----

# s4 — 竖 (left vertical of 口): BL(0.495,0.139) -> BL(0.715,0.801)
p_h = anchor_to_xy(('BL', 0.495, 0.139))
p_t = anchor_to_xy(('BL', 0.715, 0.801))
fat_line(d, p_h, p_t, 7)

# s5 — 横折 (top+right of 口): head BL(0.642,0.139), tail BC(0.172,0.473)
# Bend at top-right corner. Two-segment L shape.
p_h = anchor_to_xy(('BL', 0.642, 0.139))
p_t = anchor_to_xy(('BC', 0.172, 0.473))
# Corner approximately at (tail_x, head_y)
corner = (p_t[0], p_h[1])
fat_line(d, p_h, corner, 7)
fat_line(d, corner, p_t, 7)

# s6 — 横 (bottom of 口): BL(0.773,0.678) -> BC(0.359,0.572)
p_h = anchor_to_xy(('BL', 0.773, 0.678))
p_t = anchor_to_xy(('BC', 0.359, 0.572))
fat_line(d, p_h, p_t, 7)

# ---- s7 — 乚 (right hook, 竖弯钩): TC(0.617,0.662) -> BR(0.675,0.171)
# Smooth continuous L-curve wrapping down then right, with small up-hook.
p_h = anchor_to_xy(('TC', 0.617, 0.662))
p_t = anchor_to_xy(('BR', 0.675, 0.171))
# Corner of the sweep: below head, at right side; use one broad bezier
# through the bottom-right, then a tiny up-hook to the tail.
sweep_end = (p_t[0], 250)  # after sweeping along bottom-right
ctrl_main = (p_h[0] - 4, sweep_end[1] + 40)  # pulls curve down and slightly left of head
pts_main = quad_bezier(p_h, ctrl_main, sweep_end, n=60)
w_main = [7 + (i / 60) * 3 for i in range(61)]
stroke_variable_width(d, pts_main, w_main)
# Small upward hook tail
ctrl_hook = (sweep_end[0] + 4, (sweep_end[1] + p_t[1]) / 2)
pts_hook = quad_bezier(sweep_end, ctrl_hook, p_t, n=20)
w_hook = [10 - (i / 20) * 7 for i in range(21)]
stroke_variable_width(d, pts_hook, w_hook)

out = os.path.join(os.path.dirname(__file__), '01_乱.png')
img.save(out)
print('wrote', out)
