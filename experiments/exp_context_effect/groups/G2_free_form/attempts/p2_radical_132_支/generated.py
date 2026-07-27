"""Render 支 (radical, 4 strokes) to a 300x300 PNG.

Decomposition (4 strokes):
  1) top 横 — medium length, near y=95 (top-heavy, upper section)
  2) short 竖 — small vertical descending from middle of the 横
  3) 横撇 — a short 横 then flick 撇 down-left (upper part of 又-bottom)
  4) 捺 — long diagonal sweep from upper-left toward lower-right

Silhouette family: square-ish, ~70% x, ~80% y, centered.
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def stroke(points, width_start=8, width_end=8, steps=60):
    """Draw a tapered stroke through a list of Bezier-ish control points
    by sampling as a quadratic through consecutive triples. For simplicity
    we linearly interpolate along the polyline and vary width."""
    # Sample the polyline to N points
    seg_lens = []
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        seg_lens.append(math.hypot(x1 - x0, y1 - y0))
    total = sum(seg_lens) or 1
    samples = []
    for i in range(steps + 1):
        t = i / steps
        target = t * total
        acc = 0
        for j, L in enumerate(seg_lens):
            if acc + L >= target or j == len(seg_lens) - 1:
                local = (target - acc) / L if L > 0 else 0
                local = max(0, min(1, local))
                x0, y0 = points[j]
                x1, y1 = points[j + 1]
                samples.append((x0 + (x1 - x0) * local, y0 + (y1 - y0) * local))
                break
            acc += L
    for i, (x, y) in enumerate(samples):
        t = i / steps
        w = width_start + (width_end - width_start) * t
        r = max(1, w / 2)
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def hdab(x, y, r=5):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# --- Stroke 1: top 横 ---
# medium horizontal, slight up-tilt, at top region
# starts left of center, ends right of center
s1 = [(95, 100), (170, 96), (215, 94)]
stroke(s1, width_start=7, width_end=6, steps=50)
hdab(95, 100, 5)
hdab(215, 94, 5)

# --- Stroke 2: short 竖 ---
# From near middle-top (just left of 横 midpoint), descends short distance
# Note in the GT the vertical looks like a small stub above the 横 then
# continues down to meet where 又 starts. Draw a short 竖 descending from
# the 横 down to ~y=150.
s2 = [(155, 75), (155, 100), (155, 150)]
stroke(s2, width_start=6, width_end=7, steps=40)
hdab(155, 75, 5)

# --- Stroke 3: 横撇 (unified: short 横 then folds and flicks down-left) ---
# Single continuous stroke: starts at left, moves right slightly (short
# horizontal), then bends downward-left into a long 撇.
s3 = [
    (95, 160),
    (135, 158),
    (175, 160),      # end of the short 横 / shoulder
    (160, 180),      # shoulder turn
    (135, 210),
    (105, 240),
    (75, 268),
]
stroke(s3, width_start=7, width_end=2, steps=90)
hdab(95, 160, 5)

# --- Stroke 4: 捺 ---
# Long diagonal starting from the shoulder area of stroke 3, sweeping
# down-right with a broad terminal foot.
s4 = [(150, 175), (185, 210), (215, 240), (240, 260)]
stroke(s4, width_start=3, width_end=10, steps=70)
# Foot terminal
d.ellipse((240 - 8, 260 - 5, 240 + 9, 260 + 6), fill="black")

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_132_支/01_支.png")
print("saved")
