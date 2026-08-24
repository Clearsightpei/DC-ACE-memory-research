"""
乡 — 3 strokes, top-down:
  1. 撇折 (top): short 撇 down-left, shoulder dab, short 横 rightward
  2. 撇折 (middle): same shape, positioned lower
  3. 撇 (bottom): long throw-away 撇 sweeping from upper-right to lower-left,
     starting at the joint of the middle 撇折 and going all the way down.

Structure hint (from GT): the two 撇折 loops stack on the left/upper half;
the bottom stroke is a LONG 撇 that begins near the middle 撇折's shoulder
and sweeps down-left, giving 乡 its characteristic diagonal descent.

Memory refs:
- drawer_memory "撇折 family": 折-shoulder + short 横 with slight up-tilt.
- errata p2_radical_巛: two 撇折 loops stacked → distinguishing hint.
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def brush_dab(cx, cy, r):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill="black")

def bezier(p0, p1, p2, widths, steps=60):
    # quadratic bezier with variable width (widths = (w_start, w_end))
    w0, w1 = widths
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        w = w0 + (w1 - w0) * t
        brush_dab(x, y, w / 2)

def line_taper(p0, p1, w0, w1, steps=40):
    for i in range(steps + 1):
        t = i / steps
        x = p0[0] + (p1[0] - p0[0]) * t
        y = p0[1] + (p1[1] - p0[1]) * t
        w = w0 + (w1 - w0) * t
        brush_dab(x, y, w / 2)


def pie_zhe(start, tip, hend, w_pie_start=10, w_pie_end=5, w_heng=6):
    """撇折: short 撇 from start->tip (bezier), then shoulder dab, then short 横 from tip->hend."""
    # 撇 primary — start dab
    brush_dab(*start, w_pie_start / 2 + 1)
    ctrl = (start[0] - (start[0] - tip[0]) * 0.35, start[1] + (tip[1] - start[1]) * 0.55)
    bezier(start, ctrl, tip, (w_pie_start, w_pie_end))
    # shoulder joint dab
    brush_dab(*tip, (w_pie_end + w_heng) / 2 + 1)
    # 横 rightward, slight up-tilt, terminal press
    line_taper(tip, hend, w_heng, w_heng - 1)
    # terminal press
    brush_dab(*hend, w_heng / 2 + 1.5)


# --- Stroke 1: top 撇折 ---
# 撇 goes from upper-right to lower-left; then 横 goes rightward
s1_start = (180, 55)
s1_tip = (115, 115)
s1_hend = (185, 108)
pie_zhe(s1_start, s1_tip, s1_hend, w_pie_start=10, w_pie_end=5, w_heng=6)

# --- Stroke 2: middle 撇折 ---
s2_start = (195, 130)
s2_tip = (125, 185)
s2_hend = (205, 178)
pie_zhe(s2_start, s2_tip, s2_hend, w_pie_start=11, w_pie_end=5, w_heng=6)

# --- Stroke 3: long 撇 sweeping down from mid-right to lower-left ---
# starts near the middle 撇折's 横 end, sweeps down-left across the char
p0 = (210, 180)
p2 = (75, 285)
ctrl = (190, 250)  # bow rightward/downward
# start dab
brush_dab(*p0, 5)
bezier(p0, ctrl, p2, (11, 3), steps=80)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0091_乡/01_乡.png")
