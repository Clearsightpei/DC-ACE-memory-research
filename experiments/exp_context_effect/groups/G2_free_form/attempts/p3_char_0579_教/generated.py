"""
Render 教 at 300x300, black ink on white.

Structural read (11 strokes):
  Left component = 耂 (top) + 子 (bottom):
    1. 横 (top short horizontal, upper-left)
    2. 横 (second/longer horizontal, crossing)
    3. 竖 (short vertical through the two horizontals)
    4. 撇 (long left-sweeping pie starting from upper-right of 耂)
    5. 横撇/横折 top of 子 (short horizontal into a down-left arc)
    6. 弯钩 of 子 (curved vertical with UP-LEFT hook flick)
    7. 横 across 子 (middle horizontal)
  Right component = 攵:
    8. 短撇 (top short pie)
    9. 横 (short horizontal below the dot)
    10. 撇 (long down-left sweep)
    11. 捺 (long down-right sweep with foot flare)

# SIGNATURE CHECK (攵 frozen-cohort row):
#   攵 = 撇 + 撇 + 横 + 捺; the 横 crosses BOTH 撇s at mid; the 4th 捺
#   originates near same midpoint (per frozen_cohort.md).
# TIER-0 H: components must TOUCH — the long left 撇 of 耂 crosses into
#   the right component's 撇/捺 sweep zone (~x=170). Ensure no gap.
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

# ============ LEFT: 耂 + 子 ============

# 1. top short 横 of 耂
h1 = bez((60, 60), (90, 58), (125, 58), (150, 62), n=40)
stroke(h1, (5, 5))

# 2. longer 横 crossing (below the short one)
h2 = bez((35, 105), (80, 103), (140, 103), (170, 107), n=50)
stroke(h2, (6, 6))

# 3. short 竖 through the two horizontals
v1 = bez((108, 40), (108, 70), (108, 95), (108, 115), n=40)
stroke(v1, (6, 6))

# 4. long 撇 sweeping from upper-right down-left across the character
pie_left = bez((160, 75), (130, 135), (90, 185), (25, 240), n=90)
stroke(pie_left, (11, 4))

# 5. 横撇 top of 子: short horizontal into a down-left curve (starts inside 撇)
zi_top_h = bez((70, 165), (100, 163), (135, 163), (160, 167), n=45)
stroke(zi_top_h, (6, 5))
# turn dab
d.ellipse((155, 163, 168, 176), fill="black")
zi_top_arc = bez((160, 167), (155, 185), (145, 200), (130, 210), n=40)
stroke(zi_top_arc, (6, 4))

# 6. 弯钩 of 子: curved vertical, hook UP-LEFT
zi_hook = bez((115, 175), (120, 210), (110, 245), (95, 265), n=60)
stroke(zi_hook, (7, 6))
# hook flick UP-and-LEFT into character body
hk = bez((95, 265), (85, 258), (75, 250), (65, 245), n=25)
stroke(hk, (7, 3))

# 7. 横 across 子 (middle horizontal cross-bar of 子, spans lower body)
h_zi = bez((45, 235), (80, 233), (130, 233), (160, 237), n=45)
stroke(h_zi, (5, 5))

# ============ RIGHT: 攵 ============

# 8. 短撇 (top short pie)
sp = bez((225, 85), (218, 105), (210, 120), (200, 135), n=40)
stroke(sp, (8, 3))

# 9. short 横
h_r = bez((195, 145), (215, 143), (240, 143), (260, 146), n=40)
stroke(h_r, (5, 5))

# 10. long 撇 sweeping down-left from upper 攵 area
pie_r = bez((240, 155), (215, 195), (190, 230), (165, 275), n=80)
stroke(pie_r, (10, 4))

# 11. long 捺 sweeping down-right with foot flare
na = bez((215, 165), (240, 205), (265, 240), (285, 265), n=80)
stroke(na, (4, 12))
# foot flare
foot = bez((285, 265), (289, 267), (292, 268), (295, 269), n=15)
stroke(foot, (12, 3))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0579_教/01_教.png")
