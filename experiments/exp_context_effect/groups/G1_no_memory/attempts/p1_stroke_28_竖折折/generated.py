"""
G1 attempt for p1_stroke_28_竖折折 (vertical + horizontal-right + vertical-down).
As in the top-left of 鼎: goes down, turns right, turns down again — a step shape.
Renders to 01_竖折折.png at 300x300, white background, black ink.
"""
import turtle
from PIL import Image
import os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
PS_PATH = os.path.join(OUT_DIR, "01_竖折折.eps")
PNG_PATH = os.path.join(OUT_DIR, "01_竖折折.png")

# Canvas: 300x300 white background.
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

# 竖折折 = 竖 (down) → 折 (right) → 折 (down).
# Three segments joined by two 90-degree corners. Overall shape is a
# right-facing "step" or reversed "Z" with square corners. In 鼎 the
# stroke sits in the upper-left, forming the outer frame of the top box.
# Turtle coord: origin at center, y-up.
#
# Segment plan (fits within ~240px, centered):
#   竖  : (-80,  100) → (-80,   10)   length ~90 (first vertical, medium)
#   折₁ : (-80,   10) → ( 40,   10)   length ~120 (horizontal right)
#   折₂ : ( 40,   10) → ( 40, -100)   length ~110 (second vertical, longer)

p_start   = (-80,  100)
p_corner1 = (-80,   10)
p_corner2 = ( 40,   10)
p_end     = ( 40, -100)

# Small 顿笔 at start (subtle press).
t.penup()
t.goto(p_start)
t.dot(14)

# 竖 (down).
t.setheading(-90)
t.pendown()
t.goto(p_corner1)

# Corner 1: emphasize the joint (顿笔).
t.dot(14)

# 折₁ (right).
t.setheading(0)
t.goto(p_corner2)

# Corner 2: emphasize the joint.
t.dot(14)

# 折₂ (down).
t.setheading(-90)
t.goto(p_end)

# Terminal emphasis.
t.dot(14)

screen.update()

# Export to EPS then convert to 300x300 PNG.
canvas = screen.getcanvas()
canvas.postscript(file=PS_PATH, width=300, height=300)

img = Image.open(PS_PATH)
img.load(scale=2)
bg = Image.new("RGB", img.size, "white")
bg.paste(img, mask=None)
bg = bg.resize((300, 300), Image.LANCZOS)
bg.save(PNG_PATH, "PNG")

try:
    os.remove(PS_PATH)
except OSError:
    pass

try:
    screen.bye()
except turtle.Terminator:
    pass
