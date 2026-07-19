"""
G1 no-memory attempt: p1_stroke_26_横折折 (heng-zhe-zhe)
Renders 横折折 as a single continuous stroke: horizontal right,
turn 90 deg down, then turn 90 deg right (horizontal again).
Output: 300x300 white background, black ink PNG.
"""
import turtle
from PIL import Image
import os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
PNG_OUT = os.path.join(OUT_DIR, "01_横折折.png")
PS_OUT = os.path.join(OUT_DIR, "_tmp.eps")

# Canvas 300x300
screen = turtle.Screen()
screen.setup(width=300, height=300)
screen.screensize(300, 300)
screen.bgcolor("white")
turtle.setworldcoordinates(-150, -150, 150, 150)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.color("black")
t.pensize(12)

# Stroke plan (turtle coords, y up):
#   Segment 1 (heng): from (-90, 70) to (70, 70) horizontal right,
#     with a slight downward tick at the end (顿笔 into the turn).
#   Segment 2 (zhe #1): from (70, 70) down to (70, -20) vertical.
#   Segment 3 (zhe #2): from (70, -20) horizontal right to (-70, -20)?
#     For 横折折, the second zhe turns back the OTHER way (left) OR
#     continues; the canonical 横折折 (as in 凹) has: right, down, left.
# Use: right -> down -> left, characteristic Z-shape.

# Segment 1: horizontal right (heng)
t.penup()
t.goto(-90, 60)
t.pendown()
t.setheading(0)
t.forward(150)   # to (60, 60)
# small 顿笔 (small down tick) into first turn
t.setheading(-90)
t.forward(6)     # slight tick to (60, 54)

# Segment 2: vertical down (first zhe)
t.setheading(-90)
t.forward(80)    # to (60, -26)
# small tick into second turn (leftward)
t.setheading(180)
t.forward(4)

# Segment 3: horizontal left (second zhe) - the second turn goes left
t.setheading(180)
t.forward(140)   # to about (-84, -30)

t.getscreen().getcanvas().postscript(file=PS_OUT)
screen.bye()

# Convert EPS to 300x300 PNG
img = Image.open(PS_OUT)
img.load(scale=4)
img = img.convert("RGB")
# Resize/pad to exactly 300x300
w, h = img.size
# Fit into 300x300 preserving aspect
img.thumbnail((300, 300), Image.LANCZOS)
canvas = Image.new("RGB", (300, 300), "white")
cw, ch = img.size
canvas.paste(img, ((300 - cw) // 2, (300 - ch) // 2))
canvas.save(PNG_OUT, "PNG")

try:
    os.remove(PS_OUT)
except OSError:
    pass

print(f"Wrote {PNG_OUT}")
