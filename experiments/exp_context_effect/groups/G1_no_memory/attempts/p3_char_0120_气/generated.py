"""G1 render of 气 (qi) - 4 strokes: piě, héng, héng, héngzhéwāngōu."""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

W = 7  # stroke width

def line(pts):
    d.line(pts, fill="black", width=W, joint="curve")

def curve(pts, steps=50):
    (x0, y0), (x1, y1), (x2, y2) = pts
    prev = (x0, y0)
    for i in range(1, steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * x1 + t * t * x2
        y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * y1 + t * t * y2
        d.line([prev, (x, y)], fill="black", width=W)
        prev = (x, y)

# Stroke 1: piě (short slanting stroke) at top - descending from upper-right to lower-left
line([(155, 70), (75, 100)])

# Stroke 2: middle short horizontal (slightly rising to the right)
line([(90, 130), (185, 122)])

# Stroke 3: longer horizontal at bottom-left region (slightly rising)
line([(60, 185), (200, 175)])

# Stroke 4: 横折弯钩 - starts at upper right (near end of stroke 1 / top of char),
# goes horizontally right, turns down, curves left/down, ends with hook.
# Piece A: top horizontal segment (starts high, near where piě ends its right side)
line([(155, 100), (225, 108)])
# Piece B: vertical-ish drop with slight rightward bow
curve([(225, 108), (240, 200), (215, 260)])
# Piece C: hook curling up-left at the end
line([(215, 260), (232, 245)])

out = os.path.join(os.path.dirname(__file__), "01_气.png")
img.save(out)
print(f"Saved {out}")
