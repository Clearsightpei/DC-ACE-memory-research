"""G1 attempt for 俚 (person radical 亻 + 里)."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = "black"
LW = 5

def line(pts, w=LW):
    d.line(pts, fill=INK, width=w, joint="curve")

# ---- Left radical 亻 (person) ----
# Slanting stroke 丿 - starts high right, sweeps down-left
line([(95, 65), (55, 175)], w=6)
# Vertical stroke 丨 - joins at pie midpoint
line([(78, 130), (78, 245)], w=6)

# ---- Right side 里 ----
# 日 on top: keep compact (about 1/3 of height)
# top horizontal
line([(150, 65), (245, 65)])
# left vertical of 日
line([(152, 65), (152, 145)])
# right vertical of 日
line([(243, 65), (243, 145)])
# middle horizontal of 日
line([(152, 105), (243, 105)])
# bottom horizontal of 日
line([(152, 145), (243, 145)])

# 土 lower part: continues down from 日
# central vertical extends from top of 日 through bottom
line([(197, 65), (197, 245)], w=6)
# middle horizontal of 土 (short-ish)
line([(160, 195), (238, 195)])
# base horizontal (widest, extends past 日)
line([(120, 250), (275, 250)], w=6)

out = os.path.join(os.path.dirname(__file__), "01_俚.png")
img.save(out)
print("wrote", out)
