"""Cycle 89 — 笑 (xiào). 10 strokes: 竹 + 夭."""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy  # noqa
from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
from dian import draw_dian
from na import draw_na


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
    # 竹 top: 2 small 个-like (6 strokes)
    # left 个
    draw_pie(t, ("TL", 0.5, 0.3), ("TL", 0.2, 0.7))
    draw_heng(t, ("TL", 0.2, 0.5), ("TL", 0.8, 0.5))
    draw_dian(t, ("TL", 0.4, 0.7), ("TL", 0.5, 1.0))
    # right 个
    draw_pie(t, ("TR", 0.5, 0.3), ("TR", 0.2, 0.7))
    draw_heng(t, ("TR", 0.2, 0.5), ("TR", 0.8, 0.5))
    draw_dian(t, ("TR", 0.4, 0.7), ("TR", 0.5, 1.0))
    # 夭 bottom: 撇 + 横 + 大-bottom (pie + na)
    draw_pie(t, ("ML", 0.7, 0.5), ("ML", 0.4, 0.9))                # top pie
    draw_heng(t, ("ML", 0.2, 0.9), ("MR", 0.8, 0.9))               # mid heng
    draw_pie(t, ("C", 0.5, 1.0), ("BL", 0.3, 1.0))                 # 大 pie
    draw_na(t, ("C", 0.5, 1.0), ("BR", 0.7, 1.0))                  # 大 na
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_笑.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
