"""Render 卂 (character) to 300x300 PNG. Revised."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 5

# GT reads like 孔 shape:
#   Top: long horizontal
#   Left component: short downward slash + horizontal crossbar + vertical going down
#   Right component: 乚 - tall vertical curving right into hook at bottom

# 1) Top long horizontal (spans most of width), y=100, x=55 to x=230
d.line([(55, 100), (230, 100)], fill=INK, width=LW)

# 2) Right vertical + bottom hook (乚 style):
#    Vertical drops from near top-right down; then curves rightward/down at bottom
d.line([(215, 95), (218, 210)], fill=INK, width=LW)
# curved hook at bottom
hook_pts = [(218, 210), (222, 240), (232, 265), (238, 275)]
d.line(hook_pts, fill=INK, width=LW, joint="curve")

# 3) Left component: short downward-left slash starting inside upper region
#    From about (135, 115) going down-left to (110, 165)
d.line([(135, 115), (108, 165)], fill=INK, width=LW)

# 4) Middle horizontal crossbar at y~165, from x=70 to x=175
d.line([(70, 165), (175, 165)], fill=INK, width=LW)

# 5) Vertical going down from crossbar (from about x=130, y=165 down to x=135, y=265)
d.line([(130, 165), (135, 265)], fill=INK, width=LW)

out_path = os.path.join(os.path.dirname(__file__), "01_卂.png")
img.save(out_path)
print(f"Saved: {out_path}")
