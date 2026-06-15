"""Cycle 84 — 唐 (táng). 10 strokes."""
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
    draw_dian(t, ("TC", 0.332, 0.168), ("TC", 0.812, 0.464))
    draw_heng(t, ("TL", 0.84, 0.868), ("TR", 0.592, 0.684))
    draw_pie(t, ("TL", 0.556, 0.776), ("BL", -0.192, 1.3))
    draw_pie(t, ("C", 0.028, 0.524), ("BR", 0.168, 0.164))
    draw_heng(t, ("ML", 0.796, 0.984), ("MR", 1.164, 0.824))
    draw_heng(t, ("BC", 0.036, 0.424), ("BR", 0.432, 0.304))
    draw_shu(t, ("C", 0.528, 0.032), ("BC", 0.616, 0.656))
    draw_pie(t, ("BL", 0.876, 0.872), ("BC", 0.192, 1.3))
    draw_shu(t, ("BC", 0.108, 0.872), ("BR", 0.18, 1.3))
    draw_heng(t, ("BC", 0.252, 1.3), ("BR", 0.412, 1.3))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_唐.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
