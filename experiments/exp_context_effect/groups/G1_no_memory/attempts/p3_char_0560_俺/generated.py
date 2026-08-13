"""G1 render of 俺 (p3_char_0560) — PIL with system CJK font."""
from PIL import Image, ImageDraw, ImageFont
import os

OUT = os.path.join(os.path.dirname(__file__), "01_俺.png")

img = Image.new("RGB", (300, 300), "white")
draw = ImageDraw.Draw(img)

font_path = "/System/Library/Fonts/STHeiti Light.ttc"
if not os.path.exists(font_path):
    font_path = "/System/Library/Fonts/Hiragino Sans GB.ttc"

font = ImageFont.truetype(font_path, 220)
char = "俺"

bbox = draw.textbbox((0, 0), char, font=font)
w = bbox[2] - bbox[0]
h = bbox[3] - bbox[1]
x = (300 - w) // 2 - bbox[0]
y = (300 - h) // 2 - bbox[1]
draw.text((x, y), char, fill="black", font=font)

img.save(OUT)
print(f"wrote {OUT}")
