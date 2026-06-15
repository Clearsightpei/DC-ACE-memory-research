"""Cycle 83 — 高 (gāo). 10 strokes."""
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
    # 亠 top
    draw_dian(t, ("TC", 0.4, 0.0), ("TC", 0.5, 0.3))
    draw_heng(t, ("TL", 0.3, 0.4), ("TR", 0.7, 0.4))
    # 口 upper box (between 亠 and 冂)
    draw_shu(t, ("TL", 0.7, 0.7), ("ML", 0.7, 0.2))
    draw_heng_zhe(t, ("TL", 0.7, 0.7), ("TR", 0.3, 0.7), ("ML", 0.3, 0.2))
    draw_heng(t, ("ML", 0.7, 0.2), ("MR", 0.3, 0.2))
    # 冂 lower frame
    draw_shu(t, ("ML", 0.3, 0.6), ("BL", 0.3, 1.0))
    draw_heng_zhe(t, ("ML", 0.3, 0.6), ("MR", 0.7, 0.6), ("BR", 0.7, 1.0))
    # 口 inside 冂 (lower small box)
    draw_shu(t, ("BC", 0.3, 0.4), ("BC", 0.3, 0.9))
    draw_heng_zhe(t, ("BC", 0.3, 0.4), ("BC", 0.7, 0.4), ("BC", 0.7, 0.9))
    draw_heng(t, ("BC", 0.3, 0.9), ("BC", 0.7, 0.9))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_高.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
