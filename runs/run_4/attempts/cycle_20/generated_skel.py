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


# ── Task 01 | 入 | ru
def draw_ru_skel(t):
    """Skeleton phase: 入 = 捺 DOMINANT + 撇 shorter, attached partway
    down 捺's upper portion (NOT a shared apex like 人).

    From brief:
      捺 main: head (0, +130) → kick base (+170, -120).
      捺 kick: (+170, -120) → (+220, -110).
      撇: head (+15, +120) → tail (-150, -80).
        — 撇 head starts ON the upper portion of 捺 (just below the
          捺 head, slightly to the right), then sweeps lower-left.
    """
    t.pensize(3)  # uniform thin — skeleton phase only

    # 捺 main sweep: head (0, +130) → kick base (+170, -120)
    t.penup()
    t.goto(0, 130)
    t.pendown()
    t.goto(170, -120)
    # Stitched flat kick: (+170, -120) → (+220, -110)
    t.goto(220, -110)
    t.penup()

    # 撇 attached partway down 捺's upper portion:
    # head (+15, +120) → tail (-150, -80)
    t.penup()
    t.goto(15, 120)
    t.pendown()
    t.goto(-150, -80)
    t.penup()


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0)
    t = turtle.Turtle()
    reset_turtle(t)
    draw_ru_skel(t)
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_入_skel.png"))


if __name__ == "__main__":
    main()
