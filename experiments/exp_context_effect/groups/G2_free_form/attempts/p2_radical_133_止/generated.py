"""Render 止 (zhi, stop) — 4-stroke radical, ~300x300 PNG.

Stroke order (standard):
  1. 竖  short-left vertical (~y=110 -> 220), the "left leg"
  2. 横  short horizontal jutting to the right from left-leg's top
  3. 竖  taller right vertical (~y=70 -> 220), the "right leg"
  4. 横  long baseline sweeping across the whole width

Silhouette family: square-ish, bottom-heavy (mass on the base line).
Center of mass: sits low; the top-right 竖 is the tallest element,
the bottom 横 anchors everything.

Using PIL brush-dabs for a calligraphic feel (thicker start, taper).
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def stroke(pts, w_start, w_end, steps=60):
    """Draw a variable-width stroke from a list of (x, y) waypoints
    by interpolating and dabbing ellipses. Width tapers linearly from
    w_start (at first point) to w_end (at last point)."""
    # densify: linearly interpolate through all waypoints
    dense = []
    seg_count = len(pts) - 1
    per_seg = max(1, steps // seg_count)
    for i in range(seg_count):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        for k in range(per_seg):
            t = k / per_seg
            dense.append((x0 + (x1 - x0) * t, y0 + (y1 - y0) * t))
    dense.append(pts[-1])
    n = len(dense)
    for idx, (x, y) in enumerate(dense):
        t = idx / max(1, n - 1)
        w = w_start + (w_end - w_start) * t
        r = w / 2
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


# ----- Stroke 1: 竖  short left vertical (the left leg of 止) -----
# starts around (115, 115), descends to (115, 215)
stroke([(115, 115), (115, 215)], w_start=8, w_end=9)

# ----- Stroke 2: 横  crossbar that starts inside the left-竖 and extends
# rightward, past where the right-竖 will be, giving the right-side jut
# visible in the GT.
# from (115, 155) rightward to about (210, 150), slight up-tilt
stroke([(115, 155), (210, 150)], w_start=8, w_end=8)

# ----- Stroke 3: 竖  taller right vertical (dominant vertical) -----
# starts around (185, 70) and drops to (185, 220). Has 顿 dab at top.
# Placed so it crosses through stroke 2 near its right end.
stroke([(185, 70), (185, 220)], w_start=10, w_end=10)

# ----- Stroke 4: 横  long bottom horizontal (baseline) -----
# spans from about (55, 235) to (260, 232) — the widest stroke
# slight up-tilt from left to right
stroke([(55, 238), (260, 230)], w_start=9, w_end=10)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_133_止/01_止.png")
