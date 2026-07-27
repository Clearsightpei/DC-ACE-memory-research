"""G1 render for 皿 (dish/vessel radical)."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)
INK = "black"
LW = 6

# 皿 has 5 strokes:
# 1. Left vertical (slightly slanted inward at bottom): 丨
# 2. Top horizontal
# 3. Middle vertical
# 4. Right vertical (slanted inward at bottom): 丨
# 5. Bottom long horizontal (widest)

# Layout — occupy roughly middle band vertically, wide horizontally
# Top of box ~ y=95, bottom of box ~ y=205, bottom horizontal ~ y=225
top_y = 95
box_bot_y = 205
bot_hline_y = 228

# Top horizontal edges (a bit narrower than bottom)
top_left_x = 85
top_right_x = 215

# Bottom of interior verticals (slightly narrower — legs kick inward)
inner_bl_x = 92
inner_br_x = 208

# Bottom long horizontal (widest)
hline_left = 55
hline_right = 250

# Middle vertical positions at top and bottom
mid_top_x = (top_left_x + top_right_x) // 2  # 150
mid_bot_x = (inner_bl_x + inner_br_x) // 2   # 150

# --- Stroke 1: left vertical (slants slightly inward toward bottom)
draw.line([(top_left_x, top_y), (inner_bl_x, box_bot_y)], fill=INK, width=LW)

# --- Stroke 2: top horizontal
draw.line([(top_left_x - 4, top_y), (top_right_x + 4, top_y)], fill=INK, width=LW)

# --- Stroke 3: middle vertical
draw.line([(mid_top_x, top_y + 3), (mid_bot_x, box_bot_y)], fill=INK, width=LW)

# --- Stroke 4: right vertical (slants slightly inward)
draw.line([(top_right_x, top_y), (inner_br_x, box_bot_y)], fill=INK, width=LW)

# Second interior vertical to make it feel like 皿's 3 verticals inside plus outer
# Actually 皿 = left vertical | inner vertical | inner vertical | right vertical + top + bottom
# Traditional shape: left边, 两竖 inside, right边, top横, bottom横. Let's add another inner vertical.
# Re-render: verticals at top_left_x, ~1/3, ~2/3, top_right_x
# Redo — clear and draw again cleanly

img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# 皿 stroke order (5 strokes):
#   1. 丨 left vertical
#   2. 丨 first inner vertical
#   3. 丨 second inner vertical (some fonts: middle vertical only 3 verticals total? Actually 皿 = 5 strokes: 丨丨丨𠃍一 → left|, middle|, right| (with hook joining top), bottom—)
# Actually per MMH: 皿 is 5 strokes: 丨, 𠃌 (top+right combined), 丨, 丨, 一 (bottom).
# We'll draw shape by shape.

top_y = 100
box_bot_y = 200
bot_hline_y = 230

left_top_x = 88
right_top_x = 212
left_bot_x = 96
right_bot_x = 204

hline_left = 55
hline_right = 250

# Left vertical (slight inward slant)
draw.line([(left_top_x, top_y), (left_bot_x, box_bot_y)], fill=INK, width=LW)

# Top horizontal + right vertical combined (single stroke 𠃌-like)
# top horizontal
draw.line([(left_top_x - 3, top_y), (right_top_x + 3, top_y)], fill=INK, width=LW)
# right vertical connected to it
draw.line([(right_top_x, top_y), (right_bot_x, box_bot_y)], fill=INK, width=LW)

# Two inner verticals
inner1_top_x = left_top_x + (right_top_x - left_top_x) // 3   # ~129
inner2_top_x = left_top_x + 2 * (right_top_x - left_top_x) // 3  # ~170
inner1_bot_x = left_bot_x + (right_bot_x - left_bot_x) // 3   # ~132
inner2_bot_x = left_bot_x + 2 * (right_bot_x - left_bot_x) // 3

draw.line([(inner1_top_x, top_y + 3), (inner1_bot_x, box_bot_y)], fill=INK, width=LW)
draw.line([(inner2_top_x, top_y + 3), (inner2_bot_x, box_bot_y)], fill=INK, width=LW)

# Bottom long horizontal (extends past left and right)
draw.line([(hline_left, bot_hline_y), (hline_right, bot_hline_y)], fill=INK, width=LW)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0195_皿/01_皿.png")
print("saved")
