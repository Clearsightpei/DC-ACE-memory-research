"""
Render 佟 = 亻 (left) + 冬 (right)
Revision: use dense interpolation so tapered dabs form solid strokes.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)
BLACK = (0, 0, 0)


def bezier_pts(p0, p1, p2, steps=200):
    out = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        out.append((x, y))
    return out


def poly_pts(waypoints, steps_each=60):
    out = []
    for i in range(len(waypoints) - 1):
        p0 = waypoints[i]
        p1 = waypoints[i + 1]
        for j in range(steps_each + 1):
            t = j / steps_each
            out.append((p0[0] * (1 - t) + p1[0] * t, p0[1] * (1 - t) + p1[1] * t))
    return out


def stroke_taper(points, w_start, w_end):
    n = len(points)
    for i, (x, y) in enumerate(points):
        t = i / max(1, n - 1)
        w = w_start * (1 - t) + w_end * t
        r = w / 2
        draw.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


# ==== 亻 (person radical), left ====
# 撇: from upper mid down and to the left
pie = bezier_pts((90, 75), (75, 140), (40, 215), steps=250)
stroke_taper(pie, 9, 3)

# 竖: vertical, starts near top of 撇 body
shu = poly_pts([(95, 120), (95, 260)], steps_each=200)
stroke_taper(shu, 9, 8)

# ==== 冬 (right side) ====
# 夂: short 撇 from upper right down-left
pie2 = bezier_pts((195, 60), (175, 100), (145, 135), steps=200)
stroke_taper(pie2, 8, 3)

# 横撇 + 长捺 as one continuous sweep: from the meeting point,
# goes right/up-slightly across the top, then down-right as long 捺
top = bezier_pts((145, 130), (215, 110), (275, 165), steps=250)
stroke_taper(top, 8, 10)
# 捺 tail (thin flick)
tail = bezier_pts((275, 165), (280, 172), (272, 180), steps=80)
stroke_taper(tail, 10, 2)

# Two 点 below (冬's characteristic dots)
# Left 点 (slanting down-right)
dot1 = bezier_pts((175, 205), (185, 220), (195, 240), steps=100)
stroke_taper(dot1, 3, 8)

# Right 点 (slanting down-left)
dot2 = bezier_pts((235, 205), (225, 222), (213, 240), steps=100)
stroke_taper(dot2, 3, 8)


img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0348_佟/01_佟.png")
print("saved")
