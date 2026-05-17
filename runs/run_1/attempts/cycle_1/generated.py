import io, os, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1)
    img.convert("RGBA").save(path, "PNG")

def reset_turtle(t):
    t.reset(); t.hideturtle(); t.speed(0)
    t.pencolor("black"); t.pensize(3)
    t.penup(); t.goto(0, 0); t.setheading(90)

# ── Task 01 | 横 | heng
def task_01(t):
    # Horizontal stroke, left-to-right, faint upward tilt.
    # Length ~ 300 px, slight upward slope (~3 degrees).
    # Start a bit below-left of center, end slightly above-right of center.
    t.penup()
    t.goto(-150, -8)
    t.setheading(3)   # almost horizontal, with a tiny upward tilt
    t.pendown()
    t.forward(300)

# ── Task 02 | 竖 | shu
def task_02(t):
    # Vertical stroke, top-to-bottom, perfectly straight.
    # Length ~ 300 px, centered horizontally at x=0.
    t.penup()
    t.goto(0, 150)
    t.setheading(270)  # straight down
    t.pendown()
    t.forward(300)

# ── Task 03 | 撇 | pie
def task_03(t):
    # Left-falling sweep: starts upper-right, ends lower-left,
    # convex bulge toward the right.
    # Implemented as a circular arc. To bulge right while traveling
    # from upper-right (e.g. ~(100, 130)) toward lower-left, the arc's
    # center must be to the right of the travel direction at each point,
    # which means turning *right* (negative radius in turtle's circle()).
    # Start heading: pointing down-and-to-the-left (~225 degrees).
    t.penup()
    t.goto(100, 130)
    # Heading 225 = down-left. We want to curve so the path bulges right
    # of the chord. Using circle(-r, extent) turns right while drawing.
    t.setheading(225)
    t.pendown()
    # Arc of ~60 degrees on a moderately large radius produces a gentle
    # convex-right curve, ending roughly in the lower-left quadrant.
    t.circle(-260, 60)

def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT); screen.bgcolor("white")
    screen.tracer(0, 0)
    t = turtle.Turtle()
    for idx, (key, fn) in enumerate([
        ("heng", task_01),
        ("shu",  task_02),
        ("pie",  task_03),
    ], start=1):
        reset_turtle(t)
        fn(t)
        screen.update()
        save_canvas_to_png(screen, os.path.join(OUT_DIR, f"{idx:02d}_{key}.png"))

if __name__ == "__main__":
    main()
