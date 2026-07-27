"""Render 乜 to a 300x300 PNG using PIL.

乜 has 2 strokes:
  Stroke 1 (横折): starts as a short vertical drop at top-left (around x=115,
    y=80), then folds horizontal to the right ending around x=200, y=80.
    Small 顿 at the fold. Optional soft down-tick from the fold.
  Stroke 2 (竖弯钩): starts high up (around x=110, y=75 or a hair right),
    sweeps down-LEFT as a long shallow 撇/横 across most of the canvas
    (crossing under the fold), then curls back RIGHT along a baseline,
    finally hooking UP at the right end.

The GT silhouette shows: a horizontal top-lid on the left, a small pointer
mid-right (an inverted V from the tail curling), and a wide U shape from
the 竖弯钩 which contains the top-lid.

Revision from attempt 1: the right descent is not a straight vertical — it
must be the 竖弯钩 curling right along the bottom baseline and hooking up
at the far right. The "top-lid" (stroke 1) is short, sitting inside the
upper-left of the U.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

def line(x1, y1, x2, y2, width=6):
    draw.line([(x1, y1), (x2, y2)], fill="black", width=width)

def dab(x, y, r=4):
    draw.ellipse((x-r, y-r, x+r, y+r), fill="black")

def bezier(p0, p1, p2, width=7, n=60):
    pts = []
    for i in range(n+1):
        t = i / n
        x = (1-t)**2 * p0[0] + 2*(1-t)*t*p1[0] + t*t*p2[0]
        y = (1-t)**2 * p0[1] + 2*(1-t)*t*p1[1] + t*t*p2[1]
        pts.append((x, y))
    for a, b in zip(pts[:-1], pts[1:]):
        draw.line([a, b], fill="black", width=width)

# ---------------------------------------------------------------
# Stroke 1: 横折 — the "top-lid" piece inside the enclosure
# Small vertical drop then fold right.
# ---------------------------------------------------------------
# tiny 顿 dab at start
dab(115, 85, r=4)
# small vertical descent
line(115, 85, 115, 110, width=7)
# fold: shoulder dab + horizontal to right
dab(115, 110, r=4)
line(115, 110, 195, 115, width=7)
# small terminal dab
dab(195, 115, r=4)

# ---------------------------------------------------------------
# Stroke 2: 竖弯钩 sweeping wide — this is the huge "container"
# stroke that forms the outer body of 乜.
# Start high up around (135, 75). Sweep down-LEFT to (35, 175) as
# a long shallow arc (the "撇-like" phase). Then curve back RIGHT
# to (230, 235) as the bottom baseline. Finally HOOK up-right to
# ~(230, 195) at the far right.
# We approximate the 竖弯钩 by two bezier arcs + a hook segment.
# ---------------------------------------------------------------

# Phase A: down-left long sweep (start above, ends bottom-left)
bezier((140, 70), (85, 130), (35, 178), width=8)
dab(140, 70, r=5)

# Phase B: bottom curl going right along baseline, rising slightly at right end
bezier((35, 178), (110, 250), (230, 230), width=8)

# Phase C: terminal hook up-right
line(230, 230, 235, 200, width=7)
dab(235, 200, r=4)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0018_乜/01_乜.png")
print("saved")
