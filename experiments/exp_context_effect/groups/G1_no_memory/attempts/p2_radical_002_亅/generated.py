"""Render 亅 (radical, 1画): vertical stroke with a hook at bottom-left (竖钩)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

ink = "black"
sw = 5

# Shaft: taller, slightly right of center
x_shaft = 175
y_top = 55
y_bot = 235

# Rounded top: small curve entering the shaft (顿笔)
# Draw a short arc at the top corner
top_arc_bbox = [x_shaft - 12, y_top - 2, x_shaft + 2, y_top + 20]
d.arc(top_arc_bbox, start=180, end=360, fill=ink, width=sw)

# Main vertical shaft
d.line([(x_shaft, y_top + 8), (x_shaft, y_bot)], fill=ink, width=sw)

# Bottom hook: rounded corner curving from shaft to the left
hook_bbox = [x_shaft - 40, y_bot - 20, x_shaft + 5, y_bot + 10]
d.arc(hook_bbox, start=0, end=90, fill=ink, width=sw)

# Extend the hook horizontally to the left
hook_end_x = 130
hook_y = y_bot + 8
d.line([(x_shaft - 18, hook_y), (hook_end_x, hook_y)], fill=ink, width=sw)

# Small upward tick at hook tip
d.line([(hook_end_x, hook_y), (hook_end_x - 2, hook_y - 8)], fill=ink, width=sw)

out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "01_亅.png")
img.save(out_path)
print(out_path)
