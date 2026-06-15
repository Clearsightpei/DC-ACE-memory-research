"""Cycle 85 — 真 (zhēn). 10 strokes: 十 + 目 + 八-like bottom."""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy  # noqa
from heng import draw_heng
from shu import draw_shu
from heng_zhe import draw_heng_zhe
from pie import draw_pie
from na import draw_na
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
    # 十 top: heng + shu
    draw_heng(t, ("TL", 0.2, 0.6), ("TR", 0.8, 0.6))               # top heng (wide)
    draw_shu(t, ("TC", 0.5, 0.2), ("TC", 0.5, 0.9))                # vertical (top portion)
    # 目 middle (aligned box)
    draw_shu(t, ("ML", 0.7, 0.2), ("ML", 0.7, 1.0))                # left wall
    draw_heng_zhe(t, ("ML", 0.7, 0.2), ("MR", 0.3, 0.2), ("MR", 0.3, 1.0))  # top + right
    draw_heng(t, ("ML", 0.7, 0.5), ("MR", 0.3, 0.5))               # internal upper
    draw_heng(t, ("ML", 0.7, 0.8), ("MR", 0.3, 0.8))               # internal lower
    draw_heng(t, ("ML", 0.7, 1.0), ("MR", 0.3, 1.0))               # closing bottom
    # bottom heng + 八
    draw_heng(t, ("BL", 0.2, 0.4), ("BR", 0.8, 0.4))               # long bottom heng
    draw_dian(t, ("BC", 0.3, 0.6), ("BL", 0.5, 1.0))               # left dian
    draw_dian(t, ("BC", 0.7, 0.6), ("BR", 0.5, 1.0))               # right dian
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_真.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
