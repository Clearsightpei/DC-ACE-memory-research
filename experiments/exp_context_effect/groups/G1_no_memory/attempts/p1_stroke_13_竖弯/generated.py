"""
G1 no-memory attempt: p1_stroke_13_竖弯 (vertical then horizontal-right, no hook).
Renders a 300x300 white-background PNG with a black brush stroke.
"""

import turtle
from PIL import Image
import os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
EPS_PATH = os.path.join(OUT_DIR, "01_竖弯.eps")
PNG_PATH = os.path.join(OUT_DIR, "01_竖弯.png")

SIZE = 300

screen = turtle.Screen()
screen.setup(width=SIZE, height=SIZE)
screen.screensize(SIZE, SIZE)
screen.bgcolor("white")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.color("black")
t.pensize(14)
t.speed(0)

# 竖弯: start upper-middle, come straight down, then curve smoothly to the right,
# ending with a horizontal segment (no upward hook).

# Coords are turtle math coords: (0,0) center, +y up.
# Vertical descent from top-middle to just below center.
t.penup()
t.goto(-30, 110)      # top of the vertical
t.setheading(-90)     # pointing down
t.pendown()

# straight vertical drop
t.goto(-30, -60)

# curved corner: quarter-circle-ish sweep from downward to rightward.
# Turtle's circle() with negative radius curves clockwise (to the left of heading);
# from heading=-90 (down), we want to turn LEFT relative to heading to face +x (right).
# Left turn while heading down => face right. Use circle(radius=40, extent=90).
t.circle(40, 90)

# horizontal tail extending to the right (no hook up).
t.forward(80)

screen.update()

# Save as EPS then convert to PNG at exact 300x300 with PIL.
canvas = screen.getcanvas()
canvas.postscript(file=EPS_PATH, colormode="color")

try:
    img = Image.open(EPS_PATH)
    img.load(scale=4)
    img = img.convert("RGB")
    # Force exact 300x300 canvas: paste centered on white bg after resizing to fit.
    img.thumbnail((SIZE, SIZE), Image.LANCZOS)
    bg = Image.new("RGB", (SIZE, SIZE), "white")
    off = ((SIZE - img.width) // 2, (SIZE - img.height) // 2)
    bg.paste(img, off)
    bg.save(PNG_PATH, "PNG")
finally:
    if os.path.exists(EPS_PATH):
        os.remove(EPS_PATH)

try:
    screen.bye()
except turtle.Terminator:
    pass
