"""Cycle 79 — 重 (zhòng). 9 strokes."""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy  # noqa
from pie import draw_pie
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
    # short pie + top heng (千-like top)
    draw_pie(t, ("TC", 0.6, 0.3), ("TC", 0.3, 0.7))                # pie short
    draw_heng(t, ("TL", 0.2, 0.8), ("TR", 0.8, 0.8))               # top heng (long)
    # 日 box middle (aligned corners) — wider
    draw_shu(t, ("ML", 0.7, 0.3), ("ML", 0.7, 1.0))                # left wall
    draw_heng_zhe(t, ("ML", 0.7, 0.3), ("MR", 0.3, 0.3), ("MR", 0.3, 1.0))  # top+right
    draw_heng(t, ("ML", 0.7, 0.65), ("MR", 0.3, 0.65))             # internal heng
    draw_heng(t, ("ML", 0.7, 1.0), ("MR", 0.3, 1.0))               # closing bottom
    # 千 stem (long shu through everything)
    draw_shu(t, ("TC", 0.5, 0.5), ("BC", 0.5, 1.0))                # center vertical
    # 二 bottom (2 hengs)
    draw_heng(t, ("BL", 0.3, 0.6), ("BR", 0.7, 0.6))               # bottom heng 1
    draw_heng(t, ("BL", 0.2, 1.0), ("BR", 0.8, 1.0))               # bottom heng 2 (longest)
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_重.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
