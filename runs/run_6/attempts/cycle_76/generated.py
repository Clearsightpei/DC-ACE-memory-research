"""Cycle 76 — 春 (chūn). 9 strokes: 三 + 人 + 日 (with aligned-corner box)."""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy  # noqa
from heng import draw_heng
from pie import draw_pie
from na import draw_na
from shu import draw_shu
from heng_zhe import draw_heng_zhe


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
    # 三 (3 hengs, stacked)
    draw_heng(t, ("TL", 0.3, 0.5), ("TR", 0.7, 0.5))
    draw_heng(t, ("TL", 0.3, 1.0), ("TR", 0.7, 1.0))
    draw_heng(t, ("ML", 0.2, 0.5), ("MR", 0.8, 0.5))
    # 人 (pie + na)
    draw_pie(t, ("TC", 0.5, 0.5), ("ML", 0.2, 1.0))
    draw_na(t, ("TC", 0.5, 0.5), ("MR", 0.8, 1.0))
    # 日 box (aligned corners) at bottom — TL, TR, BL, BR at same y/x
    draw_shu(t, ("BL", 0.85, 0.4), ("BL", 0.85, 1.0))                       # left wall
    draw_heng_zhe(t, ("BL", 0.85, 0.4), ("BC", 0.95, 0.4), ("BC", 0.95, 1.0))  # top + right wall
    draw_heng(t, ("BL", 0.85, 0.7), ("BC", 0.95, 0.7))                      # internal heng
    draw_heng(t, ("BL", 0.85, 1.0), ("BC", 0.95, 1.0))                      # closing bottom
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_春.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
