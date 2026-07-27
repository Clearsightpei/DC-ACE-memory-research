"""Render 疒 (illness radical) at 300x300, black on white.

Structure (5 strokes, per GT):
  1. Top-right 点 (a slanted dot near top-center-right)
  2. Long 横 sweeping from just left of that dot to the right side
  3. Short upper 撇-dot on the left of the vertical (inside upper-left)
  4. Short lower 撇-dot on the left (below the first)
  5. Long 撇 (curved left-falling stroke) starting from the horizontal's
     left end, going down and gently left to the bottom-left corner.

Silhouette family: 广/尸/户 — off-center L, top-heavy, upper+left filled,
lower-right open. Two inner dots on the LEFT of the descending 撇, not
the right (that's what distinguishes 疒 from 广).
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def dab_line(pts, width_start=8, width_end=8):
    """Draw a variable-width polyline via overlapping circles."""
    if len(pts) < 2:
        return
    # sample densely between points
    n_seg = len(pts) - 1
    for si in range(n_seg):
        x0, y0 = pts[si]
        x1, y1 = pts[si + 1]
        steps = max(int(((x1-x0)**2 + (y1-y0)**2)**0.5), 1)
        for t in range(steps + 1):
            u = t / steps
            # width interpolated along the WHOLE polyline
            global_u = (si + u) / n_seg
            w = width_start * (1 - global_u) + width_end * global_u
            x = x0 + (x1 - x0) * u
            y = y0 + (y1 - y0) * u
            r = w / 2
            d.ellipse([x - r, y - r, x + r, y + r], fill="black")

# --- Stroke 1: top 点 (slanted dot, sits ABOVE the horizontal, right-of-center) ---
# short slanted dot, from upper-left to lower-right; small
dab_line([(160, 45), (180, 72)], width_start=4, width_end=8)

# --- Stroke 2: long 横 (horizontal top bar) ---
# from just left of top-center to right edge; slightly rising then flat
dab_line([(105, 95), (160, 92), (255, 98)], width_start=6, width_end=6)

# --- Stroke 3: upper inner 点 (short slanted flick, 冫-style upper) ---
# inside the character, upper-left area
dab_line([(60, 130), (82, 148)], width_start=4, width_end=8)

# --- Stroke 4: lower inner 提/点 (short slanted flick, 冫-style lower) ---
# below the first, slanted opposite direction (rising to the right, like 提)
dab_line([(45, 195), (78, 178)], width_start=8, width_end=4)

# --- Stroke 5: long 撇 (curved left-falling from top-horizontal's left end) ---
# starts near where stroke 2 begins (upper), goes nearly straight down then
# curves left at the bottom — classic 广-family descender.
curve = [
    (105, 95),
    (103, 140),
    (100, 185),
    (95, 225),
    (80, 265),
    (65, 280),
]
dab_line(curve, width_start=9, width_end=5)

img.save("01_疒.png")
print("saved 01_疒.png")
