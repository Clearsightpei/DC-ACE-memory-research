"""
p3_char_0240_仰 — G2 attempt (revision 2).

Composition: 仰 = 亻 (left) + 卬-body.
卬 = 丿 + 竖提(mirror-卩) on the middle, + 卩(横折钩 + 竖) on the right.

Reading the GT: three vertical components, left one (亻) tallest,
middle a bit shorter, right (卩) reaches near baseline. The right
卩 has a clear 横 shoulder that turns down, with a separate 竖 to
its left.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def bezier(p0, p1, p2, p3, n=80):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 3 * p0[0] + 3 * (1 - t) ** 2 * t * p1[0] + 3 * (1 - t) * t * t * p2[0] + t ** 3 * p3[0]
        y = (1 - t) ** 3 * p0[1] + 3 * (1 - t) ** 2 * t * p1[1] + 3 * (1 - t) * t * t * p2[1] + t ** 3 * p3[1]
        pts.append((x, y))
    return pts


def stroke(pts, w_start=6, w_end=6):
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / max(1, n - 1)
        r = w_start + (w_end - w_start) * t
        r = max(1.5, r)
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# ---------- 亻 (left radical) ----------
# 撇 (top slant)
pts = bezier((100, 75), (95, 105), (80, 135), (60, 170), n=60)
stroke(pts, w_start=5, w_end=3)
# 竖 (long vertical)
pts = bezier((95, 100), (95, 155), (93, 210), (90, 258), n=60)
stroke(pts, w_start=5, w_end=4)


# ---------- Middle: 丿 + 竖提 (mirror-卩) ----------
# short 丿 curving down-left
pts = bezier((150, 95), (145, 125), (137, 155), (125, 180), n=50)
stroke(pts, w_start=5, w_end=3)
# 竖提 — vertical dropping then a small right-flick at bottom
pts = bezier((155, 105), (155, 155), (155, 205), (158, 235), n=50)
stroke(pts, w_start=5, w_end=4)
# flick
pts = bezier((158, 235), (168, 232), (178, 228), (185, 222), n=20)
stroke(pts, w_start=4, w_end=2)


# ---------- Right: 卩 (横折钩 + 竖) ----------
# 竖 (left vertical of 卩)
pts = bezier((195, 105), (195, 155), (197, 205), (200, 250), n=60)
stroke(pts, w_start=5, w_end=4)

# 横折钩: 横 shoulder, then turn down, then hook flick up-left
pts = bezier((205, 100), (225, 100), (245, 100), (252, 105), n=40)
stroke(pts, w_start=5, w_end=5)
# turn down
pts = bezier((252, 105), (252, 140), (250, 180), (245, 215), n=50)
stroke(pts, w_start=5, w_end=4)
# small hook flick up-left
pts = bezier((245, 215), (240, 213), (232, 210), (225, 208), n=15)
stroke(pts, w_start=4, w_end=2)


img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0240_仰/01_仰.png")
