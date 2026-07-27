"""
Render 乌 (wū, crow) — 4 strokes. Revision 2.

Layout notes from GT:
  - Head is a small loop in the UPPER area (~y 40-130), roughly
    centered horizontally, offset slightly to the right of center.
  - There's a short internal horizontal bar inside the head.
  - Then a long swooping body going down-left and out to the right,
    ending in a small hook up. The base is wide, occupying most of
    the lower half.
  - Small flick/piě at top-left of head.

Stroke order (standard):
  1. 撇 — small diagonal flick at top-left of head
  2. 横折 — horizontal top of head → down-right corner → small
     inward curl (does NOT close at bottom in 乌)
  3. 横 — short horizontal cross-bar inside the head
  4. 竖折折钩 — starts from top-left of body, sweeps down and left,
     then long horizontal base to the right, ending in an up-right hook.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
BR = 6

def dab(x, y, r=BR):
    d.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)

def stroke(points, r=BR):
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        dx, dy = x1 - x0, y1 - y0
        dist = max(abs(dx), abs(dy), 1)
        steps = max(int(dist * 2), 2)
        for s in range(steps + 1):
            t = s / steps
            dab(x0 + dx * t, y0 + dy * t, r)

def curve(points, r=BR, samples=60):
    if len(points) == 3:
        (x0, y0), (x1, y1), (x2, y2) = points
        for s in range(samples + 1):
            t = s / samples
            x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * x1 + t * t * x2
            y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * y1 + t * t * y2
            dab(x, y, r)
    elif len(points) == 4:
        (x0, y0), (x1, y1), (x2, y2), (x3, y3) = points
        for s in range(samples + 1):
            t = s / samples
            b0 = (1 - t) ** 3
            b1 = 3 * (1 - t) ** 2 * t
            b2 = 3 * (1 - t) * t * t
            b3 = t ** 3
            x = b0 * x0 + b1 * x1 + b2 * x2 + b3 * x3
            y = b0 * y0 + b1 * y1 + b2 * y2 + b3 * y3
            dab(x, y, r)
    else:
        stroke(points, r)

# ---------------- Stroke 1: 撇 (top little flick) ----------------
curve([(155, 40), (145, 52), (130, 68)], r=5)

# ---------------- Stroke 2: 横折 (head top + right side) ----------------
# top horizontal
stroke([(140, 70), (195, 62)], r=6)
# corner then down-curve, terminating with slight inward curl (open bottom)
curve([(195, 62), (208, 105), (188, 145)], r=6)
# tiny inward flick at end (does NOT close the loop)
curve([(188, 145), (178, 148), (168, 145)], r=5)

# ---------------- Stroke 3: 横 (internal bar) ----------------
stroke([(150, 108), (190, 105)], r=5)

# ---------------- Stroke 4: 竖折折钩 (body swoop with hook) ----------------
# start upper-left of body, sweep down and out to left
curve([(135, 130), (105, 180), (60, 240)],
      r=7, samples=80)
# long base going right
stroke([(60, 240), (230, 245)], r=7)
# terminal up-right hook
curve([(230, 245), (250, 240), (255, 220)], r=7)

img.save("01_乌.png")
print("wrote 01_乌.png")
