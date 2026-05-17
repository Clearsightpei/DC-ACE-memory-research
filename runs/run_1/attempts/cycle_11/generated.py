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
    # Corrected memory theory (lesson #6): 天 = a SHORT heng on top,
    # then the CONFIRMED 大 recipe directly below it (c8, scored 1.00).
    # The embedded 大 has the ONE full-width bar; the pie starts ABOVE
    # that bar and pierces through it (pie's top is the highest point of
    # the 大), na crosses from the same point. NOT 二 + 人, NOT two
    # stacked full bars with detached legs.
    t.pensize(11)

    # Short heng on top (narrower than the 大's bar below it)
    t.penup(); t.goto(-90, 150); t.setheading(2)
    t.pendown(); t.forward(180); t.penup()

    # ----- embedded 大 (confirmed c8 recipe, scaled/centered) -----
    # The single full-width bar of the 大. The pie pierces through it
    # from above, so it must start ABOVE this bar.
    bar_y = 70
    # Heng of the 大 (the only full-width horizontal)
    t.penup(); t.goto(-160, bar_y); t.setheading(2)
    t.pendown(); t.forward(320); t.penup()

    # pie: starts ABOVE the bar (its top is the highest point of the 大)
    # and sweeps down-left, piercing through the bar.
    t.penup(); t.goto(40, 140); t.setheading(255)
    t.pendown()
    for _ in range(60):
        t.forward(220 / 60)
        t.right(0.85)          # gentle leftward sweep
    t.penup()

    # na: from the same crossing region, sweeps down-right.
    t.penup(); t.goto(20, 130); t.setheading(305)
    t.pendown()
    for i in range(60):
        t.forward(210 / 60)
        t.left(0.5 if i < 35 else 0.12)   # front-loaded curve, flat tail
    t.penup()


# ── Task 02 | 王 | wang
def task_02(t):
    # 三 with a vertical spine through all three bar centres.
    # Top bar, shorter middle bar, widest bottom bar; one vertical
    # connecting their centres.
    t.pensize(11)

    top_y, mid_y, bot_y = 150, 0, -150

    # top heng
    t.penup(); t.goto(-150, top_y); t.setheading(2)
    t.pendown(); t.forward(300); t.penup()

    # middle heng (shorter)
    t.penup(); t.goto(-110, mid_y); t.setheading(2)
    t.pendown(); t.forward(220); t.penup()

    # bottom heng (widest)
    t.penup(); t.goto(-165, bot_y); t.setheading(2)
    t.pendown(); t.forward(330); t.penup()

    # vertical spine through the centres
    t.penup(); t.goto(0, top_y + 8); t.setheading(270)
    t.pendown(); t.forward((top_y - bot_y) + 16); t.penup()


# ── Task 03 | 土 | tu
def task_03(t):
    # A short heng crossed by a vertical (like 十), then a wider
    # heng across the bottom — the bottom bar is the widest.
    t.pensize(11)

    mid_y, bot_y = 60, -150

    # upper (shorter) heng
    t.penup(); t.goto(-110, mid_y); t.setheading(2)
    t.pendown(); t.forward(220); t.penup()

    # bottom heng (widest)
    t.penup(); t.goto(-170, bot_y); t.setheading(2)
    t.pendown(); t.forward(340); t.penup()

    # vertical spine: from above the upper heng down to the bottom heng
    t.penup(); t.goto(0, 160); t.setheading(270)
    t.pendown(); t.forward(160 - bot_y); t.penup()


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT); screen.bgcolor("white")
    screen.tracer(0, 0)
    t = turtle.Turtle()
    for idx, (key, fn) in enumerate([
        ("天", task_01),
        ("王", task_02),
        ("土", task_03),
    ], start=1):
        reset_turtle(t)
        fn(t)
        screen.update()
        save_canvas_to_png(screen, os.path.join(OUT_DIR, f"{idx:02d}_{key}.png"))


if __name__ == "__main__":
    main()
