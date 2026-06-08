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
    t.reset()
    t.hideturtle()
    t.speed(0)
    t.pencolor("black")
    t.pensize(3)
    t.penup()
    t.goto(0, 0)
    t.setheading(90)


# ── Task 01 | 又 | you
def draw_you_skel(t):
    """Skeleton phase: 又 = 横撇 (top) + 捺 (bottom-right sweep crossing through).

    From brief:
      横撇:
        heng: (-100, +120) → (+50, +120)
        折 + 撇 tail to (-100, -150)
      捺:
        head (-30, +30) → kick base (+150, -130) → kick tip (+200, -120)
    """
    t.pensize(3)  # uniform thin — skeleton only

    # 横撇 (top compound stroke)
    # heng segment
    t.penup()
    t.goto(-100, 120)
    t.pendown()
    t.goto(50, 120)
    # 撇 tail from corner down-left
    t.goto(-100, -150)
    t.penup()

    # 捺 (bottom-right sweep crossing through the 撇)
    # head (-30, +30) → kick base (+150, -130) → kick tip (+200, -120)
    t.penup()
    t.goto(-30, 30)
    t.pendown()
    t.goto(150, -130)
    t.goto(200, -120)
    t.penup()


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0)
    t = turtle.Turtle()
    reset_turtle(t)
    draw_you_skel(t)
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_又_skel.png"))


if __name__ == "__main__":
    main()
