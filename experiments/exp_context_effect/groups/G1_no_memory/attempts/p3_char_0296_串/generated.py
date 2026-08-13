"""Render 串 (chuàn) — two stacked 口 boxes pierced by a central vertical stroke."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
LW = 6

# Two stacked boxes (口) centered horizontally, one above the other.
# Upper box
u_left, u_right = 100, 200
u_top, u_bot = 55, 145
# Lower box
l_left, l_right = 100, 200
l_top, l_bot = 155, 245

# Central vertical line piercing both boxes and extending below
cx = 150
v_top = 25
v_bot = 285

# Draw central vertical first
draw.line([(cx, v_top), (cx, v_bot)], fill=INK, width=LW)

def box(left, top, right, bot):
    # Left vertical
    draw.line([(left, top), (left, bot)], fill=INK, width=LW)
    # Top horizontal
    draw.line([(left, top), (right, top)], fill=INK, width=LW)
    # Right vertical
    draw.line([(right, top), (right, bot)], fill=INK, width=LW)
    # Bottom horizontal
    draw.line([(left, bot), (right, bot)], fill=INK, width=LW)

box(u_left, u_top, u_right, u_bot)
box(l_left, l_top, l_right, l_bot)

# Add short horizontal middle bars inside each box (串 has crossbars)
draw.line([(u_left, (u_top + u_bot) // 2), (u_right, (u_top + u_bot) // 2)], fill=INK, width=LW)
draw.line([(l_left, (l_top + l_bot) // 2), (l_right, (l_top + l_bot) // 2)], fill=INK, width=LW)

out_path = os.path.join(os.path.dirname(__file__), "01_串.png")
img.save(out_path)
print(f"Saved: {out_path}")
