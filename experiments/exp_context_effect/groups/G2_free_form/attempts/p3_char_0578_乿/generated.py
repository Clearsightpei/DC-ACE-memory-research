"""
Render 乿 (alt form of 亂 — "chaos") at 300x300.

Structural read from GT:
  Left ~60%: two organic 幺-like clusters (short strokes + dots),
    upper cluster y=50..135, lower cluster y=145..235.
  Right ~40%: tall 乚 (竖弯钩) — vertical stem, curves right at bottom,
    UP-and-LEFT flick at the terminal (TIER-0 rule B).

TIER-0 F applied: taper on all 撇/点, shoulder dab at 乚 corner,
bezier for curved sweep, UP-LEFT hook flick.
TIER-0 H applied: 乚 nudged left so its stem sits closer to the
left cluster (small residual gap matches GT).
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


# ==========================================================
# LEFT SIDE — UPPER cluster (~y 50..130)
# 爪-like: 撇 sweeping out top, short 横, small nubs, 竖 stub
# ==========================================================
# small top-left flick
u_flick = bez((55, 65), (65, 60), (75, 60), (85, 62), n=30)
stroke(u_flick, (5, 4))
# upper 撇 sweeping down-left from center-top
u_pie = bez((115, 55), (95, 72), (75, 92), (55, 115), n=50)
stroke(u_pie, (6, 3))
# small horizontal bar mid-cluster
u_bar = bez((80, 90), (105, 88), (130, 88), (150, 92), n=40)
stroke(u_bar, (5, 5))
# small down-right stroke
u_dr = bez((145, 92), (150, 105), (155, 118), (152, 128), n=30)
stroke(u_dr, (5, 4))
# nubs / dots
dab(95, 108, 3)
dab(120, 115, 3)

# ==========================================================
# LEFT SIDE — LOWER cluster (~y 145..235)
# similar tangle mirrored below
# ==========================================================
l_flick = bez((55, 155), (68, 152), (82, 152), (95, 155), n=30)
stroke(l_flick, (5, 4))
l_pie = bez((125, 150), (105, 170), (80, 195), (55, 220), n=50)
stroke(l_pie, (6, 3))
l_bar = bez((75, 195), (105, 193), (135, 193), (155, 197), n=40)
stroke(l_bar, (5, 5))
l_dr = bez((150, 197), (154, 212), (158, 225), (150, 235), n=30)
stroke(l_dr, (5, 4))
dab(95, 215, 3)
dab(125, 220, 3)
# bottom hook stub
l_hook = bez((90, 235), (100, 240), (110, 243), (118, 244), n=20)
stroke(l_hook, (4, 3))

# ==========================================================
# RIGHT SIDE — big 乚 (竖弯钩), spans y=50..260
# Stem sits close to left cluster (small gap only).
# ==========================================================
# vertical stem
stem = bez((205, 50), (204, 110), (203, 175), (203, 220), n=80)
stroke(stem, (8, 8))
# shoulder dab at corner
dab(203, 220, 6)
# horizontal sweep right
sweep = bez((203, 225), (218, 242), (238, 250), (258, 252), n=60)
stroke(sweep, (8, 9))
# shoulder dab at hook base
dab(258, 252, 6)
# UP-and-LEFT hook flick
hook = bez((258, 252), (255, 244), (250, 236), (243, 228), n=30)
stroke(hook, (9, 3))


img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0578_乿/01_乿.png")
