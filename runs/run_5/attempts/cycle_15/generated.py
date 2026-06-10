"""cycle 15 — 王 / 土 / 口

Renderer: turtle + postscript, NO subprocess.

Measurements from GT (px → turtle math: tx=px-400, ty=300-py):

王 GT:
  top heng    cx=405 cy=237 w=183  -> ox=5  oy=64   scale=0.46
  mid heng    cx~405 cy~345 w~150  -> ox=5  oy=-45  scale=0.38
  bottom heng cx=407 cy=458 w=326  -> ox=7  oy=-158 scale=0.82
  shu (full)  cx=403 y=225..473    -> ox=3  oy=-49  scale=0.62  (half-len 124, base 200)

土 GT:
  top heng    cx=402 cy=325 w=187  -> ox=2  oy=-25  scale=0.47
  bottom heng cx=408 cy=457 w=322  -> ox=8  oy=-157 scale=0.805
  shu         cx~400 y=202..449    -> ox=0  oy=-25  scale=0.62  (pierces both hengs)

口 GT (3-stroke 楷书 order: 竖 left, 横折 top+right, 横 bottom):
  left shu  cx=313 cy=361 h=177    -> ox=-87 oy=-61  scale=0.44
  heng_zhe  corner≈(498,265)        -> ox=8   oy=-73  scale=0.85
  bottom heng cx=420 cy=420 w=154  -> ox=20  oy=-120 scale=0.385
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
from heng_zhe import draw as draw_hz


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
    """王 — 4 strokes: top heng, mid heng, bottom heng (long), shu through all."""
    # shu first as background (then heng overlap on top is fine — both black)
    draw_shu(t, ox=3, oy=-49, scale=0.62)
    draw_heng(t, ox=5, oy=64, scale=0.46)
    draw_heng(t, ox=5, oy=-45, scale=0.38)
    draw_heng(t, ox=7, oy=-158, scale=0.82)


def draw_tu(t):
    """土 — 3 strokes: top heng (short), shu, bottom heng (long & piercing)."""
    draw_shu(t, ox=0, oy=-25, scale=0.62)
    draw_heng(t, ox=2, oy=-25, scale=0.47)
    draw_heng(t, ox=8, oy=-157, scale=0.805)


def draw_kou(t):
    """口 — 3 strokes (楷书 stroke order): left shu, 横折 (top+right), bottom heng."""
    draw_shu(t, ox=-87, oy=-61, scale=0.44)
    draw_hz(t, ox=8, oy=-73, scale=0.85)
    draw_heng(t, ox=20, oy=-120, scale=0.385)


def render_one(screen, t, draw_fn, filename):
    reset(t)
    draw_fn(t)
    screen.update()
    out_path = os.path.join(OUT_DIR, filename)
    save_canvas_to_png(screen, out_path)


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.tracer(0, 0)
    t = turtle.Turtle()
    render_one(screen, t, draw_wang, "01_王.png")
    render_one(screen, t, draw_tu, "02_土.png")
    render_one(screen, t, draw_kou, "03_口.png")
    try:
        screen.bye()
    except turtle.Terminator:
        pass


if __name__ == "__main__":
    main()
