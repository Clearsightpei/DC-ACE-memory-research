"""
Render 佘 (yu2/she2) at 300x300, black ink on white.

Structural read from GT:
  Top:    big 人 (撇 + 捺) forming an inverted V that spans most of the width.
  Middle: two short horizontals tucked under the 人 apex.
  Bottom: 小 — center 竖钩 (with UP-LEFT flick per index tier-0 rule),
          left 点/撇, right 点.
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
    """Draw a variable-width stroke via overlapping circles."""
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / max(n - 1, 1)
        if isinstance(widths, tuple):
            w = widths[0] + (widths[1] - widths[0]) * t
        else:
            w = widths
        r = w / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")

# --- 人 top ---
# 撇: starts near top-center, sweeps down-left, thins slightly at tail
pie = bez((150, 40), (135, 90), (100, 130), (55, 175), n=80)
stroke(pie, (11, 5))

# 捺: starts near apex, sweeps down-right with a slight belly and a foot at the end
na_main = bez((150, 55), (175, 100), (210, 140), (245, 170), n=80)
stroke(na_main, (5, 13))
# foot flare at the end of 捺 (small extra bit)
foot = bez((245, 170), (252, 172), (258, 174), (262, 175), n=20)
stroke(foot, (13, 4))

# --- two middle horizontals under the apex ---
# upper short horizontal (a bit longer)
h1 = bez((105, 150), (135, 148), (170, 148), (195, 152), n=40)
stroke(h1, (6, 6))

# lower short horizontal (narrower, centered)
h2 = bez((115, 190), (145, 188), (175, 188), (200, 192), n=40)
stroke(h2, (5, 5))

# --- 小 bottom ---
# 竖钩 center
sg = bez((155, 200), (155, 235), (155, 260), (152, 275), n=50)
stroke(sg, (7, 7))
# hook flick UP-and-LEFT
hook = bez((152, 275), (148, 270), (144, 264), (140, 258), n=20)
stroke(hook, (7, 3))

# left 撇/dot of 小
left_dot = bez((125, 220), (115, 240), (108, 255), (100, 270), n=40)
stroke(left_dot, (7, 3))

# right dot of 小
right_dot = bez((185, 225), (200, 240), (212, 255), (222, 268), n=40)
stroke(right_dot, (4, 8))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0338_佘/01_佘.png")
