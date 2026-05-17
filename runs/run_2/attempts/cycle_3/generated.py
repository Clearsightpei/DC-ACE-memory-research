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
    # Corrected recipe: round dab, NOT a line.
    t.penup(); t.goto(0, 0); t.pendown()
    t.dot(11)
    t.penup()

# ── Task 02 | 捺 | na
def task_02(t):
    # Corrected concave-UP recipe: steeper start (~300), curve CLOCKWISE
    # with t.right, thin pensize 3, ~74 px.
    t.penup(); t.goto(-28, 30); t.setheading(300)
    t.pendown()
    steps = 60
    for i in range(steps):
        t.forward(74.0 / steps)
        t.right(0.7 if i < steps * 0.55 else 0.18)
    t.penup()

# ── Task 03 | 点 | dian
def task_03(t):
    # Same recipe as task_01 (independent repeat).
    t.penup(); t.goto(0, 0); t.pendown()
    t.dot(11)
    t.penup()

# ── Task 04 | 捺 | na
def task_04(t):
    # Same recipe as task_02 (independent repeat).
    t.penup(); t.goto(-28, 30); t.setheading(300)
    t.pendown()
    steps = 60
    for i in range(steps):
        t.forward(74.0 / steps)
        t.right(0.7 if i < steps * 0.55 else 0.18)
    t.penup()

# ── Task 05 | 撇 | pie
def task_05(t):
    # Mastered recipe (0.936) — reuse verbatim.
    t.penup(); t.goto(24, 35); t.setheading(260)
    t.pendown()
    steps = 60
    for _ in range(steps):
        t.forward(70.0 / steps)
        t.right(55.0 / steps)
    t.penup()

# ── Task 06 | 提 | ti
def task_06(t):
    # Mastered recipe (0.932) — reuse verbatim.
    t.penup(); t.goto(-30, -20); t.setheading(33)
    t.pendown(); t.forward(70); t.penup()

def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT); screen.bgcolor("white")
    screen.tracer(0, 0)
    t = turtle.Turtle()
    for idx, (key, fn) in enumerate([
        ("dian", task_01),
        ("na",   task_02),
        ("dian", task_03),
        ("na",   task_04),
        ("pie",  task_05),
        ("ti",   task_06),
    ], start=1):
        reset_turtle(t)
        fn(t)
        screen.update()
        save_canvas_to_png(screen, os.path.join(OUT_DIR, f"{idx:02d}_{key}.png"))

if __name__ == "__main__":
    main()
