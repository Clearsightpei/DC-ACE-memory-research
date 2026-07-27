"""Render 矢 (arrow) to 01_矢.png at 300x300."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=4):
    d.line(pts, fill="black", width=width, joint="curve")

# Stroke 1: short slanted tick at top (丿 short)
line([(130, 55), (115, 82)], width=4)

# Stroke 2: horizontal top (short), slight downward slope
line([(115, 92), (195, 88)], width=4)

# Stroke 3: left-falling 丿 from top-center curving down through middle
line([(160, 70), (140, 115), (105, 165)], width=4)

# Stroke 4: horizontal middle (longer)
line([(75, 158), (220, 150)], width=4)

# Stroke 5: left-falling 丿 (main body) from center down to lower-left
line([(150, 155), (115, 215), (78, 268)], width=4)

# Stroke 6: right-falling 捺 from center down to lower-right
line([(152, 178), (195, 225), (245, 268)], width=4)

out = os.path.join(os.path.dirname(__file__), "01_矢.png")
img.save(out)
print(f"Saved {out}")
