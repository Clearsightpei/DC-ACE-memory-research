"""
Render 信 (xin4) at 300x300, black ink on white.

Structure: 亻 (left, ~1/3 width) + 言 (right, ~2/3 width).
  Left 亻: short 撇 down-left from top + long 竖 through the body.
  Right 言:
    - 点 at top (short down-right dot)
    - long 横 (spans right side)
    - two short 横s (stacked, indented)
    - 口 at bottom (small rectangle)

Applying TIER-0.F 4-move recipe (compound char, 亻 prefix):
  - tapered strokes via stroke(pts, widths) helper
  - Bezier for 撇 and 点
  - shoulder dab at 口 corners
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


# --- 亻 (left radical, ~x=40..90) ---
# 撇: from top-right of radical, curving down-left, meeting 竖 near its top
pie = bez((78, 60), (70, 95), (55, 120), (38, 145), n=60)
stroke(pie, (10, 4))
# 竖: long vertical, starts where 撇 originates (joint), ends around y=260
shu = bez((78, 105), (78, 165), (78, 215), (78, 260), n=60)
stroke(shu, (7, 7))

# --- 言 (right, ~x=110..270) ---

# 点 at top (short down-right dot)
dian = bez((175, 40), (180, 48), (185, 55), (190, 62), n=30)
stroke(dian, (4, 10))

# long 横 (spans right side)
h_long = bez((115, 85), (155, 82), (225, 82), (270, 86), n=50)
stroke(h_long, (8, 8))

# short 横 upper
h_up = bez((140, 125), (170, 123), (220, 123), (250, 126), n=40)
stroke(h_up, (6, 6))

# short 横 lower
h_lo = bez((140, 165), (170, 163), (220, 163), (250, 166), n=40)
stroke(h_lo, (6, 6))

# 口 at bottom (rectangle box, ~x=140..255, y=200..270)
# left 竖
kl = bez((140, 205), (140, 225), (140, 250), (140, 272), n=40)
stroke(kl, (6, 6))
# top 横折 shoulder: top-horizontal then right-竖
kt = bez((140, 205), (180, 203), (225, 203), (255, 208), n=40)
stroke(kt, (6, 6))
dab(255, 208, r=5)  # shoulder dab at 折 corner
kr = bez((255, 208), (255, 230), (255, 252), (255, 272), n=40)
stroke(kr, (6, 6))
# bottom 横
kb = bez((140, 272), (180, 270), (225, 270), (255, 272), n=40)
stroke(kb, (6, 6))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0447_信/01_信.png")
