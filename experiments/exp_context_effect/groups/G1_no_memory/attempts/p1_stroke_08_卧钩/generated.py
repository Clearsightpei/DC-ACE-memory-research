"""
G1 (no-memory control) — Drawer attempt for p1_stroke_08_卧钩
Renders 卧钩 (lying hook, as in the bottom of 心) as a 300x300 PNG.
White background, black ink. One-shot, no memory.

Shape: shallow curve starting at upper-left, sweeping right and slightly
down (belly hanging), then hooking sharply up-and-left at the end.
"""

import turtle
from PIL import Image
import os
import math

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
PNG_PATH = os.path.join(OUT_DIR, "01_卧钩.png")
EPS_PATH = os.path.join(OUT_DIR, "_tmp.eps")

# Canvas
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
t.pensize(9)

# Coordinates in turtle math-convention: (0,0) is center, y grows UP.
# 卧钩 lies across the middle of the cell, belly hangs below center.
# Start: upper-left region. End of curve: right side. Hook: sharp up-left.

# Draw the main curved body using a series of small segments approximating
# a shallow parabola-like arc.
def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Start point (top-left of stroke)
x0, y0 = -95, 35
# End point of curve (right side, slightly lower)
x1, y1 = 80, -15
# Belly (lowest point of the curve) roughly 60% along, dipping down
# We'll parametrize as a quadratic Bezier with control point below middle.
cx, cy = -5, -70  # control point pulls curve downward

move_to(x0, y0)

STEPS = 60
for i in range(1, STEPS + 1):
    u = i / STEPS
    # Quadratic Bezier
    x = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * cx + u ** 2 * x1
    y = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * cy + u ** 2 * y1
    t.goto(x, y)

# Now the hook: from (x1, y1), sharp hook up and to the left.
# The 卧钩 hook points up-left, short and decisive.
hook_end_x = x1 - 40
hook_end_y = y1 + 45
# Slight curve into the hook
HK_STEPS = 20
hx0, hy0 = x1, y1
# control point up and slightly right to give the hook a hint of curl
hcx, hcy = x1 + 5, y1 + 20
for i in range(1, HK_STEPS + 1):
    u = i / HK_STEPS
    x = (1 - u) ** 2 * hx0 + 2 * (1 - u) * u * hcx + u ** 2 * hook_end_x
    y = (1 - u) ** 2 * hy0 + 2 * (1 - u) * u * hcy + u ** 2 * hook_end_y
    t.goto(x, y)

screen.update()

# Save canvas to EPS then convert to PNG at exact 300x300.
canvas = screen.getcanvas()
canvas.postscript(file=EPS_PATH, colormode='color')

# Convert EPS -> PNG using PIL
img = Image.open(EPS_PATH)
img.load(scale=4)  # higher res load for quality
img = img.convert("RGB")

# Composite onto white background
white_bg = Image.new("RGB", img.size, "white")
white_bg.paste(img, (0, 0))
white_bg = white_bg.resize((SIZE, SIZE), Image.LANCZOS)
white_bg.save(PNG_PATH, "PNG")

try:
    os.remove(EPS_PATH)
except OSError:
    pass

print(f"Wrote {PNG_PATH}")

try:
    turtle.bye()
except turtle.Terminator:
    pass
