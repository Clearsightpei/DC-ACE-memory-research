"""G1 render of 山 (radical 063). 300x300 PNG, white bg, black ink."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
T = 6  # stroke thickness

# Layout: 山 has three vertical prongs standing on a bottom horizontal.
# Middle prong is tallest, left and right are shorter.
# Bottom horizontal connects left-prong-bottom to right-prong-bottom.

# Coordinates (image coords: y grows DOWN)
# Center vertical (stroke 1): tallest, x ~= 150, from top ~90 to bottom ~215
mid_x = 150
mid_top_y = 85
mid_bot_y = 215

# Left vertical part of 竖折 (stroke 2 starts): x ~= 85, from ~130 to bottom ~220
left_x = 85
left_top_y = 130
left_bot_y = 222

# Right vertical (stroke 3): x ~= 215, from ~120 to ~220
right_x = 215
right_top_y = 120
right_bot_y = 222

# Bottom horizontal (part of stroke 2 竖折): from left_x to right_x, y ~= 220
bot_y = 220

# --- Stroke 1: middle vertical ---
draw.line([(mid_x, mid_top_y), (mid_x, mid_bot_y)], fill=INK, width=T)

# --- Stroke 2: 竖折 — left vertical then bottom horizontal (one continuous stroke) ---
draw.line([(left_x, left_top_y), (left_x, left_bot_y)], fill=INK, width=T)
draw.line([(left_x, bot_y), (right_x, bot_y)], fill=INK, width=T)

# --- Stroke 3: right vertical ---
draw.line([(right_x, right_top_y), (right_x, right_bot_y)], fill=INK, width=T)

out_path = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_063_山/01_山.png"
img.save(out_path)
print(f"Saved {out_path}")
