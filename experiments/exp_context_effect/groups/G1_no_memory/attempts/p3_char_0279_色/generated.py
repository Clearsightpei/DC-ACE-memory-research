"""G1 render of 色 (color) — 6 strokes.
Top: 刀-like component (撇 + 横折钩)
Bottom: 巴 component with 竖弯钩 curving out to lower-right
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

def line(pts, width=5):
    draw.line(pts, fill="black", width=width, joint="curve")

# --- Top component (刀-like) ---
# 撇: diagonal from upper-right area down-left
line([(155, 55), (95, 135)], width=5)
# 横折钩: horizontal top + right vertical + small hook
line([(115, 75), (190, 75)], width=5)
line([(190, 75), (180, 140)], width=5)
line([(180, 140), (165, 135)], width=5)  # small hook

# --- Bottom component: 巴 ---
# Stroke: 竖 (left side)
line([(100, 150), (100, 240)], width=5)
# Stroke: 横折 (top + right down)
line([(100, 150), (200, 150)], width=5)
line([(200, 150), (200, 200)], width=5)
# Stroke: middle horizontal
line([(100, 195), (200, 195)], width=5)
# Stroke: 竖弯钩 base — bottom horizontal extending right, curving up
line([(100, 240), (215, 240)], width=5)
line([(215, 240), (220, 215)], width=5)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0279_色/01_色.png")
print("saved")
