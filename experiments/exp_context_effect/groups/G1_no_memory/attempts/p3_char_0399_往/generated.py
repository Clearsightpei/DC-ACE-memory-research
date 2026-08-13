"""G1 render of 往 (character)."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=6):
    d.line(pts, fill="black", width=width, joint="curve")

# 往 = 彳 (left radical, 3 strokes) + 主 (right side, 5 strokes)

# --- 彳 (left radical) ---
# Top short diagonal (piě), slanting down-left
stroke([(78, 75), (60, 105)], width=6)
# Second piě (longer), coming from ~vertical top down-left
stroke([(88, 120), (55, 165)], width=6)
# Vertical stroke (long, gently curving)
stroke([(80, 155), (78, 250)], width=6)

# --- 主 (right side) ---
# Top dot (小点 slanting)
stroke([(200, 60), (215, 85)], width=7)
# Top short horizontal
stroke([(165, 115), (235, 115)], width=6)
# Middle horizontal
stroke([(150, 165), (255, 165)], width=6)
# Vertical stroke (center of 主)
stroke([(198, 115), (198, 245)], width=6)
# Bottom horizontal (longest)
stroke([(130, 245), (265, 245)], width=6)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_往.png"))
print("saved 01_往.png")
