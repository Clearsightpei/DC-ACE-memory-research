"""Cycle 81 — 信 (xìn). 9 strokes: 亻 + 言."""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy  # noqa
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
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
    # 亻 left
    draw_pie(t, ("TL", 0.672, 0.352), ("BL", -0.228, 0.032))
    draw_shu(t, ("ML", 0.44, 0.436), ("BL", 0.46, 1.3))
    # 言 right
    draw_dian(t, ("TC", 0.7, 0.236), ("TR", 0.172, 0.636))
    draw_heng(t, ("ML", 0.932, 0.192), ("MR", 1.088, 0.008))
    draw_heng(t, ("C", 0.424, 0.656), ("MR", 0.428, 0.548))
    draw_heng(t, ("BC", 0.392, 0.136), ("BR", 0.444, 0.028))
    draw_shu(t, ("BC", 0.252, 0.624), ("BC", 0.516, 1.3))
    draw_heng(t, ("BC", 0.488, 0.644), ("BR", 0.34, 1.092))
    draw_heng(t, ("BC", 0.596, 1.3), ("BR", 0.6, 1.252))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_信.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
