"""G1 render for 些 — 此 (止+匕) on top, 二 on bottom."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 6

def line(pts, width=LW):
    d.line(pts, fill="black", width=width, joint="curve")

# ---- Top-left: 止 ----
# main vertical
line([(85, 65), (85, 155)])
# left small dot/short stroke on upper-left
line([(55, 105), (78, 92)])
# left short vertical/horizontal (middle-left short stroke)
line([(55, 115), (55, 155)])
# middle horizontal (crossing the vertical)
line([(55, 130), (115, 130)])
# bottom horizontal of 止
line([(45, 155), (130, 155)])

# ---- Top-right: 匕 ----
# short top-left slanted stroke (the little horizontal-ish top of 匕)
line([(150, 95), (185, 85)])
# main body of 匕: diagonal down then hook to the right (one continuous)
line([(200, 70), (200, 140), (170, 155), (155, 155)])
# no wait — 匕 is: short stroke top-left, then the body which is
# a down-and-right hook stroke starting from upper right going down-left
# then sweeping right into a hook.
# Redraw body:

# Actually redo: the 匕 body — starts from about (215, 80), curves down-left
# then right into hook
# We'll clear and redraw carefully via separate strokes

out_dir = os.path.dirname(os.path.abspath(__file__))

# Rebuild image cleanly for 匕
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=LW):
    d.line(pts, fill="black", width=width, joint="curve")

# ---- Top-left: 止 ----
line([(85, 65), (85, 155)])                # main vertical
line([(55, 108), (78, 92)])                # upper-left short slant
line([(55, 115), (55, 155)])               # left short vertical
line([(55, 130), (115, 130)])              # middle horizontal
line([(45, 155), (130, 155)])              # bottom horizontal

# ---- Top-right: 匕 ----
# short top-left slanted stroke
line([(150, 100), (188, 88)])
# body: vertical down then hook out right
line([(198, 75), (198, 145), (215, 158), (240, 145)])

# ---- Middle short horizontal (dash between top and 二) ----
line([(130, 195), (175, 195)])

# ---- Bottom: 二 ----
line([(95, 225), (215, 225)])              # top of 二
line([(50, 265), (250, 265)])              # bottom of 二 (longer)

img.save(os.path.join(out_dir, "01_些.png"))
print("saved", os.path.join(out_dir, "01_些.png"))
