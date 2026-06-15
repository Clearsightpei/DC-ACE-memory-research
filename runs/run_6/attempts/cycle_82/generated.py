"""Cycle 82 — 法 (fǎ). 8 strokes: 氵 + 去."""
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
    # 氵 water (3 dots)
    draw_dian(t, ("TL", 0.4, 0.4), ("ML", 0.4, 0.0))               # top dot
    draw_dian(t, ("ML", 0.3, 0.3), ("ML", 0.5, 0.6))               # mid dot
    draw_dian(t, ("BL", 0.4, 0.2), ("ML", 0.5, 1.0))               # bottom ti
    # 去 right
    draw_heng(t, ("TC", 0.2, 0.7), ("TR", 0.8, 0.7))               # top heng
    draw_shu(t, ("TC", 0.5, 0.5), ("MR", 0.5, 0.5))                # vertical
    draw_heng(t, ("MR", 0.0, 0.3), ("MR", 1.0, 0.3))               # mid heng (long)
    draw_pie(t, ("MR", 0.7, 0.4), ("BC", 0.6, 0.5))                # pie
    draw_na(t, ("MR", 0.6, 0.6), ("BR", 0.9, 1.0))                 # na
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_法.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
