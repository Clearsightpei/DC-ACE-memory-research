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
from pie import draw_pie


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
    draw_dian(t, ("TC", 0.192, 0.144), ("TC", 0.596, 0.42))
    draw_heng(t, ("TL", 0.324, 0.86), ("TR", 0.7, 0.72))
    draw_shu(t, ("ML", 0.868, 0.156), ("C", 0.1, 0.764))
    draw_heng(t, ("ML", 0.98, 0.136), ("C", 0.744, 0.456))
    draw_heng(t, ("C", 0.18, 0.692), ("C", 0.976, 0.58))
    draw_shu(t, ("BL", 0.22, 0.108), ("BL", 0.336, 1.3))
    draw_pie(t, ("BL", 0.472, 0.14), ("BR", 0.092, 1.296))
    draw_shu(t, ("BL", 0.86, 0.468), ("BC", 0.116, 1.136))
    draw_heng(t, ("BC", 0.064, 0.464), ("BC", 0.92, 0.824))
    draw_heng(t, ("BC", 0.184, 1.036), ("BC", 0.968, 0.956))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_高.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
