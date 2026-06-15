"""Cycle 77 — 看 (kàn). 9 strokes: 手 + 目."""
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
    # 手 top
    draw_pie(t, ("TR", 0.132, 0.412), ("TL", 0.624, 0.696))
    draw_heng(t, ("ML", 0.688, 0.14), ("TR", 0.216, 0.956))
    draw_heng(t, ("ML", -0.088, 0.8), ("MR", 1.004, 0.532))
    draw_pie(t, ("TC", 0.256, 0.656), ("BL", -0.228, 1.3))
    # 目 box bottom (5 strokes)
    draw_shu(t, ("BC", 0.032, 0.052), ("BC", 0.036, 1.3))
    draw_shu(t, ("BC", 0.164, 0.08), ("BC", 0.904, 1.3))
    draw_heng(t, ("BC", 0.204, 0.608), ("BC", 0.816, 0.5))
    draw_heng(t, ("BC", 0.188, 1.016), ("BC", 0.832, 0.916))
    draw_heng(t, ("BC", 0.156, 1.3), ("BC", 0.98, 1.292))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_看.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
