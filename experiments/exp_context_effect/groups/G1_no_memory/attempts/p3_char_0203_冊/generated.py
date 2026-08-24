"""G1 render of 冊 (character p3_char_0203_冊)."""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

ink = "black"
w = 6  # stroke width

# 冊 has 5 strokes:
# 1) Left curving vertical (撇 style) - down and slightly left
# 2) Left top: short horizontal then vertical drop (like left half of 冂)
# 3) Middle short vertical (a small hook down)
# 4) Right top: horizontal then vertical drop (like right half of 冂)
# 5) Long middle horizontal crossing both boxes

# Reference bounds inside 300x300
left_x  = 70    # left vertical top
mid_x   = 150   # middle divider
right_x = 235   # right vertical
top_y   = 70
bot_y   = 260
mid_y   = 170   # middle horizontal

# Stroke 1: left vertical (curves out left at bottom - 撇 feel)
d.line([(left_x, top_y), (left_x, mid_y-5)], fill=ink, width=w)
# curve the bottom part outward to lower-left
d.line([(left_x, mid_y-5), (left_x-8, bot_y-25)], fill=ink, width=w)
d.line([(left_x-8, bot_y-25), (left_x-25, bot_y)], fill=ink, width=w)

# Stroke 2: top-left short horizontal + vertical (like 横折) forming middle column left side
# Actually in 冊, the middle vertical is the second stroke: a short horizontal then vertical
# Let's place a top horizontal from left_x to mid_x
d.line([(left_x+2, top_y+5), (mid_x, top_y+5)], fill=ink, width=w)
# vertical drop from that turn down through bottom
d.line([(mid_x, top_y+5), (mid_x, bot_y-10)], fill=ink, width=w)

# Stroke 3: right top: horizontal from mid to right, then vertical down (横折)
d.line([(mid_x+2, top_y+5), (right_x, top_y+5)], fill=ink, width=w)
d.line([(right_x, top_y+5), (right_x, bot_y-5)], fill=ink, width=w)

# Stroke 4: long horizontal through middle crossing both boxes
d.line([(left_x-15, mid_y), (right_x+15, mid_y)], fill=ink, width=w)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0203_冊/01_冊.png")
print("wrote 01_冊.png")
