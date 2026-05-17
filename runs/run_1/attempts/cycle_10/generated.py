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


# ── Task 01 | 天 | tian
def task_01(t):
    # 天 = two stacked horizontal bars on top (upper shorter),
    # then a 人 below them: pie + na that SHARE one top apex and
    # splay outward WITHOUT crossing (memory: bottom must be 人,
    # not a crossed 乂 — that reads as 元).
    t.pensize(11)

    # Upper (shorter) bar, near-flat
    t.penup(); t.goto(-90, 150); t.setheading(0)
    t.pendown(); t.forward(180); t.penup()

    # Lower (longer) bar, near-flat
    t.penup(); t.goto(-150, 70); t.setheading(0)
    t.pendown(); t.forward(300); t.penup()

    # 人 bottom: shared apex at the centre underside of the lower bar.
    apex_x, apex_y = 0, 70

    # pie — left-falling sweep from the shared apex, gentle curve
    t.penup(); t.goto(apex_x, apex_y); t.setheading(250)
    t.pendown()
    for _ in range(60):
        t.forward(200 / 60)
        t.right(0.5)
    t.penup()

    # na — right-falling press from the SAME shared apex, splaying
    # outward the other way. They meet only at the apex (no crossing).
    t.penup(); t.goto(apex_x, apex_y); t.setheading(290)
    t.pendown()
    for i in range(60):
        t.forward(205 / 60)
        t.left(0.45 if i < 35 else 0.12)
    t.penup()


# ── Task 02 | 中 | zhong
def task_02(t):
    # 中 = enclosed rectangular box with one long vertical stroke
    # passing straight down through its centre, extending well above
    # and below the box. Reuse the working enclosed-box approach.
    t.pensize(11)

    box_left, box_right = -90, 90
    box_top, box_bottom = 90, -90

    # Enclosed box (single closed rectangle path)
    t.penup(); t.goto(box_left, box_top)
    t.pendown()
    t.goto(box_right, box_top)
    t.goto(box_right, box_bottom)
    t.goto(box_left, box_bottom)
    t.goto(box_left, box_top)
    t.penup()

    # Long central vertical, extending above and below the box
    t.penup(); t.goto(0, box_top + 80); t.setheading(270)
    t.pendown()
    t.forward((box_top + 80) - (box_bottom - 80))
    t.penup()


# ── Task 03 | 日 | ri
def task_03(t):
    # 日 = a tall enclosed box divided by one horizontal bar across
    # its middle. Reuse the working enclosed-box (口) approach,
    # taller than wide.
    t.pensize(11)

    box_left, box_right = -75, 75
    box_top, box_bottom = 150, -150

    # Enclosed box (tall rectangle, single closed path)
    t.penup(); t.goto(box_left, box_top)
    t.pendown()
    t.goto(box_right, box_top)
    t.goto(box_right, box_bottom)
    t.goto(box_left, box_bottom)
    t.goto(box_left, box_top)
    t.penup()

    # Middle horizontal divider, spanning the full box width
    t.penup(); t.goto(box_left, 0); t.setheading(0)
    t.pendown(); t.forward(box_right - box_left); t.penup()


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT); screen.bgcolor("white")
    screen.tracer(0, 0)
    t = turtle.Turtle()
    for idx, (key, fn) in enumerate([
        ("天", task_01),
        ("中", task_02),
        ("日", task_03),
    ], start=1):
        reset_turtle(t)
        fn(t)
        screen.update()
        save_canvas_to_png(screen, os.path.join(OUT_DIR, f"{idx:02d}_{key}.png"))


if __name__ == "__main__":
    main()
