"""
原 (yuán) — 10 strokes. Compound: 厂 canopy over inside (白 + 小).

Stroke breakdown:
  厂 (2):  1. 一 top horizontal (right-going, slight up-tilt)
           2. 丿 left sweep (long, belly-right / concave-left, taper thick→thin)
  白 (5):  3. 丿 short flick on top of 白
           4. 丨 left vertical of 白 box
           5. 横折 top-horiz+right-down
           6. 一 middle horizontal inside box
           7. 一 bottom horizontal closing box
  小 (3):  8. 亅 center 竖钩 — UP-LEFT flick per index tier-0 rule B
           9. 丿 left dot/flick of 小
          10. 丶 right dot of 小

Layout (300x300):
  厂 corner at (52, 55). 一 stretches to (275, 50). 丿 sweeps to (44, 275).
  Inside components tucked INSIDE the 厂 canopy (per Tier-0 H: touch/overlap):
    白 box: x=100..205, y=85..180
    白 top-撇: from (155, 65) down to (110, 90)
    小: y=190..258, center around x=155
"""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def bez3(p0, p1, p2, p3, n=60):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u*u*u*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t*t*t*p3[0]
        y = u*u*u*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t*t*t*p3[1]
        pts.append((x, y))
    return pts


def bez2(p0, p1, p2, n=50):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u*u*p0[0] + 2*u*t*p1[0] + t*t*p2[0]
        y = u*u*p0[1] + 2*u*t*p1[1] + t*t*p2[1]
        pts.append((x, y))
    return pts


def stroke(pts, widths):
    """Variable-width stroke via overlapping ellipses."""
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


# =========================================================
# 厂 canopy — 2 strokes sharing top-left corner (52, 55)
# =========================================================
CORNER = (52, 55)

# shoulder dab at the shared corner (顿笔)
dab(CORNER[0], CORNER[1], 5.5)

# Stroke 1: 一 top horizontal, slight up-tilt, tapers slightly
h_top = bez2((52, 55), (160, 52), (275, 50), n=80)
stroke(h_top, (9, 6))
# terminal blunt press on right
dab(275, 50, 4.5)

# Stroke 2: 丿 long left sweep, belly RIGHT, concave LEFT, thick→thin taper
pie_pts = bez3((52, 55), (75, 130), (60, 200), (44, 275), n=100)
stroke(pie_pts, (10, 2))

# =========================================================
# 白 (inside upper) — 5 strokes, tucked under canopy
# =========================================================
L, R = 105, 200
T, B = 100, 180

# Stroke 3: short 丿 on top of 白 — start well above box, land at box top-left
top_pie = bez3((155, 68), (140, 78), (125, 88), (108, 100), n=50)
stroke(top_pie, (8, 2))

# Stroke 4: 竖 left vertical of box
stroke([(L, y) for y in range(T + 1, B + 1)], (6, 6))

# Stroke 5: 横折 (top horizontal, then down as right vertical)
# top horiz
stroke([(x, T) for x in range(L - 2, R + 1)], (6, 6))
# corner shoulder dab (顿 at 折)
dab(R, T, 4.5)
# right down
stroke([(R, y) for y in range(T + 1, B + 1)], (6, 6))

# Stroke 6: 一 middle horizontal inside box
MID_Y = T + (B - T) // 2 + 2
stroke([(x, MID_Y) for x in range(L + 4, R - 2)], (5, 5))

# Stroke 7: 一 bottom horizontal closing box
stroke([(x, B) for x in range(L - 2, R + 3)], (6, 6))

# =========================================================
# 小 (bottom) — 3 strokes, center under 白
# =========================================================
# Stroke 8: 竖钩 center — UP-and-LEFT hook flick (TIER-0 B)
sg_body = [(153, y) for y in range(190, 255)]
stroke(sg_body, (7, 7))
# hook flick UP-and-LEFT (angle ~ -110°)
hook = bez2((153, 254), (147, 249), (140, 243), n=25)
stroke(hook, (7, 3))

# Stroke 9: 左点/撇 of 小 — flick down-left
left_flick = bez3((132, 202), (124, 222), (117, 242), (110, 262), n=50)
stroke(left_flick, (7, 2))

# Stroke 10: 右点 of 小
right_dot = bez3((178, 205), (192, 222), (204, 240), (215, 260), n=50)
stroke(right_dot, (3, 8))


# =========================================================
here = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(here, "01_原.png")
img.save(out)
print(f"saved {out}")
