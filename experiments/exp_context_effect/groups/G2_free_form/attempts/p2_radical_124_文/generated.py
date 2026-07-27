"""Render 文 (4-画 radical) — 300x300, PIL.

Structure of 文 (observed in GT):
  1. 点 top dot - small teardrop centered near top (~x=150 y=55).
  2. 横 - medium horizontal below the dot, slight up-tilt.
  3. 撇 - long diagonal from upper-right area sweeping down-left,
         starting from just above the middle-right of the 横 and
         crossing DOWN through/past the 横 into lower-left.
  4. 捺 - long diagonal from upper-left area sweeping down-right,
         starting from left side near the 横, crossing the 撇
         to form an X, ending in lower-right with broad foot.

Both 撇 and 捺 originate near the CENTER of the 横 area and splay
outward, meeting each other to form the characteristic X-cross of 文.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def stamp_taper(p0, p1, w_start, w_end, n=60):
    """Draw a tapered stroke by stamping circles of varying radius."""
    x0, y0 = p0
    x1, y1 = p1
    for i in range(n + 1):
        t = i / n
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = w_start + (w_end - w_start) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def stamp_curve(pts, widths, n=80):
    """Stamp along a piecewise linear path with per-segment width interpolation."""
    # Resample the polyline evenly
    total = 0.0
    lens = []
    for i in range(len(pts) - 1):
        dx = pts[i + 1][0] - pts[i][0]
        dy = pts[i + 1][1] - pts[i][1]
        seg = (dx * dx + dy * dy) ** 0.5
        lens.append(seg)
        total += seg
    for i in range(n + 1):
        t = i / n
        target = t * total
        # find segment
        acc = 0.0
        for j in range(len(lens)):
            if acc + lens[j] >= target or j == len(lens) - 1:
                seg_t = (target - acc) / lens[j] if lens[j] > 0 else 0
                x = pts[j][0] + (pts[j + 1][0] - pts[j][0]) * seg_t
                y = pts[j][1] + (pts[j + 1][1] - pts[j][1]) * seg_t
                w = widths[0] + (widths[1] - widths[0]) * t
                draw.ellipse((x - w, y - w, x + w, y + w), fill="black")
                break
            acc += lens[j]


# ---- Stroke 1: 点 (top dot) ----
# In 文 the top dot behaves like a short 撇-flick: starts upper-right,
# ends lower-left. Thin -> slightly thicker; short (~35 px).
stamp_taper((170, 55), (140, 82), w_start=2.0, w_end=4.0, n=30)

# ---- Stroke 2: 横 (horizontal across the middle-upper area) ----
# Medium length, slight up-tilt (right end a hair higher than left).
# Positioned so the X-cross below sits nicely.
stamp_curve(
    pts=[(75, 118), (150, 112), (225, 115)],
    widths=(4.5, 4.0),
    n=90,
)
# small 顿 dabs at endpoints
draw.ellipse((70, 114, 80, 122), fill="black")
draw.ellipse((222, 111, 232, 121), fill="black")

# ---- Stroke 3: 撇 (long diagonal, upper-right -> lower-left) ----
# Starts near the right-middle area just above/at the 横, sweeps down-left
# with gentle rightward bow, ending in lower-left.
# Start x ~ 175, y ~ 130 ; end x ~ 70, y ~ 260.
撇_pts = [
    (178, 128),
    (160, 155),
    (135, 190),
    (108, 225),
    (78, 258),
]
stamp_curve(撇_pts, widths=(5.5, 2.0), n=110)

# ---- Stroke 4: 捺 (long diagonal, upper-left -> lower-right) ----
# Starts near left-middle area just above/at the 横, sweeps down-right,
# CROSSES the 撇 around the center, ends in lower-right with broad foot.
# Start x ~ 115, y ~ 135 ; end x ~ 240, y ~ 255. Thin -> thick.
捺_pts = [
    (118, 135),
    (145, 170),
    (175, 205),
    (208, 235),
    (240, 255),
]
stamp_curve(捺_pts, widths=(2.5, 6.5), n=110)
# broad terminal foot on 捺
draw.ellipse((233, 250, 250, 264), fill="black")

img.save("01_文.png")
print("wrote 01_文.png")
