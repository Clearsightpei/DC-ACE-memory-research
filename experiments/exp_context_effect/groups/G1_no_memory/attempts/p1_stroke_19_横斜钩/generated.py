"""G1 no-memory attempt: p1_stroke_19_横斜钩 (heng xie gou).

横斜钩: a compound stroke that begins with a short horizontal segment
(横), curves down-and-right into a long diagonal (斜) with a gentle
bow, and ends with a small hook flicking up-and-left (钩). Appears in
飞, 气, 风. Rendered with PIL onto a 300x300 white canvas in black ink.
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


# --- Segment 1: 横 (short horizontal top segment) ---
# Slightly rising then leveling; ends where the diagonal turn begins.
h_start = (60, 70)
h_ctrl = (95, 66)
h_end = (135, 72)  # turn point into the diagonal

Nh1 = 40
prev = None
for i in range(Nh1 + 1):
    t = i / Nh1
    pt = bezier(h_start, h_ctrl, h_end, t)
    # slight taper: thicker at start (顿笔), a bit thinner toward turn
    w = 9 - 2 * t
    if prev is not None:
        draw.line([prev, pt], fill="black", width=max(2, int(round(w))))
    prev = pt

# 顿笔 (initial press) at the start of 横
draw.ellipse([h_start[0] - 5, h_start[1] - 5, h_start[0] + 5, h_start[1] + 5], fill="black")

# Small emphasis at the turn corner (folding point) for the 折/转
draw.ellipse([h_end[0] - 5, h_end[1] - 4, h_end[0] + 5, h_end[1] + 6], fill="black")

# --- Segment 2: 斜 (long diagonal, gently bowed) ---
# Starts at the turn, sweeps down-and-right with a bulge toward lower-left.
d_start = h_end
d_ctrl = (170, 190)   # control point — biases the curve to bow lower-left
d_end = (250, 245)    # bottom-right end (just before the hook)

Nd = 140
prev = None
for i in range(Nd + 1):
    t = i / Nd
    pt = bezier(d_start, d_ctrl, d_end, t)
    # thickness: thick just after the turn, tapering slightly toward hook base
    w = 9 - 3 * t
    if prev is not None:
        draw.line([prev, pt], fill="black", width=max(2, int(round(w))))
    prev = pt

# --- Segment 3: 钩 (short hook flicking up-and-left) ---
hook_start = d_end
hook_ctrl = (252, 222)
hook_end = (232, 205)

Nh2 = 40
prev = None
for i in range(Nh2 + 1):
    t = i / Nh2
    pt = bezier(hook_start, hook_ctrl, hook_end, t)
    # hook tapers to a point
    w = 8 - 6 * t
    if prev is not None:
        draw.line([prev, pt], fill="black", width=max(1, int(round(w))))
    prev = pt

out = os.path.join(os.path.dirname(__file__), "01_横斜钩.png")
img.save(out)
print(out)
