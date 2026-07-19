"""
G1 no-memory attempt: 横折折撇 (heng-zhe-zhe-pie)
Compound stroke as seen in 及, 建.
Sequence: horizontal right -> turn down (zhe) -> turn down-right (zhe) -> pie sweep down-left.
Rendered to 300x300 white background, black ink.
"""

import turtle
from PIL import Image
import os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
PS_PATH = os.path.join(OUT_DIR, "_tmp.eps")
PNG_PATH = os.path.join(OUT_DIR, "01_横折折撇.png")

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
t.pensize(8)

# Turtle uses math coords centered at (0,0). Canvas is 300x300, so
# usable range is roughly [-140, 140] in both axes.
# 横折折撇 layout (looks like the right shoulder of 及 / top of 建):
#   1) heng: short horizontal from upper-left to upper-right
#   2) zhe1: turn ~90deg, short vertical drop
#   3) zhe2: turn again, short diagonal going down-right (small)
#   4) pie: long sweeping diagonal down-left from that corner

def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Segment 1: heng (horizontal right)
move_to(-60, 90)
t.setheading(0)
t.forward(90)   # ends at (30, 90)

# Segment 2: zhe1 (short vertical drop)
t.setheading(-90)
t.forward(45)   # ends at (30, 45)

# Segment 3: zhe2 (short diagonal down-right, like a small horizontal-ish turn)
# This is the second fold — a small angled segment before the pie sweeps out.
t.setheading(-25)  # slightly downward, going right
t.forward(45)   # ends near (71, 26)

# Segment 4: pie (long sweeping diagonal down-left)
# Draw as a curved sweep using small forward+left steps for calligraphic feel.
t.setheading(-135)  # heading down-left
steps = 30
step_len = 4
for i in range(steps):
    t.forward(step_len)
    t.left(0.6)  # gentle curve, opening the pie outward

screen.update()

# Export via postscript -> PNG
canvas = screen.getcanvas()
canvas.postscript(file=PS_PATH, width=SIZE, height=SIZE,
                  pagewidth=SIZE, pageheight=SIZE)

# Convert EPS to PNG at exact 300x300
img = Image.open(PS_PATH)
img.load(scale=2)
img = img.convert("RGB")
img = img.resize((SIZE, SIZE), Image.LANCZOS)
img.save(PNG_PATH, "PNG")

try:
    os.remove(PS_PATH)
except OSError:
    pass

try:
    turtle.bye()
except turtle.Terminator:
    pass

print(f"Wrote {PNG_PATH}")
