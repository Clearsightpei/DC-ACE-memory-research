"""Cycle 88 — 部 (bù). 10 strokes."""
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
    # 咅 left (7 strokes)
    draw_dian(t, ("TL", 0.4, 0.0), ("TL", 0.4, 0.3))               # top dot
    draw_heng(t, ("TL", 0.1, 0.5), ("TL", 0.9, 0.5))               # top heng
    draw_shu(t, ("TL", 0.5, 0.5), ("ML", 0.5, 0.5))                # vertical
    draw_heng(t, ("ML", 0.1, 0.5), ("ML", 0.9, 0.5))               # mid heng
    # 口 box (aligned) bottom of 咅
    draw_shu(t, ("ML", 0.3, 0.7), ("BL", 0.3, 0.7))
    draw_heng_zhe(t, ("ML", 0.3, 0.7), ("ML", 0.7, 0.7), ("BL", 0.7, 0.7))
    draw_heng(t, ("BL", 0.3, 0.7), ("BL", 0.7, 0.7))
    # 阝 right (3 strokes)
    draw_heng_zhe(t, ("TR", 0.3, 0.4), ("TR", 0.7, 0.4), ("MR", 0.7, 0.4))
    draw_shu(t, ("TR", 0.3, 0.4), ("BR", 0.3, 0.4))                # left vertical
    draw_pie(t, ("MR", 0.3, 0.5), ("BR", 0.5, 0.8))                # tail pie
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_部.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
