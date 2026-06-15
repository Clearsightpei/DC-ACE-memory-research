"""Cycle 80 — 香 (xiāng). 9 strokes: 禾 + 日."""
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
from na import draw_na
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
    # 禾 top
    draw_pie(t, ("TC", 0.6, 0.3), ("TL", 0.7, 0.7))                # short pie
    draw_heng(t, ("TL", 0.2, 0.7), ("TR", 0.8, 0.7))               # top heng
    draw_shu(t, ("TC", 0.5, 0.5), ("ML", 0.5, 1.0))                # vertical
    draw_heng(t, ("ML", 0.2, 0.7), ("MR", 0.8, 0.7))               # mid heng
    draw_pie(t, ("ML", 0.5, 0.7), ("BL", 0.1, 0.5))                # 禾 pie
    draw_na(t, ("ML", 0.5, 0.7), ("BR", 0.9, 0.5))                 # 禾 na
    # 日 box bottom (aligned)
    draw_shu(t, ("BC", 0.3, 0.4), ("BC", 0.3, 0.95))               # left wall
    draw_heng_zhe(t, ("BC", 0.3, 0.4), ("BC", 0.7, 0.4), ("BC", 0.7, 0.95))  # top + right
    draw_heng(t, ("BC", 0.3, 0.95), ("BC", 0.7, 0.95))             # closing bottom
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_香.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
