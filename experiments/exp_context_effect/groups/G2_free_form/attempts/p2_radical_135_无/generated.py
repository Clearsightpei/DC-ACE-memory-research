"""Render 无 (4-stroke radical) to a 300x300 PNG.

Stroke analysis from GT:
  1) top 横 — short, ~x=110→200, y~85, slight up-tilt
  2) middle 横 — long, ~x=55→235, y~150, slight up-tilt, dabs both ends
  3) 撇 — long diagonal from upper right area (~x=175,y=110) sweeping
     down-left through the middle 横, ending near (~x=70,y=255)
  4) 竖弯钩 — starts at ~x=170,y=155 (just below middle heng, right of
     center), drops down as a vertical/slight left-bow, then curves
     right to form a rightward foot, ending ~x=225,y=255
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("L", (W, H), 255)
draw = ImageDraw.Draw(img)


def dab(cx, cy, r):
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=0)


def tapered_line(p0, p1, w0, w1, steps=60):
    """Draw a line from p0 to p1 with tapered width."""
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        w = w0 + (w1 - w0) * t
        r = w / 2
        draw.ellipse((x - r, y - r, x + r, y + r), fill=0)


def tapered_curve(points, widths, steps_per=30):
    """Sample a poly-line with a width per vertex, taper linearly between."""
    for i in range(len(points) - 1):
        tapered_line(points[i], points[i + 1], widths[i], widths[i + 1], steps=steps_per)


# --- Stroke 1: top short 横 ---
# start dab, taper across, end dab
tapered_line((112, 88), (198, 82), 7, 6)
dab(112, 88, 4)
dab(198, 82, 5)  # small terminal press

# --- Stroke 2: middle long 横 ---
# long, slight up-tilt
tapered_line((55, 155), (238, 148), 6, 7)
dab(55, 155, 4)
dab(238, 148, 6)  # terminal press

# --- Stroke 3: long 撇 crossing through middle 横 ---
# starts upper-right area above the second heng, sweeps down-left,
# gentle rightward bow (i.e. the middle of the stroke is a hair to the
# right of the straight line between endpoints)
pie_points = [
    (185, 95),    # start (upper right, above middle heng)
    (168, 135),
    (140, 175),
    (108, 215),
    (65, 262),    # end lower-left, past canvas center-left
]
pie_widths = [8, 7, 6, 5, 3]  # thick to thin taper
tapered_curve(pie_points, pie_widths, steps_per=25)
dab(185, 95, 5)  # 顿 dab at start

# --- Stroke 4: 竖弯钩 (vertical-then-curve-right with hook) ---
# starts just below middle heng, right of center; goes down slightly
# leftward bow, then curves right into a horizontal foot ending in a
# small upward hook
# vertical segment
shu_points = [
    (175, 158),   # start (just below middle heng, right of center)
    (170, 200),
    (170, 232),
    (183, 255),   # begin the curve
    (210, 265),
    (238, 262),   # foot end (further right)
]
shu_widths = [7, 7, 7, 7, 7, 6]
tapered_curve(shu_points, shu_widths, steps_per=25)
dab(175, 158, 5)  # start dab
# small hook flick at the end (up)
tapered_line((238, 262), (245, 245), 7, 2, steps=20)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_135_无/01_无.png"
)
print("saved 无 PNG 300x300")
