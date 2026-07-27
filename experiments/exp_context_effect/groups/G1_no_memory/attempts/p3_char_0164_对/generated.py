"""G1 render of 对 (duì) — 5 strokes total.
Left component 又 (2 strokes): 横撇 (horizontal-turn-down-left) + 捺 (right-falling).
Right component 寸 (3 strokes): 一 (horizontal), 亅 (vertical hook), 丶 (dot).
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
STROKE_W = 5


def line(pts, width=STROKE_W):
    draw.line(pts, fill=INK, width=width, joint="curve")


# ---- LEFT: 又 (occupies roughly x=35..150, y=90..245) ----
# Stroke 1: 横撇 — horizontal top then sweeps down-left as a 撇
line([(50, 110), (140, 105), (55, 235)])

# Stroke 2: 捺 — starts from mid of 又, sweeps down-right past bottom
line([(90, 145), (165, 245)])

# ---- RIGHT: 寸 (occupies roughly x=165..280, y=90..260) ----
# Stroke 3: 一 horizontal (mid-height)
line([(170, 150), (280, 148)])

# Stroke 4: 亅 vertical with small hook at bottom-left
line([(230, 100), (230, 255), (215, 245)])

# Stroke 5: 丶 dot (short slanted stroke, upper-right of intersection)
line([(245, 165), (265, 185)], width=STROKE_W + 1)

out_path = os.path.join(os.path.dirname(__file__), "01_对.png")
img.save(out_path)
print(f"wrote {out_path}")
