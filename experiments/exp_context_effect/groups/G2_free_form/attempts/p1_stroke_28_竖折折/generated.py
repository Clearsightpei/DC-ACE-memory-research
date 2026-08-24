"""
p1_stroke_28_竖折折 (shu-zhe-zhe): 竖折 + 折
Three beats with two shouldered (folded) corners:
  1) 竖 going down
  2) 折 corner -> 横 going right
  3) 折 corner -> 竖 going down again

Rendered with PIL brush-dab technique (per drawer_memory.md):
- uniform radius body, small 顿-dab at endpoints,
- slightly-larger shoulder dab at each 折 corner,
- blunt terminal press (no flick, since it's 折 not 折钩).
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

R = 5          # base ink radius
DUN = R + 2    # endpoint 顿-dab radius
SHOULDER = R + 3  # 折 corner shoulder dab (slightly bigger)

def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")

def segment(x0, y0, x1, y1, r_start, r_end, steps=400):
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)

# Coordinates chosen so the whole stroke sits centered and legible.
# Beat 1: 竖 top -> down
p1 = (110, 70)
p2 = (110, 165)      # corner 1

# Beat 2: 横 right (slight up-tilt like a standalone 横 is fine; keep near-flat)
p3 = (220, 160)      # corner 2 (a hair higher than p2 to give faint 3° up-tilt)

# Beat 3: 竖 down again from corner 2
p4 = (220, 250)

# --- Beat 1: 竖 down ---
dab(*p1, DUN)                          # 顿 at very top
segment(p1[0], p1[1], p2[0], p2[1], R, R)  # uniform body
dab(*p2, SHOULDER)                     # shoulder dab at 折 #1

# --- Beat 2: 横 rightward ---
segment(p2[0], p2[1], p3[0], p3[1], R, R)
dab(*p3, SHOULDER)                     # shoulder dab at 折 #2

# --- Beat 3: 竖 down (blunt terminal press, no hook flick) ---
segment(p3[0], p3[1], p4[0], p4[1], R, R)
dab(*p4, DUN)                          # blunt end-press

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p1_stroke_28_竖折折/01_竖折折.png")
print("saved")
