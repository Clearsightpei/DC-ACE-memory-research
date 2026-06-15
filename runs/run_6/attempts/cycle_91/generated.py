"""Cycle 91 — 喜 (xǐ). 12 strokes."""
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
    # 士 top
    draw_heng(t, ("TL", 0.2, 0.3), ("TR", 0.8, 0.3))               # top heng (long)
    draw_shu(t, ("TC", 0.5, 0.3), ("TC", 0.5, 0.7))                # vertical
    draw_heng(t, ("TC", 0.3, 0.7), ("TC", 0.7, 0.7))               # bottom heng of 士 (short)
    # 口 upper
    draw_shu(t, ("TL", 0.7, 0.9), ("ML", 0.7, 0.2))
    draw_heng_zhe(t, ("TL", 0.7, 0.9), ("TR", 0.3, 0.9), ("ML", 0.3, 0.2))
    draw_heng(t, ("ML", 0.7, 0.2), ("ML", 0.3, 0.2))
    # 一 (long horizontal)
    draw_heng(t, ("ML", 0.1, 0.6), ("MR", 0.9, 0.6))               # very long heng
    # 口 lower
    draw_shu(t, ("BL", 0.7, 0.3), ("BL", 0.7, 0.9))
    draw_heng_zhe(t, ("BL", 0.7, 0.3), ("BR", 0.3, 0.3), ("BR", 0.3, 0.9))
    draw_heng(t, ("BL", 0.7, 0.9), ("BR", 0.3, 0.9))
    # 2 internal hengs of 口 (to make 12 total)
    draw_heng(t, ("TC", 0.3, 0.5), ("TC", 0.7, 0.5))               # added heng
    draw_heng(t, ("BC", 0.3, 0.5), ("BC", 0.7, 0.5))               # added heng
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_喜.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
