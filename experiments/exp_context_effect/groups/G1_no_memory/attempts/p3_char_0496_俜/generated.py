"""G1 render for 俜 (p3_char_0496).
Uses PIL with a system Chinese font to render a 300x300 black-ink glyph
on white. Kept intentionally simple per G1 policy (no memory).
"""
from PIL import Image, ImageDraw, ImageFont
import os

OUT = os.path.join(os.path.dirname(__file__), "01_俜.png")

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# Try common macOS CJK fonts
candidates = [
    "/System/Library/Fonts/PingFang.ttc",
    "/System/Library/Fonts/STHeiti Medium.ttc",
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

char = "俜"
if font is not None:
    bbox = draw.textbbox((0, 0), char, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    x = (W - tw) // 2 - bbox[0]
    y = (H - th) // 2 - bbox[1]
    draw.text((x, y), char, fill="black", font=font)
else:
    # Fallback: draw an X so failure is visible
    draw.line((20, 20, 280, 280), fill="black", width=5)
    draw.line((20, 280, 280, 20), fill="black", width=5)

img.save(OUT)
print(f"Saved {OUT}")
