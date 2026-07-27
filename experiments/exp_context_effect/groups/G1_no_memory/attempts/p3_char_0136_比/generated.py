"""Render 比 to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

W = 7  # stroke width

# 比 - two halves, each with a top slanted stroke + short horizontal + vertical.
# Standard stroke order for 比:
#   1. 横 (short horizontal, tilted up) - left component top
#   2. 竖 (vertical) - left component
#   3. 撇 (diagonal down-left) - right component
#   4. 竖弯钩 (vertical curving right) - right component
# But from the GT image both halves look mirror-symmetric with a diagonal at top.

# --- LEFT HALF ---
# Top: diagonal going from upper-right down to lower-left (撇-like) — this is the top slanted line
draw.line([(115, 100), (75, 165)], fill="black", width=W)
# Middle horizontal: short 横 sticking out to the right at the joint
draw.line([(75, 155), (140, 150)], fill="black", width=W)
# Vertical going down from left end
draw.line([(78, 155), (95, 240)], fill="black", width=W)

# --- RIGHT HALF ---
# Top: diagonal going from upper-right down to lower-left (撇)
draw.line([(210, 100), (170, 175)], fill="black", width=W)
# Middle horizontal: short 横 sticking out right
draw.line([(170, 165), (230, 160)], fill="black", width=W)
# 竖弯钩: vertical going down then curving right at the bottom
# Vertical part
draw.line([(173, 165), (183, 225)], fill="black", width=W)
# Curve at bottom flowing right
draw.line([(183, 225), (230, 240)], fill="black", width=W)

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_比.png")
img.save(out_path)
print(f"Saved {out_path}")
