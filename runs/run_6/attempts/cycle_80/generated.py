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
    draw_pie(t, ("TR", 0.048, 0.428), ("TL", 0.644, 0.804))
    draw_heng(t, ("ML", 0.228, 0.34), ("MR", 0.684, 0.152))
    draw_shu(t, ("TC", 0.324, 0.696), ("BC", 0.472, 0.024))
    draw_pie(t, ("C", 0.352, 0.308), ("BL", -0.108, 0.384))
    draw_na(t, ("C", 0.58, 0.288), ("BR", 1.216, 0.056))
    draw_shu(t, ("BL", 0.808, 0.232), ("BL", 0.904, 1.3))
    draw_shu(t, ("BC", 0.032, 0.276), ("BC", 0.768, 1.3))
    draw_heng(t, ("BC", 0.064, 0.868), ("BC", 0.72, 0.76))
    draw_heng(t, ("BC", 0.012, 1.3), ("BC", 0.864, 1.3))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_香.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
