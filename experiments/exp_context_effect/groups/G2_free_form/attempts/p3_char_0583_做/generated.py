"""
Render 做 (zuo4) at 300x300, black ink on white.

Structural read from GT (3 components, LR-LR):
  Left:   亻 (person radical) — 撇 + 竖. Compressed to x~25-70.
  Middle: 古 (十 + 口) — 横 top, 竖 middle, 口 box below. x~75-155.
  Right:  攵 — 撇 + 横 + 撇 + 捺. Third 横 crosses BOTH 撇s at midpoint;
          fourth 捺 originates from same midpoint (per frozen_cohort 攵 row).
          x~165-285.

Applies the 4-move calligraphic recipe:
  1. Teardrop taper on every 撇/捺/点
  2. Shoulder dabs at 折 corners of 口
  3. Bezier for curved sweeps
  4. No hook in this character (no 钩 present)
Components must TOUCH: 亻竖 touches 古 at ~x=70; 古 right edge touches 攵 at ~x=160.
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
        t = i / max(n - 1, 1) if n > 1 else 0
        if isinstance(widths, tuple):
            w = widths[0] + (widths[1] - widths[0]) * t
        else:
            w = widths
        r = w / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def dab(x, y, r=6):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# ============================================================
# LEFT: 亻 (person radical) — compressed, 竖 ends near body bottom
# ============================================================
# 撇 of 亻
pie_ren = bez((72, 55), (65, 100), (55, 135), (42, 170), n=60)
stroke(pie_ren, (10, 3))
# 竖 of 亻 — starts on the 撇 curve, ends around y=250 (near 口 bottom, not below)
sh_ren = bez((65, 105), (65, 155), (65, 210), (65, 258), n=60)
stroke(sh_ren, (7, 6))


# ============================================================
# MIDDLE: 古 (十 + 口) — nudged left so its left edge touches 亻
# ============================================================
# 横 top of 十
h_top = bez((82, 78), (115, 76), (145, 76), (170, 80), n=50)
stroke(h_top, (6, 6))
dab(82, 78, r=5)
dab(168, 82, r=6)

# 竖 of 十
sh_shi = bez((122, 62), (122, 95), (122, 125), (122, 152), n=50)
stroke(sh_shi, (7, 7))

# 口 box
kou_top = bez((88, 160), (110, 158), (140, 158), (162, 160), n=40)
stroke(kou_top, (6, 6))
kou_left = bez((90, 160), (90, 188), (90, 212), (90, 235), n=40)
stroke(kou_left, (6, 6))
dab(162, 161, r=6)
kou_right = bez((162, 162), (162, 190), (162, 214), (162, 235), n=40)
stroke(kou_right, (6, 5))
kou_bot = bez((90, 234), (115, 236), (140, 236), (164, 234), n=40)
stroke(kou_bot, (6, 6))


# ============================================================
# RIGHT: 攵 — 4 strokes: 撇, 横, 撇, 捺
# Joint at ~(220, 155) — third 撇 & fourth 捺 both originate here.
# ============================================================
# stroke 1: upper 撇
pie1 = bez((215, 60), (210, 78), (203, 95), (192, 112), n=40)
stroke(pie1, (7, 3))

# stroke 2: 横 — crosses under the upper 撇
heng_pu = bez((180, 118), (215, 116), (250, 116), (275, 120), n=50)
stroke(heng_pu, (5, 6))
dab(180, 118, r=5)
dab(275, 121, r=5)

# stroke 3: long 撇 — originates from JOINT area (~220,150), sweeps down-left
pie2 = bez((225, 128), (215, 165), (200, 200), (175, 250), n=80)
stroke(pie2, (9, 3))

# stroke 4: 捺 — originates from same joint (~220,150), sweeps down-right with foot flare
na = bez((222, 138), (240, 175), (260, 210), (282, 250), n=80)
stroke(na, (4, 12))
foot = bez((282, 250), (287, 252), (291, 253), (294, 254), n=15)
stroke(foot, (12, 3))


img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0583_做/01_做.png")
