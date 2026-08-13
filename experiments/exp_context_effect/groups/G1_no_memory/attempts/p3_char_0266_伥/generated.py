"""Render 伥 = 亻 (person radical) + 长 (long) to a 300x300 PNG."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=6):
    d.line(pts, fill="black", width=width, joint="curve")

# --- 亻 (person radical), left side, spans ~y 70-235 ---
# 撇: diagonal from upper right sloping down-left
stroke([(95, 75), (55, 200)], width=7)
# 丨: vertical starting from where the 撇 was, going down
stroke([(90, 130), (90, 240)], width=7)

# --- 长 on the right side, spans ~x 130-265, y 70-265 ---
# Stroke 1: 撇 (short down-left slant near top)
stroke([(175, 75), (150, 130)], width=6)
# Stroke 2: 横 (horizontal top)
stroke([(155, 115), (230, 110)], width=6)
# Stroke 3: 竖提 - vertical going down then a small hook up-right
stroke([(170, 130), (170, 220)], width=7)
stroke([(170, 220), (210, 210)], width=6)
# Stroke 4: 撇 - long sweeping diagonal from upper mid down-left
stroke([(215, 130), (135, 255)], width=7)
# Stroke 5: 捺 - long sweep to lower right, starting mid
stroke([(190, 175), (270, 265)], width=8)

out = os.path.join(os.path.dirname(__file__), "01_伥.png")
img.save(out)
print("Wrote", out)
