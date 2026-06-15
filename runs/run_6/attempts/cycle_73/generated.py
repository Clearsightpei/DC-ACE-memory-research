"""Cycle 73 — 国 (guó). 8 MMH strokes.

Decomposition (from brief):
  s1 shu     — 囗 left wall
  s2 heng_zhe — 囗 top + right wall
  s3 heng    — 玉 upper internal heng
  s4 heng    — 玉 middle internal heng
  s5 shu     — 玉 vertical
  s6 heng    — 玉 lower internal heng
  s7 dian    — 玉 small dot
  s8 heng    — 囗 closing bottom
"""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from _anchor import anchor_to_xy  # noqa: F401
from shu import draw_shu
from heng import draw_heng
from heng_zhe import draw_heng_zhe
from dian import draw_dian


def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1)
    img.convert("RGBA").save(path, "PNG")


def reset(t):
    t.reset(); t.hideturtle(); t.speed(0); t.pencolor("black")
    t.penup(); t.goto(0, 0); t.setheading(90)


def task_01(t, screen):
    reset(t)
    # s1: 囗 left wall
    draw_shu(t, ("TL", 0.316, 0.568), ("BL", 0.348, 1.3))
    # s2: 囗 top + right wall (heng_zhe)
    draw_heng_zhe(t,
                  ("TL", 0.616, 0.812),
                  ("TR", 0.744, 0.812),
                  ("BR", 0.744, 1.3))
    # s3: 玉 upper internal heng
    draw_heng(t, ("ML", 0.928, 0.288), ("MR", 0.104, 0.152))
    # s4: 玉 middle internal heng
    draw_heng(t, ("ML", 0.888, 0.988), ("MR", 0.024, 0.912))
    # s5: 玉 vertical
    draw_shu(t, ("C", 0.364, 0.364), ("BC", 0.408, 0.532))
    # s6: 玉 lower internal heng
    draw_heng(t, ("BL", 0.724, 0.716), ("BR", 0.304, 0.624))
    # s7: 玉 dian (repositioned to MR cell for visibility — distinguish 玉 from 王)
    draw_dian(t, ("MR", 0.6, 0.7), ("MR", 0.85, 0.95))
    # s8: 囗 closing bottom heng
    draw_heng(t, ("BL", 0.48, 1.3), ("BR", 0.54, 1.156))

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_国.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
