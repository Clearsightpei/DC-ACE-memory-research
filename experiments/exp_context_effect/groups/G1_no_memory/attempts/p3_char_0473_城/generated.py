"""Render 城 to 300x300 PNG. Left: 土. Right: 成."""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=3):
    d.line(pts, fill="black", width=width)

# ===== LEFT: 土 (earth) radical, in left third =====
# Short top horizontal
line([(35, 145), (100, 143)], width=3)
# Vertical stem
line([(68, 110), (66, 215)], width=3)
# Bottom horizontal — the 提 (rising stroke) as radical form, longer
line([(20, 215), (110, 208)], width=3)

# ===== RIGHT: 成 (occupies right ~2/3) =====
# 1. Small 横 top (short bar, upper-left of 成)
line([(140, 100), (175, 95)], width=3)
# 2. 撇 - the long left-descending curve from top going down-left, forms the left side of 成
line([(155, 95), (150, 170), (140, 240), (125, 275)], width=3)
# 3. Horizontal middle bar (short 横) inside 成
line([(165, 165), (220, 160)], width=3)
# 4. Vertical drop from middle-right of that bar, small hook (竖折)
line([(218, 160), (218, 200), (200, 208)], width=3)
# 5. Small 撇 stroke from center down-left (inside 成)
line([(190, 175), (170, 215)], width=3)
# 6. 斜钩 — the signature diagonal sweep of 成, from upper area down to lower-right with hook
line([(170, 115), (200, 155), (240, 210), (275, 260), (285, 245)], width=3)
# 7. Small 撇 near top-right (short down-left slash)
line([(238, 90), (225, 115)], width=3)
# 8. 点 (dot) at very top-right
line([(258, 85), (272, 100)], width=4)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0473_城/01_城.png")
print("saved")
