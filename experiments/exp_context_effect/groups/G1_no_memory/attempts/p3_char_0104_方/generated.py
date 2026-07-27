"""G1 render of 方 — 4 strokes, PIL, 300x300 white bg / black ink."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 6

def stroke(pts, width=LW):
    d.line(pts, fill=BLACK, width=width, joint="curve")
    # rounded caps
    r = width / 2
    for (x, y) in [pts[0], pts[-1]]:
        d.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)

# Stroke 1: top dot / short slanted stroke (点)
# small stroke slanting down-right near top-center
stroke([(140, 55), (168, 82)], width=7)

# Stroke 2: long horizontal (横) crossing middle-upper area
# Slightly rising to the right
stroke([(45, 118), (255, 110)], width=7)

# Stroke 3: left-falling curve (撇) — starts around center just under horizontal,
# curves down-left to bottom-left corner
s3 = [
    (132, 122),
    (122, 155),
    (105, 190),
    (80, 225),
    (52, 260),
    (35, 280),
]
stroke(s3, width=7)

# Stroke 4: horizontal-fold-hook (横折钩) — small enclosed shape hanging from
# the main horizontal, sitting to the right of the pie's start
s4_h    = [(132, 152), (215, 155)]                     # short horizontal top of the box
s4_v    = [(215, 155), (208, 220), (198, 250)]         # down, curving slightly left
s4_hook = [(198, 250), (170, 258), (150, 245)]         # hook curling back up-left
stroke(s4_h, width=7)
stroke(s4_v, width=7)
stroke(s4_hook, width=7)

out = os.path.join(os.path.dirname(__file__), "01_方.png")
img.save(out)
print("wrote", out)
