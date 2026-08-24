"""Draw 冉 at 300x300, black on white.

冉 structure (from GT):
- Short top horizontal (near top-center)
- Left vertical (long, extending well below the frame bottom, slight ノ tail)
- Right vertical: starts with tiny 横 shoulder then drops (横折) with hook up-left at bottom
- Wide middle horizontal that extends OUTSIDE both verticals
- Short upper inner horizontal (inside the frame, above the wide one)
- Central vertical bar through the middle (short, ends at wide horizontal or slightly below)
Not a sibling-risk target; drawing fresh from GT.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 6  # main stroke width

# Frame geometry
top_y = 70          # top horizontal y
mid_y = 175         # wide middle horizontal y
bot_y = 230         # left vertical bottom
left_x = 100        # left vertical x
right_x = 200       # right vertical x
inner_top_y = 125   # small inner horizontal

# 1) Top short horizontal (a bit centered, slightly right of left vert)
d.line([(left_x + 12, top_y), (right_x - 5, top_y)], fill=BLACK, width=LW)

# 2) Left vertical (long, from top horizontal down past frame bottom, slight curve)
# Use a slight ノ tail at end
d.line([(left_x, top_y - 2), (left_x - 8, bot_y + 40)], fill=BLACK, width=LW)

# 3) Right vertical with 横折 shoulder + 竖 with hook flick up-left
# Small horizontal shoulder from top horizontal end, then vertical down
d.line([(right_x - 5, top_y - 3), (right_x, top_y + 3)], fill=BLACK, width=LW)  # shoulder
d.line([(right_x, top_y + 3), (right_x, bot_y + 30)], fill=BLACK, width=LW)     # vertical
# Hook flick UP-and-LEFT
d.line([(right_x, bot_y + 30), (right_x - 14, bot_y + 22)], fill=BLACK, width=LW)

# 4) Wide middle horizontal — extends beyond both verticals
d.line([(left_x - 40, mid_y), (right_x + 40, mid_y)], fill=BLACK, width=LW)

# 5) Small upper inner horizontal (inside frame)
d.line([(left_x + 8, inner_top_y), (right_x - 8, inner_top_y)], fill=BLACK, width=LW)

# 6) Central vertical bar (short — from inner horizontal down to wide middle horizontal)
cx = (left_x + right_x) // 2
d.line([(cx, inner_top_y - 3), (cx, mid_y + 3)], fill=BLACK, width=LW)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0201_冉/01_冉.png")
