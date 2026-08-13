"""Render 俳 (person radical 亻 + 非) to a 300x300 PNG."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(p1, p2, w=5):
    d.line([p1, p2], fill="black", width=w)

# --- 亻 (person radical, left) ---
# short slash from upper area, going down-left
line((80, 70), (55, 130), w=5)
# long vertical stroke
line((85, 90), (85, 260), w=5)

# --- 非 (right side) ---
# Two verticals
left_v_x = 155
right_v_x = 235

# Left vertical of 非
line((left_v_x, 75), (left_v_x, 260), w=5)
# Right vertical of 非
line((right_v_x, 75), (right_v_x, 260), w=5)

# Three horizontal short strokes on left side (pointing left from the left vertical)
# In 非, left side has 3 horizontals going left
for y in [110, 155, 200]:
    line((left_v_x - 45, y), (left_v_x, y), w=4)

# Three horizontal short strokes on right side (pointing right from the right vertical)
# Actually in 非, the right side has 3 horizontals attached to the right vertical, going left
# Looking at GT: the right vertical has 3 short horizontals going LEFT toward the left vertical
for y in [110, 155, 200]:
    line((right_v_x - 45, y), (right_v_x, y), w=4)

# Also the top of the left vertical typically has a small horizontal going right (top bar of 非)
# Looking at GT: there's a short horizontal at top of left vertical going right
# Actually 非 structure: left vertical with 3 horizontals going LEFT out of it,
# right vertical with 3 horizontals going LEFT into it
# Let me redo — clear and redraw

img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

# 亻
line((80, 75), (55, 135), w=5)     # short slash
line((88, 100), (88, 265), w=5)    # vertical

# 非 - left half
lv = 150
line((lv, 75), (lv, 265), w=5)     # left vertical
# 3 horizontals going LEFT from left vertical
for y in [105, 155, 205]:
    line((lv - 45, y), (lv, y), w=4)

# 非 - right half
rv = 235
line((rv, 75), (rv, 265), w=5)     # right vertical
# 3 horizontals going RIGHT from right vertical (toward outside)
# Wait, looking at GT again: right side horizontals go RIGHT (outward)
for y in [105, 155, 205]:
    line((rv, y), (rv + 45, y), w=4)

out = os.path.join(os.path.dirname(__file__), "01_俳.png")
img.save(out)
print("saved", out)
