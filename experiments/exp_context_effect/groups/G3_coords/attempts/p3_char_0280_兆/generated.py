"""兆 (zhao) — 6 strokes. Revised to better match GT proportions.
Left: 撇 (top-left, going down-left) + 点 (below, going down-right) + long 竖弯钩 arc
Right: 点 (top, small down-right) + 撇 (middle-right, going down-left) + long 竖弯钩
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=4):
    d.line(pts, fill="black", width=width, joint="curve")

def bezier(p0, p1, p2, steps=80, width=4):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1-t)*(1-t)*p0[0] + 2*(1-t)*t*p1[0] + t*t*p2[0]
        y = (1-t)*(1-t)*p0[1] + 2*(1-t)*t*p1[1] + t*t*p2[1]
        pts.append((x, y))
    line(pts, width=width)

def cubic(p0, p1, p2, p3, steps=100, width=4):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u*u*u*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t*t*t*p3[0]
        y = u*u*u*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t*t*t*p3[1]
        pts.append((x, y))
    line(pts, width=width)

W_STROKE = 4

# --- LEFT HALF ---
# Stroke 1: short 撇 (top-left), starting high, going down-left
bezier((92, 78), (75, 108), (52, 138), width=W_STROKE)

# Stroke 2: 点 below-inside, a short mark going down-right
bezier((70, 138), (82, 148), (98, 160), width=W_STROKE)

# Stroke 3: long main left curve — starts near top-center, sweeps down and to the left,
# then hooks back up-right (this is the character's leftmost long stroke)
cubic((125, 70), (100, 140), (60, 220), (55, 258), width=W_STROKE)
# Hook lifting up-right at the bottom
bezier((55, 258), (78, 262), (108, 248), width=W_STROKE)

# --- RIGHT HALF ---
# Stroke 4: 点 (top-right small dot / short mark), going down-right
bezier((172, 90), (180, 102), (190, 116), width=W_STROKE)

# Stroke 5: short 撇 (middle-right), going down-left
bezier((222, 128), (205, 148), (183, 170), width=W_STROKE)

# Stroke 6: long right stroke — nearly vertical descending, then curves right with a small hook
cubic((208, 68), (215, 130), (225, 210), (238, 240), width=W_STROKE)
# curve/hook to the right at bottom
bezier((238, 240), (255, 258), (278, 252), width=W_STROKE)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0280_兆/01_兆.png")
print("saved")
