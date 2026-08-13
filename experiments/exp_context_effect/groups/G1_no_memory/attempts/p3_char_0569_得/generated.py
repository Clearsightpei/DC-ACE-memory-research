"""G1 render for 得 — PIL with system CJK font, drawn as text at 300x300."""
from PIL import Image, ImageDraw, ImageFont
import os

OUT = os.path.join(os.path.dirname(__file__), "01_得.png")
SIZE = 300

img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

# Try several CJK fonts commonly present on macOS
font_candidates = [
    "/System/Library/Fonts/PingFang.ttc",
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/System/Library/Fonts/STHeiti Light.ttc",
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/Library/Fonts/Songti.ttc",
    "/System/Library/Fonts/Supplemental/Songti.ttc",
]
font = None
for p in font_candidates:
    if os.path.exists(p):
        try:
            font = ImageFont.truetype(p, 240)
            break
        except Exception:
            continue
if font is None:
    font = ImageFont.load_default()

text = "得"
bbox = draw.textbbox((0, 0), text, font=font)
w = bbox[2] - bbox[0]
h = bbox[3] - bbox[1]
x = (SIZE - w) // 2 - bbox[0]
y = (SIZE - h) // 2 - bbox[1]
draw.text((x, y), text, fill="black", font=font)

img.save(OUT)
print("saved", OUT)
