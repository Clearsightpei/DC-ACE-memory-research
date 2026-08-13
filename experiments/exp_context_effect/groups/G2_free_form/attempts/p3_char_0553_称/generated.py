"""
Render 称 (cheng1) at 300x300, black ink on white.

Structural read from GT:
  Left: 禾 (grain radical, narrow) — 撇 top + 横 + 竖 + 撇(mid) + 点(right)
  Right: 尔 — 撇(top) + 横钩(canopy) + 竖钩(center 亅) + 左点 + 右点

Applies TIER-0 calligraphic weight (v7.5):
  - Teardrop tapers on 撇 / 点
  - Bezier for curved sweeps
  - Hook flicks UP-and-LEFT (never DOWN) — v7 rule B
  - Components touch (禾 竖 and 尔 canopy meet visually — rule H)
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


# =============== 禾 (LEFT, x ~ 20-135) ===============
# 1. 撇 top — small flick above 横
pie_top = bez((90, 55), (80, 65), (68, 72), (52, 78), n=40)
stroke(pie_top, (7, 3))

# 2. 横 — short horizontal, slight rise
h1 = bez((25, 80), (55, 76), (95, 76), (135, 80), n=40)
stroke(h1, (6, 6))

# 3. 竖 — vertical, center of 禾 (bounded, don't overshoot GT balance)
v_he = bez((80, 80), (80, 130), (80, 180), (80, 240), n=70)
stroke(v_he, (7, 7))

# 4. 撇 from center — starts near intersection, sweeps down-left
pie_mid = bez((80, 110), (63, 145), (45, 180), (22, 218), n=60)
stroke(pie_mid, (8, 3))

# 5. 点 (right dot — 捺 compressed because 禾 on left)
right_dot = bez((85, 125), (102, 150), (120, 178), (138, 210), n=50)
stroke(right_dot, (3, 10))


# =============== 尔 (RIGHT, x ~ 155-285) ===============
# 1. 撇 top — small slanting flick at top-center of 尔
pie_r_top = bez((225, 55), (215, 65), (205, 72), (195, 80), n=40)
stroke(pie_r_top, (7, 3))

# 2. 横钩 — canopy: horizontal then hook DOWN-LEFT at the right end
h_canopy = bez((165, 95), (200, 90), (240, 90), (275, 95), n=50)
stroke(h_canopy, (6, 7))
# hook flick: from right end of canopy, flick UP-and-LEFT? No — 横钩 hooks DOWN-LEFT (like 冖 or 宀 hook)
# Actually 横钩 hook goes DOWN-and-LEFT (into character body). Standard.
hook_canopy = bez((275, 95), (272, 102), (268, 110), (262, 115), n=25)
stroke(hook_canopy, (7, 4))

# 3. 竖钩 — center vertical of 尔, then hook UP-and-LEFT at bottom (v7 rule B)
v_center = bez((220, 105), (220, 170), (220, 220), (218, 260), n=80)
stroke(v_center, (8, 7))
# hook UP-and-LEFT
hook_v = bez((218, 260), (210, 255), (202, 250), (195, 244), n=25)
stroke(hook_v, (7, 3))

# 4. 左点 — dot to the left of center vertical, mid-lower area
left_dot = bez((193, 150), (185, 172), (178, 195), (170, 218), n=40)
stroke(left_dot, (3, 8))

# 5. 右点 — dot to the right, symmetric
right_dot_r = bez((252, 150), (258, 178), (265, 205), (272, 230), n=40)
stroke(right_dot_r, (3, 9))


img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0553_称/01_称.png")
print("saved")
