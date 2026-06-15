"""Cycle 84 — 唐 (táng). 10 strokes."""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy  # noqa
from dian import draw_dian
from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
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
    # 广 outer
    draw_dian(t, ("TC", 0.4, 0.0), ("TC", 0.5, 0.3))               # top dot
    draw_heng(t, ("TL", 0.4, 0.4), ("TR", 0.7, 0.4))               # 广 top heng
    draw_pie(t, ("TL", 0.6, 0.5), ("BL", -0.2, 1.0))               # 广 long pie
    # 彐 inside top
    draw_heng(t, ("ML", 0.4, 0.4), ("MR", 0.7, 0.4))               # 彐 top heng
    draw_shu(t, ("ML", 0.4, 0.4), ("ML", 0.4, 0.9))                # 彐 left wall
    draw_heng(t, ("ML", 0.4, 0.9), ("MR", 0.7, 0.9))               # 彐 mid heng
    draw_heng(t, ("ML", 0.4, 1.0), ("MR", 0.8, 1.0))               # 彐 bottom heng (longer)
    # 口 inside at bottom
    draw_shu(t, ("BC", 0.3, 0.3), ("BC", 0.3, 0.9))                # left wall
    draw_heng_zhe(t, ("BC", 0.3, 0.3), ("BC", 0.7, 0.3), ("BC", 0.7, 0.9))  # top + right
    draw_heng(t, ("BC", 0.3, 0.9), ("BC", 0.7, 0.9))               # closing bottom
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_唐.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
