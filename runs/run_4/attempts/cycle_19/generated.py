"""Cycle 19 — 人 brushwork (iter 2: 捺 head slightly below 撇 apex)."""

import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code'))
from pie import draw as draw_pie
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


# ── Task 01 | 人 | ren
def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0)

    t = turtle.Turtle()
    reset_turtle(t)

    # 撇 dominant: head at apex (+15, +120). Reaches well down-left.
    # pie head canonical (+150,+200) at scale 0.70 = (+105,+140).
    # Want head (+15,+120): ox=15-105=-90, oy=120-140=-20.
    draw_pie(t, ox=-90, oy=-20, scale=0.70)

    # 捺 head SLIGHTLY BELOW 撇's apex — at (+15, +90), making the
    # junction visibly below the top (vs 入 where 捺 starts much lower).
    # na head canonical (-150,+200) at scale 0.50 = (-75,+100).
    # Want head (+15,+90): ox=15-(-75)=90, oy=90-100=-10.
    draw_na(t, ox=90, oy=-10, scale=0.50)

    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_人.png"))


if __name__ == "__main__":
    main()
