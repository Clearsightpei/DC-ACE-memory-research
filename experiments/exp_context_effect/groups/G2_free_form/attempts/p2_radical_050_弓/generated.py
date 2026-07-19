"""
弓 (gong) — 3-stroke radical.

Stroke order (canonical):
1. 横折 — top: heng rightward, shoulder, short shu down
2. 横   — middle horizontal
3. 竖折折钩 — bottom: shu down, shoulder, heng rightward, shoulder,
             short down-left going, hook up-and-left

Actually, canonical 弓 is 3 strokes:
1. 横折 (top hat)
2. 横 (middle bar)
3. 竖折折钩 (bottom Z with hook)

Rendered PIL brush-dab technique per drawer memory. 300x300, white bg, black ink.
Image coords: y grows DOWN. Origin top-left.

Layout (looking at GT — narrow tall glyph, centered around x=155):
- Left edge of horizontals ~ x=95
- Right edge of top/middle horizontals ~ x=205
- Top y ~ 75
- Middle y ~ 145
- Bottom baseline ~ y=245, hook flicks up

Stroke 1 (横折):
  横 from (95, 78) to (200, 72)  — slight up-tilt
  shoulder at (200, 72)
  竖 down to (195, 108)

Stroke 2 (横):
  From (100, 145) to (198, 140) — slight up-tilt

Stroke 3 (竖折折钩):
  Start at (100, 185)  — a bit below middle heng, or actually canonical starts
  Actually stroke 3 begins from a bit above baseline going right-then-down-then-hook.
  Let me use the 竖折折钩 template: down, shoulder, right, shoulder, down-left, hook up-left.

  Beat 1 (short 竖 or actually starts as 横): from (100, 185) right to (200, 178)
  Beat 2 (shoulder + 竖): down to (195, 235)
  Beat 3 (shoulder + short heng going left-back... no wait)

  Actually the bottom stroke of 弓 is often described as 横折折钩 or 竖折折钩. Looking at GT:
  - Starts middle-left, goes right (horizontal)
  - Turns down (shoulder)
  - Curves/turns to lower-left (the belly-down going)
  - Ends with hook flicking UP-and-LEFT

  So: 横 (100,185)→(200,178) + shoulder + 竖 to (185, 235) + curve down-left to (130, 262)
      + hook up-left to (115, 240)
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


R = 5.0  # base uniform radius

# Revised layout — fill full 300x300 canvas vertically, spread strokes
# Top y ~ 55, baseline y ~ 260. Left edge ~ 90, right edge ~ 210.

# ---------------- Stroke 1: 横折 ----------------
# 横: (90, 62) -> (205, 55), slight up-tilt
dab(90, 62, R + 2)  # 顿笔 at start
line_dabs(90, 62, 205, 55, R, R, steps=200)
# Shoulder press at corner
dab(205, 55, R + 2.5)
# 竖 down: (205, 55) -> (198, 108) — noticeably longer than before
line_dabs(205, 55, 198, 108, R, R, steps=100)
dab(198, 108, R + 1)  # blunt end

# ---------------- Stroke 2: 横 (middle bar) ----------------
# (95, 148) -> (200, 142)
dab(95, 148, R + 2)
line_dabs(95, 148, 200, 142, R, R, steps=180)
dab(200, 142, R + 2)

# ---------------- Stroke 3: 竖折折钩 (bottom) ----------------
# Beat 1: 横 (95, 190) -> (203, 183) — slight up-tilt
dab(95, 190, R + 2)  # 顿笔 at start
line_dabs(95, 190, 203, 183, R, R, steps=180)
# Shoulder 1 at (203, 183)
dab(203, 183, R + 2.5)
# Beat 2: 竖 down-with-slight-left-lean: (203, 183) -> (188, 245)
line_dabs(203, 183, 188, 245, R, R, steps=110)
# Shoulder 2 at (188, 245)
dab(188, 245, R + 2.5)
# Beat 3: down-and-left curving toward baseline — use Bezier so it swoops
# From (188, 245) curving down-and-left to (115, 275)
bezier_dabs(
    (188, 245),
    (165, 278),
    (115, 275),
    R,
    R,
    steps=180,
)
# Hook flick up-and-left from (115, 275) — angle ~-140° (up-left, more prominent)
# length ~42 px, taper thick->thin
hook_len = 42
hook_angle = math.radians(-140)
hx = 115 + hook_len * math.cos(hook_angle)
hy = 275 + hook_len * math.sin(hook_angle)
line_dabs(115, 275, hx, hy, R + 0.5, 1.2, steps=100)

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_弓.png")
img.save(out_path)
print(f"Saved {out_path}")
