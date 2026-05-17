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


# ── Task 01 | 点 | dian
def task_01(t):
    # GT 点 is tiny (~17 px), roundish, a small pressed dab — not a line.
    # A short blunt dab: pen down, tiny down-right move.
    t.penup(); t.goto(-6, 8); t.setheading(-60)  # down-right
    t.pendown()
    t.pensize(5)
    t.forward(16)
    t.penup()


# ── Task 02 | 撇 | pie
def task_02(t):
    # Upper-right -> lower-left, convex to the right. ~70 px total,
    # gentle clockwise arc (~55° over length). Thin pensize 3.
    t.penup(); t.goto(24, 35); t.setheading(260)
    t.pendown()
    steps = 60
    for _ in range(steps):
        t.forward(70.0 / steps)
        t.right(55.0 / steps)
    t.penup()


# ── Task 03 | 捺 | na
def task_03(t):
    # Upper-left -> lower-right, shallow ~45° descent, gentle bow that
    # flattens toward the tail. ~72 px. Front-load a small left-curve
    # then straighten.
    t.penup(); t.goto(-30, 28); t.setheading(-40)  # down-right, ~45°
    t.pendown()
    steps = 60
    for i in range(steps):
        t.forward(72.0 / steps)
        # bow more at the start, flatten toward the tail
        if i < steps * 0.5:
            t.left(0.55)
        else:
            t.left(0.05)
    t.penup()


# ── Task 04 | 提 | ti
def task_04(t):
    # Short, thin, straight rising line ~70 px, lower-left -> upper-right
    # at ~33°. No start blob.
    t.penup(); t.goto(-30, -20); t.setheading(33)
    t.pendown()
    t.forward(70)
    t.penup()


# ── Task 05 | 捺 | na  (second attempt — same recipe as task_03)
def task_05(t):
    t.penup(); t.goto(-30, 28); t.setheading(-40)
    t.pendown()
    steps = 60
    for i in range(steps):
        t.forward(72.0 / steps)
        if i < steps * 0.5:
            t.left(0.55)
        else:
            t.left(0.05)
    t.penup()


# ── Task 06 | 提 | ti  (second attempt — same recipe as task_04)
def task_06(t):
    t.penup(); t.goto(-30, -20); t.setheading(33)
    t.pendown()
    t.forward(70)
    t.penup()


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT); screen.bgcolor("white")
    screen.tracer(0, 0)
    t = turtle.Turtle()
    for idx, (key, fn) in enumerate([
        ("dian", task_01),
        ("pie",  task_02),
        ("na",   task_03),
        ("ti",   task_04),
        ("na",   task_05),
        ("ti",   task_06),
    ], start=1):
        reset_turtle(t)
        fn(t)
        screen.update()
        save_canvas_to_png(screen, os.path.join(OUT_DIR, f"{idx:02d}_{key}.png"))


if __name__ == "__main__":
    main()
