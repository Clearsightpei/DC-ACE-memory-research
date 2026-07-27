"""
为 — 4 strokes.
Reading the GT (300x300):
  Stroke 1: small dot/short 撇 at upper-mid-right area, tilted down-left
  Stroke 2: long 撇 sweeping from mid-top down to lower-left corner (curved)
  Stroke 3: 横折钩 — starts horizontal near left-middle crossing the 撇,
             folds down on the right, then hooks left at the bottom
  Stroke 4: small internal dot inside the box (mid-lower)

Rendered with PIL Bezier-sampling (segments as short lines with round caps).
"""
from PIL import Image, ImageDraw

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

def bezier(p0, p1, p2, p3, n=60):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1-t)**3 * p0[0] + 3*(1-t)**2*t*p1[0] + 3*(1-t)*t*t*p2[0] + t**3*p3[0]
        y = (1-t)**3 * p0[1] + 3*(1-t)**2*t*p1[1] + 3*(1-t)*t*t*p2[1] + t**3*p3[1]
        pts.append((x, y))
    return pts

def draw_bezier(p0, p1, p2, p3, w0, w1, n=60):
    pts = bezier(p0, p1, p2, p3, n)
    for i in range(len(pts) - 1):
        t = i / (len(pts) - 1)
        w = w0 + (w1 - w0) * t
        draw.line([pts[i], pts[i+1]], fill="black", width=max(1, int(round(w))))
    # round caps via ellipse dabs at endpoints
    for (x, y), w in [(pts[0], w0), (pts[-1], w1)]:
        r = max(1, w / 2)
        draw.ellipse([x-r, y-r, x+r, y+r], fill="black")

# Stroke 1: upper dot — short 撇/dot tilting down-LEFT (GT: from ~(135,80) to ~(115,105))
draw_bezier((138, 78), (130, 88), (122, 98), (114, 108), w0=5, w1=2)

# Stroke 2: long 撇 — from top-middle-right sweeping to bottom-left
# top around (180, 55) curving down through (120, 170) to (60, 275)
draw_bezier((180, 55), (155, 130), (110, 200), (58, 275), w0=6, w1=4)

# Stroke 3: 横折钩
# Part A: horizontal top — from (95, 155) crossing right to (215, 140) (slight up-right tilt)
draw_bezier((95, 158), (135, 150), (175, 144), (215, 140), w0=5, w1=6)
# Part B: fold down — from (215, 140) curving down to (222, 265)
draw_bezier((215, 140), (223, 175), (225, 220), (222, 262), w0=6, w1=5)
# Part C: hook flick left — from (222, 262) short flick up-left to (200, 255)
draw_bezier((222, 262), (216, 262), (210, 260), (200, 254), w0=5, w1=1)

# Stroke 4: interior dot — small tick, tilts down-LEFT (GT: mid-lower interior)
draw_bezier((170, 200), (162, 210), (155, 218), (148, 224), w0=4, w1=2)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0096_为/01_为.png")
print("saved")
