"""
Render 畚 (ben3) at 300x300.

Structural read from GT:
  Top:    龹 element — looks like an inverted 大 with an extra small
          hook-cap at top-right and a right-side horizontal flare.
          Composed as: 撇 (down-left), 捺 (down-right with foot),
          one short 横 across the middle, small top-right cap.
  Bottom: 田 — square with internal cross.

Uses the calligraphic-weight 4-move recipe from memory_index tier-0 F:
tapered strokes, shoulder dabs at 折 joints, bezier curves for 撇/捺.
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

def line_seg(p0, p1, w):
    stroke(bez(p0, (p0[0]+(p1[0]-p0[0])/3, p0[1]+(p1[1]-p0[1])/3),
              (p0[0]+2*(p1[0]-p0[0])/3, p0[1]+2*(p1[1]-p0[1])/3), p1, n=40), w)

def shoulder(x, y, r=6):
    d.ellipse((x-r, y-r, x+r, y+r), fill="black")

# ================== TOP: 龹 (spans y~20-160) ==================
# main 撇: from top-center down-left
pie = bez((150, 25), (135, 65), (110, 105), (75, 145), n=80)
stroke(pie, (10, 4))

# main 捺: from top-center down-right, S-curve with foot
na = bez((150, 40), (175, 80), (200, 115), (230, 145), n=80)
stroke(na, (4, 12))
foot = bez((230, 145), (238, 148), (245, 150), (250, 152), n=15)
stroke(foot, (12, 3))

# small top cap (short 撇 or 点 at very top center-right - the little hook)
cap = bez((162, 20), (168, 28), (172, 38), (170, 48), n=25)
stroke(cap, (5, 3))

# middle 横 across the top element (~y=95, spans width)
h_mid = bez((80, 95), (120, 92), (170, 92), (220, 96), n=40)
stroke(h_mid, (6, 6))

# right-side flare/横折 - the little hook on right (~y=125-155)
# short 横 going right with a downward折
hr = bez((165, 130), (195, 128), (225, 128), (250, 132), n=40)
stroke(hr, (5, 5))
shoulder(250, 132, 4)
# small downward flick
hr_flick = bez((250, 132), (252, 138), (253, 145), (252, 152), n=20)
stroke(hr_flick, (5, 3))

# ================== BOTTOM: 田 (y~160-285) — touching 龹 above ==================
TOP_Y = 162  # tucked up so 田's top overlaps 龹's descending strokes
BOT_Y = 285
LX = 108
RX = 222
MX = 165

# Left 竖
left_v = bez((LX, TOP_Y), (LX, 200), (LX, 245), (LX, BOT_Y), n=50)
stroke(left_v, (7, 7))

# Top 横 with 折 down = right 竖 (横折)
top_h = bez((LX, TOP_Y+2), (140, TOP_Y), (180, TOP_Y), (RX, TOP_Y+2), n=40)
stroke(top_h, (6, 6))
shoulder(RX, TOP_Y+2, 5)
right_v = bez((RX, TOP_Y+2), (RX, 210), (RX, 245), (RX, BOT_Y), n=50)
stroke(right_v, (7, 7))

# Middle 横 (inside 田)
mid_h = bez((LX+2, 223), (140, 222), (180, 222), (RX-2, 223), n=40)
stroke(mid_h, (5, 5))

# Middle 竖 (inside 田)
mid_v = bez((MX, TOP_Y+3), (MX, 200), (MX, 245), (MX, BOT_Y-2), n=50)
stroke(mid_v, (5, 5))

# Bottom 横 (closes 田)
bot_h = bez((LX, BOT_Y), (140, BOT_Y), (180, BOT_Y), (RX, BOT_Y), n=40)
stroke(bot_h, (6, 6))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0502_畚/01_畚.png")
