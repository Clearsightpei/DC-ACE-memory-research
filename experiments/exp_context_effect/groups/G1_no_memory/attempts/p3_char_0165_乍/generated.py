"""Render 乍 (character p3_char_0165) to a 300x300 PNG."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
INK = (0, 0, 0)
BG = (255, 255, 255)
img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

def line(p0, p1, width=5):
    d.line([p0, p1], fill=INK, width=width)

# 乍 stroke order (5 strokes):
# 1) 撇 (piě) — slanted stroke from upper-mid-right down to lower-left
# 2) 横 (héng) — top short horizontal (at top of vertical)
# 3) 竖 (shù) — vertical drop from top-right area going down through middle-bottom
# 4) 横 (héng) — middle horizontal on right
# 5) 横 (héng) — bottom horizontal on right

# Stroke 1: 撇 — long diagonal down-left, gently curved
# approximate with two segments to suggest curvature
line((150, 55), (110, 130), width=5)
line((110, 130), (70, 200), width=5)

# Stroke 2: top short horizontal (near top of the vertical)
line((135, 90), (200, 90), width=5)

# Stroke 3: 竖 — vertical drop through middle to bottom
line((145, 90), (145, 265), width=5)

# Stroke 4: middle horizontal on right
line((145, 165), (225, 165), width=5)

# Stroke 5: bottom horizontal on right
line((145, 235), (225, 235), width=5)

out = os.path.join(os.path.dirname(__file__), "01_乍.png")
img.save(out)
print("wrote", out)
