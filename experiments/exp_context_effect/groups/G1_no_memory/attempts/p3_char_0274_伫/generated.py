"""Render 伫 to a 300x300 PNG using PIL with a system CJK font."""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(__file__), "01_伫.png")
CHAR = "伫"

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

# Try common CJK fonts on macOS
candidates = [
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/System/Library/Fonts/PingFang.ttc",
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/Library/Fonts/Songti.ttc",
    "/System/Library/Fonts/Supplemental/Songti.ttc",
    "/System/Library/Fonts/STHeiti Light.ttc",
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

# Center the glyph
bbox = draw.textbbox((0, 0), CHAR, font=font)
w = bbox[2] - bbox[0]
h = bbox[3] - bbox[1]
x = (SIZE - w) // 2 - bbox[0]
y = (SIZE - h) // 2 - bbox[1]
draw.text((x, y), CHAR, fill="black", font=font)

img.save(OUT)
print("wrote", OUT)
