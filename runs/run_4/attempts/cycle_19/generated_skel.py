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


# ── Task 01 | 人 | ren
def draw_ren_skel(t):
    """Skeleton phase: 人 = 撇 + 捺 with SHARED apex (key difference from 八).

    Both stroke heads start at the SAME point (+30, +100). The two strokes
    then sweep outward — 撇 to the lower-left, 捺 to the lower-right with
    its flat-kick release. The shared apex is what distinguishes 人 from
    八 (which has an ~80 px gap between heads).

    From brief:
      撇: head (+30, +100) → tail (-100, -130).
      捺 main: head (+30, +100) → kick base (+150, -120).
      捺 kick: (+150, -120) → (+200, -110).
    """
    t.pensize(3)  # uniform thin — skeleton phase only

    # 撇: head (+30, +100) → tail (-100, -130)
    t.penup()
    t.goto(30, 100)
    t.pendown()
    t.goto(-100, -130)
    t.penup()

    # 捺 main sweep: head (+30, +100) → kick base (+150, -120)
    t.penup()
    t.goto(30, 100)
    t.pendown()
    t.goto(150, -120)
    # Stitched flat kick: (+150, -120) → (+200, -110)
    t.goto(200, -110)
    t.penup()


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0)
    t = turtle.Turtle()
    reset_turtle(t)
    draw_ren_skel(t)
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_人_skel.png"))


if __name__ == "__main__":
    main()
