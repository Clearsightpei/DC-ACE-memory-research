"""Cycle 74 — 雨 (yǔ, rain). 8 MMH strokes."""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy  # noqa
from heng import draw_heng
from shu import draw_shu
from heng_gou import draw_heng_gou
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
    draw_heng(t, ("TL", 0.7, 0.768), ("TR", 0.44, 0.628))
    draw_shu(t, ("ML", 0.1, 0.524), ("BL", 0.38, 1.192))
    draw_heng_gou(t, ("ML", 0.38, 0.72), ("TR", 0.096, 0.72), ("BR", 0.096, 1.056))
    draw_shu(t, ("TC", 0.312, 0.868), ("BC", 0.46, 1.004))
    draw_dian(t, ("ML", 0.724, 0.948), ("BC", 0.072, 0.12))
    draw_dian(t, ("BL", 0.692, 0.472), ("BC", 0.036, 0.676))
    draw_dian(t, ("C", 0.844, 0.812), ("MR", 0.24, 0.956))
    draw_dian(t, ("BC", 0.844, 0.38), ("BR", 0.2, 0.564))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_雨.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
