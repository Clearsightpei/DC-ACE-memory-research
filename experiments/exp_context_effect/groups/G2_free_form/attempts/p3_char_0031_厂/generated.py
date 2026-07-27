"""
G2 first attempt of p3_char_0031_厂 (standalone character).

Design (per memory_index → radical_position_rules + form_catalog):
- 厂 is in the "off-center L" family: top+left filled, right-bottom empty.
- Top-heavy: mass in upper third, 撇 tapers as it drops.
- TWO strokes sharing the TOP-LEFT corner:
    1) 横 sweeping from shared corner rightward with slight up-tilt.
    2) 撇 starting at the same corner, curving down-left (belly on RIGHT,
       concave-LEFT), tapering thick→thin.

Standalone character (not left-radical), so uses fuller canvas than the
retry-radical version: 横 stretches wider and the 撇 sweeps longer/lower.

Renderer: PIL brush-dabs (drawer_memory technique).
"""

from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# Shared top-left corner. Standalone char → push slightly left+higher for
# a fuller footprint than the 部首 attempt.
CORNER = (75, 80)


def dab(cx, cy, r):
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")


def line_dabs(p0, p1, r0, r1, steps=400):
    for i in range(steps + 1):
        t = i / steps
        x = p0[0] + (p1[0] - p0[0]) * t
        y = p0[1] + (p1[1] - p0[1]) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=500):
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# --- Stroke 1: 横 (rightward with slight up-tilt) ---
heng_start = CORNER              # (75, 80)
heng_end = (265, 74)             # extend further right, mild rise
line_dabs(heng_start, heng_end, r0=5.2, r1=4.0, steps=500)
# terminal blunt press
dab(heng_end[0], heng_end[1], 4.6)

# 顿 dab at the shared corner (both strokes begin here)
dab(CORNER[0], CORNER[1], 7.8)

# --- Stroke 2: 撇 (long body-sweeping, belly on RIGHT) ---
pie_start = CORNER               # (75, 80)
pie_end = (48, 268)              # long sweep, ending lower-left
pie_ctrl = (110, 175)            # control pulled right ⇒ belly-right / concave-left

# Thick at 顿 seat, taper to sharp tip
bezier_dabs(pie_start, pie_ctrl, pie_end, r0=6.8, r1=1.1, steps=650)

# --- Save ---
here = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(here, "01_厂.png")
img.save(out)
print(f"saved {out}")
