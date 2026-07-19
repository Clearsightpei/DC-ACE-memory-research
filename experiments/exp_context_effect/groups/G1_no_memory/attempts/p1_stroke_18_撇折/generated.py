"""
G1 no-memory attempt: 撇折 (pie stroke, then turn right into a small heng).
As seen in 车, 去. Structure:
  - First segment: a 撇 (pie) — starts upper-right, slants down-left,
    with slight curvature and a subtle taper.
  - Sharp turn (折) at the bottom-left endpoint.
  - Second segment: a short 横 (heng), horizontal to the right,
    typically flat with a tiny 顿笔 (pause) at the end.
Output: 01_撇折.png, 300x300, white bg, black ink.
"""

import turtle
from PIL import Image
import os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
EPS_PATH = os.path.join(OUT_DIR, "_tmp.eps")
PNG_PATH = os.path.join(OUT_DIR, "01_撇折.png")

CANVAS = 300

screen = turtle.Screen()
screen.setup(width=CANVAS, height=CANVAS)
screen.screensize(CANVAS, CANVAS)
screen.bgcolor("white")
screen.tracer(0, 0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.color("black")
t.pensize(9)

# Coordinate system: math convention, origin at center, +y up.
# The 撇折 sits roughly in the central cell of a 米字格.

# --- 撇 segment: upper-right to lower-left, gently curved ---
# Start point: upper-right area
start_x, start_y = 55, 70
# End point: lower-left area (this is the corner where 折 happens)
turn_x, turn_y = -50, -40

t.penup()
t.goto(start_x, start_y)
t.pendown()

# Slight 起笔 (subtle entry thickening) — draw pie as a curve using
# many small segments approximating a gentle arc that bulges upward.
steps = 40
import math
for i in range(1, steps + 1):
    u = i / steps
    # Linear interpolation with a slight arc offset (bulge upward-right)
    lx = start_x + (turn_x - start_x) * u
    ly = start_y + (turn_y - start_y) * u
    # Bulge: a small perpendicular offset peaking mid-stroke
    bulge = math.sin(u * math.pi) * 6  # px
    # Perpendicular direction (rotate travel vector 90 deg CCW):
    dx = turn_x - start_x
    dy = turn_y - start_y
    length = math.hypot(dx, dy)
    px = -dy / length
    py = dx / length
    t.goto(lx + px * bulge, ly + py * bulge)

# --- 折 corner: pen stays down; we're at (turn_x, turn_y) roughly ---
# Small 顿笔 at the corner: draw a tiny thickening by overlapping a dot
t.dot(11, "black")

# --- 横 segment: from corner, horizontal to the right, short ---
# Length ~ 80 px, slight upward tilt is typical; keep near flat.
heng_end_x = turn_x + 85
heng_end_y = turn_y + 3  # very slight rise
t.goto(heng_end_x, heng_end_y)

# End 顿笔 (pause dot at end of heng)
t.dot(12, "black")

# --- Export ---
canvas = screen.getcanvas()
canvas.postscript(file=EPS_PATH, width=CANVAS, height=CANVAS)

# Convert EPS -> PNG via PIL
img = Image.open(EPS_PATH)
img.load(scale=4)  # supersample then downscale for cleaner edges
img = img.convert("RGB")
img = img.resize((CANVAS, CANVAS), Image.LANCZOS)
img.save(PNG_PATH, "PNG")

try:
    os.remove(EPS_PATH)
except OSError:
    pass

screen.bye()
