"""
Render 畏 (wei4) at 300x300, black ink on white.

Structural read from GT:
  Top:    a 田-like rectangular grid (roughly upper 55%), containing
          two internal horizontals and a central vertical.
  Middle: a wide horizontal that extends past the rectangle base.
  Bottom: a long 撇 sweeping down-left from under the rectangle center,
          and a 捺 sweeping down-right from near the same origin.
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

def shoulder(x, y, r=6):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")

# --- Top 田/rectangle body (upper ~55%) ---
# 1. left 竖 (down the left side of rectangle)
s1 = bez((95, 45), (95, 85), (95, 125), (95, 160), n=50)
stroke(s1, (7, 7))

# 2. 横折 top+right (top edge then down the right)
top_h = bez((95, 45), (140, 43), (185, 43), (215, 46), n=60)
stroke(top_h, (6, 7))
shoulder(215, 46, r=5)
right_v = bez((215, 46), (215, 85), (215, 125), (212, 160), n=50)
stroke(right_v, (7, 6))

# 3. middle horizontal (inside)
mid_h1 = bez((95, 88), (140, 87), (180, 87), (213, 88), n=40)
stroke(mid_h1, (5, 5))

# 4. central 竖 inside the rectangle
mid_v = bez((153, 46), (153, 85), (153, 125), (153, 160), n=50)
stroke(mid_v, (6, 6))

# 5. second interior horizontal
mid_h2 = bez((95, 128), (140, 127), (180, 127), (213, 128), n=40)
stroke(mid_h2, (5, 5))

# 6. bottom of rectangle (short)
bot_rect = bez((95, 160), (140, 159), (180, 159), (212, 160), n=40)
stroke(bot_rect, (6, 6))

# --- Middle wide horizontal (extends past rectangle) ---
# 7. long 横 near y=185
wide_h = bez((55, 188), (130, 184), (200, 184), (250, 190), n=80)
stroke(wide_h, (7, 7))

# --- Bottom 撇 and 捺 ---
# 8. 撇 sweeping down-left from center-upper
pie = bez((140, 190), (128, 218), (108, 245), (65, 280), n=80)
stroke(pie, (10, 3))

# 9. 捺 with S-curve sweeping down-right
na = bez((155, 205), (180, 235), (215, 260), (255, 275), n=80)
stroke(na, (4, 12))
# foot flare at the end
foot = bez((255, 275), (262, 277), (268, 278), (272, 278), n=20)
stroke(foot, (12, 3))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0436_畏/01_畏.png")
