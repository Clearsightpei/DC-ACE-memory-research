"""Render 行 (character) at 300x300, white bg, black ink."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# 行 = 彳 (left, 3 strokes) + 亍-like (right, 3 strokes) = 6 strokes total.

# ---- LEFT component 彳 ----
# Stroke 1: short 撇 top
line([(90, 75), (70, 110)], width=5)

# Stroke 2: second 撇 below/right of first
line([(115, 110), (85, 150)], width=5)

# Stroke 3: long vertical from middle of second 撇 straight down
line([(97, 135), (100, 255)], width=5)

# ---- RIGHT component ----
# Stroke 4: short 撇 at top-left of right component
line([(180, 90), (163, 125)], width=5)

# Stroke 5: horizontal 一 through middle of right component
line([(150, 165), (255, 160)], width=5)

# Stroke 6: long vertical 竖钩 from below the top 撇, going down with slight hook
line([(210, 130), (213, 265)], width=5)
# hook at bottom (leftward small tick)
line([(213, 265), (200, 258)], width=5)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_行.png"))
print("saved")
