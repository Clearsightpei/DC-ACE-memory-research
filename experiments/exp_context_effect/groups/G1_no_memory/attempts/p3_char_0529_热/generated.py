"""G1 render for 热 (p3_char_0529). Cold render, no memory."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# Try common macOS Chinese fonts
candidates = [
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/System/Library/Fonts/STHeiti Light.ttc",
    "/System/Library/Fonts/PingFang.ttc",
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/Library/Fonts/Songti.ttc",
    "/System/Library/Fonts/Supplemental/Songti.ttc",
]
font = None
for p in candidates:
    if os.path.exists(p):
        try:
            font = ImageFont.truetype(p, 220)
            break
        except Exception:
            continue

char = "热"
if font is not None:
    # measure and center
    bbox = draw.textbbox((0, 0), char, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    x = (W - tw) // 2 - bbox[0]
    y = (H - th) // 2 - bbox[1]
    draw.text((x, y), char, fill="black", font=font)
else:
    # fallback: crude turtle-style stroke skeleton
    # top-left 扌 (hand radical)
    draw.line([(60, 100), (130, 100)], fill="black", width=6)  # horizontal
    draw.line([(95, 60), (95, 190)], fill="black", width=6)   # vertical
    draw.line([(95, 190), (130, 170)], fill="black", width=6) # hook
    draw.line([(60, 150), (100, 130)], fill="black", width=6) # tick
    # top-right 丸-like
    draw.line([(150, 80), (230, 80)], fill="black", width=6)
    draw.line([(200, 60), (170, 200)], fill="black", width=6)
    draw.arc([(160, 100), (260, 220)], start=270, end=60, fill="black", width=6)
    draw.line([(220, 120), (240, 110)], fill="black", width=6)
    # bottom 灬
    for x0 in (80, 130, 180, 230):
        draw.line([(x0, 240), (x0 + 8, 275)], fill="black", width=5)

out = os.path.join(os.path.dirname(__file__), "01_热.png")
img.save(out, "PNG")
print(f"wrote {out}")
