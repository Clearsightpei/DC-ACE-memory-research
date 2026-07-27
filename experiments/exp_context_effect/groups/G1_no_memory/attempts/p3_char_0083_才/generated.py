"""Render 才 as a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
TH = 6

def line(p1, p2, w=TH):
    d.line([p1, p2], fill=INK, width=w)
    r = w // 2
    for (x, y) in (p1, p2):
        d.ellipse([x - r, y - r, x + r, y + r], fill=INK)

# 才 has 3 strokes:
#   1) 一 (horizontal), slight upward tilt to the right
#   2) 亅 (vertical hook), crosses horizontal at its right-of-center,
#      goes to near bottom, small hook toward upper-left
#   3) 丿 (left-falling), starts at intersection, curves down-left

# Stroke 1: horizontal, mid-upper, spans most of width
line((45, 128), (250, 112), TH)

# Stroke 2: vertical hook — starts above horizontal, ends near bottom w/ hook
# top slightly right of horizontal midpoint
line((172, 78), (158, 262), TH)
# hook to upper-left
line((158, 262), (128, 248), TH)

# Stroke 3: 丿 left-falling curve, starts at intersection of 一 and 亅
curve_pts = [
    (165, 122),
    (145, 155),
    (120, 195),
    (95, 235),
    (68, 268),
]
for a, b in zip(curve_pts, curve_pts[1:]):
    line(a, b, TH)

out_path = os.path.join(os.path.dirname(__file__), "01_才.png")
img.save(out_path)
print("wrote", out_path)
