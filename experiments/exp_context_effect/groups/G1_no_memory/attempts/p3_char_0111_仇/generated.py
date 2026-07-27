"""Render 仇 (chóu) — 4 strokes: 亻 (ノ丨) + 九 (丿横折弯钩)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 7

def curve(pts, width=LW):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=BLACK, width=width, joint="curve")
    # round the endpoints
    for p in (pts[0], pts[-1]):
        d.ellipse([p[0]-width//2, p[1]-width//2, p[0]+width//2, p[1]+width//2], fill=BLACK)

# --- Left: 亻 (person radical) ---
# Stroke 1: 撇 — slanted left-falling from upper area down-left
s1 = [(105, 55), (98, 90), (85, 130), (68, 170), (55, 200)]
curve(s1)

# Stroke 2: 丨 vertical — meets the 撇 partway down
s2 = [(95, 105), (95, 265)]
curve(s2)

# --- Right: 九 ---
# Stroke 3: 丿 — from upper-right down-left
s3 = [(175, 80), (162, 115), (145, 155), (128, 195), (118, 220)]
curve(s3)

# Stroke 4: 横折弯钩 — top horizontal, right turn down, curve, hook up
s4 = [
    (155, 110),
    (185, 105),
    (215, 108),
    (240, 118),
    (250, 140),
    (252, 175),
    (250, 210),
    (248, 240),
    (255, 258),
    (270, 250),
    (278, 235),
]
curve(s4)

out = os.path.join(os.path.dirname(__file__), "01_仇.png")
img.save(out)
print(f"wrote {out}")
