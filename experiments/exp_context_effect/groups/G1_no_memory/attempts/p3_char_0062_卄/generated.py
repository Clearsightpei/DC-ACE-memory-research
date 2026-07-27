"""Render 卄 to a 300x300 PNG using PIL.

卄 has 4 strokes:
 - two vertical strokes (left, right)
 - a short upper horizontal that crosses the top region
 - a longer lower horizontal that crosses lower on the verticals
"""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
W = 6  # stroke width

# Vertical strokes: extend from ~y=70 to ~y=260
# Left vertical at x ~ 105, right vertical at x ~ 195
left_x = 110
right_x = 195
v_top = 75
v_bot = 260

# Left vertical (slight lean)
draw.line([(left_x + 3, v_top), (left_x - 2, v_bot)], fill=BLACK, width=W)
# Right vertical
draw.line([(right_x - 2, v_top), (right_x + 2, v_bot)], fill=BLACK, width=W)

# Upper (shorter) horizontal — sits between the two verticals, ~ y=120
# In GT it's short — barely extends past verticals, slight upward slope
h1_y = 120
draw.line([(left_x + 5, h1_y + 3), (right_x - 5, h1_y - 8)], fill=BLACK, width=W)

# Lower (longer) horizontal — at ~ y=175, extends well beyond verticals
h2_y = 175
draw.line([(55, h2_y + 6), (245, h2_y - 2)], fill=BLACK, width=W)

out_path = os.path.join(os.path.dirname(__file__), "01_卄.png")
img.save(out_path)
print(f"Saved {out_path}")
