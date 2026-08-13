"""Render 盅 = 中 (top) + 皿 (bottom). G1 no-memory, PIL, 300x300."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = "black"
LW = 6

def line(p1, p2, w=LW):
    d.line([p1, p2], fill=INK, width=w)

# ---- Top: 中 (roughly upper 55% of canvas) ----
# Box for 口 in middle
box_left, box_right = 90, 200
box_top, box_bot = 60, 130
# Left vertical
line((box_left, box_top), (box_left, box_bot))
# Top horizontal
line((box_left, box_top), (box_right, box_top))
# Right vertical (with slight hook down)
line((box_right, box_top), (box_right, box_bot))
# Bottom horizontal of the box
line((box_left, box_bot), (box_right, box_bot))
# Middle horizontal (a bit wider than box, characteristic of 中)
line((box_left - 5, (box_top + box_bot)//2), (box_right + 5, (box_top + box_bot)//2))
# Central vertical (longer — extends above box and below)
line((145, 25), (145, 175))

# ---- Bottom: 皿 (lower portion) ----
# Top rim (a bit wider than box)
rim_left, rim_right = 70, 225
rim_top = 195
line((rim_left, rim_top), (rim_right, rim_top))
# Left wall (slight inward slant)
line((rim_left, rim_top), (rim_left + 8, 245))
# Right wall
line((rim_right, rim_top), (rim_right - 8, 245))
# Two inner verticals
line((115, rim_top), (118, 245))
line((175, rim_top), (172, 245))
# Bottom horizontal (widest — the base), extending slightly
base_y = 255
line((50, base_y), (250, base_y))

out_path = os.path.join(os.path.dirname(__file__), "01_盅.png")
img.save(out_path)
print("wrote", out_path)
