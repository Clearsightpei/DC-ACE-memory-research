"""
Render 保 (bao3) at 300x300, black ink on white.

Structural read from GT:
  Left:  亻 (person radical) — small 撇 (top) + long 竖 (full-height vertical).
  Right: 呆 = 口 (top, small mouth) + 木 (bottom, tree).
    口: compact box in the top-right.
    木: 横 (wide horizontal) + 竖 (long vertical) + 撇 + 捺 crossing.

Applying the calligraphic-weight 4-move recipe:
  1. Teardrop taper on 撇/捺/点.
  2. Shoulder dab at every 折 corner (口's top-right corner).
  3. Bezier for curved sweeps (撇 bowed, 捺 S-curve).
  4. No hooks in this glyph (亻 uses 竖, 木 uses 竖 not 竖钩).
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

# ============ 亻 (left radical) ============
# 撇: from top-right of radical, sweeps down-left with a bow
pie = bez((78, 55), (68, 100), (55, 130), (35, 175), n=80)
stroke(pie, (10, 4))

# 竖: long straight vertical, starts near top of 撇, drops to bottom
shu_left = bez((78, 95), (78, 155), (78, 215), (78, 270), n=60)
stroke(shu_left, (7, 7))

# ============ 呆: 口 (top-right box) ============
# Small mouth in upper-right region
x1, y1, x2, y2 = 135, 55, 235, 115

# top 横 with entry dab
h_top = bez((x1, y1), (x1+30, y1-1), (x2-30, y1-1), (x2, y1), n=40)
stroke(h_top, (6, 6))

# right 竖 (part of 横折): shoulder dab at corner, then down
dab(x2, y1, r=4)
v_right = bez((x2, y1), (x2, y1+20), (x2, y2-20), (x2-2, y2), n=40)
stroke(v_right, (6, 5))

# left 竖
v_left = bez((x1, y1+3), (x1, y1+25), (x1, y2-15), (x1, y2), n=40)
stroke(v_left, (7, 6))

# bottom 横 (sealing the box)
h_bot = bez((x1, y2), (x1+30, y2), (x2-30, y2), (x2, y2), n=40)
stroke(h_bot, (6, 6))

# ============ 呆: 木 (bottom-right tree) ============
# 横 (wide horizontal below 口)
h_wood = bez((100, 155), (155, 152), (215, 152), (270, 156), n=60)
stroke(h_wood, (7, 7))

# 竖 (long vertical through the horizontal down to bottom)
v_wood = bez((185, 120), (185, 175), (185, 225), (185, 275), n=60)
stroke(v_wood, (8, 8))

# 撇 (from crossing, sweeps down-left with a bow)
pie_wood = bez((180, 165), (160, 195), (135, 225), (110, 265), n=70)
stroke(pie_wood, (9, 3))

# 捺 (from crossing, S-curve down-right with foot flare)
na_wood = bez((190, 165), (215, 200), (240, 235), (258, 260), n=70)
stroke(na_wood, (4, 12))
# foot flare
foot = bez((258, 260), (263, 262), (268, 264), (272, 265), n=20)
stroke(foot, (12, 3))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0479_保/01_保.png")
