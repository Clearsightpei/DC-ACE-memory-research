"""
Render 验 (yan4) — left 马 (compressed) + right 佥.
Applies TIER-0 F 4-move: bez curves, variable stroke widths,
shoulder dabs at folds, UP-LEFT hook flick, and component TOUCH rule.

Structure from GT:
  Left: 马 compressed, x ~ 25..130 (three strokes: 横折, 竖折折钩, 一)
  Right: 佥, x ~ 140..285
    - top 人 apex ~215,40, 撇 to (155,130), 捺 to (285,130)
    - two horizontals under apex (upper longer)
    - two 点 pair at bottom (left dot slanting down-left, right dot down-right)

Components touch: bottom 一 of 马 extends toward the right component base.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def bez(p0, p1, p2, p3, n=60):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u*u*u*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t*t*t*p3[0]
        y = u*u*u*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t*t*t*p3[1]
        pts.append((x, y))
    return pts


def stroke(pts, widths):
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / max(n - 1, 1)
        if isinstance(widths, tuple):
            w = widths[0] + (widths[1] - widths[0]) * t
        else:
            w = widths
        r = w / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# ================= LEFT: 马 (compressed to ~25..130 width) =================
# Stroke 1: 横折 — top horizontal + right descent of upper box
top_h = bez((40, 75), (65, 72), (95, 70), (115, 72), n=40)
stroke(top_h, (5, 5))
dab(115, 72, 4)  # shoulder dab
right_wall = bez((115, 72), (117, 95), (118, 115), (118, 130), n=40)
stroke(right_wall, (5, 4))

# Stroke 2: 竖折折钩 — left wall + middle horizontal + descent + hook
left_wall = bez((38, 75), (35, 100), (33, 125), (33, 135), n=40)
stroke(left_wall, (5, 5))
dab(33, 135, 4)
mid_h = bez((33, 135), (60, 133), (90, 132), (118, 133), n=40)
stroke(mid_h, (5, 5))
dab(118, 133, 4)
lower_desc = bez((118, 133), (122, 160), (128, 185), (132, 210), n=40)
stroke(lower_desc, (5, 5))
# hook flick UP-and-LEFT into character body
hook = bez((132, 210), (125, 205), (118, 200), (110, 195), n=25)
stroke(hook, (5, 2))

# Stroke 3: 一 bottom horizontal — extends left AND touches right component
bot = bez((22, 240), (70, 238), (110, 238), (145, 240), n=50)
stroke(bot, (6, 5))

# ================= RIGHT: 佥 (x ~ 140..285) =================
# 人 top
# 撇: from apex (215, 40) sweeping down-left to (150, 130)
pie = bez((215, 40), (200, 70), (175, 100), (148, 132), n=70)
stroke(pie, (10, 4))

# 捺: from apex down-right, S-curve to (285, 135) with foot
na = bez((218, 55), (240, 85), (260, 110), (280, 133), n=70)
stroke(na, (4, 12))
foot = bez((280, 133), (285, 135), (289, 136), (292, 137), n=15)
stroke(foot, (12, 3))

# --- two middle horizontals ---
h1 = bez((165, 152), (200, 150), (240, 150), (270, 154), n=40)
stroke(h1, (5, 5))

h2 = bez((175, 182), (210, 180), (240, 180), (262, 184), n=40)
stroke(h2, (5, 5))

# --- two 点 pair at bottom ---
# left dot: slanting down-left (short 撇)
left_dot = bez((198, 205), (188, 220), (180, 235), (172, 250), n=30)
stroke(left_dot, (7, 3))

# right dot: slanting down-right (short 捺)
right_dot = bez((238, 205), (250, 220), (260, 235), (270, 250), n=30)
stroke(right_dot, (3, 8))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0521_验/01_验.png")
print("Saved 01_验.png")
