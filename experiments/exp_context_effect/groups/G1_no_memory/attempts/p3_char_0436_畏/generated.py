"""G1 render of 畏 (fear) — revision.
Top: 田 box with cross, positioned upper-center.
Below the 田: a long horizontal, then piě on left and long 捺 on right,
with a short vertical dropping from the 田 center.
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=6):
    d.line(pts, fill="black", width=width)

def stroke(points, base=6, taper=0):
    for i in range(len(points)-1):
        w = base + int(taper * (i / max(1, len(points)-1)))
        d.line([points[i], points[i+1]], fill="black", width=w)

# ---- Top: 田 box ----
# Box: x 100..200, y 40..135
# outer left vertical (drawn first)
line([(103, 40), (103, 135)], 6)
# top horizontal
line([(100, 42), (203, 45)], 6)
# right vertical (slight inward slope)
line([(200, 45), (197, 135)], 6)
# bottom horizontal (closes box)
line([(103, 135), (200, 135)], 6)
# inner horizontal
line([(105, 88), (198, 90)], 6)
# inner vertical
line([(150, 45), (150, 135)], 6)

# ---- Middle long horizontal (below 田) ----
line([(55, 168), (250, 172)], 7)

# ---- Short vertical dropping from 田 center to horizontal ----
# (connects 田's bottom center to base region — subtle)
# skipped: the horizontal already touches near bottom of 田

# ---- Left piě: from about (140, 145) curving down-left ----
pts = []
for t in range(0, 25):
    u = t / 24
    x = 140 - 55 * u
    y = 145 + 105 * u + 12 * math.sin(math.pi * u)
    pts.append((x, y))
stroke(pts, base=6)

# Small vertical/hook near left piě upper (short stroke like 衣's dot area)
line([(148, 148), (146, 178)], 5)

# ---- Right long 捺 (falling diagonal) from about (150, 175) to (275, 265) ----
pts2 = []
for t in range(0, 35):
    u = t / 34
    x = 150 + 125 * u
    # slight downward curve
    y = 175 + 92 * u + 6 * math.sin(math.pi * u)
    pts2.append((x, y))
stroke(pts2, base=5, taper=4)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0436_畏/01_畏.png")
print("saved")
