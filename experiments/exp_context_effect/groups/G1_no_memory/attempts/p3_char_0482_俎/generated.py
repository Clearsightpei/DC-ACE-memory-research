from PIL import Image, ImageDraw, ImageFont
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# Use a Chinese brush-like font available on macOS
font_candidates = [
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/System/Library/Fonts/STHeiti Light.ttc",
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/Library/Fonts/Songti.ttc",
    "/System/Library/Fonts/Supplemental/Songti.ttc",
]
font = None
for p in font_candidates:
    if os.path.exists(p):
        try:
            font = ImageFont.truetype(p, 220)
            break
        except Exception:
            pass
if font is None:
    font = ImageFont.load_default()

char = "俎"
bbox = draw.textbbox((0, 0), char, font=font)
tw = bbox[2] - bbox[0]
th = bbox[3] - bbox[1]
x = (W - tw) // 2 - bbox[0]
y = (H - th) // 2 - bbox[1]
draw.text((x, y), char, fill="black", font=font)

out = os.path.join(os.path.dirname(__file__), "01_俎.png")
img.save(out)
print("wrote", out)
