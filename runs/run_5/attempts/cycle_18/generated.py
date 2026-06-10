"""Cycle 18 — 玉 / 末 / 未.

All three are 1-stroke extensions of mastered Success Bank characters:
    玉 = 王 + 点 (dot in bottom-right quadrant)
    末 = 木 + LONG top heng
    未 = 木 + SHORT top heng (shorter than 木's middle heng)
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

from wang import draw as draw_wang  # noqa: E402
from mu   import draw as draw_mu    # noqa: E402
from heng import draw as draw_heng  # noqa: E402
from dian import draw as draw_dian  # noqa: E402


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


# ----------------- draw functions -----------------

def draw_yu(t):
    """玉 = 王 + 点 at bottom-right (above the bottom heng, right of shu)."""
    draw_wang(t, ox=0, oy=0, scale=1.0)
    # 王's bottom heng sits at oy=-158, scale 0.82 (spans ~[-160, +170]).
    # The dot in 玉 lives ABOVE bottom heng, RIGHT of the shu, ~midway down.
    draw_dian(t, ox=70, oy=-115, scale=0.95)


def draw_mo(t):
    """末 = 木 + LONG top heng above 木's middle heng."""
    # 木's middle heng is at oy=13, scale 0.55 (half-length ~110).
    # In 末 the top heng is LONGER than the middle heng.
    draw_mu(t, ox=0, oy=0, scale=1.0)
    draw_heng(t, ox=-3, oy=105, scale=0.68)


def draw_wei(t):
    """未 = 木 + SHORT top heng above 木's middle heng."""
    # In 未 the top heng is SHORTER than the middle heng (key distinction from 末).
    draw_mu(t, ox=0, oy=0, scale=1.0)
    draw_heng(t, ox=-3, oy=105, scale=0.40)


# ----------------- main render -----------------

def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.tracer(0)
    t = turtle.Turtle()

    tasks = [
        ("01_玉.png", draw_yu),
        ("02_末.png", draw_mo),
        ("03_未.png", draw_wei),
    ]
    for fname, fn in tasks:
        reset(t)
        fn(t)
        screen.update()
        out = os.path.join(OUT_DIR, fname)
        save_canvas_to_png(screen, out)
        print("wrote", out)

    try:
        screen.bye()
    except turtle.Terminator:
        pass


if __name__ == "__main__":
    main()
