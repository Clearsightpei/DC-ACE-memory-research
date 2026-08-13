"""G1 render of 伢 (person radical 亻 + 牙).
300x300, white bg, black ink."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = "black"
LW = 4

# --- Left: 亻 (person radical) ---
# 撇: short falling diagonal
d.line([(95, 100), (55, 180)], fill=INK, width=LW)
# 竖: long vertical
d.line([(90, 130), (90, 255)], fill=INK, width=LW)

# --- Right: 牙 ---
# Stroke 1: short 撇 at very top-left of 牙 (small diagonal down-left)
d.line([(180, 95), (165, 120)], fill=INK, width=LW)
# Stroke 2: 横 (top horizontal) then 折 down (horizontal-fold)
d.line([(165, 118), (240, 115)], fill=INK, width=LW)  # top horizontal
d.line([(240, 115), (235, 165)], fill=INK, width=LW)  # fold down
# Stroke 3: middle 横 (shelf) crossing left to right, meeting the fold
d.line([(150, 165), (235, 160)], fill=INK, width=LW)
# Stroke 4: 竖钩 — long vertical from middle-right area down with small hook
d.line([(215, 160), (215, 255)], fill=INK, width=LW)
d.line([(215, 255), (200, 248)], fill=INK, width=LW)  # small hook left
# Stroke 5: long 撇 sweeping from upper-middle down-left to lower-left
d.line([(200, 135), (140, 265)], fill=INK, width=LW)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_伢.png"))
print("wrote 01_伢.png")
