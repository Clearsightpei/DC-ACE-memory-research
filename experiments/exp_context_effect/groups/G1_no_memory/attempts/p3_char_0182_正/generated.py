"""Render 正 (correct/upright) - 5 strokes."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
T = 5  # stroke thickness

def line(p1, p2, w=T):
    d.line([p1, p2], fill=INK, width=w)

# Character 正 stroke order (5 strokes):
# 1. Top horizontal (一)
# 2. Left vertical (丨) - from top row down
# 3. Middle short horizontal (一) - shorter, to right of vertical
# 4. Short bottom-left horizontal (一) - small, sits on/near bottom line at left
# 5. Bottom horizontal (一) - longest

# Top horizontal
line((75, 85), (220, 88))

# Left vertical (drops from top down toward bottom, slight lean left)
line((92, 85), (82, 235))

# Middle short horizontal (right of the vertical)
line((92, 152), (200, 150))

# Short bottom horizontal on the LEFT (a small stroke that meets the vertical)
line((55, 232), (95, 232))

# Bottom horizontal (longest, extends from near vertical to right)
line((82, 235), (240, 232))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0182_正/01_正.png")
print("saved")
