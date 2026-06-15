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
    draw_pie(t, ("TR", 0.124, 0.508), ("TL", 0.732, 0.852))
    draw_heng(t, ("ML", 0.02, 0.336), ("MR", 1.012, 0.128))
    draw_shu(t, ("ML", 0.596, 0.648), ("BL", 0.896, 0.608))
    draw_heng(t, ("ML", 0.76, 0.632), ("BR", 0.168, 0.524))
    draw_heng(t, ("BC", 0.116, 0.08), ("BC", 0.876, 0.012))
    draw_shu(t, ("BL", 0.972, 0.532), ("BC", 0.988, 0.372))
    draw_shu(t, ("TC", 0.352, 0.78), ("BC", 0.412, 1.3))
    draw_heng(t, ("BL", 0.88, 0.968), ("BR", 0.12, 0.932))
    draw_heng(t, ("BL", 0.26, 1.3), ("BR", 0.852, 1.3))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_重.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
