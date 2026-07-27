"""Render 孑 as 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 5

# Character 孑 (jié): 3 strokes
# 1) 横撇 (heng-pie): horizontal top that turns down-left at the right end
# 2) 横 (heng): horizontal through middle
# 3) 竖钩/弯钩 (curved vertical with hook at bottom) going down

# Stroke 1: 横撇 — starts upper-left, goes right, then turns down-left
# Top horizontal from ~(80, 90) to (200, 85)
draw.line([(80, 92), (200, 85)], fill=BLACK, width=LW)
# Then a downward-left slanted stroke (short 撇)
draw.line([(200, 85), (150, 140)], fill=BLACK, width=LW)

# Stroke 2: 横 — horizontal through the middle, roughly at y=155
draw.line([(90, 165), (230, 145)], fill=BLACK, width=LW)

# Stroke 3: 弯钩 — a curved vertical from top-center (~150,140) down
# curving slightly then ending with a small hook to the left at bottom
# Approximate curve with a series of points
curve_points = [
    (155, 140),
    (158, 170),
    (160, 200),
    (160, 230),
    (155, 255),
]
draw.line(curve_points, fill=BLACK, width=LW, joint="curve")
# hook to the left
draw.line([(155, 255), (130, 245)], fill=BLACK, width=LW)

out_path = os.path.join(os.path.dirname(__file__), "01_孑.png")
img.save(out_path)
print(f"Saved: {out_path}")
