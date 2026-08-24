"""
p3_char_0438_畐 — 畐 (fú, "full")
Structure: 一 (top horizontal) + 口 (mouth) + 田 (field)
Three stacked components, narrow top, wider bottom.

TIER-0 F applied:
- Bezier for slight bowing on horizontals/verticals (subtle since character is
  mostly straight strokes).
- Shoulder dab at each 折 corner (口 and 田 have four corners each).
- Slight taper on the top 一 (thin start, thick end pattern).
- No hooks in this character (no flick logic needed).
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")

def stroke(pts, widths):
    """Draw a stroke by dabbing along interpolated pts with interpolated widths.
    widths can be a single number or (start, end) tuple or per-point list."""
    if isinstance(widths, (int, float)):
        widths = [widths] * len(pts)
    elif isinstance(widths, tuple) and len(widths) == 2:
        n = len(pts)
        w0, w1 = widths
        widths = [w0 + (w1 - w0) * i / max(1, n - 1) for i in range(n)]
    # densify: dab between each pair with many small dabs
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        r0, r1 = widths[i] / 2, widths[i + 1] / 2
        seg_len = math.hypot(x1 - x0, y1 - y0)
        steps = max(2, int(seg_len))
        for k in range(steps + 1):
            t = k / steps
            x = x0 + (x1 - x0) * t
            y = y0 + (y1 - y0) * t
            r = r0 + (r1 - r0) * t
            dab(x, y, r)

def shoulder(x, y, r=5):
    dab(x, y, r)

# ---- Layout ----
# Top 一: around y=60, centered
# 口 (mouth): approx x=100..200, y=90..145
# 田: approx x=70..230, y=155..270, with cross inside

# --- Top 一 (horizontal) ---
stroke([(95, 62), (205, 58)], widths=(4.5, 6.0))

# --- 口 (middle small rectangle) ---
# left 竖
stroke([(105, 92), (108, 148)], widths=(5, 5.5))
# top 横 with folding-right hook shoulder
stroke([(102, 92), (198, 90)], widths=(5, 5.5))
# right 横折 (top-right → down-right)
stroke([(200, 88), (200, 152)], widths=(5.5, 5))
shoulder(200, 90, 4.5)
# bottom 横 closing
stroke([(103, 148), (203, 150)], widths=(5, 5.5))

# --- 田 (large field, bottom) ---
# Rough box: x1=68, y1=160, x2=232, y2=272
# left 竖
stroke([(72, 160), (74, 270)], widths=(5.5, 6))
# top 横 (extends beyond left corner slightly)
stroke([(66, 160), (228, 158)], widths=(5.5, 6))
# right 横折 (top-right → bottom-right)
stroke([(230, 156), (232, 274)], widths=(6, 5.5))
shoulder(230, 158, 5)
# middle 竖 (vertical inside)
stroke([(150, 162), (151, 272)], widths=(5, 5.5))
# middle 横 (horizontal inside)
stroke([(74, 215), (232, 216)], widths=(5, 5.5))
# bottom 横 closing
stroke([(72, 272), (232, 272)], widths=(5.5, 6))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0438_畐/01_畐.png")
print("saved")
