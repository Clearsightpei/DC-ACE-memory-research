"""G1 render of 勻 (4 strokes): 撇 + 横折钩 (勹 enclosure) + two inner 横."""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
W = 5


def stroke(points, width=W):
    d.line(points, fill=INK, width=width, joint="curve")


# Stroke 1: 撇 — diagonal from upper-middle sweeping down-left (independent)
stroke([(155, 55), (135, 80), (110, 115), (95, 135)], width=W)

# Stroke 2: 横折钩 — the 勹 enclosure
# top short horizontal → down long → hook left at bottom
stroke(
    [
        (150, 82),     # start on top, right of where 撇 begins
        (210, 82),     # horizontal to right
        (215, 105),    # slight corner
        (218, 170),    # descending vertical (slight outward curve)
        (215, 225),    # continue
        (208, 245),    # bottom curve
        (188, 248),    # hook tip pointing left
    ],
    width=W,
)

# Stroke 3: upper inner 横 — short horizontal, centered in enclosure
stroke([(135, 150), (195, 148)], width=W)

# Stroke 4: lower inner 横 — short horizontal, centered in enclosure
stroke([(135, 190), (195, 188)], width=W)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_勻.png"))
print("wrote 01_勻.png")
