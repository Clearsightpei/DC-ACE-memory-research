"""G1 render of 元 (Phase 3, char 0152).
4 strokes: short horizontal top, longer horizontal, left-falling (撇), vertical-hook (竖弯钩).
"""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
W = 8  # stroke width

# Stroke 1: short horizontal (top) — slightly slanted down-right, then flat
# roughly x=95..165, y=75
d.line([(95, 78), (170, 72)], fill=BLACK, width=W)

# Stroke 2: longer horizontal — x=55..230, y=118
d.line([(55, 122), (235, 115)], fill=BLACK, width=W)

# Stroke 3: 撇 (left-falling) — from around (125, 130) curving down-left to (75, 250)
# Draw as a smooth curve using multiple segments
pts_pie = [(128, 130), (118, 160), (105, 195), (90, 225), (72, 252)]
for i in range(len(pts_pie) - 1):
    d.line([pts_pie[i], pts_pie[i+1]], fill=BLACK, width=W)

# Stroke 4: 竖弯钩 (vertical bend hook) — starts near (175, 130), goes down, curves right, hook up
# Vertical portion
pts_hook = [
    (178, 132), (180, 170), (183, 210), (190, 235),
    (205, 252), (225, 258), (245, 255), (250, 235)  # curve right then hook up
]
for i in range(len(pts_hook) - 1):
    d.line([pts_hook[i], pts_hook[i+1]], fill=BLACK, width=W)

out_path = os.path.join(os.path.dirname(__file__), "01_元.png")
img.save(out_path)
print(f"Saved {out_path}")
