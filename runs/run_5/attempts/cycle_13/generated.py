"""Cycle 13 drawer — 王, 主, 生.

GT-measured positions:

王 (3 components):
  top heng:    turtle center (5, 63),   width 183 → scale 0.46
  middle heng: turtle center (3, 24),   width ~150 → scale 0.38
  shu:         turtle center (3, -48),  length 193 → scale 0.48
  bottom heng: turtle center (7, -157), width 326 → scale 0.82

主 (4 components):
  dian:        turtle center (4, 99)
  top heng:    turtle center (4, 18),   width 193 → scale 0.48
  middle heng: turtle center (0, ~-65), width ~150 → scale 0.38
  shu:         turtle center (0, -80),  length 169 → scale 0.42
  bottom heng: turtle center (12, -175), width 338 → scale 0.85

生 (3 components, lots of fusion):
  pie:         turtle center (-94, -14), height ~125 (steep, curved)
  shu:         center x=8, y_top=114, y_bot=-167, scale 0.70, center y=-26
  top heng (the right-of-pie short one): turtle (54, 5), width ~92 → scale 0.23
  middle heng: turtle (6, -88), width 150 → scale 0.38
  bottom heng: turtle (11, -182), width 317 → scale 0.79
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

from heng import draw as draw_heng
from shu import draw as draw_shu
from pie import draw as draw_pie
from dian import draw as draw_dian


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


def draw_wang(t):
    """王: top heng + middle heng + shu through both + bottom heng."""
    # top heng (short)
    draw_heng(t, ox=5, oy=63, scale=0.46)
    # middle heng (shorter)
    draw_heng(t, ox=3, oy=24, scale=0.38)
    # shu through middle
    draw_shu(t, ox=3, oy=-48, scale=0.48)
    # bottom heng (long)
    draw_heng(t, ox=7, oy=-157, scale=0.82)


def draw_zhu(t):
    """主: dian + 王-pattern (top/mid heng + shu + bottom heng)."""
    # dian at top
    draw_dian(t, ox=4, oy=99, scale=1.0)
    # top heng
    draw_heng(t, ox=4, oy=18, scale=0.48)
    # middle heng (shorter)
    draw_heng(t, ox=0, oy=-65, scale=0.38)
    # shu through middle area
    draw_shu(t, ox=0, oy=-80, scale=0.42)
    # bottom heng (long)
    draw_heng(t, ox=12, oy=-175, scale=0.85)


def draw_sheng(t):
    """生: pie + top heng + middle heng + shu + bottom heng."""
    # pie (top-left, steep): scale ~0.32, center at (-94, -14)
    # canonical pie center is approx (-15, 10) at scale 1; at scale 0.32 -> (-5, 3)
    # so ox = -94 - (-5) = -89, oy = -14 - 3 = -17
    draw_pie(t, ox=-89, oy=-17, scale=0.32)
    # top heng — short, sits to the right of the pie tail-area
    # It runs from where the pie ends (around x=-70, y=5) rightward.
    # Measured: center x=54, y=5, width 92 -> scale 0.23
    draw_heng(t, ox=54, oy=5, scale=0.23)
    # middle heng crossing the shu
    draw_heng(t, ox=6, oy=-88, scale=0.38)
    # shu (long vertical)
    draw_shu(t, ox=8, oy=-26, scale=0.70)
    # bottom heng (long)
    draw_heng(t, ox=11, oy=-182, scale=0.79)


def render_all():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.tracer(0, 0)
    t = turtle.Turtle()

    tasks = [
        ("01_王.png", draw_wang),
        ("02_主.png", draw_zhu),
        ("03_生.png", draw_sheng),
    ]

    for fname, fn in tasks:
        reset(t)
        fn(t)
        screen.update()
        save_canvas_to_png(screen, os.path.join(OUT_DIR, fname))

    try:
        screen.bye()
    except Exception:
        pass


if __name__ == "__main__":
    render_all()
