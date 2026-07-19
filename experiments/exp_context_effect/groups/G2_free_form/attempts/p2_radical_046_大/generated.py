"""
G2 attempt at radical 大 (3 strokes).

Structure (image coords, y grows DOWN, canvas 300x300):
  Stroke 1: 横 (heng) — horizontal bar, slight up-tilt, upper-middle.
  Stroke 2: 撇 (pie) — throws from just above the heng crossing to lower-left.
            Must CROSS THROUGH the heng (top of pie visible above heng line).
  Stroke 3: 捺 (na) — press-down from about the same crossing point to
            lower-right, thin->thick, ending in broad flat foot.

Applying memory principles:
- Standalone scale: use r=6-7 for base radius; small 顿 dabs (r+1) at heng
  endpoints, not r+2 balloons.
- 撇 crosses the 横 (crossing signature is critical — 大's identity).
- 撇 has gentle rightward bow (Bezier control on the interior/right side).
- 捺 thin->thick ending in flat foot (terminal press).
- The 撇 and 捺 both cross/touch the 横 near its midpoint; the two tails
  spread wide to fill the lower half of the canvas.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=None):
    dx, dy = x1 - x0, y1 - y0
    length = math.hypot(dx, dy)
    if steps is None:
        steps = max(60, int(length * 2.2))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + dx * t
        y = y0 + dy * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=None, easing=None):
    if steps is None:
        steps = 260
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        et = easing(t) if easing else t
        r = r0 + (r1 - r0) * et
        dab(x, y, r)


# --- Stroke 1: 横 heng ---
# Horizontal bar, slight up-tilt (left lower than right by ~4 px).
# Sits in the upper-middle area, y ~ 130.
H_X0, H_Y0 = 60, 138
H_X1, H_Y1 = 240, 130
dab(H_X0, H_Y0, 7)          # 顿 start — modest at standalone scale
line_dabs(H_X0, H_Y0, H_X1, H_Y1, 6, 6)
dab(H_X1, H_Y1, 6.5)        # subtle end press (no ball)


# --- Stroke 2: 撇 pie ---
# Starts ABOVE the 横 (around y=60), crosses through the 横 near x=150,
# then throws down-and-left to about (55, 265).
# Gentle rightward bow: Bezier control pulled toward the right (interior).
PIE_P0 = (155, 55)
PIE_P2 = (55, 265)
PIE_CTRL = (140, 160)       # control pulled right of chord midpoint
dab(PIE_P0[0], PIE_P0[1], 9)  # 顿笔 at start (thick head)
bezier_dabs(PIE_P0, PIE_CTRL, PIE_P2, 9, 1.3, steps=320)


# --- Stroke 3: 捺 na ---
# Starts near the 撇/横 crossing (around x=155, y=115 — just above the heng),
# presses down-and-right, thin->thick, ending in a broad flat foot at
# lower-right (~(255, 260)). Slight downward curve (belly on lower side).
NA_P0 = (152, 115)
NA_P2 = (258, 258)
NA_CTRL = (185, 210)        # slight belly toward lower-left of chord

# Thin -> thick ramp with easing so most of the thickening happens in the
# last third (canonical 捺 profile).
def na_ease(t):
    return t ** 1.3

bezier_dabs(NA_P0, NA_CTRL, NA_P2, 1.5, 10, steps=320, easing=na_ease)
# Terminal broad flat foot: extend a short horizontal press from the tip.
FOOT_END = (283, 258)
line_dabs(NA_P2[0], NA_P2[1], FOOT_END[0], FOOT_END[1], 10, 3)


img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_046_大/01_大.png")
print("saved 大")
