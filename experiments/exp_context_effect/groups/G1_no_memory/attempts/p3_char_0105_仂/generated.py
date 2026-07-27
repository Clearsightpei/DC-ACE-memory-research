"""G1 render for 仂 = 亻(left) + 力(right)."""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

def stroke(pts, w=7):
    d.line(pts, fill="black", width=w, joint="curve")
    r = w // 2
    for (x, y) in [pts[0], pts[-1]]:
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")

# --- 亻 person radical (left) ---
# 撇 (piě): from upper area sweeping down-left
stroke([(110, 55), (95, 120), (75, 180), (55, 235)], w=7)
# 竖 (shù): vertical starting from mid of 撇
stroke([(105, 130), (108, 265)], w=7)

# --- 力 (right) ---
# 横折钩: top horizontal → turn down → hook
stroke([(140, 95), (240, 90)], w=7)                                # 横
stroke([(240, 90), (232, 160), (215, 220), (195, 245)], w=7)       # 折 curve down
stroke([(195, 245), (178, 232)], w=7)                              # 钩
# 撇: from upper-left of 力 diagonally down-left through bottom
stroke([(165, 130), (155, 190), (135, 250), (120, 275)], w=7)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_仂.png"))
print("wrote", os.path.join(out_dir, "01_仂.png"))
