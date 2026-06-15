"""Cycle 93 — 路 (lù). 13 strokes: 足 + 各."""
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
    # 足 left (7 strokes)
    draw_shu(t, ("TL", 0.5, 0.3), ("ML", 0.5, 0.2))                # 口 left wall
    draw_heng_zhe(t, ("TL", 0.5, 0.3), ("TL", 0.8, 0.3), ("ML", 0.8, 0.2))  # 口 top+right
    draw_heng(t, ("ML", 0.5, 0.2), ("ML", 0.8, 0.2))               # 口 bottom
    draw_heng(t, ("ML", 0.3, 0.6), ("ML", 0.9, 0.6))               # mid heng
    draw_shu(t, ("ML", 0.6, 0.6), ("BL", 0.4, 0.6))                # vertical down
    draw_pie(t, ("BL", 0.5, 0.5), ("BL", 0.1, 0.9))                # pie
    draw_na(t, ("BL", 0.5, 0.6), ("BL", 1.0, 1.0))                 # na
    # 各 right (6 strokes)
    draw_pie(t, ("TR", 0.6, 0.3), ("TR", 0.2, 0.7))                # pie
    draw_pie(t, ("MR", 0.6, 0.2), ("MR", 0.2, 0.5))                # second pie/折
    draw_na(t, ("MR", 0.4, 0.3), ("MR", 0.9, 0.5))                 # na
    # 口 at bottom of 各
    draw_shu(t, ("BR", 0.3, 0.5), ("BR", 0.3, 0.9))
    draw_heng_zhe(t, ("BR", 0.3, 0.5), ("BR", 0.7, 0.5), ("BR", 0.7, 0.9))
    draw_heng(t, ("BR", 0.3, 0.9), ("BR", 0.7, 0.9))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_路.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
