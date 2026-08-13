"""G1 render of 痃 (illness radical 疒 + 玄). Revised."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 4


def stroke(pts, w=LW):
    d.line(pts, fill="black", width=w, joint="curve")


# ==== LEFT: 疒 radical ====
# Top dot slanting down-right
stroke([(78, 45), (92, 62)])

# Horizontal top stroke of 疒 (short, slight downward tilt)
stroke([(48, 82), (118, 76)])

# Left long pie (curving down-left from near top-left of horizontal)
stroke([(70, 82), (58, 140), (42, 205), (25, 270)])

# Two small marks inside 疒 (the 冫 dots on left interior)
stroke([(52, 128), (65, 142)])
stroke([(52, 172), (65, 186)])

# ==== RIGHT: 玄 ====
# Top dot (small slant)
stroke([(185, 45), (198, 60)])

# Top horizontal of 亠
stroke([(148, 82), (250, 76)])

# 幺 upper: small folded stroke (like ㄥ)
stroke([(175, 110), (215, 105)])   # small horizontal
stroke([(215, 105), (188, 138)])   # slant down-left
stroke([(188, 138), (220, 145)])   # small hook right

# 幺 lower: another folded stroke
stroke([(175, 168), (215, 162)])
stroke([(215, 162), (188, 196)])
stroke([(188, 196), (222, 203)])

# Bottom horizontal (long, sweeping) with a small hook
stroke([(150, 258), (255, 250)])
stroke([(255, 250), (260, 238)])

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_痃.png"))
print("saved")
