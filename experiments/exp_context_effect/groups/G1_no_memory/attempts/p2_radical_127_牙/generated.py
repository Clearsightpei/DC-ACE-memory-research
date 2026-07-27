"""G1 render of radical 牙 (4 strokes) — revised."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"

def stroke_curve(pts, width=4):
    d.line(pts, fill=INK, width=width, joint="curve")

# 牙 stroke order (standard):
# 1) 横 (short horizontal at top)
# 2) 竖折 (short vertical then horizontal) forming the small box on the left
# 3) 撇 (long diagonal from upper right sweeping down-left)
# 4) 竖钩 (long vertical on the right with hook at bottom-left)

# Coordinates for a 300x300 image, character bounded roughly x=70..230, y=70..260

# Stroke 1: top horizontal — from upper-left across to upper-right
s1 = [(95, 95), (140, 92), (190, 90), (210, 92)]
stroke_curve(s1, width=5)

# Stroke 2: 竖折 — starts near left end of stroke 1, goes down, then right (a small L)
# Vertical portion
s2 = [(105, 95), (103, 125), (102, 155)]
stroke_curve(s2, width=5)
# Horizontal portion continuing
s2b = [(102, 155), (140, 152), (185, 150), (205, 152)]
stroke_curve(s2b, width=5)

# Stroke 3: 撇 — long diagonal sweeping from upper-right of the middle horizontal down to bottom-left
# Starts around top-right area (near end of stroke 1) and curves down-left
s3 = [(175, 108), (155, 145), (130, 180), (100, 220), (70, 265)]
stroke_curve(s3, width=5)

# Stroke 4: 竖钩 — long vertical on the right, ends with small hook to the left at bottom
s4 = [(207, 100), (208, 150), (209, 200), (210, 250), (207, 265)]
stroke_curve(s4, width=5)
# hook: small curve to left at bottom
hook = [(210, 258), (202, 268), (192, 270)]
stroke_curve(hook, width=5)

out_path = os.path.join(os.path.dirname(__file__), "01_牙.png")
img.save(out_path)
print("Saved:", out_path)
