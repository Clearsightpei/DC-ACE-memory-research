"""Render 地 (earth) to 300x300 PNG. G1 no-memory attempt."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = "black"

def stroke(pts, w=5):
    d.line(pts, fill=INK, width=w, joint="curve")

# --- LEFT: 提土旁 (土 radical, narrower) ---
# short horizontal (slight up-right slant)
stroke([(30, 145), (110, 138)], w=5)
# long vertical through the horizontal
stroke([(68, 95), (68, 215)], w=5)
# 提 (rising bottom stroke)
stroke([(35, 235), (118, 210)], w=5)

# --- RIGHT: 也 ---
# top horizontal
stroke([(150, 120), (255, 118)], w=5)
# left short vertical hanging from the horizontal (slight left lean at bottom)
stroke([(165, 120), (158, 195)], w=5)
# middle vertical, longer, goes below into the 竖弯钩 bowl
stroke([(205, 100), (205, 240)], w=5)
# 竖弯钩 - starts from top-right of horizontal, drops down, curves left along bottom then hook up
# vertical part
stroke([(255, 118), (255, 225)], w=5)
# curve segment along bottom (using multi-point curve)
stroke([(255, 225), (252, 245), (240, 255), (215, 258), (185, 253)], w=5)
# hook up
stroke([(185, 253), (183, 235)], w=5)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0223_地/01_地.png")
print("saved")
