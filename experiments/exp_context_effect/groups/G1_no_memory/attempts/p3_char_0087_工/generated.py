"""Render 工 as a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

ink = "black"
thick = 6

# 工 has 3 strokes: top horizontal, middle vertical, bottom horizontal
# Top horizontal (shorter)
top_y = 100
top_x1, top_x2 = 85, 210
draw.line([(top_x1, top_y), (top_x2, top_y)], fill=ink, width=thick)

# Middle vertical
mid_x = 150
draw.line([(mid_x, top_y), (mid_x, 210)], fill=ink, width=thick)

# Bottom horizontal (longer)
bot_y = 210
bot_x1, bot_x2 = 55, 250
draw.line([(bot_x1, bot_y), (bot_x2, bot_y)], fill=ink, width=thick)

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0087_工/01_工.png"
img.save(out)
print("saved", out)
