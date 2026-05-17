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


# ── Task 01 | 捺 | na
def task_01(t):
    # Shallow ~45° right-falling press: heading 325° (down-and-right),
    # front-loaded left curve, flattening tail. Verbatim from memory.
    t.penup(); t.goto(-30, 25); t.setheading(325)
    t.pendown()
    for i in range(60):
        t.forward(75 / 60)
        if i < 35:
            t.left(0.55)   # early curve
        else:
            t.left(0.12)   # tail flattens toward horizontal
    t.penup()


# ── Task 02 | 点 | dian
def task_02(t):
    # Smallest stroke: a tiny round dab, not a line. Filled 10px dot.
    t.penup(); t.goto(0, 0); t.pendown()
    t.dot(10)
    t.penup()


# ── Task 03 | 横折 | heng_zhe
def task_03(t):
    # Compact right-angle fold: ~45px horizontal then sharp fold south
    # for ~45px. Recentered on canvas. Verbatim from memory.
    t.penup(); t.goto(-22, 5); t.setheading(4)
    t.pendown()
    t.forward(45)        # horizontal, shorter than a lone heng
    t.right(94)          # fold to straight-down
    t.forward(45)        # vertical drop
    t.penup()


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT); screen.bgcolor("white")
    screen.tracer(0, 0)
    t = turtle.Turtle()
    for idx, (key, fn) in enumerate([
        ("na", task_01),
        ("dian", task_02),
        ("heng_zhe", task_03),
    ], start=1):
        reset_turtle(t)
        fn(t)
        screen.update()
        save_canvas_to_png(screen, os.path.join(OUT_DIR, f"{idx:02d}_{key}.png"))


if __name__ == "__main__":
    main()
