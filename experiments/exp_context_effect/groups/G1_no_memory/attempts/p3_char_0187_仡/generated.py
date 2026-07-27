"""G1 render of 仡 (person + qi). PIL, 300x300, black on white."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, w=5):
    d.line(pts, fill="black", width=w, joint="curve")

# --- 亻 (person radical, left side) ---
# Stroke 1: 撇 (slanted left-down from upper area)
stroke([(95, 75), (88, 130), (70, 200)], w=6)
# Stroke 2: 竖 (vertical stroke)
stroke([(100, 130), (100, 245)], w=6)

# --- 乞 (right side) ---
# Stroke 1: 撇 (short slant top-right)
stroke([(200, 80), (155, 110)], w=6)
# Stroke 2: 横 (horizontal, upper)
stroke([(145, 135), (235, 130)], w=6)
# Stroke 3: 横折弯钩 (horizontal-turn-curve-hook, the long final stroke)
# Smoother curve using more sub-points
pts = [
    (150, 175),
    (180, 173),
    (215, 172),
    (222, 182),
    (215, 205),
    (198, 230),
    (180, 255),
    (195, 262),
    (220, 263),
    (245, 258),
    (252, 245),
    (250, 232),
]
stroke(pts, w=6)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_仡.png"))
print("saved")
