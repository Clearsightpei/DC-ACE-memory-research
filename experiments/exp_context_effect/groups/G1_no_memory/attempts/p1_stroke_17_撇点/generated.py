"""
G1 no-memory drawer: 撇点 (pie then dot going down-right)
As seen in 女: a downward-left pie stroke that turns sharply into a
down-right dot/na segment. 300x300 white bg, black ink.
"""
import turtle
from PIL import Image
import os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
PNG_PATH = os.path.join(OUT_DIR, "01_撇点.png")
EPS_PATH = os.path.join(OUT_DIR, "_tmp.eps")

SIZE = 300

screen = turtle.Screen()
screen.setup(width=SIZE, height=SIZE)
screen.screensize(SIZE, SIZE)
screen.bgcolor("white")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.color("black")
t.pensize(6)

# --- Stroke 1: 撇 (pie) — start upper-right, slope down-left, taper implied ---
# Use math coords (turtle default: origin center, +y up).
# Start around (60, 90), end around (-70, -40).
t.penup()
t.goto(60, 90)
t.pendown()
t.setheading(0)
# Draw pie as a gently curved line down-left, thickening feel via slight overdraw
# Approximate with a short arc: turn heading and go straight, small curve.
t.setheading(210)  # down-left-ish
# Slight curve: two segments
t.forward(80)
t.setheading(215)
t.forward(70)

# --- Turn: pen up, reposition to the base of pie for the 点 ---
# The 点 in 撇点 starts near the tail of the pie and goes down-right.
t.penup()
# End of pie is roughly at:
end_x, end_y = t.xcor(), t.ycor()
# Move pen up slightly to start dot from near pie tail
t.goto(end_x + 5, end_y + 5)
t.pendown()

# --- Stroke 2: 点 (down-right dot / short na) ---
# A short thick stroke going down-right, thicker at bottom
t.pensize(5)
t.setheading(-45)  # down-right at 45 deg below horizontal
t.forward(15)
t.pensize(8)
t.forward(20)
t.pensize(10)
t.forward(15)

screen.update()

# Save EPS then convert to PNG at exact 300x300
canvas = screen.getcanvas()
canvas.postscript(file=EPS_PATH, width=SIZE, height=SIZE)

# Convert EPS to PNG via PIL
img = Image.open(EPS_PATH)
img.load(scale=2)
img = img.convert("RGB")
# Force exact 300x300
img = img.resize((SIZE, SIZE), Image.LANCZOS)
img.save(PNG_PATH, "PNG")

# Cleanup
try:
    os.remove(EPS_PATH)
except OSError:
    pass

try:
    screen.bye()
except turtle.Terminator:
    pass

print(f"Saved: {PNG_PATH}")
