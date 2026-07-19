"""
G1 attempt for p1_stroke_15_竖折 (vertical then right turn, "L" shape).
Renders to 01_竖折.png at 300x300, white background, black ink.
"""
import turtle
from PIL import Image
import os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
PS_PATH = os.path.join(OUT_DIR, "01_竖折.eps")
PNG_PATH = os.path.join(OUT_DIR, "01_竖折.png")

# Canvas setup: 300x300 white background.
screen = turtle.Screen()
screen.setup(width=300, height=300)
screen.screensize(300, 300)
screen.bgcolor("white")
screen.tracer(0, 0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(14)
t.color("black")

# 竖折 = a vertical descending stroke, then a sharp 90-degree turn to
# horizontal-right. Shape resembles an "L". Occupies the middle-left area
# of the character cell in typical use (e.g., bottom-left of 山).
# Turtle coord system: origin at center, y-up.

# Start near upper-middle-left, go straight down (竖), then turn and go right (折).
# Slight terminal thickening approximated by an extra dot at the corner and end.

start_x, start_y = -70, 90   # top of the vertical
corner_x, corner_y = -70, -70  # bottom of the vertical / start of horizontal
end_x, end_y = 80, -70       # right end of the horizontal

# Vertical stroke (竖) — straight down.
t.penup()
t.goto(start_x, start_y)
t.setheading(-90)  # facing down
t.pendown()
t.goto(corner_x, corner_y)

# Small rounded/emphasized corner (subtle 顿笔 at the joint).
t.penup()
t.goto(corner_x, corner_y)
t.dot(14)

# Horizontal stroke (折) — sharp turn right.
t.setheading(0)  # facing right
t.pendown()
t.goto(end_x, end_y)

# Slight terminal emphasis at right end.
t.penup()
t.goto(end_x, end_y)
t.dot(14)

screen.update()

# Export to EPS, then convert to PNG at 300x300.
canvas = screen.getcanvas()
canvas.postscript(file=PS_PATH, width=300, height=300)

# Convert EPS to PNG using PIL (requires ghostscript).
img = Image.open(PS_PATH)
img.load(scale=2)
# Ensure white background and 300x300.
bg = Image.new("RGB", img.size, "white")
bg.paste(img, mask=None)
bg = bg.resize((300, 300), Image.LANCZOS)
bg.save(PNG_PATH, "PNG")

# Cleanup EPS.
try:
    os.remove(PS_PATH)
except OSError:
    pass

try:
    screen.bye()
except turtle.Terminator:
    pass
