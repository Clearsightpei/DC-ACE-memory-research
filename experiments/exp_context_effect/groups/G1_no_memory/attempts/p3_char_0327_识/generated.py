"""Render 识 (shi) - simplified form.
Structure: 讠 (speech radical, left) + 只 (right).
"""
from PIL import Image, ImageDraw

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)
W = 6


def line(pts, w=W):
    d.line(pts, fill="black", width=w, joint="curve")


# ============ Left: 讠 (speech radical, simplified) ============
# Top dot (short diagonal stroke)
line([(70, 70), (85, 90)], w=W)

# Horizontal-fold-hook: goes right then down-left as the "reverse L"
# In simplified 讠 the second stroke is like a short horizontal then turning down
line([(55, 115), (110, 115), (75, 200)], w=W)

# ============ Right: 只 ============
# Top: 口 (small square-ish mouth)
# Left side of 口
line([(150, 100), (150, 145)], w=W)
# Top of 口
line([(150, 100), (215, 100)], w=W)
# Right side of 口 (with slight turn)
line([(215, 100), (215, 145)], w=W)
# Bottom of 口
line([(150, 145), (215, 145)], w=W)

# Bottom of 只: 撇 and 点/捺 flare out from bottom of 口
# 撇 - falling left stroke
line([(165, 148), (130, 235)], w=W)
# 捺 - falling right stroke
line([(200, 148), (245, 235)], w=W)

out_path = __file__.rsplit("/", 1)[0] + "/01_识.png"
img.save(out_path)
print("saved", out_path)
