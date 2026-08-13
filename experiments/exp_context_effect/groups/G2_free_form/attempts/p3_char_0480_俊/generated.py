"""
Render 俊 (jùn) at 300x300, black ink on white.

Structural read from GT:
  Left: 亻 (person radical) — 撇 top-left + long 竖 straight down.
  Right: 夋
    Top:    small ㄙ/ハ shape (撇 + 点/短横) forming a tiny apex.
    Middle: one short horizontal under the apex.
    Bottom: 夂 — 撇 sweeping down-left from upper-right,
            and 捺 sweeping down-right, crossing near center.

Applies the 4-move calligraphic weight recipe (bez + variable-width
stroke() helper) from TIER-0.F.
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


# ---------------- 亻 (left) ----------------
# 撇: from upper area sweeping down-left, thinning at tail
pie_ren = bez((92, 55), (80, 90), (65, 120), (48, 155), n=70)
stroke(pie_ren, (10, 4))

# 竖: long straight down, thick
shu_ren = bez((88, 105), (88, 165), (88, 220), (88, 268), n=70)
stroke(shu_ren, (9, 8))


# ---------------- 夋 top: small ㄙ (mu) shape ----------------
# 撇 of the tiny apex
apex_pie = bez((188, 50), (172, 68), (155, 82), (142, 95), n=40)
stroke(apex_pie, (7, 3))

# short 折/点 going down-right from the apex peak (like a comma)
apex_dot = bez((188, 55), (198, 72), (208, 88), (215, 100), n=40)
stroke(apex_dot, (4, 8))
# shoulder dab at the top join
dab(190, 55, 5)


# ---------------- middle short horizontal ----------------
h1 = bez((140, 120), (170, 118), (200, 118), (225, 122), n=40)
stroke(h1, (5, 6))


# ---------------- 夂 (bottom right) ----------------
# 撇: sweeping from upper-right down-left through center
pie_zhi = bez((205, 145), (180, 185), (155, 220), (120, 260), n=80)
stroke(pie_zhi, (9, 4))

# small 横撇 shoulder before the 捺 (a short horizontal joining onto 撇)
sh = bez((135, 168), (155, 165), (175, 165), (195, 168), n=40)
stroke(sh, (5, 5))
dab(195, 168, 4)

# 捺: from mid, sweeping down-right with a flared foot
na_main = bez((155, 185), (185, 215), (215, 240), (245, 262), n=80)
stroke(na_main, (4, 12))
# foot flare
foot = bez((245, 262), (252, 264), (258, 265), (263, 266), n=20)
stroke(foot, (12, 3))


img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0480_俊/01_俊.png")
