"""G1 render for p3_char_0416_侉 (侉 = 亻 + 夸)."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# Try to render using a system CJK font — cleanest & most faithful for Phase 3.
char = "侉"
font = None
candidates = [
    "/System/Library/Fonts/PingFang.ttc",
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/Library/Fonts/Songti.ttc",
    "/System/Library/Fonts/Supplemental/Songti.ttc",
]
for path in candidates:
    if os.path.exists(path):
        try:
            font = ImageFont.truetype(path, 240)
            break
        except Exception:
            continue

if font is not None:
    # Center the glyph on the canvas.
    bbox = draw.textbbox((0, 0), char, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    x = (W - tw) // 2 - bbox[0]
    y = (H - th) // 2 - bbox[1]
    draw.text((x, y), char, fill="black", font=font)
else:
    # Fallback: coarse stroke sketch.
    # 亻 (left radical)
    draw.line([(70, 60), (55, 130)], fill="black", width=4)   # 撇
    draw.line([(70, 100), (70, 240)], fill="black", width=4)  # 竖
    # 夸 top: 大
    draw.line([(150, 80), (240, 80)], fill="black", width=4)  # 一
    draw.line([(190, 60), (170, 130)], fill="black", width=4) # 撇
    draw.line([(190, 60), (230, 130)], fill="black", width=4) # 捺
    # 亏 bottom
    draw.line([(140, 160), (250, 160)], fill="black", width=4) # 一
    draw.line([(200, 160), (200, 220)], fill="black", width=4) # gou
    draw.line([(200, 220), (170, 240)], fill="black", width=4)

out = os.path.join(os.path.dirname(__file__), "01_侉.png")
img.save(out)
print("wrote", out)
