"""G1 render of 长 (4-stroke radical). PIL-based, 300x300, white bg, black ink."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
LW = 7  # stroke width

def line(pts, width=LW):
    draw.line(pts, fill=INK, width=width, joint="curve")

# Analysis of 长 (simplified, 4 strokes):
# Stroke 1: 撇 — short slant at top, going from upper-center down-left
# Stroke 2: 横 — long horizontal crossing middle (dominant width)
# Stroke 3: 竖提 — vertical from upper area down, hooking up-right at bottom
# Stroke 4: 捺 — long right-falling curve from center-upper area to lower-right

# Stroke 1: 撇 (top short slant)
line([(130, 70), (100, 120)], width=LW)

# Stroke 3: 竖提 (vertical + hook at bottom) — draw first so 横 crosses it visually
# Vertical descending
line([(130, 80), (128, 220)], width=LW)
# 提 hook up-right
line([(128, 220), (175, 195)], width=LW)

# Stroke 2: 横 (long horizontal across middle)
line([(50, 150), (195, 148)], width=LW)

# Stroke 4: 捺 (long right-falling curve)
# Starts near top-center-right (above horizontal), curves through the cross,
# then sweeps down-right with a long flare
line([(145, 95), (160, 130), (185, 165), (220, 195), (255, 215), (275, 220)], width=LW)

out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "01_长.png")
img.save(out_path)
print(f"Saved: {out_path}")
