"""Render 出 (chū) at 300x300 using PIL.

Structure: two stacked 凵 shapes sharing a central vertical.
- Bottom 凵: wider U covering the lower half
- Top 凵: smaller U sitting on top of the bottom 凵's horizontal
- Central vertical stem extending from top through both
"""

from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 6  # line width

# Coordinate system: PIL y grows downward.
# Bottom 凵 (larger, occupies lower half)
b_left_x = 75
b_right_x = 235
b_top_left_y = 175   # top of left vertical
b_top_right_y = 155  # top of right vertical (extends higher — matches GT)
b_bottom_y = 275     # bottom horizontal

# Bottom 凵 left vertical
draw.line([(b_left_x, b_top_left_y), (b_left_x, b_bottom_y)], fill=INK, width=LW)
# Bottom 凵 base horizontal
draw.line([(b_left_x - LW//2, b_bottom_y), (b_right_x + LW//2, b_bottom_y)], fill=INK, width=LW)
# Bottom 凵 right vertical (taller than left in GT)
draw.line([(b_right_x, b_top_right_y), (b_right_x, b_bottom_y)], fill=INK, width=LW)

# Central vertical stem — the middle | goes from top of upper 凵's area
# down to the bottom horizontal.
stem_top_y = 40
stem_bottom_y = b_bottom_y - LW//2
stem_x = 150
draw.line([(stem_x, stem_top_y), (stem_x, stem_bottom_y)], fill=INK, width=LW)

# Top 凵 (smaller, sits above center, base at midline of composition)
t_left_x = 115
t_right_x = 195
t_top_left_y = 110
t_top_right_y = 95
t_bottom_y = 175  # its base horizontal aligns with bottom 凵 left vertical top

# Top 凵 left vertical
draw.line([(t_left_x, t_top_left_y), (t_left_x, t_bottom_y)], fill=INK, width=LW)
# Top 凵 base horizontal
draw.line([(t_left_x - LW//2, t_bottom_y), (t_right_x + LW//2, t_bottom_y)], fill=INK, width=LW)
# Top 凵 right vertical
draw.line([(t_right_x, t_top_right_y), (t_right_x, t_bottom_y)], fill=INK, width=LW)

out_path = os.path.join(os.path.dirname(__file__), "01_出.png")
img.save(out_path)
print(f"Saved {out_path}")
