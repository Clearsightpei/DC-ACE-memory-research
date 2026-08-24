# p3_char_0217_凹 — G3 render
# Shape: rectangular outline with a rectangular notch cut into the top-center.
# 5-stroke MMH character; here rendered as a continuous outline with 8 line
# segments — decomposed fresh (G3 v8 signature freedom; no bank primitive
# fits this envelope shape without extreme transformation).
#
# Layout (canvas 300x300, math-free pixel coords, y grows DOWN as PIL):
#   left outer x = 55, right outer x = 245
#   top y = 85, bottom y = 255
#   notch left x = 115, notch right x = 185
#   notch bottom y = 170 (about mid-height, slightly above center)
#
# The GT shows a slight lift on the outer top edges (like they don't quite
# reach the top of the inner tabs) — the inner tabs actually poke up a bit
# higher. Mirror that: outer top corners at y=100, inner tab tops at y=85.

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

w = 7  # stroke width — matches GT thin-ink look

# Outer envelope
# left vertical
d.line([(55, 100), (55, 250)], fill="black", width=w)
# bottom horizontal
d.line([(52, 250), (248, 250)], fill="black", width=w)
# right vertical
d.line([(245, 100), (245, 250)], fill="black", width=w)

# Top-left segment: outer-top going to the left tab
d.line([(55, 100), (115, 100)], fill="black", width=w)
# Left tab vertical (going up to top of notch)
d.line([(115, 100), (115, 85)], fill="black", width=w)
# Top of notch (bottom of the cutout) — the bar across the top
# Actually notch has: from top of left tab (115,85) go right across (top edge)
# to (185,85), then down to (185,100), then right to (245,100)
# But we already drew left tab going UP from (115,100) to (115,85).
# So continue: top edge of notch from (115,85) to (185,85)
d.line([(115, 85), (185, 85)], fill="black", width=w)
# Right tab vertical (going down from top-of-notch to inner-corner)
d.line([(185, 85), (185, 100)], fill="black", width=w)
# Top-right segment: from right tab to outer top-right corner
d.line([(185, 100), (245, 100)], fill="black", width=w)

# Now the inner notch cutout bottom — the "凹" concavity floor:
# from left tab inner side down, across the floor, up the right tab inner side.
# Left inner wall
d.line([(115, 100), (115, 170)], fill="black", width=w)
# Inner floor
d.line([(115, 170), (185, 170)], fill="black", width=w)
# Right inner wall
d.line([(185, 170), (185, 100)], fill="black", width=w)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0217_凹/01_凹.png")
print("wrote 01_凹.png")
