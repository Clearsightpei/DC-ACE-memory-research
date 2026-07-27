"""Render radical 攴 (pu) — retry #1.

Errata diagnosis of retry_0: "conflated the two halves". Fix per errata:
  - Top = 卜 (short 竖 + a small 点/短横 to the right at MID-height,
    not touching the vertical).
  - Bottom = 又 (横撇 as ONE compound stroke: short 横 then bends into
    a 撇 sweeping down-left) + 捺 (crossing the 撇 forming 又).

Prior retry_0 error: bottom was drawn as raw 撇 + 捺 X-cross with
separate origins in the middle. The canonical bottom 又 has stroke 3
(横撇) START as a short horizontal at the upper-left of the bottom
half, then bend into a 撇 going down-left. Stroke 4 (捺) starts near
the 横撇's shoulder-joint area and sweeps down-right through the 撇.

GT observed silhouette: top-vertical short and left-of-center; small
horizontal FLICK to its right; big lower X made of one 横撇-with-bend
and a broad-footed 捺.
"""

from PIL import Image, ImageDraw
import math
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(p0, p1, r0, r1, steps=None):
    x0, y0 = p0
    x1, y1 = p1
    dist = math.hypot(x1 - x0, y1 - y0)
    if steps is None:
        steps = max(80, int(dist * 4))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=240):
    x0, y0 = p0
    xc, yc = p1
    x1, y1 = p2
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * x0 + 2 * u * t * xc + t * t * x1
        y = u * u * y0 + 2 * u * t * yc + t * t * y1
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# =================================================================
# TOP HALF — 卜 shape
# =================================================================

# Stroke 1: short 竖 (the vertical of 卜) — left-of-center, upper region.
# GT shows this vertical is somewhat left of the character's center and
# short (about y=55 to y=125).
v_top = (130, 55)
v_bot = (130, 125)
dab(*v_top, 6)        # 顿 dab at top
line_dabs(v_top, v_bot, 5, 5)
dab(*v_bot, 5)

# Stroke 2: the 点 of 卜 — rendered here as a short 横-flick angled
# slightly downward, sitting at MID-height of the vertical (roughly
# y=85), STARTING to the right of the vertical with a small gap
# (~15 px) so it does NOT touch. GT shows this as a compact rightward
# tick with a small taper.
p_left = (150, 82)
p_right = (195, 90)
dab(*p_left, 5)
line_dabs(p_left, p_right, 5, 3)
dab(*p_right, 3)

# =================================================================
# BOTTOM HALF — 又 shape (横撇 + 捺)
# =================================================================

# Stroke 3: 横撇 — starts as a SHORT horizontal at upper-left of the
# bottom half, then bends at a shoulder-joint into a 撇 sweeping
# down-and-left with thick→thin taper.
#
# The horizontal segment is short (~40 px) then the 撇 body is long
# (~180 px). Drawn as two segments joined at the shoulder.

# Segment 3a: 横 (going right) — wider so the 又 has room to be an X.
h1_start = (75, 155)
h1_end = (155, 158)
dab(*h1_start, 6)     # 顿 dab at start
line_dabs(h1_start, h1_end, 5, 6)
# joining dab at shoulder — SAME radius as segment
shoulder = h1_end
dab(*shoulder, 6)

# Segment 3b: 撇 sweeping down-left from shoulder — steeper angle so
# the crossing with 捺 happens in the mid-bottom.
pie_ctrl = (115, 215)
pie_end = (55, 280)
bezier_dabs(shoulder, pie_ctrl, pie_end, 6, 1.5)

# Stroke 4: 捺 — start near the shoulder-joint area of the 横撇 (top
# of the X), sweep down-right with thin→thick taper ending in broad
# flat foot. Must CROSS the 撇 mid-body forming a clean X.
na_start = (140, 165)
na_ctrl = (210, 235)
na_end = (270, 275)
bezier_dabs(na_start, na_ctrl, na_end, 2.5, 9)
# broad terminal foot — extend slightly rightward flat
dab(*na_end, 9)
line_dabs(na_end, (280, 273), 9, 5)

out = os.path.join(os.path.dirname(__file__), "01_攴.png")
img.save(out)
print("Saved:", out)
