"""Cycle 78 — 美 (měi). 9 strokes."""
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
    draw_pie(t, ("TL", 0.864, 0.392), ("TC", 0.224, 0.696))
    draw_dian(t, ("TC", 0.868, 0.196), ("TC", 0.568, 0.808))
    draw_heng(t, ("ML", 0.58, 0.132), ("TR", 0.304, 0.924))
    draw_heng(t, ("ML", 0.848, 0.6), ("MR", 0.052, 0.464))
    draw_shu(t, ("C", 0.324, 0.172), ("C", 0.372, 0.924))
    draw_heng(t, ("BL", 0.284, 0.092), ("MR", 0.616, 0.92))
    draw_heng(t, ("BL", 0.496, 0.632), ("BR", 0.468, 0.536))
    draw_pie(t, ("BC", 0.196, 0.136), ("BL", 0.256, 1.3))
    draw_na(t, ("BC", 0.472, 0.66), ("BR", 1.116, 1.3))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_美.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
