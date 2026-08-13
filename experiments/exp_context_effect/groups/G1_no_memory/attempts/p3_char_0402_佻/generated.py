"""Render 佻 as a 300x300 PNG."""
from PIL import Image, ImageDraw
from pathlib import Path

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

LW = 4

def line(pts):
    d.line(pts, fill="black", width=LW, joint="curve")

# ===== 亻 radical (left) - occupies roughly x=40..95 =====
# Top short slant (撇)
line([(80, 70), (55, 115)])
# Long vertical (竖)
line([(70, 105), (68, 175), (66, 260)])

# ===== 兆 (right) - occupies roughly x=110..270 =====
# Structure: 冫 on left + 儿-like on right, with two inner diagonals
# Reference: 冫丿 on left, 丨乚 on right roughly

# Left component of 兆:
# top tick (short diagonal)
line([(140, 80), (128, 100)])
# left long stroke: vertical descending, slight curve
line([(130, 105), (128, 165), (128, 225), (145, 258)])
# left middle small tick
line([(128, 165), (110, 178)])

# Inner-left diagonal (short slash going down-left)
line([(170, 110), (160, 170), (150, 220)])

# Inner-right diagonal (short slash going down-right)
line([(205, 115), (215, 175), (225, 220)])

# Right component of 兆:
# top tick
line([(255, 85), (248, 105)])
# right long stroke: vertical then curves right (hooks)
line([(248, 108), (252, 170), (258, 230), (270, 255)])
# right middle small tick
line([(248, 170), (265, 180)])

out = Path(__file__).parent / "01_佻.png"
img.save(out)
print(f"Saved {out}")
