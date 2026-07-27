"""Render 无 (4-stroke radical) to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
TH = 5  # stroke thickness


def line(p1, p2, width=TH):
    draw.line([p1, p2], fill=INK, width=width)


def poly(pts, width=TH):
    for i in range(len(pts) - 1):
        line(pts[i], pts[i + 1], width)


# Stroke 1: top short horizontal (upper 横), slightly tilted up-right
poly([(115, 95), (200, 88)])

# Stroke 2: second horizontal (longer, main 横), slightly tilted
poly([(70, 150), (220, 142)])

# Stroke 3: left downward 撇 - starts near top-right of stroke1/upper area,
# curves down and to the left, ending near lower-left
poly([
    (150, 100),
    (140, 150),
    (120, 200),
    (95, 245),
    (75, 265),
])

# Stroke 4: 竖弯钩 - starts near right end of second horizontal,
# goes straight down, then curves right, ending with small upward hook
poly([
    (185, 145),
    (188, 200),
    (192, 235),
    (205, 255),
    (230, 260),
    (245, 255),
    (248, 245),
])

out = os.path.join(os.path.dirname(__file__), "01_无.png")
img.save(out)
print("saved", out)
