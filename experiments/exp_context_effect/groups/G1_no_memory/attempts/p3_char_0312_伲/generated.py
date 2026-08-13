"""G1 render of 伲 (person radical 亻 + 尼) — revision 1."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=4):
    d.line(pts, fill="black", width=width, joint="curve")

# --- Left radical 亻 (person) ---
# Piě: diagonal from upper right to lower left
stroke([(100, 75), (72, 205)], width=4)
# Shù: vertical from mid-piě going straight down
stroke([(90, 135), (92, 250)], width=4)

# --- Right part 尼 ---
# 尸 top: horizontal
stroke([(150, 90), (220, 88)], width=4)
# 尸: vertical drop from right end going down and slightly left (short)
stroke([(220, 88), (218, 130)], width=4)
# 尸 middle horizontal
stroke([(152, 128), (218, 128)], width=4)
# 尸: long piě sweeping down-left from left of top
stroke([(152, 90), (125, 210)], width=4)

# --- 匕 inside 尼 (bottom-right) ---
# Short piě starting inside 尸
stroke([(180, 155), (160, 195)], width=4)
# Horizontal-vertical-hook: like a shovel shape
# bottom curve: from left, across bottom, up on right with small hook
stroke([(155, 200), (155, 245), (235, 245), (235, 195), (225, 200)], width=4)

os.makedirs(os.path.dirname(__file__), exist_ok=True)
out = os.path.join(os.path.dirname(__file__), "01_伲.png")
img.save(out)
print("wrote", out)
