from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"

def line(pts, th=5):
    d.line(pts, fill=INK, width=th, joint="curve")

# 仵 = 亻 (left person radical) + 午 (right)

# --- 亻 (left person radical) ---
# 撇 (pie): slanted stroke top-right down to left
line([(95, 75), (55, 210)], th=6)
# 竖 (vertical): starts about midway of pie, straight down
line([(85, 145), (85, 255)], th=6)

# --- 午 (right side) ---
# 短撇 (short pie): short slanted at top
line([(185, 65), (155, 105)], th=6)
# 横 (upper short horizontal): under the pie
line([(140, 110), (215, 105)], th=6)
# 长横 (longer middle horizontal): wider
line([(120, 165), (245, 158)], th=6)
# 竖 (vertical): central, going down through both horizontals
line([(180, 105), (178, 275)], th=7)

out_path = os.path.join(os.path.dirname(__file__), "01_仵.png")
img.save(out_path)
print("saved", out_path)
