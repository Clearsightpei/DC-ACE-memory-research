"""
Render 侶 (lv3) at 300x300, black ink on white.

Structural read from GT:
  Left:  亻 (person radical) — 撇 (top-left sweep) + 竖 (tall vertical from
         mid-撇 down). Occupies roughly the left 1/3, tall.
  Right: 呂 — two 口 boxes stacked vertically with a small tick between them.
         Upper box a bit smaller, lower box a bit wider. Occupies right 2/3.

Applying calligraphic 4-move:
  1. Teardrop taper on 撇/点.
  2. Shoulder dab at every 折 corner (both boxes: top-right corners).
  3. Bezier for the 撇 sweep.
  4. No hook here (no 钩 strokes in 侶).
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

# =========================================================
# LEFT: 亻 (person radical)
# =========================================================
# 撇 — starts top ~ (95,55), sweeps down-left with taper thin→thin (bowed)
pie = bez((95, 55), (80, 110), (60, 155), (40, 205), n=80)
stroke(pie, (10, 4))

# 竖 — vertical from mid-撇 down; starts around (80, 110) goes to (80, 265)
vert = bez((80, 115), (80, 165), (80, 215), (80, 265), n=60)
stroke(vert, (8, 8))

# =========================================================
# RIGHT: 呂 — upper 口, tiny 丿 connector, lower 口
# =========================================================

# ---- UPPER 口 ---- (roughly x=140..225, y=55..130)
UX1, UY1, UX2, UY2 = 140, 55, 225, 130
# Left vertical (竖)
lv = bez((UX1, UY1+4), (UX1, UY1+30), (UX1, UY1+55), (UX1, UY2), n=40)
stroke(lv, (7, 7))
# Top horizontal + right-turn (横折) as one continuous stroke:
#   top from (UX1, UY1) to (UX2, UY1), then down to (UX2, UY2)
top_h = bez((UX1-2, UY1), (UX1+25, UY1-1), (UX2-25, UY1-1), (UX2, UY1), n=50)
stroke(top_h, (7, 8))
# shoulder dab at top-right corner
dab(UX2, UY1, 5.5)
right_v = bez((UX2, UY1), (UX2, UY1+30), (UX2, UY1+55), (UX2, UY2), n=40)
stroke(right_v, (8, 7))
# Bottom horizontal (closes the box)
bot_h = bez((UX1, UY2), (UX1+25, UY2+1), (UX2-25, UY2+1), (UX2, UY2), n=50)
stroke(bot_h, (7, 7))

# ---- tiny connector 丿 between the two boxes ----
conn = bez((190, 133), (188, 140), (185, 148), (180, 155), n=25)
stroke(conn, (6, 3))

# ---- LOWER 口 ---- (roughly x=135..235, y=170..255)
LX1, LY1, LX2, LY2 = 135, 170, 235, 255
lv2 = bez((LX1, LY1+4), (LX1, LY1+30), (LX1, LY1+55), (LX1, LY2), n=40)
stroke(lv2, (7, 7))
top_h2 = bez((LX1-2, LY1), (LX1+30, LY1-1), (LX2-30, LY1-1), (LX2, LY1), n=50)
stroke(top_h2, (7, 8))
# shoulder dab at top-right corner of lower box
dab(LX2, LY1, 5.5)
right_v2 = bez((LX2, LY1), (LX2, LY1+30), (LX2, LY1+55), (LX2, LY2), n=40)
stroke(right_v2, (8, 7))
bot_h2 = bez((LX1, LY2), (LX1+30, LY2+1), (LX2-30, LY2+1), (LX2, LY2), n=50)
stroke(bot_h2, (7, 7))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0470_侶/01_侶.png")
