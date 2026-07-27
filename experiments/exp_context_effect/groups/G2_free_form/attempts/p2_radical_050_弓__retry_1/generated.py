"""
弓 (gong) — 3-stroke radical, retry #1.

# SIGNATURE CHECK (弓 family):
# - 3 strokes: 横折 + 横 + 竖折折钩 (the last is one connected stroke:
#   横→折→竖→折→横 with terminal hook flicking UP-and-LEFT).
# - Silhouette: stacked E open-to-the-LEFT. All right-edge folds sit
#   flush on the RIGHT side of the glyph.
# - Bottom stroke has a real BELLY (the curve swings down below
#   baseline before returning up-and-left for the hook).
# - Hook flicks UP-and-LEFT at ~-125° (per TIER-0 B: 横折折钩 flick).
# - Prior fail (batch B1): three bars looked disconnected. Fix: draw
#   real 折 shoulders that make the E-shape read as CONNECTED, not
#   three isolated bars.

Layout (300x300, y-down):
  - Left x ~ 82
  - Right x ~ 218 (all right-edge folds line up here)
  - Top y ~ 60
  - Middle y ~ 145
  - Bottom baseline y ~ 250, belly swings to y ~ 268
"""

from PIL import Image, ImageDraw
import math
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r_start, r_end, steps=None):
    if steps is None:
        d = math.hypot(x1 - x0, y1 - y0)
        steps = max(int(d * 3), 60)
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r_start, r_end, steps=200):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


R = 5.0  # base uniform brush radius

# ----- Anchor coordinates (right edge alignment ~ x=216) -----
RIGHT = 216
LEFT = 85

# ---------------- Stroke 1: 横折 (top hat) ----------------
# Slight up-tilt heng from LEFT to RIGHT, then shoulder press + short 竖 down
x0, y0 = LEFT, 68
x1, y1 = RIGHT, 60  # slight up-tilt
dab(x0, y0, R + 2)  # 顿笔 at start
line_dabs(x0, y0, x1, y1, R, R, steps=200)
dab(x1, y1, R + 2.8)  # shoulder press
# 竖 down to (RIGHT-4, 118)
line_dabs(x1, y1, RIGHT - 4, 118, R, R, steps=110)
dab(RIGHT - 4, 118, R + 1)  # blunt terminal

# ---------------- Stroke 2: 横 (middle bar) ----------------
# Slightly shorter than top and bottom, spans across
x0, y0 = LEFT + 5, 152
x1, y1 = RIGHT - 6, 146
dab(x0, y0, R + 2)
line_dabs(x0, y0, x1, y1, R, R, steps=180)
dab(x1, y1, R + 2)

# ---------------- Stroke 3: 竖折折钩 (bottom, connected with hook) ----------------
# Beat 1: short 横 from left going right (slight up-tilt)
x0, y0 = LEFT, 195
x1, y1 = RIGHT, 187
dab(x0, y0, R + 2.2)  # 顿笔
line_dabs(x0, y0, x1, y1, R, R, steps=200)
# Shoulder 1 (top-right fold)
dab(x1, y1, R + 2.8)
# Beat 2: 竖 down with slight left lean, forming right side of bowl
x2, y2 = RIGHT - 8, 248
line_dabs(x1, y1, x2, y2, R, R, steps=110)
# Shoulder 2 (bottom-right fold)
dab(x2, y2, R + 2.8)
# Beat 3: BELLY — curve swings down-and-LEFT (bowl bottom), Bezier
# from (x2, y2) with control (170, 278) to (108, 268) — real belly
belly_end = (108, 265)
bezier_dabs(
    (x2, y2),
    (170, 282),
    belly_end,
    R,
    R,
    steps=200,
)
# Hook flick UP-and-LEFT from belly_end (~-125°, per TIER-0 flick table)
hook_len = 34
hook_angle = math.radians(-125)  # up-left, into the character body
hx = belly_end[0] + hook_len * math.cos(hook_angle)
hy = belly_end[1] + hook_len * math.sin(hook_angle)
line_dabs(belly_end[0], belly_end[1], hx, hy, R + 0.5, 1.2, steps=100)

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_弓.png")
img.save(out_path)
print(f"Saved {out_path}")
