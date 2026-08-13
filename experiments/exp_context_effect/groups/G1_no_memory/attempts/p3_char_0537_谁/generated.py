"""G1 render of 谁 (left: 讠 speech radical; right: 隹 short-tailed bird).
PIL text render with a CJK system font."""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(__file__), "01_谁.png")
SIZE = 300
CHAR = "谁"

img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

candidates = [
    "/System/Library/Fonts/STHeiti Light.ttc",
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/System/Library/Fonts/PingFang.ttc",
    "/System/Library/Fonts/Supplemental/Songti.ttc",
    "/Library/Fonts/Songti.ttc",
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
]
font = None
for path in candidates:
    if os.path.exists(path):
        try:
            font = ImageFont.truetype(path, 240)
            break
        except Exception:
            continue
if font is None:
    font = ImageFont.load_default()

bbox = draw.textbbox((0, 0), CHAR, font=font)
w = bbox[2] - bbox[0]
h = bbox[3] - bbox[1]
x = (SIZE - w) / 2 - bbox[0]
y = (SIZE - h) / 2 - bbox[1]
draw.text((x, y), CHAR, fill="black", font=font)

img.save(OUT)
print("wrote", OUT)
