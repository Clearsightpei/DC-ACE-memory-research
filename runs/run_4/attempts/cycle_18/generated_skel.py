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


# ── Task 01 | 八 | ba
def draw_ba_skel(t):
    """Skeleton phase: 八 = SEPARATED 撇 (left) + 捺 (right).
    Heads near each other at upper-middle but NOT TOUCHING (~80 px gap).
    Both sweep downward and outward.

    From brief:
      撇: head (-30, +75)  → tail (-100, -110).
      捺 main: head (+50, +100) → kick base (+150, -110).
      Kick: (+150, -110) → (+200, -100).
    """
    t.pensize(3)  # uniform thin — skeleton phase only

    # 撇 (left): head (-30, +75) → tail (-100, -110)
    t.penup()
    t.goto(-30, 75)
    t.pendown()
    t.goto(-100, -110)
    t.penup()

    # 捺 main sweep: head (+50, +100) → kick base (+150, -110)
    t.penup()
    t.goto(50, 100)
    t.pendown()
    t.goto(150, -110)
    # Stitched flat kick: (+150, -110) → (+200, -100)
    t.goto(200, -100)
    t.penup()


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0)
    t = turtle.Turtle()
    reset_turtle(t)
    draw_ba_skel(t)
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_八_skel.png"))


if __name__ == "__main__":
    main()
