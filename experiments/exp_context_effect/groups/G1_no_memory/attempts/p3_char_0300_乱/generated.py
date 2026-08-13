"""Render 乱 (chaos) at 300x300 using PIL. Revision 1."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 5

def line(pts, width=LW):
    d.line(pts, fill=BLACK, width=width, joint="curve")

# ============ LEFT COMPONENT: 舌 (tongue) ============
# Layout: small piece on top, then 千-like cross, then 口 at bottom
# Approx bounding box: x 25..155, y 55..255

# Top small stroke - short diagonal like 丿 (upper-left of 舌)
line([(75, 60), (55, 90)], width=LW)

# First horizontal (upper) - shorter
line([(45, 100), (130, 95)], width=LW)

# Vertical descending down through center (the 千 vertical)
line([(90, 60), (90, 205)], width=LW)

# Second horizontal (middle) - longer, the main crossbar of 千
line([(30, 140), (150, 135)], width=LW)

# Bottom 口 (mouth square)
# left vertical
line([(55, 200), (55, 250)], width=LW)
# right vertical
line([(130, 200), (130, 255)], width=LW)
# top horizontal
line([(55, 200), (130, 200)], width=LW)
# bottom horizontal
line([(55, 250), (132, 253)], width=LW)

# ============ RIGHT COMPONENT: 乚 (large hook) ============
# Tall vertical descending then curving out to the right
line([(240, 50), (238, 240)], width=LW)
# Curve at the bottom sweeping right
line([(238, 240), (250, 260), (275, 265), (285, 260)], width=LW)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0300_乱/01_乱.png")
print("saved")
