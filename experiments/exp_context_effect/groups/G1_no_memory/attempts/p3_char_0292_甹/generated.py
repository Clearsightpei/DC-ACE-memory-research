"""G1 draw of 甹 (pīng). Top: 由 with long protruding vertical.
Bottom: long horizontal + 丂-like hook."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, w=4):
    d.line(pts, fill="black", width=w, joint="curve")

# ---- Top component: 由 with long tail ----
# Box for 由
L, R, T, B = 115, 180, 55, 130
cx = (L + R) // 2  # center vertical x

# Long vertical stroke: protrudes above top, passes through box, dips slightly below bottom
line([(cx, 25), (cx, B + 3)], 4)

# Left vertical
line([(L, T), (L, B)], 4)
# Right vertical (slight downward flare)
line([(R, T), (R + 3, B + 4)], 4)
# Top horizontal
line([(L, T), (R, T)], 4)
# Middle horizontal
line([(L, (T + B) // 2), (R, (T + B) // 2)], 4)
# Bottom horizontal
line([(L, B), (R + 3, B + 4)], 4)

# ---- Long horizontal separating top / bottom ----
# GT shows a long slightly rising horizontal across most of the width
line([(35, 172), (265, 165)], 5)

# ---- Bottom component: 丂/亏-like ----
# Short horizontal near top of bottom half
line([(120, 205), (215, 208)], 4)
# Right descending stroke that becomes a hook
# Down-and-left curve
curve1 = [
    (205, 208), (198, 225), (188, 240),
    (172, 253), (152, 265),
]
line(curve1, 4)
# Hook curl at the bottom (curls back to the right slightly)
curve2 = [
    (152, 265), (140, 270), (132, 265), (135, 255),
]
line(curve2, 4)

# Save
out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_甹.png"))
print("saved", os.path.join(out_dir, "01_甹.png"))
