"""
俾 = 亻 (left) + 卑 (right)  — ~10 strokes total

亻 (left column, x~40..115, y~55..255):
  1. 撇 — steep left-position flick (short)
  2. 竖 — straight vertical, meets 撇 body

卑 (right, x~120..280):
  Top: short 撇 sloping down-left (over the 田-ish top)
  Middle box (like 白): left 竖, top 横折, internal short 横 (dot-like),
    bottom 横 closing box.
  Bottom-wide: long 横 across full width of the right side.
  Through-stroke: long 竖 piercing vertically from the box's top through
    the bottom horizontal all the way down.

Hook flick note: 卑 has NO 钩 — the through 竖 ends straight down.

# SIGNATURE CHECK (H): 亻 竖 must touch/overlap right component; no white gap.
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


# ---------------- 亻 (left) ----------------
# Stroke 1: 撇 — steep left-position flick, teardrop taper
pie_points = [
    (105, 55),
    (95, 85),
    (82, 115),
    (65, 150),
    (48, 185),
    (35, 220),
]
pie_widths = [5.0, 5.0, 4.5, 4.0, 3.0, 1.6]
brush_stroke(pie_points, pie_widths)

# Stroke 2: 竖 (vertical drop), touches 撇 body at ~ (85, 115)
shu_points = [(85, 118), (85, 170), (85, 220), (85, 260)]
shu_widths = [5.5, 5.5, 5.5, 5.0]
brush_stroke(shu_points, shu_widths)
dab(83, 116, r=4)


# ---------------- 卑 (right) ----------------
# The right-side layout: box top ~y=70..170, bottom-wide ~y=200, through-竖 to y=275.

# Stroke 3: top 撇 — longer slanting flick over the box; starts upper-right, ends at box top-left area
top_pie = [(215, 55), (195, 68), (170, 82), (150, 95)]
top_pie_w = [5.0, 4.5, 3.5, 1.8]
brush_stroke(top_pie, top_pie_w)

# Stroke 4: left 竖 of the box
line(155, 92, 155, 175, width=6)

# Stroke 5: 横折 (top-horizontal + right-vertical of box)
line(155, 92, 245, 92, width=7)      # top 横
line(245, 92, 245, 175, width=7)     # right vertical (short 折)

# Stroke 6: middle short 横 inside box (the little bar in 白/甶)
line(160, 135, 240, 135, width=6)

# Stroke 7: bottom 横 closing the box
line(155, 172, 245, 172, width=6)

# Stroke 8: long 横 across the whole width of right side (卑's signature wide baseline)
line(125, 210, 275, 210, width=7)

# Stroke 9: long 竖 piercing vertically from top of box through the wide 横 to bottom
# This is 卑's signature through-stroke.
brush_stroke(
    [(200, 78), (200, 135), (200, 175), (200, 210), (200, 275)],
    [5.0, 6.0, 6.0, 6.0, 5.0],
)


img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0562_俾/01_俾.png"
)
print("saved 01_俾.png")
