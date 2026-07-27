"""
他 = 亻 (left) + 也 (right)  — 5 strokes total

Composition (300x300):
 亻: left column, x ~40..115, y ~55..255
   Stroke 1: 撇 — steep left-position flick
   Stroke 2: 竖 — straight vertical drop, meets pie body
 也: right column, x ~120..270, y ~85..255
   Stroke 3: 横折钩 — top horizontal + right vertical wall + tiny bottom flick
   Stroke 4: middle 竖 — pierces the top-lid
   Stroke 5: 竖弯钩 — big belly sweep, arcs across bottom, hook UP-LEFT at right

Hook flicks (per memory_index TIER-0 B):
 - 横折钩 terminal (bottom-left of stroke 3): UP-and-LEFT (~-115°)
 - 竖弯钩 terminal (right end of stroke 5): UP-and-LEFT (~-105°)
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def brush_stroke(points, widths):
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        w0, w1 = widths[i], widths[i + 1]
        dx, dy = x1 - x0, y1 - y0
        seg = max(abs(dx), abs(dy))
        steps = max(int(seg) * 2, 8)
        for s in range(steps + 1):
            t = s / steps
            x = x0 + dx * t
            y = y0 + dy * t
            r = w0 * (1 - t) + w1 * t
            d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line(x1, y1, x2, y2, width=7):
    d.line([(x1, y1), (x2, y2)], fill="black", width=width)


def dab(x, y, r=4):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def bezier(p0, p1, p2, width=7, n=80):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    for a, b in zip(pts[:-1], pts[1:]):
        d.line([a, b], fill="black", width=width)


# ---------------- 亻 (left) ----------------
# Stroke 1: 撇 — steep left-position flick
pie_points = [
    (110, 55),
    (100, 85),
    (85, 115),
    (68, 150),
    (52, 185),
    (38, 220),
]
pie_widths = [5.0, 5.0, 4.5, 4.0, 3.0, 1.6]
brush_stroke(pie_points, pie_widths)

# Stroke 2: 竖 (vertical drop) — meets pie body around x=90, y=115
shu_points = [(90, 118), (90, 170), (90, 220), (90, 265)]
shu_widths = [5.5, 5.5, 5.5, 5.0]
brush_stroke(shu_points, shu_widths)
dab(88, 116, r=4)


# ---------------- 也 (right) ----------------
# Stroke 3: 横折钩 — top lid + right vertical + tiny bottom-left flick
dab(140, 120, r=5)
line(140, 120, 258, 115, width=7)          # top horizontal
dab(258, 115, r=6)                          # shoulder
line(258, 115, 265, 260, width=7)          # right vertical drop
# terminal hook (up-left flick) at bottom of right wall
angle = math.radians(-120)
hx = 265 + 18 * math.cos(angle)
hy = 260 + 18 * math.sin(angle)
line(265, 260, hx, hy, width=6)

# Stroke 4: middle 竖 — pierces the top lid, drops well down
dab(195, 75, r=4)
line(195, 75, 195, 210, width=7)

# Stroke 5: 竖弯钩 — signature belly
# Phase A: start upper-left, sweep down-left
dab(145, 145, r=4)
bezier((145, 145), (128, 195), (125, 240), width=7)
# Phase B: bottom curl right along baseline
bezier((125, 240), (200, 280), (275, 250), width=7)
# Phase C: terminal hook UP-and-LEFT
angle2 = math.radians(-110)
hx2 = 275 + 24 * math.cos(angle2)
hy2 = 250 + 24 * math.sin(angle2)
line(275, 250, hx2, hy2, width=6)


img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0154_他/01_他.png"
)
print("saved 01_他.png")
