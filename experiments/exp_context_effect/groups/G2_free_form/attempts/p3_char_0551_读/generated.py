"""
Render 读 (du2) at 300x300.

Structure: 讠 (left) + 卖 (right = 士 top + 冖 middle + 大 bottom).
讠 recipe: dot + coiled hook as continuous polyline.
Apply 4-move recipe (taper, shoulder dabs, bezier, hook flick).
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


def shoulder(cx, cy, r=5):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")


# ============ 讠 (left radical) ============
# top 丶 dot (visible teardrop, slanting down-right)
dot = bez((55, 60), (60, 68), (66, 76), (72, 85), n=25)
stroke(dot, (4, 9))

# coiled body: short 横 → fold down → sweep → hook flick, ONE polyline feel
zi_pts = []
zi_pts += bez((45, 115), (60, 112), (78, 112), (92, 115), n=30)
zi_pts += bez((92, 115), (90, 130), (80, 148), (65, 162), n=30)
zi_pts += bez((65, 162), (60, 178), (60, 195), (65, 210), n=30)
zi_pts += bez((65, 210), (75, 222), (88, 232), (100, 238), n=30)
stroke(zi_pts, (3, 5))
hook_zi = bez((100, 238), (96, 232), (92, 226), (87, 220), n=20)
stroke(hook_zi, (5, 2))
shoulder(92, 115, r=4)
shoulder(65, 210, r=3)

# ============ 卖 (right body) ============
# --- 士 top: short 横 (top), 竖 through middle, longer 横 (base) ---
# top short 横
h_top = bez((160, 55), (185, 53), (210, 53), (230, 55), n=30)
stroke(h_top, (5, 6))
# 竖 through — from top 横 down to base 横
shu = bez((195, 55), (195, 78), (195, 100), (195, 118), n=30)
stroke(shu, (7, 7))
# base 横 (longer, wider than top)
h_wide = bez((135, 118), (175, 116), (215, 116), (255, 118), n=40)
stroke(h_wide, (5, 7))

# --- 冖 (top-cover): left dot + horizontal + right tick ---
cap_dot = bez((140, 138), (143, 143), (146, 148), (149, 154), n=20)
stroke(cap_dot, (3, 6))
# main cover: 横 then folds down at right
cap_h = bez((150, 140), (185, 138), (220, 140), (248, 143), n=40)
stroke(cap_h, (5, 6))
cap_r = bez((248, 143), (247, 158), (245, 172), (242, 185), n=25)
stroke(cap_r, (6, 3))
shoulder(248, 143, r=4)

# --- 大 bottom ---
# 一 (horizontal crossbar, spans width)
big_h = bez((135, 205), (175, 203), (215, 203), (255, 205), n=40)
stroke(big_h, (5, 7))
# 撇 — sweep down-left from top-right of crossbar
pie = bez((198, 190), (180, 215), (160, 240), (130, 275), n=60)
stroke(pie, (9, 3))
# 捺 — S-curve down-right, thick tail with foot flare
na = bez((200, 205), (220, 230), (245, 255), (270, 273), n=60)
stroke(na, (4, 11))
foot = bez((270, 273), (275, 274), (280, 275), (285, 275), n=15)
stroke(foot, (11, 3))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0551_读/01_读.png")
