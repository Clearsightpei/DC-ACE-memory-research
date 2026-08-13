"""G1 render of 做 (make/do) — 亻 + 古 + 攵."""
from PIL import Image, ImageDraw, ImageFont
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

# Try to find a CJK font available on macOS
font = None
for path in [
    "/System/Library/Fonts/STHeiti Light.ttc",
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/System/Library/Fonts/PingFang.ttc",
    "/Library/Fonts/Songti.ttc",
    "/System/Library/Fonts/Supplemental/Songti.ttc",
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
]:
    if os.path.exists(path):
        try:
            font = ImageFont.truetype(path, 240)
            break
        except Exception:
            continue

if font is None:
    font = ImageFont.load_default()

text = "做"
bbox = draw.textbbox((0, 0), text, font=font)
w = bbox[2] - bbox[0]
h = bbox[3] - bbox[1]
x = (SIZE - w) // 2 - bbox[0]
y = (SIZE - h) // 2 - bbox[1]
draw.text((x, y), text, fill="black", font=font)

out = os.path.join(os.path.dirname(__file__), "01_做.png")
img.save(out)
print("saved", out)
