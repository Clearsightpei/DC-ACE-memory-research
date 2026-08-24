"""Render radical 韦 (4画) to 300x300 PNG. Revision 1.

Revised after comparing render vs GT:
  - Middle 横 needs more slope (dips slightly right→left is wrong;
    GT actually slants down slightly left→right and extends wider).
    Actually GT middle 横 tilts UP slightly on right end — normal 横 rise.
  - The lower-right 横折钩 is BIGGER in GT and more rounded, with a
    prominent leftward hook at the bottom terminal.
  - Top short 横 in GT is more like a very short horizontal stub +
    the small down-tick; keep it small.
  - Removed the prominent 顿 dab at top of 竖 (GT shows just a
    small start, no bulb).
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def taper_stroke(p1, p2, w1, w2, steps=28):
    x1, y1 = p1
    x2, y2 = p2
    for i in range(steps):
        t0 = i / steps
        t1 = (i + 1) / steps
        xa = x1 + (x2 - x1) * t0
        ya = y1 + (y2 - y1) * t0
        xb = x1 + (x2 - x1) * t1
        yb = y1 + (y2 - y1) * t1
        w = w1 + (w2 - w1) * ((t0 + t1) / 2)
        r = w / 2
        d.ellipse((xa - r, ya - r, xa + r, ya + r), fill=BLACK)
        d.ellipse((xb - r, yb - r, xb + r, yb + r), fill=BLACK)
        d.line([(xa, ya), (xb, yb)], fill=BLACK, width=max(1, int(w)))


def taper_curve(pts, w1, w2, steps=40):
    """Sample a quadratic Bezier through 3 points with tapered width."""
    p0, p1, p2 = pts
    prev = None
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        w = w1 + (w2 - w1) * t
        r = w / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)
        if prev is not None:
            d.line([prev, (x, y)], fill=BLACK, width=max(1, int(w)))
        prev = (x, y)


# --- Stroke 1: short top 横 with a short down-tick on the right ---
# Slight upward tilt (typical 横)
taper_stroke((130, 82), (205, 76), 5, 6)
# Down tick (small 横折 stub)
taper_stroke((205, 76), (203, 105), 6, 5)

# --- Stroke 2: long middle 横, slight up-tilt, wide ---
taper_stroke((45, 148), (250, 138), 5, 7)

# --- Stroke 3: central 竖, long, from just above top 横 down to base ---
taper_stroke((150, 68), (150, 280), 6, 6)

# --- Stroke 4: 横折钩 lower right (larger, rounder, with leftward hook) ---
# Horizontal part from central axis area to right side, y ~ 190
taper_stroke((150, 195), (238, 190), 5, 7)
# Fold: curved corner into the right wall descending to bottom-right
taper_curve([(238, 190), (238, 210), (235, 255)], 7, 6)
# Hook back-left at bottom terminal
taper_stroke((235, 255), (198, 248), 6, 3)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_123_韦/01_韦.png"
)
