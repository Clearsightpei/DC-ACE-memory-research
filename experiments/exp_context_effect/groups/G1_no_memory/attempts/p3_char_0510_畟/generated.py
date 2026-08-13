"""G1 render of 畟 (p3_char_0510). PIL with system CJK font."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).parent / "01_畟.png"
SIZE = 300
CHAR = "畟"

img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

# Try common macOS CJK fonts, take first that works.
candidates = [
    ("/System/Library/Fonts/Supplemental/Songti.ttc", 1),
    ("/System/Library/Fonts/STHeiti Medium.ttc", 0),
    ("/System/Library/Fonts/STHeiti Light.ttc", 0),
    ("/System/Library/Fonts/Hiragino Sans GB.ttc", 0),
]
font = None
for path, idx in candidates:
    try:
        f = ImageFont.truetype(path, 220, index=idx)
        # Verify glyph exists by test-rendering.
        probe = Image.new("L", (300, 300), 255)
        ImageDraw.Draw(probe).text((30, 30), CHAR, fill=0, font=f)
        if any(v < 200 for v in probe.getdata()):
            font = f
            break
    except Exception:
        continue
if font is None:
    font = ImageFont.load_default()

# Center the glyph.
bbox = draw.textbbox((0, 0), CHAR, font=font)
w = bbox[2] - bbox[0]
h = bbox[3] - bbox[1]
x = (SIZE - w) // 2 - bbox[0]
y = (SIZE - h) // 2 - bbox[1]
draw.text((x, y), CHAR, fill="black", font=font)

img.save(OUT)
print("wrote", OUT)
