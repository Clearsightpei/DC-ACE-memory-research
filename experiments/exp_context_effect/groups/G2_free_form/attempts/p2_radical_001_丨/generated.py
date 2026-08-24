"""Render 丨 (radical, 1 stroke) to 300x300 PNG.

丨 is a straight vertical stroke. The GT PNG shows a calligraphic form
where the top has a subtle rightward curve into the vertical (a small
入笔 press that arcs down), then a straight descent. We match this by
using a quadratic Bezier for the first ~1/6 of the stroke, then straight
vertical for the rest, with a slight taper.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


# Stroke path: top starts near (150, 55) with a small entry arc curving
# from a point slightly up-and-right down into the vertical spine at
# roughly (145, 90), then straight down to (145, 250).
# Slight taper thin at top press → uniform mid → thin blunt bottom.

# Entry arc (quadratic Bezier)
P0 = (152, 55)     # top start
P1 = (140, 68)     # control pulled left/down
P2 = (145, 95)     # end of arc → start of straight spine

arc_steps = 140
for i in range(arc_steps + 1):
    t = i / arc_steps
    x = (1 - t) ** 2 * P0[0] + 2 * (1 - t) * t * P1[0] + t ** 2 * P2[0]
    y = (1 - t) ** 2 * P0[1] + 2 * (1 - t) * t * P1[1] + t ** 2 * P2[1]
    # Slight thickness ramp: thin at very top → r=4 at end of arc
    r = 2.5 + 1.5 * t
    dab(x, y, r)

# Straight vertical spine from arc end to bottom
x_top, y_top = P2
x_bot, y_bot = 145, 250

spine_steps = 400
for i in range(spine_steps + 1):
    t = i / spine_steps
    x = x_top + (x_bot - x_top) * t
    y = y_top + (y_bot - y_top) * t
    # uniform ~r=4 with very slight thinning near bottom
    r = 4.0 - 0.8 * t
    dab(x, y, r)

# Subtle terminal blunt at bottom
dab(x_bot, y_bot, 3.5)

img.save(
    "<REPO_ROOT>/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p2_radical_001_丨/01_丨.png"
)
