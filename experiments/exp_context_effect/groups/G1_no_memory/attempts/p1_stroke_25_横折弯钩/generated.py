"""G1 no-memory attempt: p1_stroke_25_横折弯钩 (heng zhe wan gou).

横折弯钩: a compound stroke composed of four segments:
  1) 横 — a short horizontal segment at the top with 顿笔 at start.
  2) 折 — a sharp corner turning downward (nearly vertical).
  3) 弯 — the vertical segment curves smoothly rightward into a
        gentle bowl along the bottom.
  4) 钩 — at the far right end, a small hook flicking up-and-left.

Appears in 九, 几, 亿, forming the outer skeleton of those characters.
Rendered with PIL onto a 300x300 white canvas in black ink.
"""

from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def bezier(p0, p1, p2, t):
    x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
    y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
    return (x, y)


def stroke_bezier(p0, p1, p2, N, w_start, w_end, min_w=2):
    prev = None
    for i in range(N + 1):
        t = i / N
        pt = bezier(p0, p1, p2, t)
        w = w_start + (w_end - w_start) * t
        if prev is not None:
            draw.line([prev, pt], fill="black", width=max(min_w, int(round(w))))
        prev = pt


# --- Segment 1: 横 (short horizontal top segment) ---
# Slight rightward stroke with a tiny downward tilt; ends at the fold.
h_start = (75, 75)
h_ctrl = (110, 74)
h_end = (150, 80)   # fold corner (top-right)

stroke_bezier(h_start, h_ctrl, h_end, 40, w_start=9, w_end=7)

# 顿笔 (initial press) at start of 横
draw.ellipse([h_start[0] - 5, h_start[1] - 5, h_start[0] + 5, h_start[1] + 5], fill="black")

# Emphasis at the fold corner (折)
draw.ellipse([h_end[0] - 6, h_end[1] - 4, h_end[0] + 6, h_end[1] + 7], fill="black")

# --- Segment 2 + 3: 折 into 弯 ---
# After the fold, the stroke goes nearly straight down, then curves
# rightward smoothly into a horizontal-ish bottom sweep.
# We render this as one long quadratic Bezier from the fold corner,
# through a control point in the lower-left interior, out to the
# bottom-right where the hook begins.
v_start = h_end                # top of the vertical/curve section
v_ctrl = (150, 235)            # keeps the segment vertical then bends right
v_end = (235, 240)             # bottom-right where hook starts

stroke_bezier(v_start, v_ctrl, v_end, 160, w_start=8, w_end=7)

# --- Segment 4: 钩 (short hook flicking up-and-left) ---
hook_start = v_end
hook_ctrl = (238, 218)
hook_end = (215, 205)

stroke_bezier(hook_start, hook_ctrl, hook_end, 40, w_start=8, w_end=1, min_w=1)


out = os.path.join(os.path.dirname(__file__), "01_横折弯钩.png")
img.save(out)
print(out)
