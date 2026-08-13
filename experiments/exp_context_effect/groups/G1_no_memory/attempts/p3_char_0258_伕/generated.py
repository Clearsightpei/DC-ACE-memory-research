from PIL import Image, ImageDraw, ImageFont
import os

SIZE = 300
CHAR = "伕"
OUT = os.path.join(os.path.dirname(__file__), f"01_{CHAR}.png")

img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

font_paths = [
    "/System/Library/Fonts/STHeiti Light.ttc",
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/System/Library/Fonts/PingFang.ttc",
    "/Library/Fonts/Arial Unicode.ttf",
    "/System/Library/Fonts/Supplemental/Songti.ttc",
]
font = None
for p in font_paths:
    if os.path.exists(p):
        try:
            font = ImageFont.truetype(p, 240)
            break
        except Exception:
            continue
if font is None:
    font = ImageFont.load_default()

bbox = draw.textbbox((0, 0), CHAR, font=font)
w = bbox[2] - bbox[0]
h = bbox[3] - bbox[1]
x = (SIZE - w) // 2 - bbox[0]
y = (SIZE - h) // 2 - bbox[1]
draw.text((x, y), CHAR, fill="black", font=font)

img.save(OUT)
print(f"wrote {OUT}")
