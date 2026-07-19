"""G1 attempt: 殳 (radical 118, 4 strokes).

殳 has 4 strokes:
  Top part (like 几/儿-ish enclosure):
    1. 撇 (short slanted stroke on upper-left)
    2. 横折弯 (horizontal-turn-bend on the right)
  Bottom part 又:
    3. 横撇 (horizontal that turns into a long left-diagonal 撇)
    4. 捺 (right-diagonal crossing stroke 3)
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

LW = 5

def curve(points, width=LW):
    for i in range(len(points) - 1):
        d.line([points[i], points[i+1]], fill="black", width=width)
    for p in points:
        d.ellipse([p[0]-width/2, p[1]-width/2, p[0]+width/2, p[1]+width/2], fill="black")

# ---- Top part ----
# Stroke 1: 撇 — short slanted stroke starting near top going down-left
curve([(118, 70), (108, 90), (95, 115), (85, 145), (80, 160)])

# Stroke 2: 横折弯 — horizontal along top, turns down on the right,
#            gently curves left with a small tail
curve([
    (118, 70),
    (140, 68), (165, 70), (185, 78),
    (192, 92), (190, 115), (185, 140),
    (175, 155), (162, 162), (150, 160),
    (145, 152),
])

# ---- Bottom part 又 ----
# Stroke 3: 横撇 — a short horizontal that turns and descends left as a long 撇
curve([
    (70, 178), (110, 175), (145, 172), (160, 175),
    (150, 195), (128, 220), (100, 245), (75, 262),
])

# Stroke 4: 捺 — right-diagonal originating from middle, crossing stroke 3
curve([
    (115, 195), (140, 220), (170, 245), (200, 260), (225, 265),
])

os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_殳.png")
img.save(out)
print(f"Saved {out}")
