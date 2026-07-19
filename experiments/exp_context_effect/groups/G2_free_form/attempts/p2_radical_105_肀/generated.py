"""
p2_radical_105_肀 — G2 first attempt.

肀 (yù) is a 4-画 radical. Structure (from GT PNG inspection):
  - Stroke 1: a small 横折 at top-left forming a small horn/hook opening to
             the LEFT-BOTTOM. Reads as a short down-slant (like a small 撇 or
             short 竖) with a horizontal top.
  - Stroke 2: a 横 (upper horizontal) that runs across the middle-upper area.
  - Stroke 3: a 横 (lower horizontal) that runs across, roughly parallel and
             slightly longer than stroke 2.
  - Stroke 4: a long 竖 that descends through both horizontals from above
             the top horn down past the lower 横, extending well below —
             this is the tail that dominates the silhouette.

Applying B1 principles:
  - Draw the small 横折 as a real corner (shared-joint principle 2).
  - Length hierarchy: bottom 横 slightly LONGER than middle 横 (principle 6).
  - Long descending 竖 must extend well below the bottom 横 (principle 8 —
    the vertical is the anchor). No hook (肀 has a plain 竖 tail).
  - PIL brush-dabs technique (standalone scale: r=5–6 body, r+1 顿 at ends,
    keep dabs modest so they don't balloon).
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def dab_line(x0, y0, x1, y1, r0, r1, steps=None):
    dx, dy = x1 - x0, y1 - y0
    dist = math.hypot(dx, dy)
    if steps is None:
        steps = max(int(dist * 2), 30)
    for i in range(steps + 1):
        t = i / steps
        x = x0 + dx * t
        y = y0 + dy * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# =========================================================
# Stroke 1: 横折 at top — small horn on the upper-left
# short 横 running left→right, then short down-slant.
# Anchors:  (95, 60) → (145, 55)   [short 横, slight up-tilt]
#           then shoulder at (145, 55)
#           down to (135, 100)     [short down-slant, slight left lean]
# =========================================================
# top-short 横 with 顿-dab at start
dab(95, 60, 6)  # start press
dab_line(95, 60, 145, 55, 5, 5)
# shoulder dab
dab(145, 55, 7)
# short down segment (blunt end)
dab_line(145, 55, 135, 100, 5, 5)
dab(135, 100, 6)  # blunt terminal

# =========================================================
# Stroke 2: middle 横 — upper crossbar
# (55, 125) → (235, 118)   moderate horizontal, slight up-tilt
# =========================================================
dab(55, 125, 7)  # start 顿
dab_line(55, 125, 235, 118, 5, 5)
dab(235, 118, 7)  # end 顿

# =========================================================
# Stroke 3: lower 横 — longer crossbar
# (45, 175) → (250, 168)   longer than stroke 2
# =========================================================
dab(45, 175, 7)  # start 顿
dab_line(45, 175, 250, 168, 5, 5)
dab(250, 168, 7)  # end 顿

# =========================================================
# Stroke 4: long 竖 — descends from above top 横 all the way down
# (150, 50) → (150, 275)   long dominant vertical, plain blunt end
# =========================================================
dab(150, 50, 7)  # start 顿 at top
dab_line(150, 50, 150, 275, 5.5, 5.5)
dab(150, 275, 6)  # blunt terminal (no hook)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_105_肀/01_肀.png")
print("wrote 01_肀.png")
