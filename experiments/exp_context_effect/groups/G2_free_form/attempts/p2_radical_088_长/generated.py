"""
Render 长 (radical, 4 strokes) at 300x300, PIL brush-dabs.
Revision 1: tune 撇 angle (more slanted), extend 竖提 vertical below 横,
extend 提 tail further right, reposition 捺 to start where horizontals cross.

Strokes:
  1) 撇 (short) at top: leaning down-left from the top area
  2) 横 (long horizontal): crosses through
  3) 竖提: short vertical above 横 tail piece extending BELOW 横, then 提 rises
  4) 捺: from the cross point, going down-right, thin->thick with broad foot

Image coords (y grows DOWN).
"""

from PIL import Image, ImageDraw
import math, os

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r_start, r_end, steps=None):
    if steps is None:
        steps = max(60, int(math.hypot(x1 - x0, y1 - y0) * 2.2))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r_start, r_end, steps=200, ease=1.0):
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        tt = t ** ease
        r = r_start + (r_end - r_start) * tt
        dab(x, y, r)


# ---------- Stroke 1: short 撇 at top ----------
# More slanted (upper-right → lower-left) — from about (165,60) to (115,120)
bezier_dabs((165, 62), (150, 90), (112, 122), r_start=6.5, r_end=1.5,
            steps=150, ease=1.0)
dab(165, 62, 7)

# ---------- Stroke 2: long 横 ----------
# Long horizontal with slight up-tilt, from (50,158) to (260,150)
line_dabs(50, 160, 260, 150, r_start=5.5, r_end=5.5, steps=280)
dab(50, 160, 7)
dab(260, 150, 7)

# ---------- Stroke 3: 竖提 ----------
# Vertical: from (115, 118) down through 横 to (115, 220)
line_dabs(115, 118, 115, 222, r_start=5.5, r_end=5.5, steps=230)
# joining shoulder dab at 提 origin
dab(115, 222, 7)
# 提 rises up-and-right, longer than before, to (215, 172)
line_dabs(115, 222, 215, 172, r_start=6.5, r_end=1.3, steps=220)

# ---------- Stroke 4: 捺 ----------
# Starts near where 撇 meets 横 (around 115, 150), sweeps to lower-right
# thin -> thick with broad flat foot
bezier_dabs((122, 148), (175, 200), (260, 250),
            r_start=2.5, r_end=9.5, steps=240, ease=1.35)
# broad terminal foot
dab(260, 250, 10)
# short flat extension after foot
line_dabs(260, 250, 275, 249, r_start=9.0, r_end=2.0, steps=45)


out_path = os.path.join(os.path.dirname(__file__), "01_长.png")
img.save(out_path)
print(f"wrote {out_path}")
