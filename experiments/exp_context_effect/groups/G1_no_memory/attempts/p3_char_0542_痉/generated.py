"""G1 render for p3_char_0542_痉 — no memory, PIL font-based render."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

OUT = Path(__file__).parent / "01_痉.png"
SIZE = 300
CHAR = "痉"

img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

# Try a handwriting-ish CJK font, fall back to Songti
font_candidates = [
    "/System/Library/Fonts/Supplemental/Songti.ttc",
    "/System/Library/Fonts/STHeiti Light.ttc",
    "/System/Library/Fonts/PingFang.ttc",
]
font = None
for p in font_candidates:
    try:
        font = ImageFont.truetype(p, 220)
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
print(f"wrote {OUT}")
