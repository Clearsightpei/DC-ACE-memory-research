"""
Render 匸 (2 strokes) — a right-opening bracket radical.

Decomposition (per label: 2画):
  Stroke 1: 横 — top horizontal (long).
  Stroke 2: 竖折 — short vertical on the left descending from just under the
            top-横's left end, then a shoulder-corner, then a bottom horizontal
            running rightward to roughly match the top's right end.

Notes vs memory:
- Radical-composition principle #2: the two strokes SHARE the corner. The
  竖折's start sits directly under the top 横's left endpoint (no inset).
- 竖折 = shouldered corner (single 顿 press dab), NOT a smooth 弯 arc.
- Standalone scale: use PIL brush-dab technique; keep 顿-dabs modest (r+1
  at plain endpoints, r+2..3 only at the true 折 shoulder).
- The bottom 横 is slightly shorter than the top 横 (GT-consistent) and
  ends BEFORE the top's right end, giving 匸 its slight asymmetric feel.
"""

from PIL import Image, ImageDraw
import math
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=None):
    if steps is None:
        dist = math.hypot(x1 - x0, y1 - y0)
        steps = max(int(dist * 4), 50)
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# ---------- Stroke 1: top 横 (with slight up-tilt) ----------
# left endpoint slightly lower than right endpoint (typical 横 up-tilt ~3-5°)
h1_x0, h1_y0 = 55, 92
h1_x1, h1_y1 = 250, 82
r_main = 5.5
# 顿 dabs at both ends (subtle for standalone)
dab(h1_x0, h1_y0, r_main + 2)
dab(h1_x1, h1_y1, r_main + 1.5)
line_dabs(h1_x0, h1_y0, h1_x1, h1_y1, r_main, r_main)


# ---------- Stroke 2: 竖折 ----------
# The vertical starts sharing the top 横's LEFT endpoint (no inset, per
# principle #2). Descends to the bottom-left corner.
v_x0, v_y0 = h1_x0, h1_y0        # shared with 横 left end
v_x1, v_y1 = 60, 240             # bottom-left corner (slight lean-right)

# 竖 body
line_dabs(v_x0, v_y0, v_x1, v_y1, r_main, r_main)

# Shoulder dab at the corner
dab(v_x1, v_y1, r_main + 2.5)

# Bottom 横 running rightward from the corner. Slightly shorter than the
# top so the top overhangs the bottom on the right (GT-consistent).
h2_x0, h2_y0 = v_x1, v_y1
h2_x1, h2_y1 = 235, 245          # slight down-tilt away from left corner
line_dabs(h2_x0, h2_y0, h2_x1, h2_y1, r_main, r_main)

# Terminal press (blunt end, no flick — 竖折 has no hook)
dab(h2_x1, h2_y1, r_main + 1.5)


# ---------- Save ----------
out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_匸.png"))
print("wrote 01_匸.png")
