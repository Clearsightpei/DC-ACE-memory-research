"""Cycle 66 — 自 (zì). 6 MMH strokes:
   s1 pie, s2 shu, s3 heng_zhe, s4 heng, s5 heng, s6 heng.

All positions resolved via anchor_to_xy(). No magic numbers.
"""
import io
import os
import sys
import turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from _anchor import anchor_to_xy  # noqa: E402
from pie import draw_pie  # noqa: E402
from shu import draw_shu  # noqa: E402
from heng_zhe import draw_heng_zhe  # noqa: E402
from heng import draw_heng  # noqa: E402


def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1)
    img.convert("RGBA").save(path, "PNG")


def reset(t):
    t.reset()
    t.hideturtle()
    t.speed(0)
    t.pencolor("black")
    t.penup()
    t.goto(0, 0)
    t.setheading(90)


def task_01(t, screen):
    reset(t)

    # s1: pie — from ("TC", 0.308, 0.224) to ("ML", 0.664, 0.016)
    draw_pie(t, ("TC", 0.308, 0.224), ("ML", 0.664, 0.016))

    # s2: shu — from ("ML", 0.664, 0.016) to ("BL", 0.764, 1.252)
    draw_shu(t, ("ML", 0.664, 0.016), ("BL", 0.764, 1.252))

    # s3: heng_zhe — from ("ML", 0.92, 0.112), corner1 ("C", 0.96, 0.112),
    #               to ("BC", 0.96, 1.132)
    draw_heng_zhe(t,
                  ("ML", 0.92, 0.112),
                  ("C", 0.96, 0.112),
                  ("BC", 0.96, 1.132))

    # s4: upper internal heng — ("ML", 0.912, 0.864) to ("C", 0.96, 0.704)
    draw_heng(t, ("ML", 0.912, 0.864), ("C", 0.96, 0.704))

    # s5: lower internal heng — ("BL", 0.912, 0.46) to ("BC", 0.96, 0.332)
    draw_heng(t, ("BL", 0.912, 0.46), ("BC", 0.96, 0.332))

    # s6: bottom-of-box closing heng — ("BL", 0.868, 1.176) to ("BR", 0.048, 1.048)
    draw_heng(t, ("BL", 0.868, 1.176), ("BR", 0.048, 1.048))

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_自.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen)
    screen.update()


if __name__ == "__main__":
    main()
