"""G1 render of 甾 (zāi) — 巛 on top, 田 on bottom."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 5


def stroke(pts, width=LW):
    d.line(pts, fill=INK, width=width, joint="curve")


# ---- Top: 巛 (three curly strokes) ----
# Each stroke starts with a small hook top, curves down-right then down-left ("s" curl)
def curl(x_top, y_top=45, h=105):
    # Small top diagonal tick, then a smooth S-shaped downstroke.
    # Build many points so PIL renders a smooth curve.
    import math
    # tick
    stroke([(x_top - 10, y_top - 5), (x_top + 3, y_top + 8)])
    # smooth wavy body: parametric sine
    pts = []
    N = 40
    for i in range(N + 1):
        t = i / N
        y = y_top + 8 + t * h
        # amplitude of horizontal wobble
        x = x_top + 8 * math.sin(t * math.pi * 1.5)
        pts.append((x, y))
    stroke(pts)


curl(95, y_top=50, h=95)
curl(150, y_top=45, h=100)
curl(205, y_top=50, h=95)

# ---- Bottom: 田 ----
# Rectangle roughly centered, sits below 巛
left, right = 90, 215
top, bot = 175, 275

# left vertical (starts a bit above top for the classic 竖 into corner)
stroke([(left, top), (left, bot)])
# top horizontal + right vertical (turn)
stroke([(left - 2, top), (right, top), (right, bot)])
# bottom horizontal
stroke([(left, bot), (right, bot)])
# middle horizontal
midy = (top + bot) // 2
stroke([(left, midy), (right, midy)])
# middle vertical
midx = (left + right) // 2
stroke([(midx, top), (midx, bot)])

out = os.path.join(os.path.dirname(__file__), "01_甾.png")
img.save(out)
print(f"wrote {out}")
