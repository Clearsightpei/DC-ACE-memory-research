"""Cycle 90 — 朝 (cháo). 12 strokes: 十 + 日 + 月."""
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
    # 十 top-left
    draw_heng(t, ("TL", 0.1, 0.4), ("TL", 0.7, 0.4))
    draw_shu(t, ("TL", 0.4, 0.1), ("ML", 0.4, 0.4))
    # 日 (left middle, aligned box)
    draw_shu(t, ("ML", 0.2, 0.5), ("ML", 0.2, 1.0))
    draw_heng_zhe(t, ("ML", 0.2, 0.5), ("ML", 0.6, 0.5), ("ML", 0.6, 1.0))
    draw_heng(t, ("ML", 0.2, 0.75), ("ML", 0.6, 0.75))
    draw_heng(t, ("ML", 0.2, 1.0), ("ML", 0.6, 1.0))
    # 月 (right, aligned box with hook)
    draw_pie(t, ("TR", 0.4, 0.3), ("MR", 0.2, 0.5))
    draw_shu(t, ("MR", 0.3, 0.3), ("BR", 0.3, 0.9))
    draw_heng_zhe(t, ("MR", 0.3, 0.3), ("MR", 0.8, 0.3), ("BR", 0.8, 0.9))
    draw_heng(t, ("MR", 0.3, 0.6), ("MR", 0.8, 0.6))
    draw_heng(t, ("BR", 0.3, 0.4), ("BR", 0.8, 0.4))
    draw_heng(t, ("BR", 0.3, 0.9), ("BR", 0.8, 0.9))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_朝.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
