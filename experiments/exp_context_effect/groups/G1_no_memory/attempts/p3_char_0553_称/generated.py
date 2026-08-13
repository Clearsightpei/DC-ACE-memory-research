from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# 称 = 禾 (left) + 尔 (right)
# --- Left: 禾 (grain radical, 5 strokes)
# 1. Top short 撇 (downward-left slant at top)
stroke([(100, 55), (75, 85)], width=5)
# 2. Horizontal 一
stroke([(38, 100), (140, 96)], width=5)
# 3. Vertical 丨 with slight hook at bottom
stroke([(90, 82), (90, 235), (95, 240)], width=5)
# 4. Left slant 撇 from just below the cross
stroke([(90, 118), (40, 190)], width=5)
# 5. Right slant 捺
stroke([(90, 118), (145, 195)], width=5)

# --- Right: 尔 (5 strokes)
# 1. Top-left slant 撇 (top of 尔)
stroke([(210, 55), (185, 100)], width=5)
# 2. Top-right slant (dot/pie)
stroke([(210, 60), (240, 100)], width=5)
# 3. Horizontal middle bar
stroke([(160, 130), (260, 128)], width=5)
# 4. Central vertical with hook (going right)
stroke([(210, 130), (210, 240), (218, 235)], width=5)
# 5. Left 撇 dot
stroke([(190, 150), (170, 220)], width=5)
# 6. Right 点 dot
stroke([(238, 150), (255, 215)], width=5)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_称.png"))
print("saved")
