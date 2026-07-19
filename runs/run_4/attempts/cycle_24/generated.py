"""Cycle 24 — 万 (wan) brushwork.

Composes three mastered Success Bank primitives:
  - heng.py            (top horizontal)
  - heng_zhe_gou.py    (right-side frame: L-corner + hook)
  - pie.py             (diagonal sweep from above-heng down to bottom-left)

The 撇 head must visibly rise ABOVE the top heng — this is the
distinguishing feature of 万 vs 力. Per task brief composition:
  draw_heng(t, ox=20, oy=+100, scale=0.75)
  draw_heng_zhe_gou(t, ox=70, oy=-25, scale=0.5)
  draw_pie(t, ox=-105, oy=-20, scale=0.7)

At pie scale=0.7, ox=-105, oy=-20: head = (0, 120). The top heng's
midline sits at y≈100, so the 撇 head pokes ~20 px above heng.
"""

import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code'))

from heng import draw as draw_heng
from heng_zhe_gou import draw as draw_heng_zhe_gou
from pie import draw as draw_pie


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


# ── Task 01 | 万 | wan
def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0)

    t = turtle.Turtle()
    reset_turtle(t)

    # Stroke 1: top heng
    draw_heng(t, ox=20, oy=+100, scale=0.75)

    # Stroke 2: 横折钩 (right frame)
    draw_heng_zhe_gou(t, ox=70, oy=-25, scale=0.5)

    # Stroke 3: 撇 — head above heng, sweeps down-left
    draw_pie(t, ox=-105, oy=-20, scale=0.7)

    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_万.png"))


if __name__ == "__main__":
    main()
