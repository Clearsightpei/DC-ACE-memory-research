import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code'))

from heng import draw as draw_heng


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
def draw_yi(t):
    # Compose mastered 横 (heng.py, c1 rubric 10/10) at the approved skeleton position.
    # Canonical heng endpoints: (-200, -3) → (+200, +3).
    # With scale=0.8: (-160, -2.4) → (+160, +2.4).
    # With oy=-100: (-160, -102.4) → (+160, -97.6).
    # Matches approved skeleton (-160, -100) → (+160, -100) within heng's intrinsic ±2.4 tilt.
    draw_heng(t, ox=0, oy=-100, scale=0.8)


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0)
    t = turtle.Turtle()
    reset_turtle(t)
    draw_yi(t)
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_一.png"))


if __name__ == "__main__":
    main()
