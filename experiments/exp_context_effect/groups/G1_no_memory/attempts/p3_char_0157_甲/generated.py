"""G1 render of 甲 — 5 strokes:
1. 竖 (left side of box)
2. 横折 (top + right side of box)
3. 横 (middle horizontal inside box)
4. 横 (bottom of box)
5. 竖 (long vertical through middle, extending well below the box)
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
T = 6  # stroke thickness

# Box coordinates
box_left = 80
box_right = 220
box_top = 55
box_bottom = 165
mid_y = 115
center_x = 150
bottom_v = 275  # bottom of long vertical

# Stroke 1: 竖 - left side of box
d.line([(box_left, box_top), (box_left, box_bottom)], fill=INK, width=T)

# Stroke 2: 横折 - top and right side (one continuous stroke)
d.line([(box_left, box_top), (box_right, box_top)], fill=INK, width=T)
d.line([(box_right, box_top), (box_right, box_bottom)], fill=INK, width=T)

# Stroke 3: 横 - middle horizontal
d.line([(box_left, mid_y), (box_right, mid_y)], fill=INK, width=T)

# Stroke 4: 横 - bottom of box
d.line([(box_left, box_bottom), (box_right, box_bottom)], fill=INK, width=T)

# Stroke 5: 竖 - long vertical through center, extending below the box
d.line([(center_x, box_top + 4), (center_x, bottom_v)], fill=INK, width=T)

out_path = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0157_甲/01_甲.png"
img.save(out_path)
print(f"Saved {out_path}")
