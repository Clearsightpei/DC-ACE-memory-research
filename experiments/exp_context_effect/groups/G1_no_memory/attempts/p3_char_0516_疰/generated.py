"""G1 render of 疰 (illness radical 疒 + 主)."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# --- 疒 radical (sickness) ---
# 1) top dot (short slanted stroke) sitting on top of the roof
line([(120, 30), (135, 50)], width=6)

# 2) horizontal roof (点 + 横) going right
line([(80, 65), (230, 60)], width=6)

# 3) long left-falling curve (丿) from roof down to bottom-left
line([(105, 65), (95, 110), (75, 170), (50, 260)], width=6)

# 4) two small strokes on left side (like 冫)
line([(90, 105), (108, 122)], width=5)   # upper dot
line([(80, 155), (98, 172)], width=5)   # lower dot

# --- 主 inside (sits under the roof, right of 丿) ---
# top dot of 主
line([(165, 80), (178, 100)], width=6)

# top short horizontal
line([(135, 120), (215, 118)], width=6)

# middle short horizontal
line([(140, 170), (220, 168)], width=6)

# vertical through center of 主
line([(175, 102), (175, 240)], width=6)

# bottom long horizontal (base of 主)
line([(115, 240), (255, 238)], width=6)

out = os.path.join(os.path.dirname(__file__), "01_疰.png")
img.save(out)
print("wrote", out)
