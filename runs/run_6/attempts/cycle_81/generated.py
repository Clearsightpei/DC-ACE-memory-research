"""Cycle 81 — 信 (xìn). 9 strokes: 亻 + 言."""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy  # noqa
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from dian import draw_dian
from heng_zhe import draw_heng_zhe


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
    # 亻 left
    draw_pie(t, ("TL", 0.7, 0.3), ("ML", 0.4, 0.7))                # 亻 pie
    draw_shu(t, ("ML", 0.4, 0.7), ("BL", 0.4, 1.0))                # 亻 shu
    # 言 right
    draw_dian(t, ("TC", 0.7, 0.2), ("TC", 0.6, 0.5))               # top dot
    draw_heng(t, ("TR", 0.2, 0.6), ("TR", 0.9, 0.6))               # top heng (long)
    draw_heng(t, ("MR", 0.2, 0.2), ("MR", 0.8, 0.2))               # heng 2
    draw_heng(t, ("MR", 0.2, 0.6), ("MR", 0.8, 0.6))               # heng 3
    # 口 box at bottom-right
    draw_shu(t, ("MR", 0.3, 0.8), ("BR", 0.3, 0.4))                # left wall
    draw_heng_zhe(t, ("MR", 0.3, 0.8), ("MR", 0.7, 0.8), ("BR", 0.7, 0.4))  # top+right
    draw_heng(t, ("BR", 0.3, 0.4), ("BR", 0.7, 0.4))               # closing bottom
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_信.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
