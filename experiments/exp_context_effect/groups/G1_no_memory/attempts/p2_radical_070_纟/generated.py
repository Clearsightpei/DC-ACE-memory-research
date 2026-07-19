"""G1 render for radical 纟 (3画, silk-radical top form).

Three strokes, top-to-bottom:
  1. 撇折 upper: small down-left slant, then a short sharp right-down turn.
  2. 撇折 middle: same shape, slightly larger and lower.
  3. 提 (ti): rising diagonal from lower-left to upper-right at the base.
"""

from PIL import Image, ImageDraw
import os

W, H = 300, 300
INK = 0
BG = 255

img = Image.new("L", (W, H), BG)
draw = ImageDraw.Draw(img)


def poly(points, width):
    """Draw a smooth polyline with rounded joints/caps."""
    for i in range(len(points) - 1):
        draw.line([points[i], points[i + 1]], fill=INK, width=width)
    r = width // 2
    for x, y in points:
        draw.ellipse((x - r, y - r, x + r, y + r), fill=INK)


# --- Stroke 1: upper 撇折 ---
# short pie (down-left), then折 to short down-right hook segment.
stroke1 = [
    (150, 85),   # start (upper-right)
    (135, 100),  # pie down-left
    (128, 118),  # continue pie
    (150, 118),  # 折 turn right
    (162, 128),  # tiny hook down-right
]
poly(stroke1, width=6)

# --- Stroke 2: middle 撇折 (larger, lower) ---
stroke2 = [
    (155, 135),
    (135, 155),
    (122, 178),
    (155, 178),
    (172, 188),
]
poly(stroke2, width=6)

# --- Stroke 3: 提 (rising diagonal at bottom) ---
stroke3 = [
    (100, 235),
    (145, 225),
    (200, 210),
]
poly(stroke3, width=7)

out_path = os.path.join(os.path.dirname(__file__), "01_纟.png")
img.save(out_path)
print(f"wrote {out_path}")
