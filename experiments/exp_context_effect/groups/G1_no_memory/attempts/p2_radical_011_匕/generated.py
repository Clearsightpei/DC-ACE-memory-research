"""G1 render of radical 匕 (2 strokes) — first render."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

def stroke(points, width=6):
    draw.line(points, fill="black", width=width, joint="curve")
    # rounded end caps
    r = width // 2
    for (x, y) in (points[0], points[-1]):
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")

# Stroke 1: 撇 — in GT this is a mostly-vertical stroke down the left side of
# the character, curving slightly leftward at the bottom. Starts high-left,
# ends near the bottom-left where stroke 2 will curve past.
s1 = [(102, 90), (100, 130), (97, 170), (92, 205), (85, 225)]
stroke(s1, width=6)

# Stroke 2: 横 (top rightward segment that crosses stroke 1) + 竖弯钩. In MMH
# this is often written as a single 竖弯钩-like stroke starting from a short
# horizontal-rightward top. Here we treat it as one path: start on stroke 1
# around (105, 115), go up-right to (180, 105) (the crossing 横 part), then
# the reader's eye continues to the lower bowl. Actually GT shows this as
# two visual segments — the top 横 and the bottom 竖弯钩 — but MMH encodes
# stroke 2 as the crossing top. Let me draw both as one continuous ink path
# to match GT silhouette.
# Segment A (top crossing rightward): (105, 118) -> (185, 105)
sA = [(105, 118), (140, 112), (175, 106), (188, 104)]
stroke(sA, width=6)

# Segment B (the bowl / 竖弯钩): descends from stroke1 lower area, curves
# right along bottom, hooks up on the right.
sB = [
    (95, 210),
    (100, 235),
    (135, 250),
    (185, 250),
    (215, 245),
    (222, 225),
    (222, 200),
]
stroke(sB, width=6)

out = os.path.join(os.path.dirname(__file__), "01_匕.png")
img.save(out)
print(out)
