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


# ── Task 01 | 大 | da
def task_01(t):
    # 大 = heng (horizontal bar) crossed by pie + na.
    # STRUCTURAL FIX (memory c7 lesson): the pie must start ABOVE the
    # heng — its top is the character's highest point and pokes
    # through the bar. The heng is crossed near its MIDDLE, NOT
    # sitting on top of a separate 人/八 below it. If heng is the
    # topmost element with pie+na hanging below, OCR reads 天.
    t.pensize(12)

    # 1) Horizontal bar (heng), flat, centered, crossed near its middle.
    #    Place it in the upper-middle so strokes can pass above it.
    t.penup(); t.goto(-150, 70); t.setheading(0)
    t.pendown(); t.forward(300); t.penup()

    # 2) Pie: a left-falling sweep whose TOP is ABOVE the bar (highest
    #    point of the whole glyph) and which pierces through the heng,
    #    continuing well below it to the lower-left.
    t.penup(); t.goto(40, 150); t.setheading(255)
    t.pendown()
    steps = 70
    for _ in range(steps):
        t.forward(300 / steps)
        t.right(0.55)  # gentle ~38° clockwise bend over the stroke
    t.penup()

    # 3) Na: a right-falling press starting near where the pie crosses
    #    the bar (just below the bar's middle), sweeping down-right.
    t.penup(); t.goto(-20, 55); t.setheading(305)
    t.pendown()
    steps = 60
    for i in range(steps):
        t.forward(230 / steps)
        t.left(0.45 if i < 35 else 0.12)  # front-loaded curve, flat tail
    t.penup()


# ── Task 02 | 八 | ba
def task_02(t):
    # 八 = two SEPARATE splaying strokes, NOT touching at the top —
    # like two spread legs. Left = pie, right = na. Gap at the top.
    t.pensize(12)

    # Left leg: pie, top-center-ish, falling down-left.
    t.penup(); t.goto(-30, 150); t.setheading(245)
    t.pendown()
    steps = 60
    for _ in range(steps):
        t.forward(300 / steps)
        t.right(0.45)  # mild left-falling curve
    t.penup()

    # Right leg: na, starts separated from the pie's top (clear gap),
    # falling down-right.
    t.penup(); t.goto(30, 150); t.setheading(300)
    t.pendown()
    steps = 60
    for i in range(steps):
        t.forward(300 / steps)
        t.left(0.40 if i < 35 else 0.12)  # front-loaded press curve
    t.penup()


# ── Task 03 | 三 | san
def task_03(t):
    # 三 = three stacked horizontal strokes (heng), flat.
    # Top: shorter. Middle: shortest. Bottom: longest.
    t.pensize(12)

    # Top heng — shorter, upper.
    t.penup(); t.goto(-110, 120); t.setheading(0)
    t.pendown(); t.forward(220); t.penup()

    # Middle heng — short, centered vertically.
    t.penup(); t.goto(-95, 0); t.setheading(0)
    t.pendown(); t.forward(190); t.penup()

    # Bottom heng — longest, lower.
    t.penup(); t.goto(-150, -120); t.setheading(0)
    t.pendown(); t.forward(300); t.penup()


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT); screen.bgcolor("white")
    screen.tracer(0, 0)
    t = turtle.Turtle()
    for idx, (key, fn) in enumerate([
        ("大", task_01),
        ("八", task_02),
        ("三", task_03),
    ], start=1):
        reset_turtle(t)
        fn(t)
        screen.update()
        save_canvas_to_png(screen, os.path.join(OUT_DIR, f"{idx:02d}_{key}.png"))


if __name__ == "__main__":
    main()
