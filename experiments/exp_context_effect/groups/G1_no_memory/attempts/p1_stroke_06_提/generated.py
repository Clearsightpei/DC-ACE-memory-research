"""
G1 no-memory attempt: p1_stroke_06_提 (提画, rising stroke).
Renders a 提 (ti) stroke — starts lower-left with a slight press (顿笔),
then rises diagonally to upper-right, tapering to a fine point.
Output: 300x300 PNG, white bg, black ink.
"""
import turtle
from PIL import Image
import os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
PNG_PATH = os.path.join(OUT_DIR, "01_提.png")
EPS_PATH = os.path.join(OUT_DIR, "01_提.eps")

# 300x300 canvas
screen = turtle.Screen()
screen.setup(width=300, height=300)
screen.screensize(300, 300)
screen.bgcolor("white")
screen.tracer(0, 0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.color("black")
t.penup()

# 提 rising stroke: from lower-left (about -80, -60) up to upper-right (about 90, 80).
# Turtle uses math coords (y up). Start with a small 顿笔 (press) then taper.

# Segment 1: initial press / 顿笔 at lower-left — a short thick nub
t.goto(-85, -70)
t.setheading(30)  # angle up-right ~30 deg from horizontal
t.pendown()
t.pensize(14)
t.forward(10)  # small nub

# Segment 2: main rising body — gradually tapering
# Simulate taper by drawing shrinking overlapping segments
import math
start_x, start_y = t.xcor(), t.ycor()
end_x, end_y = 95, 75
total_dx = end_x - start_x
total_dy = end_y - start_y
total_len = math.hypot(total_dx, total_dy)
n_steps = 40
for i in range(n_steps):
    # taper linearly from 14 -> 1
    size = 14 - (13 * (i / (n_steps - 1)))
    t.pensize(max(1, size))
    step_len = total_len / n_steps
    t.forward(step_len)

turtle.update()

# Save as EPS then convert to PNG at 300x300
canvas = screen.getcanvas()
canvas.postscript(file=EPS_PATH, width=300, height=300)

try:
    img = Image.open(EPS_PATH)
    img.load(scale=3)
    img = img.convert("RGB")
    img = img.resize((300, 300), Image.LANCZOS)
    img.save(PNG_PATH, "PNG")
except Exception as e:
    # Fallback: pure PIL render
    from PIL import ImageDraw
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)
    # 300x300 pixel coords (y down). Map turtle (-150..150) to (0..300)
    def to_px(x, y):
        return (int(150 + x), int(150 - y))
    # start nub
    x0, y0 = to_px(-85, -70)
    # end point
    x1, y1 = to_px(95, 75)
    # draw as a series of tapered circles
    n = 60
    for i in range(n):
        f = i / (n - 1)
        px = x0 + (x1 - x0) * f
        py = y0 + (y1 - y0) * f
        # radius: thick at start (7), thin at end (1)
        r = max(1, 7 - int(6 * f))
        draw.ellipse((px - r, py - r, px + r, py + r), fill="black")
    img.save(PNG_PATH, "PNG")

# Cleanup EPS
if os.path.exists(EPS_PATH):
    try:
        os.remove(EPS_PATH)
    except OSError:
        pass

# Ensure exactly 300x300
img = Image.open(PNG_PATH)
if img.size != (300, 300):
    img = img.convert("RGB").resize((300, 300), Image.LANCZOS)
    img.save(PNG_PATH, "PNG")

print(f"Saved {PNG_PATH} size={Image.open(PNG_PATH).size}")

try:
    turtle.bye()
except turtle.Terminator:
    pass
