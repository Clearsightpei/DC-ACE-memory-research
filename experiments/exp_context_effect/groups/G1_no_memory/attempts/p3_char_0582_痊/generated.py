"""G1 render for 痊 — no memory, cold draw using PIL + system CJK font."""
from PIL import Image, ImageDraw, ImageFont
import os

SIZE = 300
CHAR = "痊"
OUT = os.path.join(os.path.dirname(__file__), f"01_{CHAR}.png")

img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

font_path = "/System/Library/Fonts/STHeiti Light.ttc"
# Fit character to roughly 240px within the 300px canvas
font = ImageFont.truetype(font_path, 240)

# Center the glyph
bbox = draw.textbbox((0, 0), CHAR, font=font)
w = bbox[2] - bbox[0]
h = bbox[3] - bbox[1]
x = (SIZE - w) // 2 - bbox[0]
y = (SIZE - h) // 2 - bbox[1]
draw.text((x, y), CHAR, font=font, fill="black")

img.save(OUT)
print(f"wrote {OUT}")
