"""
Render 伫 (亻 + 宁) to a 300x300 PNG.

Composition:
  - 亻 on left, compressed to ~30% width band (x ~30-100).
    * 撇: head upper-right, sweeps down-left.
    * 竖: straight vertical drop, touches 撇 body near top.
  - 宁 on right (x ~120-270):
    * Top 点: small dab high-center.
    * 宀 roof: 横 (horizontal) that bends down-right into a short 乁.
    * 一 (horizontal) below.
    * 亅 (short vertical, hook flick UP-and-LEFT per TIER-0 B).
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def brush_stroke(points, widths):
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        w0 = widths[i]
        w1 = widths[i + 1]
        dx = x1 - x0
        dy = y1 - y0
        seg = max(abs(dx), abs(dy))
        steps = max(int(seg) * 2, 8)
        for s in range(steps + 1):
            t = s / steps
            x = x0 + dx * t
            y = y0 + dy * t
            r = w0 * (1 - t) + w1 * t
            d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# ---- 亻 on the left ----
# 撇
pie_points = [
    (95, 55),
    (88, 85),
    (75, 120),
    (55, 160),
    (30, 200),
]
pie_widths = [5.0, 5.0, 4.5, 3.5, 1.8]
brush_stroke(pie_points, pie_widths)

# 竖
shu_points = [
    (78, 115),
    (78, 170),
    (78, 225),
    (78, 265),
]
shu_widths = [5.0, 5.0, 5.0, 4.5]
brush_stroke(shu_points, shu_widths)

# ---- 宁 on the right ----
# Top 点 (small)
dot_pts = [(195, 45), (200, 60)]
dot_ws = [3.0, 5.0]
brush_stroke(dot_pts, dot_ws)

# 宀 roof: 横 that folds into 乁 tail
roof_h = [(135, 100), (180, 98), (230, 98), (255, 100)]
roof_hw = [3.5, 4.5, 4.5, 4.5]
brush_stroke(roof_h, roof_hw)
# short 乁 falling right from roof end
roof_tail = [(255, 100), (262, 118), (268, 138)]
roof_tw = [4.5, 3.5, 2.0]
brush_stroke(roof_tail, roof_tw)

# 一 (horizontal, bottom of 宁, wide)
heng_pts = [(135, 220), (185, 218), (235, 218), (270, 220)]
heng_ws = [3.0, 4.5, 4.5, 4.0]
brush_stroke(heng_pts, heng_ws)

# 亅 (vertical hook, from roof-cell down through the 一 area, ending with UP-LEFT flick)
hook_pts = [(195, 145), (195, 190), (195, 235), (195, 258)]
hook_ws = [4.5, 4.8, 4.8, 4.2]
brush_stroke(hook_pts, hook_ws)
# hook flick UP-and-LEFT
flick_pts = [(195, 258), (188, 252), (180, 246)]
flick_ws = [4.2, 3.0, 1.8]
brush_stroke(flick_pts, flick_ws)


img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0274_伫/01_伫.png"
)
