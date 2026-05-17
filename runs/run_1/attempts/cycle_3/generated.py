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

# ── Task 01 | 撇 | pie
def task_01(t):
    # left-falling sweep. Memory fix: rotate ~60 deg total over ~60 steps,
    # forward(70/60) + right(1) per step, start (24,35) heading 260.
    t.penup(); t.goto(24, 35); t.setheading(260)
    t.pendown()
    for _ in range(60):
        t.forward(70 / 60)
        t.right(1)
    t.penup()

# ── Task 02 | 捺 | na
def task_02(t):
    # right-falling press, roughly mirror of pie: start upper-left,
    # fall down-and-to-the-right, flattening tail. Heading ~280 (south,
    # slightly east), rotate LEFT to curve convex toward the lower-left
    # so the body bulges to the left and the tail flattens out.
    t.penup(); t.goto(-24, 35); t.setheading(280)
    t.pendown()
    for _ in range(60):
        t.forward(70 / 60)
        t.left(1)
    t.penup()

# ── Task 03 | 提 | ti
def task_03(t):
    # rising flick: start lower-left, go up-and-to-the-right, straight,
    # ending higher than it began. Short stroke.
    t.penup(); t.goto(-30, -20); t.setheading(30)  # up and to the right
    t.pendown()
    t.forward(55)
    t.penup()

def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT); screen.bgcolor("white")
    screen.tracer(0, 0)
    t = turtle.Turtle()
    for idx, (key, fn) in enumerate([
        ("pie", task_01),
        ("na", task_02),
        ("ti", task_03),
    ], start=1):
        reset_turtle(t)
        fn(t)
        screen.update()
        save_canvas_to_png(screen, os.path.join(OUT_DIR, f"{idx:02d}_{key}.png"))

if __name__ == "__main__":
    main()
