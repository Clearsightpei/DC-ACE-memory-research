"""
Render 被 (bei4) at 300x300, black ink on white.

Structural decomposition:
  Left:  衤 (clothing radical, 5 strokes): 点 top, 横撇, long 竖, left 撇, right 点.
  Right: 皮 (5 strokes): short 横 top, big 撇 sweeping down-left,
         横折 shoulder into 又-like body, ending 捺 sweep down-right.

Components MUST TOUCH (tier-0 rule H): 衤 竖 shares vertical band with
皮's 撇 launching point.

Calligraphic 4-move applied: tapered bez strokes, shoulder dabs at 折,
UP-and-LEFT flicks on any hook, S-curves via bez.
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

# =========================================================
# LEFT: 衤 (clothing radical)
# =========================================================

# 1. Top 点 — small teardrop, slants down-right
p1 = bez((72, 45), (76, 52), (80, 60), (85, 70), n=30)
stroke(p1, (3, 9))

# 2. 横撇 — short horizontal, then quick pie down-left
h_top = bez((40, 90), (65, 88), (95, 88), (115, 92), n=40)
stroke(h_top, (7, 6))
# shoulder dab at right end of 横 before pie
dab(115, 92, 5)
pie_top = bez((115, 92), (110, 100), (103, 108), (95, 115), n=30)
stroke(pie_top, (7, 3))

# 3. 竖 — long vertical, slightly left-of-center of 衤
sh = bez((78, 92), (78, 165), (78, 230), (78, 275), n=60)
stroke(sh, (7, 7))

# 4. 撇 — from upper mid, sweeping down-left with bow
pie = bez((72, 160), (55, 200), (40, 235), (22, 275), n=60)
stroke(pie, (9, 3))

# 5. 点 (right) — dot on the right side of 衤
dot_r = bez((95, 175), (108, 195), (118, 215), (125, 235), n=30)
stroke(dot_r, (4, 10))

# =========================================================
# RIGHT: 皮
# =========================================================

# 1. Short top 横 — with hook down at right
h_皮 = bez((155, 55), (185, 53), (215, 53), (238, 57), n=40)
stroke(h_皮, (7, 6))
# small hook down at right end of 横
dab(238, 57, 5)
hookdown = bez((238, 57), (237, 63), (236, 70), (234, 78), n=20)
stroke(hookdown, (6, 3))

# 2. Big 撇 — from upper region, long sweep down-left
big_pie = bez((175, 55), (160, 130), (140, 200), (120, 285), n=80)
stroke(big_pie, (11, 3))

# 3. 横折 forming right wall of 又-shape (shorter horizontal, cleaner fold)
h_mid = bez((175, 125), (200, 123), (230, 123), (250, 128), n=40)
stroke(h_mid, (6, 6))
# shoulder dab at fold
dab(250, 128, 5)
v_right = bez((250, 128), (250, 150), (250, 175), (250, 195), n=40)
stroke(v_right, (7, 5))
# small hook flick UP-and-LEFT at bottom of v_right
hookflick = bez((250, 195), (245, 192), (240, 188), (234, 183), n=20)
stroke(hookflick, (5, 3))

# 4. Interior small 撇/point — the 又-mouth inner short stroke, angled down-right
inner = bez((190, 170), (208, 180), (225, 190), (240, 200), n=40)
stroke(inner, (5, 5))

# 5. 捺 — from inside body, sweeping down-right with foot flare
na = bez((200, 200), (222, 225), (248, 250), (278, 278), n=80)
stroke(na, (5, 12))
# foot flare
foot = bez((278, 278), (283, 279), (287, 279), (292, 278), n=20)
stroke(foot, (12, 4))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0523_被/01_被.png")
