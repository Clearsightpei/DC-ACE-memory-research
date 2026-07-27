"""Render 爫 (claw radical, 4 strokes).

Silhouette family: wide-flat, top-heavy — ink lives in upper third
of canvas (~y 60-140). It's a "hat" radical used above other components
in compounds like 采/受/爱/爵, so the whole glyph reads as a small,
compressed claw shape.

Stroke plan (per standard order for 爫):
1. 撇  - short, top-left, going down-left (~x 100 -> 75, y 75 -> 115).
2. 竖  - short near-vertical drop, slightly slanting inward, at
        x ~ 115, y 85 -> 125.
3. 竖  - another short near-vertical drop, x ~ 150, y 85 -> 125.
4. 横撇/横钩 - top horizontal at y ~ 75 spanning ~x 95..200 with a
        small down-flick 撇 tail at right end (down to ~x 205 y 130).

Rendered with PIL (cleaner at 300x300 than turtle). Brush = solid
black round-cap line with slight width variation via multiple passes.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def brush_stroke(points, width_start=6, width_end=6, steps=None):
    """Draw a variable-width stroke by dabbing circles along a polyline
    interpolated between the given control points.  Points are (x, y).
    Widths taper linearly from width_start (first pt) to width_end (last).
    """
    if steps is None:
        # dense sampling
        steps = 60
    # generate polyline: linear interpolation between consecutive points
    poly = []
    seg_count = len(points) - 1
    for i in range(seg_count):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        for k in range(steps):
            t = k / steps
            poly.append((x0 + t * (x1 - x0), y0 + t * (y1 - y0)))
    poly.append(points[-1])

    n = len(poly)
    for idx, (x, y) in enumerate(poly):
        t = idx / max(1, n - 1)
        w = width_start + (width_end - width_start) * t
        r = max(1.0, w / 2.0)
        d.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


# Revised: GT shows the four strokes all slanting down-left (claw-like),
# not vertical. Top is a single arcing 横 that dips slightly and ends
# in a small 顿, and three internal short 撇 flicks below it.

# --- stroke 1: leftmost 撇 (starts near top, throws down-left, short) ---
brush_stroke(
    [(108, 108), (95, 125), (82, 142)],
    width_start=6,
    width_end=3,
)

# --- stroke 2: middle short 撇 (parallel-ish to stroke 1) ---
brush_stroke(
    [(138, 110), (128, 128), (118, 145)],
    width_start=6,
    width_end=3,
)

# --- stroke 3: right-middle short 撇 ---
brush_stroke(
    [(172, 108), (162, 128), (152, 145)],
    width_start=6,
    width_end=3,
)

# --- stroke 4: top 横撇 — a slanting top arc that dips slightly then
# continues down-right to form the right shoulder of the claw ---
# arc: starts upper-left, dips through middle, ends upper-right with
# a small 顿 dab, then a short down-left flick.
brush_stroke(
    [(90, 108), (130, 100), (180, 105), (205, 118)],
    width_start=4,
    width_end=6,
)
# small down-flick tail continuing from the 顿 (the 撇 of 横撇)
brush_stroke(
    [(205, 118), (200, 135), (192, 150)],
    width_start=6,
    width_end=3,
)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_131_爫/01_爫.png"
)
print("saved 01_爫.png")
