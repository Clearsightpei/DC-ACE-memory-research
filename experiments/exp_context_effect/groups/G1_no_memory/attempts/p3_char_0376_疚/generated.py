"""G1 render of 疚 (character): 疒 radical + 久 inside. Revision 2."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 4

def line(pts, width=LW):
    d.line(pts, fill=BLACK, width=width, joint="curve")

# ============ 疒 (sickness radical, left side) ============
# 1) top dot (short slanting stroke, upper left)
line([(105, 45), (120, 62)])

# 2) top horizontal (long, slightly rising to the right, extends across)
line([(80, 85), (215, 78)])

# 3) left long descending stroke (starts near top of horizontal, curves down-left)
line([(115, 78), (100, 130), (75, 195), (55, 245)])

# 4) upper inner dot (short slash inside 疒)
line([(85, 115), (72, 132)])

# 5) lower inner dot (short slash inside 疒, below the upper dot)
line([(100, 155), (85, 172)])

# ============ 久 (right/inside portion) ============
# 6) top small piě (short slash at top of 久)
line([(150, 100), (170, 120)])

# 7) heng-pie-like: short horizontal from left, turn down-right (the top hook of 久)
line([(135, 138), (185, 132), (200, 148), (200, 165)])

# 8) main piě of 久 (long left-descending curve)
line([(160, 155), (140, 200), (115, 245), (95, 275)])

# 9) main nà of 久 (long right-descending stroke, crosses the piě)
line([(155, 185), (190, 225), (225, 260), (250, 280)])

out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "01_疚.png")
img.save(out_path)
print(f"Saved: {out_path}")
