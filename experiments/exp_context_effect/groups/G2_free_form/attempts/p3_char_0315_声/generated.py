"""
p3_char_0315_声  — G2 free-form drawer

SIGNATURE CHECK (from sibling_signature_checklist.md, applied to components):
- 声 contains 士 as its top component: TOP 横 SHORTER than bottom (~1.5x ratio).
- 声 contains 尸-like structure at bottom: top starts with 一 directly (no dot above).
- Includes a long 撇 sweeping from the left shoulder down past the base.

Stroke plan (7 strokes, MMH-standard order for 声):
  1. short 横 at top          (士 top bar, short)
  2. short 竖 through top+mid (士 vertical)
  3. long 横 across middle    (士 bottom bar / top of lower 尸)
  4. 横折 (right shoulder)    (starts on middle 横 at right, drops down)
  5. short 横 inside          (bottom bar of small right rectangle)
  6. long 撇                  (from left-top of middle 横 sweeping down-left)

Renderer: PIL brush-dabs for calligraphic taper, per drawer_memory.
"""

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_taper(x0, y0, x1, y1, r0, r1, steps=None):
    dx, dy = x1 - x0, y1 - y0
    dist = (dx * dx + dy * dy) ** 0.5
    if steps is None:
        steps = max(60, int(dist * 3))
    for i in range(steps + 1):
        t = i / steps
        dab(x0 + dx * t, y0 + dy * t, r0 + (r1 - r0) * t)


def curve_taper(pts, r0, r1, steps=400):
    """Quadratic-ish sweep through 3 control points, tapered."""
    (x0, y0), (x1, y1), (x2, y2) = pts
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * x0 + 2 * u * t * x1 + t * t * x2
        y = u * u * y0 + 2 * u * t * y1 + t * t * y2
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# ---- Stroke 1: short 横 at top (士 top bar, SHORT) ----
# ~1.0 ratio short: from x=125 to x=175, y=60
dab(125, 60, 4)  # 顿 start
line_taper(125, 60, 175, 60, 3.5, 3.5)
dab(175, 60, 4)  # closing dab

# ---- Stroke 2: short 竖 (through top bar to middle bar) ----
# x=150, y=52 to y=115
dab(150, 52, 3.5)
line_taper(150, 52, 150, 115, 3.5, 3.5)

# ---- Stroke 3: long 横 across middle (士 bottom bar, LONG) ----
# from x=65 to x=245, y=115 — much longer than stroke 1
dab(65, 115, 4.5)  # 顿 start (heavier)
line_taper(65, 115, 245, 115, 4.0, 4.0)
dab(245, 115, 4.5)  # closing 顿

# ---- Stroke 4: 横折 (right shoulder of small rectangle) ----
# The rectangle sits below the middle 横, occupying right-center area.
# Top edge x=150 to x=215 at y=145; then folds down to y=215.
dab(150, 145, 3.5)
line_taper(150, 145, 215, 145, 3.3, 3.3)
dab(215, 145, 4.5)  # 折 shoulder dab (r+1)
line_taper(215, 145, 213, 215, 3.3, 3.3)
dab(213, 215, 3.5)

# ---- Stroke 5: short 横 inside the small rectangle (bottom bar) ----
# from x=150, y=215 to x=213, y=215
dab(150, 215, 3.3)
line_taper(150, 215, 213, 215, 3.2, 3.2)
dab(213, 215, 3.3)

# ---- Stroke 6: long 撇 (sweeps from top-left down-left past base) ----
# Starts near top-left of middle 横 area (x≈95, y≈85, ABOVE middle 横),
# sweeps down through the middle 横 and out to lower-left tip (x≈32, y≈280).
# Uses cubic-like Bezier via two sub-quadratic segments for a longer smoother arc.
# Segment A: from (95, 85) via (85, 155) to (60, 210)  — heavy portion
curve_taper(
    [(95, 85), (85, 155), (60, 210)],
    r0=4.8,
    r1=2.6,
    steps=350,
)
# Segment B: from (60, 210) via (48, 245) to (32, 280) — tapering tail
curve_taper(
    [(60, 210), (48, 245), (32, 280)],
    r0=2.6,
    r1=0.9,
    steps=220,
)
# 顿 at the origin
dab(95, 85, 5)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0315_声/01_声.png"
)
print("wrote 01_声.png")
