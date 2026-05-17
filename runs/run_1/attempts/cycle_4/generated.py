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
    # Memory fix: na = shallow bow with a flattening tail, NOT a mirrored
    # pie. Start (-24,35), heading ~285°, 60 steps of forward(70/60),
    # ~20° total LEFT-rotation, front-loaded so the tail flattens.
    t.penup(); t.goto(-24, 35); t.setheading(285)
    t.pendown()
    for i in range(60):
        t.forward(70 / 60)
        if i < 30:
            t.left(0.5)   # steps 1–30: more curve
        else:
            t.left(0.15)  # steps 31–60: tail flattens
    t.penup()


# ── Task 02 | 点 | dian
def task_02(t):
    # A very short stroke (~15–20px), drawn top-to-bottom-right: a small
    # tear-drop/dot. The smallest stroke. Heading ~300° = down and to
    # the right; ~18px total.
    t.penup(); t.goto(-6, 9); t.setheading(300)
    t.pendown()
    for i in range(18):
        t.forward(18 / 18)
        t.left(0.6)  # very slight bow gives a tear-drop feel
    t.penup()


# ── Task 03 | 横折 | heng_zhe
def task_03(t):
    # Compound: horizontal segment left-to-right, then sharp ~90° turn
    # folding straight downward — like the top-right corner of a box.
    # heng length ~60px (from memory: heng ~70px, slight upward tilt);
    # then turn the corner and go down ~55px.
    t.penup(); t.goto(-30, 25); t.setheading(4)  # slight upward tilt
    t.pendown()
    t.forward(60)            # horizontal segment
    t.right(94)              # sharp ~90° fold (4° tilt + 90° → ~94° turn)
    t.forward(55)            # vertical drop
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
