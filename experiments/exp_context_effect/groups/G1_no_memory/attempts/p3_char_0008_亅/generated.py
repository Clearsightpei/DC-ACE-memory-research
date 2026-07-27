"""G1 render of 亅 (jué) — a vertical hook stroke (竖钩).
Target: thin vertical descending line, positioned slightly right of center,
starting with a small tick, curving left at the bottom into a horizontal hook.
"""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

INK = "black"
W = 6  # stroke width

# Vertical shaft — slightly right of center, from top area to near bottom
x_shaft = 170
y_top = 60
y_bot = 240

# Small starting curl at top (tiny arc/tick going up-left then into shaft)
# GT shows a small hooked entry to the upper-left
draw.arc([x_shaft - 10, y_top - 2, x_shaft + 2, y_top + 12],
         start=180, end=310, fill=INK, width=W)

# Main vertical shaft
draw.line([(x_shaft, y_top + 6), (x_shaft, y_bot)], fill=INK, width=W)

# Hook at bottom — curve left into a horizontal segment
# Use an arc/curve for smooth transition, then horizontal line
# Draw a rounded bottom-left curve then horizontal line going left
# Approximate curve using multiple short segments
import math
cx, cy = x_shaft - 14, y_bot - 14  # arc center
r = 14
# Arc from angle 0 (right of center) sweeping down to 90 (below center)
# We want the shaft's bottom to smoothly turn left; use arc from ~350° to ~270° going counterclockwise
# Simpler: draw pieslice-like curve via draw.arc
draw.arc([cx - r, cy - r, cx + r, cy + r], start=0, end=90, fill=INK, width=W)

# Horizontal hook segment extending left from the curve
hook_y = y_bot
hook_x_start = x_shaft - 14
hook_x_end = 110
draw.line([(hook_x_end, hook_y), (hook_x_start, hook_y)], fill=INK, width=W)

out_path = os.path.join(os.path.dirname(__file__), "01_亅.png")
img.save(out_path)
print(f"Saved: {out_path}")
