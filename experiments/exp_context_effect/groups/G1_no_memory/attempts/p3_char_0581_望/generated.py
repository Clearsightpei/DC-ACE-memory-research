"""G1 render of 望 (wàng) — 300x300 PNG, white bg, black ink.

Uses PIL with a CJK system font to render the character glyph.
"""
import os
from PIL import Image, ImageDraw, ImageFont

SIZE = 300
CHAR = "望"
OUT = os.path.join(os.path.dirname(__file__), f"01_{CHAR}.png")

img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

# Try a few CJK-capable fonts commonly present on macOS.
candidates = [
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/System/Library/Fonts/STHeiti Light.ttc",
    "/System/Library/Fonts/PingFang.ttc",
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/Library/Fonts/Arial Unicode.ttf",
    "/System/Library/Fonts/Supplemental/Songti.ttc",
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

# Center the character.
bbox = draw.textbbox((0, 0), CHAR, font=font)
w = bbox[2] - bbox[0]
h = bbox[3] - bbox[1]
x = (SIZE - w) // 2 - bbox[0]
y = (SIZE - h) // 2 - bbox[1]
draw.text((x, y), CHAR, fill="black", font=font)

img.save(OUT)
print(f"wrote {OUT}")
