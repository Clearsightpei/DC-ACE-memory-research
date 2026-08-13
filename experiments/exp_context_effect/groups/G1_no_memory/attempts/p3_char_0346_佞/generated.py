from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, w=5):
    d.line(pts, fill="black", width=w)

def curve(pts, w=5):
    # smooth polyline
    d.line(pts, fill="black", width=w, joint="curve")

# 佞 = 亻 (left) + 二 (top-right) + 女 (bottom-right)

# --- 亻 person radical (left) ---
# piě (slanting stroke down-left)
curve([(75, 65), (65, 110), (50, 165), (35, 200)], w=6)
# shù (vertical from mid-piě going down)
line([(68, 130), (68, 270)], w=6)

# --- 二 (top-right) ---
# top short horizontal
line([(150, 90), (245, 85)], w=5)
# second horizontal (longer, lower)
line([(130, 145), (265, 140)], w=5)

# --- 女 (bottom-right) ---
# Stroke 1: 撇点 (piě + diǎn) — curved down-left then a diagonal turn
curve([(180, 165), (165, 195), (150, 215), (140, 230)], w=5)
curve([(140, 230), (160, 235), (180, 245)], w=5)
# Stroke 2: long 撇 across from upper right down to lower left
curve([(230, 165), (210, 200), (180, 240), (140, 285)], w=5)
# Stroke 3: horizontal across middle
line([(120, 240), (275, 240)], w=5)

out = os.path.join(os.path.dirname(__file__), "01_佞.png")
img.save(out)
print("wrote", out)
