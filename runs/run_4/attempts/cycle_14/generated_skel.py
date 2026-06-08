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


# ── Task 01 | 一 | yi
def draw_yi_skel(t):
    t.pensize(3)  # uniform thin — skeleton phase only
    t.penup()
    t.goto(-160, -100)
    t.pendown()
    t.goto(160, -100)
    t.penup()


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0)
    t = turtle.Turtle()
    reset_turtle(t)
    draw_yi_skel(t)
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_一_skel.png"))


if __name__ == "__main__":
    main()
