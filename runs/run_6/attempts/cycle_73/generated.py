"""Cycle 73 — 朋 (péng). 8 MMH strokes = 月 + 月."""
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
from heng_zhe_gou import draw_heng_zhe_gou


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
    # left 月: pie + heng_zhe_gou (top+right+hook) + 2 internal hengs
    draw_pie(t, ("TL", 0.272, 0.612), ("BL", -0.2, 1.3))
    draw_heng_zhe_gou(t, ("TL", 0.532, 0.648), ("TL", 0.676, 0.648), ("BL", 0.676, 0.792))
    draw_heng(t, ("ML", 0.544, 0.492), ("ML", 0.88, 0.412))
    draw_heng(t, ("BL", 0.46, 0.06), ("ML", 0.892, 0.988))
    # right 月
    draw_pie(t, ("TC", 0.696, 0.552), ("BC", 0.304, 1.292))
    draw_heng_zhe_gou(t, ("TC", 0.952, 0.584), ("TR", 0.136, 0.584), ("BR", 0.136, 1.08))
    draw_heng(t, ("C", 1.0, 0.416), ("MR", 0.412, 0.332))
    draw_heng(t, ("BC", 0.924, 0.036), ("MR", 0.424, 0.956))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_朋.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
