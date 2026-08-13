"""
给 (gei3/ji3) — 9 strokes, left-right layout.
Left: 纟 (silk radical) — 撇折 + 撇折 + 提 (3 strokes, share joint pixels)
Right: 合 = 人 (撇+捺) + 一 + 口 (竖+横折+横) — 6 strokes.

Applies the calligraphic weight 4-move (memory_index F):
- teardrop taper via stroke(pts, widths=(a,b))
- shoulder dabs at each 折 joint
- bezier for every curved sweep
- hook flicks NONE here (no 钩 in 给)

Frozen-radical alarm: 纟 attested 2+ failed. Fix hypothesis
(frozen_cohort.md): render 纟 as 撇 + 撇折 + 提, share joint pixels.
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

def dab(x, y, r=5):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")

# =============== LEFT: 纟 (silk radical) ===============
# 撇折 #1 (upper): 撇 down-left, then 折 up-right to form a small loop base
s1a = bez((85, 70), (72, 90), (60, 108), (55, 120), n=40)  # 撇 down-left
stroke(s1a, (7, 4))
dab(55, 120, 5)                                            # shoulder dab
s1b = bez((55, 120), (72, 118), (88, 116), (95, 112), n=30)  # 折 up-right
stroke(s1b, (5, 5))

# 撇折 #2 (lower): joint shares pixels with upper #1's endpoint area
s2a = bez((95, 128), (78, 148), (63, 168), (58, 180), n=40)
stroke(s2a, (7, 4))
dab(58, 180, 5)
s2b = bez((58, 180), (78, 178), (95, 175), (105, 170), n=30)
stroke(s2b, (5, 5))

# 提 (bottom): rising left-to-right, thick to thin with a tip
ti = bez((55, 225), (78, 218), (100, 208), (118, 200), n=40)
stroke(ti, (8, 3))

# =============== RIGHT: 合 ===============
# 人 top: big 撇 + 捺 forming inverted V (apex near y=55)
# 撇 — sweeps down-left with taper thick->thin
pie = bez((195, 55), (175, 90), (155, 120), (135, 150), n=80)
stroke(pie, (11, 5))
# 捺 — sweeps down-right with belly + foot flare
na_main = bez((195, 65), (215, 100), (240, 130), (265, 155), n=80)
stroke(na_main, (5, 12))
# foot flare (捺 terminal)
foot = bez((265, 155), (270, 157), (274, 159), (277, 160), n=15)
stroke(foot, (12, 3))

# 一 — horizontal under 人, tucked below apex
h1 = bez((150, 175), (180, 173), (215, 173), (245, 176), n=40)
stroke(h1, (6, 6))

# 口 — rectangle at bottom
# 竖 (left side of 口)
kou_l = bez((160, 200), (160, 225), (160, 250), (160, 265), n=30)
stroke(kou_l, (7, 7))
# 横折 (top horizontal + right vertical, single stroke)
kou_th = bez((160, 200), (200, 199), (240, 199), (250, 200), n=40)
stroke(kou_th, (7, 6))
dab(250, 200, 5)  # shoulder dab at 折 corner
kou_tv = bez((250, 200), (250, 225), (250, 250), (250, 265), n=30)
stroke(kou_tv, (6, 7))
# 横 (bottom of 口)
kou_b = bez((160, 265), (200, 266), (240, 266), (250, 265), n=40)
stroke(kou_b, (7, 7))

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0451_给/01_给.png"
img.save(out)
print(f"wrote {out}")
