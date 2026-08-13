"""
Render 皈 (gui1) at 300x300, black ink on white.

Structure: left-right compound.
  Left:  白 (~40% width) — 5 strokes: short 撇, 竖 (left of box),
         横折 (top+right of box), middle 横, bottom 横.
  Right: 反 (~60% width) — 4 strokes: 横 (short top), 撇 (long
         sweeping down-left), 横撇 (small, top of 又), 捺 (long
         down-right foot).

Applies 4-move recipe: teardrop tapers, shoulder dabs at 折 joints,
bezier for curves, hooks flick UP-LEFT (n/a here — 反 has no hook).
"""
from PIL import Image, ImageDraw

W = H = 300
OUT = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0462_皈/01_皈.png"
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


# ============ 白 (left) ============
# Bounds roughly x: 40-125, y: 75-245.  Compact box, shorter than reach of 反.

# 1) short 撇 above the box — tiny diagonal flick down-left
p = bez((85, 60), (80, 68), (72, 76), (62, 88), n=30)
stroke(p, (6, 2))

# 2) 竖 — left vertical of the box
sv = bez((50, 92), (50, 140), (50, 195), (50, 242), n=50)
stroke(sv, (7, 7))

# 3) 横折 — top horizontal then down for right side
h_top = bez((50, 92), (75, 89), (100, 89), (118, 92), n=40)
stroke(h_top, (6, 7))
dab(118, 92, r=5)
v_right = bez((118, 92), (118, 140), (118, 195), (118, 242), n=50)
stroke(v_right, (7, 6))

# 4) middle 横
h_mid = bez((54, 165), (75, 163), (100, 163), (116, 165), n=30)
stroke(h_mid, (5, 5))

# 5) bottom 横 (closes the box)
h_bot = bez((50, 242), (75, 242), (100, 242), (118, 242), n=30)
stroke(h_bot, (6, 6))

# ============ 反 (right) ============
# Bounds roughly x: 145-285, y: 55-278.
# Stroke order: 撇 (long), 横 (top short flowing off the 撇 start),
#               横撇 (for 又), 捺.

# 1) 撇 (long) — starts near top around x=205, sweeps down-left to bottom-left
pie_long = bez((205, 60), (190, 130), (170, 200), (150, 278), n=90)
stroke(pie_long, (10, 3))

# 2) 横 — from the top of 撇 going right (top edge of 反)
h_r = bez((200, 65), (225, 63), (245, 63), (262, 66), n=40)
stroke(h_r, (6, 6))

# 3) 横撇 for 又 — small 横 turning into a short 撇 down-left, sits mid-height
h_yy = bez((185, 145), (210, 143), (232, 143), (248, 146), n=30)
stroke(h_yy, (5, 6))
dab(248, 146, r=5)
pie_yy = bez((248, 146), (238, 168), (222, 190), (202, 218), n=45)
stroke(pie_yy, (7, 3))

# 4) 捺 — long S-curve down-right from around the 又 joint
na = bez((218, 180), (235, 215), (255, 245), (278, 275), n=70)
stroke(na, (4, 12))
# foot flare at end of 捺
foot = bez((278, 275), (282, 276), (284, 277), (286, 278), n=15)
stroke(foot, (12, 3))

img.save(OUT)
print("saved", OUT)
