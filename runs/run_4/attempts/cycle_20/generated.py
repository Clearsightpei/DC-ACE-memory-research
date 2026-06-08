"""Cycle 20 — 入 brushwork (iter 1).

入 = 捺 DOMINANT + 撇 shorter, attached partway down 捺's upper portion.
Distinguished from 人 (shared apex, 撇 dominant) by the asymmetric
scales: 捺=0.65 (vs 人's 0.50) and 撇=0.45 (vs 人's 0.70).
"""

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


# ── Task 01 | 入 | ru
def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0)

    t = turtle.Turtle()
    reset_turtle(t)

    # 捺 dominant (drawn first — establishes the spine).
    # na head canonical (-150, +200) at scale 0.65 = (-97.5, +130).
    # Want head at (~0, +130): ox = 0 - (-97.5) ≈ 97, oy = 130 - 130 = 0.
    draw_na(t, ox=97, oy=0, scale=0.65)

    # 撇 shorter, attached partway down 捺's upper portion.
    # pie head canonical (+150, +200) at scale 0.45 = (+67.5, +90).
    # Want head at (~15, +120): ox = 15 - 67.5 ≈ -52, oy = 120 - 90 = 30.
    draw_pie(t, ox=-52, oy=30, scale=0.45)

    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_入.png"))


if __name__ == "__main__":
    main()
