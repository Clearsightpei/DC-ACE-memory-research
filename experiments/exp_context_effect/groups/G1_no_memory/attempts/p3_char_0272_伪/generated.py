"""Render 伪 (wei, false) to 01_伪.png at 300x300."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=6):
    d.line(pts, fill="black", width=width, joint="curve")

# ---- Left radical 亻 (person) ----
# Stroke 1: 撇 (falling-left)
stroke([(95, 75), (60, 200)], width=6)
# Stroke 2: 竖 (vertical) descending
stroke([(82, 135), (82, 265)], width=6)

# ---- Right component 为 (4 strokes) ----
# Stroke 1: short 点/丶 at top-left of component
stroke([(160, 60), (145, 90)], width=6)

# Stroke 2: 撇 - long falling-left stroke from upper right down to lower left
stroke([(230, 85), (215, 130), (180, 190), (135, 270)], width=6)

# Stroke 3: 横折折钩 - horizontal starting mid, turning down, then a small hook
# Horizontal upper: from left-mid to right
stroke([(155, 130), (240, 125)], width=6)
# Turn down (right vertical curving)
stroke([(240, 125), (245, 200), (215, 265)], width=6)
# Hook back to the left at bottom
stroke([(215, 265), (185, 250)], width=6)

# Stroke 4: inner short horizontal (small mark inside)
stroke([(175, 180), (225, 180)], width=6)

out = os.path.join(os.path.dirname(__file__), "01_伪.png")
img.save(out)
print(f"wrote {out}")
