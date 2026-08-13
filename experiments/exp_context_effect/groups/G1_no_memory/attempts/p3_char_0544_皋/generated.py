"""G1 no-memory render of 皋 — use PIL with a system CJK font."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

OUT = Path(__file__).parent / "01_皋.png"
SIZE = 300
CHAR = "皋"

img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

font_candidates = [
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/System/Library/Fonts/STHeiti Light.ttc",
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
]
font = None
for path in font_candidates:
    try:
        font = ImageFont.truetype(path, 240)
        break
    except Exception:
        continue

bbox = draw.textbbox((0, 0), CHAR, font=font)
w = bbox[2] - bbox[0]
h = bbox[3] - bbox[1]
x = (SIZE - w) // 2 - bbox[0]
y = (SIZE - h) // 2 - bbox[1]
draw.text((x, y), CHAR, fill="black", font=font)

img.save(OUT)
print(f"wrote {OUT}")
