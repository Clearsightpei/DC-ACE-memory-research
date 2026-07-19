"""
p1_stroke_17_撇点 (pie-dian)
Compound stroke: a 撇 (throw-away, upper-right -> lower-left, thick->thin)
followed by a 点 (dot) placed at the lower-right of the 撇's endpoint.
Rendered with PIL brush-dab technique per drawer_memory.md.
300x300 canvas, white bg, black ink.
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab_line(p0, p1, r_start, r_end, steps=400):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def dab_bezier(p0, p1, p2, r_start, r_end, steps=400):
    # Quadratic Bezier with linearly varying radius (thick->thin).
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * x0 + 2 * u * t * x1 + t * t * x2
        y = u * u * y0 + 2 * u * t * y1 + t * t * y2
        r = r_start + (r_end - r_start) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


# ---- 撇 (pie): from upper-right down to lower-left, thick -> thin.
# Give it a gentle bow (control point slightly toward the interior/right).
pie_start = (215, 70)       # upper-right start
pie_end   = (95, 210)       # lower-left tip
pie_ctrl  = (185, 115)      # bow control point (slight rightward curve)

# 顿笔: one slightly-larger dab at the starting endpoint
draw.ellipse((pie_start[0] - 12, pie_start[1] - 12,
              pie_start[0] + 12, pie_start[1] + 12), fill="black")

dab_bezier(pie_start, pie_ctrl, pie_end, r_start=10.0, r_end=1.5, steps=500)

# ---- 点 (dian): a short teardrop at the lower-right of the 撇's endpoint.
# The 点 in 撇点 sits so its head starts near / slightly below the 撇 tip
# and pushes down-and-to-the-right (like a 反捺 / short right-falling dot).
dian_start = (135, 195)     # upper-left of dot (near pie's tip, slightly up-right)
dian_end   = (200, 245)     # lower-right of dot (broad foot)
dian_ctrl  = (160, 210)     # slight bow

# The dot is thin -> thick (like a 捺/反捺 dot), ending in a broader press.
dab_bezier(dian_start, dian_ctrl, dian_end, r_start=3.0, r_end=10.0, steps=300)

# Terminal press: one slightly-larger dab at the dot's tail for calligraphic weight.
draw.ellipse((dian_end[0] - 12, dian_end[1] - 12,
              dian_end[0] + 12, dian_end[1] + 12), fill="black")

out_path = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p1_stroke_17_撇点/01_撇点.png"
img.save(out_path)
print(f"saved {out_path} ({W}x{H})")
