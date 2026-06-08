"""Cycle 22 — 又 brushwork (iter 2: 捺 head higher, crosses 撇 visibly)."""

import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code'))
from heng_pie import draw as draw_heng_pie
from na import draw as draw_na


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


# ── Task 01 | 又 | you
def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0)

    t = turtle.Turtle()
    reset_turtle(t)

    # 横撇 (top): heng from upper-left, then 撇 sweeps down-left through the middle.
    draw_heng_pie(t, ox=20, oy=20, scale=0.9)

    # 捺: head HIGHER (near the 横撇 corner area), so it crosses through
    # the 撇's diagonal path. Head at (+30, +110), kick at (+165, -85).
    # Canonical na head (-150,+200) at scale 0.7 = (-105, +140).
    # Want head (+30, +110): ox=135, oy=-30.
    draw_na(t, ox=135, oy=-30, scale=0.70)

    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_又.png"))


if __name__ == "__main__":
    main()
