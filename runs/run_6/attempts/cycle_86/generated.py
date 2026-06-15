"""Cycle 86 — 谁 (shéi). 10 strokes: 讠 + 隹."""
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
    # 讠 left (2 strokes)
    draw_dian(t, ("TL", 0.5, 0.3), ("TL", 0.4, 0.7))               # top dot
    draw_heng(t, ("ML", 0.2, 0.4), ("ML", 0.7, 0.4))               # heng under dot
    # 隹 right (8 strokes): 亻 + 4 hengs
    draw_pie(t, ("TC", 0.8, 0.3), ("MR", 0.0, 0.7))                # left pie
    draw_shu(t, ("MR", 0.3, 0.3), ("BR", 0.3, 0.8))                # 亻 vertical
    draw_heng(t, ("MR", 0.3, 0.3), ("MR", 0.9, 0.3))               # heng 1
    draw_heng(t, ("MR", 0.3, 0.55), ("MR", 0.9, 0.55))             # heng 2
    draw_heng(t, ("MR", 0.3, 0.8), ("MR", 0.9, 0.8))               # heng 3
    draw_heng(t, ("BR", 0.3, 0.4), ("BR", 0.9, 0.4))               # heng 4
    draw_shu(t, ("BR", 0.6, 0.4), ("BR", 0.6, 0.9))                # vertical
    draw_heng(t, ("BR", 0.3, 0.9), ("BR", 0.9, 0.9))               # bottom heng
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_谁.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
