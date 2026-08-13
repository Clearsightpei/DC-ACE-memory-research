from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 5

# Left radical 亻 (single-person)
# slanted top stroke (撇)
d.line([(95, 70), (55, 220)], fill=INK, width=LW)
# vertical stroke (丨)
d.line([(95, 130), (95, 260)], fill=INK, width=LW)

# Right side 呂 = two 口 stacked, with small connector
# Upper 口
ux1, uy1, ux2, uy2 = 145, 75, 245, 145
d.line([(ux1, uy1), (ux2, uy1)], fill=INK, width=LW)  # top
d.line([(ux1, uy1), (ux1, uy2)], fill=INK, width=LW)  # left
d.line([(ux2, uy1), (ux2, uy2)], fill=INK, width=LW)  # right
d.line([(ux1, uy2), (ux2, uy2)], fill=INK, width=LW)  # bottom

# Small connector between the two 口 (丿-like short stroke)
d.line([(190, 150), (180, 175)], fill=INK, width=LW)

# Lower 口
lx1, ly1, lx2, ly2 = 155, 180, 255, 260
d.line([(lx1, ly1), (lx2, ly1)], fill=INK, width=LW)
d.line([(lx1, ly1), (lx1, ly2)], fill=INK, width=LW)
d.line([(lx2, ly1), (lx2, ly2)], fill=INK, width=LW)
d.line([(lx1, ly2), (lx2, ly2)], fill=INK, width=LW)

out = os.path.join(os.path.dirname(__file__), "01_侶.png")
img.save(out)
print("wrote", out)
