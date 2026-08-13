"""G1 render of 块 (kuai). 300x300, PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
BLACK = (0, 0, 0)
LW = 4

def line(pts, w=LW):
    d.line(pts, fill=BLACK, width=w, joint="curve")

# --- 提土 radical (left side, roughly x=35..130) ---
# top horizontal (short)
line([(55, 115), (120, 110)])
# vertical
line([(88, 100), (88, 210)])
# bottom rising 提 (tí)
line([(45, 220), (135, 200)])

# --- 夬 (right side, roughly x=150..275) ---
# stroke 1: top short horizontal turning down (横折)
line([(165, 105), (240, 100)])
line([(240, 100), (235, 165)])
# stroke 2: middle horizontal closing partial box
line([(170, 155), (238, 152)])
# stroke 3: long horizontal (top of 大 crossing right side)
line([(150, 180), (275, 175)])
# stroke 4: 撇 (falling left) from upper area down-left
line([(215, 115), (160, 265)])
# stroke 5: 捺 (falling right) from cross area down-right
line([(210, 180), (280, 275)])

out = os.path.join(os.path.dirname(__file__), "01_块.png")
img.save(out)
print("wrote", out)
