"""G1 render for p3_char_0119_仓 (character 仓). Revision 2."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
LW = 5

def line(p0, p1, width=LW):
    draw.line([p0, p1], fill=INK, width=width)

def polyline(pts, width=LW):
    for i in range(len(pts) - 1):
        line(pts[i], pts[i+1], width)

# 仓: roof 人 on top, 横钩 below, small 口-like shape, bottom 乚 (vertical hook)
# Roof apex a bit higher; legs come down further
# Stroke 1: 撇 (left-falling from apex)
polyline([(150, 50), (130, 80), (100, 130), (65, 210)], width=LW)

# Stroke 2: 捺 (right-falling from apex)
polyline([(150, 50), (172, 85), (205, 135), (240, 190)], width=LW)

# Stroke 3: 横钩 under the roof — horizontal with a short down-hook at right end
polyline([(110, 135), (195, 135)], width=LW)
polyline([(195, 135), (188, 148)], width=LW)

# Small enclosed shape (口-like) in middle, sitting under 横钩
# left vertical
polyline([(120, 165), (120, 210)], width=LW)
# top
polyline([(120, 165), (180, 165)], width=LW)
# right vertical with tiny down-hook
polyline([(180, 165), (180, 205)], width=LW)
# bottom
polyline([(120, 210), (180, 210)], width=LW)

# Bottom 乚 (vertical then right-turn hook) — enclosing base of 仓
polyline([(205, 155), (205, 250), (245, 250)], width=LW)

out_path = os.path.join(os.path.dirname(__file__), "01_仓.png")
img.save(out_path)
print(f"Saved {out_path}")
