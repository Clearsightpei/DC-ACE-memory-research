"""Render 选 (xuǎn) - 'select/choose' at 300x300."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=6):
    d.line(pts, fill="black", width=width, joint="curve")

# 选 = 先 (upper right) + 辶 (wraps bottom-left)

# --- 先 component (upper right) ---
# 1. Top short slant 丿
stroke([(170, 40), (155, 75)], width=6)

# 2. Upper short horizontal
stroke([(130, 85), (210, 85)], width=6)

# 3. Vertical down through both horizontals
stroke([(170, 60), (170, 165)], width=7)

# 4. Second longer horizontal
stroke([(105, 155), (235, 155)], width=6)

# 5. 儿 left leg (丿)
stroke([(150, 165), (120, 225)], width=6)

# 6. 儿 right leg with hook 乚
stroke([(190, 165), (200, 215), (235, 225)], width=7)

# --- 辶 radical (walking, wraps bottom-left) ---
# 7. Top dot 丶
stroke([(75, 65), (90, 80)], width=8)

# 8. Middle small 横折折 (zig)
stroke([(60, 115), (95, 110)], width=6)
stroke([(90, 115), (70, 140), (100, 140)], width=6)

# 9. Long sweeping bottom 平捺
stroke([(55, 205), (75, 245), (170, 260), (255, 240), (280, 220)], width=8)

out_path = os.path.join(os.path.dirname(__file__), "01_选.png")
img.save(out_path)
print(f"Saved {out_path}")
