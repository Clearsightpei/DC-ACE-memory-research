"""Cycle 92 — 道 (dào). 12 strokes: 辶 + 首."""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy  # noqa
from heng import draw_heng
from shu import draw_shu
from heng_zhe import draw_heng_zhe
from pie import draw_pie
from dian import draw_dian
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
    # 首 right (9 strokes simplified)
    draw_dian(t, ("TC", 0.4, 0.0), ("TC", 0.5, 0.3))               # top dot
    draw_heng(t, ("TC", 0.2, 0.5), ("TR", 0.8, 0.5))               # top heng
    draw_pie(t, ("TC", 0.7, 0.5), ("TR", 0.2, 1.0))                # pie
    # 自-like box
    draw_shu(t, ("MR", 0.2, 0.2), ("MR", 0.2, 1.0))
    draw_heng_zhe(t, ("MR", 0.2, 0.2), ("MR", 0.9, 0.2), ("MR", 0.9, 1.0))
    draw_heng(t, ("MR", 0.2, 0.5), ("MR", 0.9, 0.5))
    draw_heng(t, ("MR", 0.2, 0.75), ("MR", 0.9, 0.75))
    draw_heng(t, ("MR", 0.2, 1.0), ("MR", 0.9, 1.0))
    # 辶 left bottom (3 strokes)
    draw_dian(t, ("TL", 0.5, 0.6), ("ML", 0.5, 0.3))               # top dot
    draw_pie(t, ("ML", 0.4, 0.5), ("BL", 0.4, 0.5))                # mid pie
    draw_na(t, ("BL", 0.3, 0.5), ("BR", 1.0, 0.9))                 # long na (sweeping right)
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_道.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
