"""G1 render of 乑."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
ink = "black"
lw = 4

def line(p0, p1, w=lw):
    d.line([p0, p1], fill=ink, width=w)

# Top piece: horizontal-ish stroke curving down with small hook at right
# (approximating the 乛/乁 top seen in GT)
line((110, 65), (175, 55))       # top horizontal (slight upslope right-to-left)
line((175, 55), (185, 90))       # small right-down hook

# Long vertical center stroke running through most of the character
line((155, 70), (155, 275))

# Left lower 人
line((100, 125), (65, 265))      # left long slant down-left (leg)
line((100, 135), (120, 175))     # short right slant

# Right lower 人
line((205, 130), (180, 175))     # left short slant
line((205, 130), (245, 260))     # right long slant down-right

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_乑.png")
img.save(out)
print("wrote", out)
