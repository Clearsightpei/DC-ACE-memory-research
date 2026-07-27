from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
ink = "black"
lw = 6

# 申: a vertical line through a box (田-like) with the vertical extending top and bottom
# Box occupies roughly the middle band vertically
box_left = 90
box_right = 210
box_top = 100
box_bottom = 220
mid_x = (box_left + box_right) // 2
mid_y = (box_top + box_bottom) // 2

# Vertical stroke extends above and below the box
v_top = 40
v_bottom = 275

# Draw box: top, bottom, left, right
d.line([(box_left, box_top), (box_right, box_top)], fill=ink, width=lw)          # top
d.line([(box_left, box_bottom), (box_right, box_bottom)], fill=ink, width=lw)    # bottom
d.line([(box_left, box_top), (box_left, box_bottom)], fill=ink, width=lw)        # left
d.line([(box_right, box_top), (box_right, box_bottom)], fill=ink, width=lw)      # right

# Horizontal middle line (inside box)
d.line([(box_left, mid_y), (box_right, mid_y)], fill=ink, width=lw)

# Vertical line through everything
d.line([(mid_x, v_top), (mid_x, v_bottom)], fill=ink, width=lw)

out = os.path.join(os.path.dirname(__file__), "01_申.png")
img.save(out)
print("wrote", out)
