"""
G1 no-memory attempt: 竖弯钩 (shu wan gou) — vertical, curve right, hook up.
Render 300x300, white bg, black ink.
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# Stroke width — moderate calligraphic weight
sw = 14

# The 竖弯钩 has three parts:
# 1) Vertical descent (shu) — starts upper-middle, drops down
# 2) Curve to the right (wan) — smooth arc turning horizontal
# 3) Hook upward (gou) — a small upward flick at the right end

# Coordinates chosen to fit centered in 300x300 with margin.
start = (110, 55)     # top of vertical
elbow = (110, 200)    # where vertical starts to curve
after_curve = (235, 235)  # end of horizontal-ish curve
hook_tip = (235, 210)     # small upward hook

# 1) Vertical segment (straight down)
draw.line([start, elbow], fill="black", width=sw)

# 2) Curved section: approximate with a smooth arc from elbow to after_curve.
# Use pieslice / arc via chord approximation with many short segments through a
# quarter-circle whose center is (after_curve.x, elbow.y) = (235, 200).
cx, cy = after_curve[0], elbow[1]  # arc center
rx = cx - elbow[0]   # 125
ry = after_curve[1] - cy  # 35
# Draw the arc by parametric points from angle 180° to 90° (going CCW)
# Actually we want to sweep from pointing-left (elbow) to pointing-down (after_curve).
# In PIL coords y grows down. Point at elbow is (cx - rx, cy). Point at after_curve is (cx, cy + ry).
# Parametrize: theta from pi (180deg) down to pi/2 going through 3pi/4,
# but ellipse: x = cx + rx*cos(theta), y = cy - ry*sin(theta) would put after_curve above.
# We want y grows downward, so: x = cx + rx*cos(theta), y = cy + ry*sin(theta+pi) ... simpler:
# Use theta from 180 to 270 degrees with y = cy - ry*sin(theta) (standard math).
# At theta=180: x=cx-rx=110, y=cy-0=200. Good (elbow).
# At theta=270: x=cx+0=235, y=cy - ry*(-1)=cy+ry=235. Good (after_curve).
import math
prev = elbow
steps = 40
for i in range(1, steps + 1):
    t = math.radians(180 + (90 * i / steps))
    x = cx + rx * math.cos(t)
    y = cy - ry * math.sin(t)
    pt = (x, y)
    draw.line([prev, pt], fill="black", width=sw)
    prev = pt

# 3) Hook upward — short upward tick
draw.line([after_curve, hook_tip], fill="black", width=sw)

# Round the joints by drawing filled circles at endpoints
for pt in [start, elbow, after_curve, hook_tip]:
    r = sw // 2
    draw.ellipse([pt[0]-r, pt[1]-r, pt[0]+r, pt[1]+r], fill="black")

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_竖弯钩.png")
img.save(out_path)
print(f"Saved: {out_path}")
