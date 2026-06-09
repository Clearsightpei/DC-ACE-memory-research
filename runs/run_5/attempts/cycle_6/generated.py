"""Cycle 6 (run_5) Drawer output.

Draws 一, 二, 三 by reusing the run_4 mastered 横 (heng) primitive
from the Success Bank. Placement is read from the MMH GT PNGs:
each GT's horizontal stroke band is measured in pixel coordinates,
then converted to turtle coordinates (canvas 800x600, origin at
center, y axis pointing UP).

Pixel->turtle (canvas 800x600):
    turtle_x = pixel_x - 400
    turtle_y = 300 - pixel_y

Each heng's span ≈ 400*scale in turtle units (canonical endpoints
P0=(-200,-3), P3=(+200,+3) per heng.py).
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

from heng import draw as draw_heng  # noqa: E402


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


# ---- Placement table (measured from ground_truths/cycle_6/*.png) ----
# Each tuple: (ox, oy, scale) in turtle coords.
# Derived from pixel x-range center and y-center of each GT stroke band.

# 一 — single heng, x=[244,568] yc=347 → cx=406, span=324
YI_HENG = (6.0, -47.0, 0.81)

# 二 — two hengs
# top    x=[313,493] yc=265 → cx=403, span=180
# bottom x=[246,566] yc=415 → cx=406, span=320
ER_TOP    = (3.0,  35.0, 0.45)
ER_BOTTOM = (6.0, -115.0, 0.80)

# 三 — three hengs
# top  x=[322,489] yc=240 → cx=405, span=167
# mid  x=[328,480] yc=338 → cx=404, span=152
# bot  x=[246,582] yc=440 → cx=414, span=336
SAN_TOP    = (5.0,   60.0, 0.42)
SAN_MID    = (4.0,  -38.0, 0.38)
SAN_BOTTOM = (14.0, -140.0, 0.84)


def task_01(t, screen):
    reset_turtle(t)
    ox, oy, sc = YI_HENG
    draw_heng(t, ox=ox, oy=oy, scale=sc)
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_一.png"))


def task_02(t, screen):
    reset_turtle(t)
    ox, oy, sc = ER_TOP
    draw_heng(t, ox=ox, oy=oy, scale=sc)
    ox, oy, sc = ER_BOTTOM
    draw_heng(t, ox=ox, oy=oy, scale=sc)
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "02_二.png"))


def task_03(t, screen):
    reset_turtle(t)
    ox, oy, sc = SAN_TOP
    draw_heng(t, ox=ox, oy=oy, scale=sc)
    ox, oy, sc = SAN_MID
    draw_heng(t, ox=ox, oy=oy, scale=sc)
    ox, oy, sc = SAN_BOTTOM
    draw_heng(t, ox=ox, oy=oy, scale=sc)
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "03_三.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0)
    t = turtle.Turtle()

    task_01(t, screen); screen.update()
    task_02(t, screen); screen.update()
    task_03(t, screen); screen.update()

    try:
        screen.bye()
    except turtle.Terminator:
        pass


if __name__ == "__main__":
    main()
