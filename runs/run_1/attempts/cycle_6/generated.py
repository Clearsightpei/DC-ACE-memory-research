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


# ── Task 01 | 一 | yi
def task_01(t):
    # heng recipe (length ~70, slight upward tilt ~4°) scaled up
    # to ~340px wide, centered on (0,0).
    HALF = 170
    t.penup(); t.goto(-HALF, 0); t.setheading(4)
    t.pendown(); t.forward(2 * HALF); t.penup()


# ── Task 02 | 十 | shi
def task_02(t):
    # plus sign: scaled heng (horizontal) crossed by scaled shu
    # (vertical) through the middle. Both ~340px, centered.
    H = 170  # half horizontal extent
    V = 170  # half vertical extent
    # heng: slight upward tilt, centered
    t.penup(); t.goto(-H, 0); t.setheading(4)
    t.pendown(); t.forward(2 * H); t.penup()
    # shu: due south through the center, centered vertically
    t.penup(); t.goto(0, V); t.setheading(270)
    t.pendown(); t.forward(2 * V); t.penup()


# ── Task 03 | 人 | ren
def task_03(t):
    # Two strokes meeting at a top apex near (0, +160).
    # pie: left-falling sweep with ~60° clockwise curve (scaled up).
    # na: right-falling press, moderately steep, gentle bow (scaled up).
    APEX_X, APEX_Y = 0, 165

    # 撇 (pie) — from apex, falling down-left. Scaled pie recipe:
    # ~60° total clockwise rotation over the stroke length.
    LEN_PIE = 320
    t.penup(); t.goto(APEX_X, APEX_Y); t.setheading(250)
    t.pendown()
    steps = 60
    for _ in range(steps):
        t.forward(LEN_PIE / steps)
        t.right(60 / steps)  # 60° total clockwise
    t.penup()

    # 捺 (na) — from apex, falling down-right. Scaled na recipe:
    # moderately steep, front-loaded curve flattening at the tail.
    LEN_NA = 320
    t.penup(); t.goto(APEX_X, APEX_Y); t.setheading(305)
    t.pendown()
    steps = 60
    for i in range(steps):
        t.forward(LEN_NA / steps)
        t.left(0.45 if i < 35 else 0.12)  # early curve, flattening tail
    t.penup()


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT); screen.bgcolor("white")
    screen.tracer(0, 0)
    t = turtle.Turtle()
    for idx, (key, fn) in enumerate([
        ("一", task_01),
        ("十", task_02),
        ("人", task_03),
    ], start=1):
        reset_turtle(t)
        fn(t)
        screen.update()
        save_canvas_to_png(screen, os.path.join(OUT_DIR, f"{idx:02d}_{key}.png"))


if __name__ == "__main__":
    main()
