"""
Render 长 (radical, 4 strokes) at 300x300, PIL brush-dabs. Retry #2.

Prior attempt (retry_0) errors (curator diagnosis in errata):
  - 捺 didn't dominate; started too low; too crowded left side.
  - 提 tail went too horizontal / too far.
  - Overall silhouette too compact (should fill 250 px wide).

GT analysis (from gt/phase2/长.png):
  - Very SHORT 撇 near top, floating above the horizontal.
  - Long 横 as the primary horizontal.
  - 竖提: short vertical on LEFT side dropping from just below 横, then a
    diagonal 提 rises up-and-right from the vertical's bottom.
  - LONG 捺: starts from upper-center (just above the 横), sweeps far
    down-and-right past the right edge with broad foot. This is the
    DOMINANT stroke visually.

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


# ---------- Stroke 1: short 撇 near top-left ----------
# Small subtle tick above the 横 — much smaller than prior render
bezier_dabs((108, 78), (98, 92), (85, 108), r_start=4.5, r_end=1.0,
            steps=100, ease=1.0)
dab(108, 78, 5)

# ---------- Stroke 2: long 横 ----------
# Long horizontal spanning roughly x=45..245, slight up-tilt to the right
line_dabs(45, 138, 245, 128, r_start=5.5, r_end=5.5, steps=260)
dab(45, 138, 7)
dab(245, 128, 6)

# ---------- Stroke 3: 竖提 ----------
# 竖: extends from just below top down to near bottom on the LEFT
# Vertical at x≈85, from y≈108 down to y≈235 (long vertical!)
line_dabs(85, 108, 85, 235, r_start=5.5, r_end=5.5, steps=260)
# shoulder joining dab at the turn
dab(85, 235, 6)
# 提: rises up-and-right steeply (~45°), thick→thin
line_dabs(85, 235, 175, 175, r_start=6.5, r_end=1.0, steps=200)

# ---------- Stroke 4: 捺 (DOMINANT) ----------
# Starts from upper-middle just above the 横, sweeps DOWN-and-RIGHT past the
# right wall, thin→thick with broad terminal foot. This is the big stroke.
bezier_dabs((110, 105), (185, 175), (275, 245),
            r_start=2.0, r_end=10.0, steps=280, ease=1.35)
# broad terminal foot
dab(275, 245, 11)
# short flat foot extension
line_dabs(275, 245, 288, 244, r_start=10.0, r_end=2.0, steps=40)


out_path = os.path.join(os.path.dirname(__file__), "01_长.png")
img.save(out_path)
print(f"wrote {out_path}")
