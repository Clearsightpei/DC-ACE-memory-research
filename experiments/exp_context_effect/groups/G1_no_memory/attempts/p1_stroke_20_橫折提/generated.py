"""
G1 no-memory attempt: p1_stroke_20_橫折提 (heng-zhe-ti)
Compound stroke:
  1. 横 (heng): horizontal stroke moving right
  2. 折 (zhe): sharp ~90 degree turn dropping down (short vertical)
  3. 提 (ti): rising stroke sweeping up to the right
Common in radicals like 讠 (as in 认, 说). Structure resembles a small
"L" whose bottom leg kicks upward.

Uses Python turtle -> EPS -> PIL to save exact 300x300 PNG.
"""

import turtle
from PIL import Image
import os
import io

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
PNG_PATH = os.path.join(OUT_DIR, "01_橫折提.png")
EPS_PATH = os.path.join(OUT_DIR, "_tmp.eps")

SIZE = 300  # target PNG size in px

# --- Turtle setup: 300x300 window, math-y (up positive) via default turtle ---
screen = turtle.Screen()
screen.setup(width=SIZE, height=SIZE)
screen.screensize(SIZE, SIZE)
screen.bgcolor("white")
screen.tracer(0, 0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.color("black")
t.penup()

def goto(x, y):
    t.penup()
    t.goto(x, y)

def line_to(x, y, width):
    t.pensize(width)
    t.pendown()
    t.goto(x, y)
    t.penup()

# Coordinate frame: turtle default origin at center, (-150..150) both axes.
# Design in a 米字格 mental grid where useful cell ~= 220 px, centered.
# --- Stroke 1: 横 (heng), slight upward tilt as brush convention ---
# Start left-mid-upper, sweep right with slight rise.
x0, y0 = -90, 70          # starting point of heng
x1, y1 =  80, 78          # end of heng (slight upward slant)
goto(x0, y0)
line_to(x1, y1, 10)

# --- Stroke 2: 折 (the vertical drop segment) ---
# Continues from heng end, drops down nearly vertically, slightly leftward
# to mimic brush pressure at the corner.
x2, y2 = 72, -30
goto(x1, y1)
line_to(x2, y2, 10)

# --- Stroke 3: 提 (ti), rising stroke sweeping up-right from bottom ---
# Starts at bottom of the vertical, kicks up and to the right, tapering.
# We simulate taper with two overlapping segments (thick base, thin tip).
x3a, y3a = x2, y2                # base of ti
x3b, y3b = x2 + 40, y2 + 15      # mid of ti
x3c, y3c = x2 + 95, y2 + 55      # tip of ti (up-right)

# thick base -> mid
goto(x3a, y3a)
line_to(x3b, y3b, 11)
# thinner mid -> tip (taper effect)
goto(x3b, y3b)
line_to(x3c, y3c, 5)

# --- Small corner reinforcement (顿笔) at the heng-zhe joint ---
# A tiny thickening dot at the top-right corner where heng meets zhe.
goto(x1 + 2, y1 - 2)
t.pensize(1)
t.pendown()
t.begin_fill()
t.fillcolor("black")
for _ in range(4):
    t.forward(8)
    t.right(90)
t.end_fill()
t.penup()

screen.update()

# --- Export via EPS -> PIL to PNG, forced to 300x300 ---
canvas = screen.getcanvas()
canvas.postscript(file=EPS_PATH, colormode="color")

# Load EPS with PIL (requires Ghostscript). Fallback: rasterize the canvas
# tk snapshot via ImageGrab if Ghostscript missing.
try:
    img = Image.open(EPS_PATH)
    img.load(scale=2)
    img = img.convert("RGB")
    # Fit/crop to exactly 300x300, centering.
    w, h = img.size
    # Scale to fit, then center-crop/pad.
    scale = min(SIZE / w, SIZE / h)
    nw, nh = max(1, int(w * scale)), max(1, int(h * scale))
    img = img.resize((nw, nh), Image.LANCZOS)
    canvas_img = Image.new("RGB", (SIZE, SIZE), "white")
    canvas_img.paste(img, ((SIZE - nw) // 2, (SIZE - nh) // 2))
    canvas_img.save(PNG_PATH, "PNG")
finally:
    if os.path.exists(EPS_PATH):
        try:
            os.remove(EPS_PATH)
        except OSError:
            pass

try:
    screen.bye()
except turtle.Terminator:
    pass

print(f"Wrote {PNG_PATH}")
