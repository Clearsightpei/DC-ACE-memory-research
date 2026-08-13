"""
Render 畎 (quan3) at 300x300, black ink on white.

Composition: 田 (left) + 犬 (right).
  田: compact rectangle with cross inside — 竖(left) + 横折(top-right corner)
      + inner 竖 + inner 横 + bottom 一 closing the box.
  犬: 大 (横 + 撇 + 捺) with a small 丶 at upper-right.

Left/right proportion: 田 ~ 40% width, 犬 ~ 55% width, slight overlap in
middle whitespace. 田 is roughly square centered vertically. 犬 spans
the full canvas height with 大's 横 at ~y=125 and 捺 sweeping to lower
right; 丶 sits above where 捺 begins.

Applies the 4-move calligraphic recipe:
  - variable-width strokes via ellipse-dab (stroke helper)
  - shoulder dab at 折 joint (top-right of 田, at 大's 撇 root)
  - bezier for 撇 and 捺
  - no hooks in this character (畎 has none)
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

# =========== 田 (left) ===========
# Box bounds: x 30..135, y 95..215
LX, RX, TY, BY = 30, 135, 95, 215
MX = (LX + RX) / 2   # inner vertical
MY = (TY + BY) / 2   # inner horizontal

# Stroke 1: 竖 (left side)
left_v = bez((LX, TY), (LX, TY+40), (LX, TY+80), (LX, BY), n=40)
stroke(left_v, (7, 6))

# Stroke 2: 横折 (top + right side)  — one continuous top 横 then folds down
top_h = bez((LX, TY), (LX+30, TY-1), (LX+70, TY-1), (RX, TY), n=40)
stroke(top_h, (6, 7))
# shoulder dab at top-right corner
dab(RX, TY, 5)
right_v = bez((RX, TY), (RX, TY+40), (RX, TY+80), (RX, BY), n=40)
stroke(right_v, (7, 6))

# Stroke 3: inner 竖 (vertical through middle)
inner_v = bez((MX, TY), (MX, TY+40), (MX, TY+80), (MX, BY), n=40)
stroke(inner_v, (6, 6))

# Stroke 4: inner 横 (horizontal through middle)
inner_h = bez((LX, MY), (LX+30, MY), (LX+70, MY), (RX, MY), n=40)
stroke(inner_h, (5, 6))

# Stroke 5: 一 (bottom of box)
bot_h = bez((LX, BY), (LX+30, BY), (LX+70, BY), (RX, BY), n=40)
stroke(bot_h, (6, 7))

# =========== 犬 (right) ===========
# Right side spans x ~ 140..285, y ~ 70..280
# 大: 横 near y=140, 撇 and 捺 crossing at ~ (210, 140)
# 丶 dot at upper-right ~ (255, 95)

# Stroke 1 (大's 一/横): from left to right across top of 大
da_h = bez((150, 138), (185, 133), (225, 133), (275, 138), n=50)
stroke(da_h, (6, 7))

# Stroke 2 (大's 撇): starts near top-center, sweeps down-left with bow
da_pie = bez((210, 100), (200, 155), (180, 210), (150, 275), n=80)
stroke(da_pie, (10, 4))
# shoulder dab at 撇 root
dab(210, 100, 4)

# Stroke 3 (大's 捺): starts near apex, sweeps down-right with belly + foot
da_na = bez((215, 145), (235, 190), (255, 230), (280, 265), n=80)
stroke(da_na, (5, 12))
foot = bez((280, 265), (283, 268), (285, 271), (287, 273), n=15)
stroke(foot, (12, 4))

# Stroke 4 (丶 dot at upper-right of 犬)
dot = bez((248, 88), (253, 95), (258, 103), (263, 112), n=25)
stroke(dot, (4, 9))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0434_畎/01_畎.png")
