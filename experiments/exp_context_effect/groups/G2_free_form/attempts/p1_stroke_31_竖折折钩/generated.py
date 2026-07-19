"""
p1_stroke_31_竖折折钩 (shu-zhe-zhe-gou)

Structure (image coords, y grows DOWN):
  Beat 1 — 竖 (short vertical) descending from upper area
  Beat 2 — 折 (shoulder) turning right into a short 横
  Beat 3 — 折 (shoulder) turning down into a 竖
  Beat 4 — 钩 (hook) flicking up-and-left from bottom endpoint

Rendered via PIL brush-dab technique (per drawer_memory.md).
Uniform r~5 for main segments, r+2 shoulder dabs at each 折 joint,
hook tapers thick->thin to a sharp tip.
Canvas: 300x300, white bg, black ink.
"""

from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def stroke_uniform(x0, y0, x1, y1, r, n=400):
    """Straight uniform-radius stroke via brush dabs."""
    for i in range(n + 1):
        t = i / n
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        dab(x, y, r)


def stroke_taper(x0, y0, x1, y1, r_start, r_end, n=400):
    """Tapered straight stroke."""
    for i in range(n + 1):
        t = i / n
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


R = 5  # main stroke radius
SHOULDER = R + 2  # 折 press dab

# Endpoints chosen so full glyph fits inside ~240x240 with margin.
# Beat 1: short 竖 (top -> mid-upper)
p1_start = (110, 60)
p1_end = (110, 130)

# Beat 2: 横 rightward (slight up-tilt like standard 横)
p2_start = p1_end
p2_end = (200, 122)  # ~8 px up-tilt over 90 px

# Beat 3: 竖 straight down
p3_start = p2_end
p3_end = (200, 235)

# Beat 4: 钩 hook flicks up-and-left from bottom endpoint
# ~40 px long, angled ~-135 deg (up-left)
import math

hook_len = 40
hook_angle_deg = -135  # image coords: negative y = up
hx = p3_end[0] + hook_len * math.cos(math.radians(hook_angle_deg))
hy = p3_end[1] + hook_len * math.sin(math.radians(hook_angle_deg))
p4_end = (hx, hy)

# --- Draw beats ---
# 顿笔 dab at very start
dab(*p1_start, SHOULDER)

# Beat 1: 竖
stroke_uniform(*p1_start, *p1_end, R)

# Shoulder dab at first 折 corner
dab(*p1_end, SHOULDER)

# Beat 2: 横
stroke_uniform(*p2_start, *p2_end, R)

# Shoulder dab at second 折 corner
dab(*p2_end, SHOULDER)

# Beat 3: 竖
stroke_uniform(*p3_start, *p3_end, R)

# Joining dab at bottom before hook
dab(*p3_end, SHOULDER)

# Beat 4: 钩 (thick -> thin)
stroke_taper(p3_end[0], p3_end[1], p4_end[0], p4_end[1], R, 1.0, n=200)

out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "01_竖折折钩.png")
img.save(out_path)
print(f"Saved: {out_path}")
