"""G1 render for character 门 (mén, door). 3 strokes."""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

W = 7  # ink width

# Stroke 1: 点 (short diagonal dot) — upper-left, sits above the vertical
draw.line([(95, 75), (78, 105)], fill="black", width=W)

# Stroke 2: 竖 (left vertical) — starts a bit below the dot
draw.line([(80, 115), (78, 260)], fill="black", width=W)

# Stroke 3: 横折钩 (horizontal-fold-hook) — right side of the door
# Top horizontal
draw.line([(115, 95), (220, 92)], fill="black", width=W)
# Right vertical (down)
draw.line([(220, 92), (222, 255)], fill="black", width=W)
# Hook at bottom going left-down
draw.line([(222, 255), (195, 268)], fill="black", width=W)

out_path = os.path.join(os.path.dirname(__file__), "01_门.png")
img.save(out_path)
print(f"Saved {out_path}")
