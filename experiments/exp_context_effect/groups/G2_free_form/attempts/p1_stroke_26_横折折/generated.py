"""
p1_stroke_26_横折折 — G2 attempt

横折折 = 横折 + 横折 (per target_description "横折加横折").
Shape: horizontal → shoulder → short vertical → shoulder → horizontal.
Four beats, three joints — each direction change is a 折 shoulder
(sharp squared corner with a single slightly-larger 顿 dab), never a
smooth arc. No terminal hook flick; ends in a blunt press.

Composition on 300x300, y grows DOWN.
  Beat 1 (横):  ( 55, 95) → (200, 88)   slight up-tilt
  Beat 2 (竖):  (198, 90) → (190,150)   short, straight down
  Beat 3 (横):  (188,152) → (255,146)   slight up-tilt, shorter
  Beat 4 (竖):  (253,148) → (245,215)   short, straight down; blunt end
Each corner gets one shoulder-dab (r_body + 3 px).
"""

from PIL import Image, ImageDraw
import math
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BODY_R = 5
SHOULDER_R = BODY_R + 3
END_R = BODY_R + 2

def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")

def segment(p0, p1, r_start, r_end, steps=400):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)

# Beat 1: 横 (slight up-tilt)
p1_start = (55, 95)
p1_end = (200, 88)
dab(*p1_start, END_R)                     # start 顿
segment(p1_start, p1_end, BODY_R, BODY_R)

# Joint 1: shoulder dab (between beat 1 and beat 2)
joint1 = (198, 90)
dab(*joint1, SHOULDER_R)

# Beat 2: short 竖 (straight down)
p2_end = (190, 150)
segment(joint1, p2_end, BODY_R, BODY_R)

# Joint 2: shoulder dab
joint2 = (188, 152)
dab(*joint2, SHOULDER_R)

# Beat 3: 横 (slight up-tilt, shorter than beat 1)
p3_end = (255, 146)
segment(joint2, p3_end, BODY_R, BODY_R)

# Joint 3: shoulder dab
joint3 = (253, 148)
dab(*joint3, SHOULDER_R)

# Beat 4: short 竖 (straight down, blunt end — no hook flick)
p4_end = (245, 215)
segment(joint3, p4_end, BODY_R, BODY_R)
dab(*p4_end, END_R)                       # terminal press

out_path = os.path.join(os.path.dirname(__file__), "01_横折折.png")
img.save(out_path)
print(f"saved {out_path}")
