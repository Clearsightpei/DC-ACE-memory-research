"""Render 面 (face) at 300x300 using PIL."""
from PIL import Image, ImageDraw
from pathlib import Path

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
T = 4

def line(p1, p2, width=T):
    d.line([p1, p2], fill=INK, width=width)

# 面 breakdown (following GT):
# 1. Top short horizontal (一)
# 2. Left pie (丿) — starts near top-center, curves down-left to become the left wall of the box
# 3. Top horizontal of the big frame (横)
# 4. Right vertical (竖) with small hook
# 5. Bottom horizontal (横) — closes the frame
# 6. Upper inner horizontal (short 一)
# 7. Lower inner horizontal (short 一)

# 1. Top short horizontal
line((115, 60), (215, 65))

# 2. Pie (丿) - from top-center curving to lower-left, forms LEFT WALL of the frame
# Draw as segments approximating a curve
line((140, 60), (95, 110))
line((95, 110), (75, 260))

# 3. Top horizontal of the big frame — from around top of pie extends right
line((95, 110), (240, 110))

# 4. Right vertical with small hook
line((240, 110), (238, 258))
line((238, 258), (228, 265))

# 5. Bottom horizontal — closes frame from left wall bottom to right vertical bottom
line((75, 260), (238, 258))

# 6. Upper inner horizontal
line((115, 160), (215, 160))

# 7. Lower inner horizontal
line((115, 210), (215, 210))

out = Path(__file__).parent / "01_面.png"
img.save(out)
print(f"Saved {out}")
