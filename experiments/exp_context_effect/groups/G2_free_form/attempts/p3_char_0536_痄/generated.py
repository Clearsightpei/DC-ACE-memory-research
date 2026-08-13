"""
Render 痄 (zha4) at 300x300, black ink on white.

Structural read from GT:
  疒 radical (wraps top+left):
    - 点   : small dot at top-center
    - 横   : long horizontal, slopes slightly up-right
    - 撇   : long enclosing 撇 from top-right down to bottom-left
    - 冫   : two interior tick strokes on the left side
  乍 (sits inside, bottom-right pocket of 疒), 5 strokes:
    - 撇   : short pie flick at top-left of 乍
    - 横   : short horizontal from 撇 shoulder going right
    - 竖   : vertical drop from right end of top 横
    - 横   : middle short horizontal (on left of 竖)
    - 横   : bottom horizontal (base) crossing the 竖

Applies TIER-0 F 4-move: Bezier curves everywhere, teardrop tapers,
shoulder dab at every 折 joint, no straight-line strokes.
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


def dab(cx, cy, r):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")


# --- 疒 radical ---

# 点 top dot: small teardrop sloping down-right
dot_top = bez((150, 30), (155, 36), (160, 44), (164, 52), n=25)
stroke(dot_top, (3, 7))

# 横 top horizontal
heng = bez((105, 68), (150, 62), (200, 58), (238, 55), n=60)
stroke(heng, (6, 6))

# 撇 long enclosing sweep from right end of 横 down to bottom-left
pie_big = bez((238, 62), (200, 130), (140, 200), (58, 280), n=100)
stroke(pie_big, (10, 4))
dab(238, 60, 6)  # shoulder dab where 横 meets 撇

# 冫 two interior ticks on left side of 疒
tick1 = bez((118, 118), (110, 128), (102, 138), (95, 148), n=25)
stroke(tick1, (7, 3))
tick2 = bez((100, 170), (92, 182), (85, 195), (78, 208), n=25)
stroke(tick2, (7, 3))

# --- 乍 inside, sits in the bottom-right pocket of 疒 ---
# body region roughly x=140..250, y=110..250

# stroke 1: 撇 short pie flick at top-left of body
za_pie = bez((170, 105), (163, 120), (157, 138), (152, 158), n=40)
stroke(za_pie, (7, 3))

# stroke 2: 横 top horizontal
za_top_h = bez((168, 118), (188, 116), (208, 116), (226, 118), n=40)
stroke(za_top_h, (5, 5))
dab(226, 118, 5)  # shoulder dab

# stroke 3: 竖 vertical drop from right end of top 横
za_shu = bez((222, 120), (220, 155), (218, 190), (216, 225), n=60)
stroke(za_shu, (7, 7))

# stroke 4: 横 middle short horizontal (left of 竖, midpoint)
za_mid_h = bez((165, 168), (185, 167), (205, 167), (220, 168), n=40)
stroke(za_mid_h, (5, 5))

# stroke 5: 横 bottom horizontal (base) - short, stays inside 撇
za_bot_h = bez((160, 218), (185, 217), (210, 217), (232, 218), n=50)
stroke(za_bot_h, (5, 6))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0536_痄/01_痄.png")
