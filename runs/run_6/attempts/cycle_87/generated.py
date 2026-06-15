"""Cycle 87 — 都 (dōu). 10 strokes: 者 + 阝."""
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
    # 者 left
    draw_heng(t, ("TL", 0.1, 0.4), ("TL", 0.9, 0.4))               # top heng
    draw_heng(t, ("TL", 0.2, 0.8), ("TL", 0.8, 0.8))               # heng 2
    draw_shu(t, ("TL", 0.5, 0.4), ("ML", 0.5, 0.5))                # vertical
    draw_pie(t, ("TL", 0.7, 0.4), ("BL", 0.0, 0.8))                # long pie
    draw_heng(t, ("ML", 0.2, 0.7), ("ML", 0.9, 0.7))               # mid heng
    # 日 box bottom of 者
    draw_shu(t, ("ML", 0.3, 0.8), ("BL", 0.3, 0.7))                # left wall
    draw_heng_zhe(t, ("ML", 0.3, 0.8), ("ML", 0.7, 0.8), ("BL", 0.7, 0.7))  # top + right
    draw_heng(t, ("BL", 0.3, 0.7), ("BL", 0.7, 0.7))               # closing bottom
    # 阝 right (2 strokes simplified)
    draw_heng_zhe(t, ("TR", 0.2, 0.5), ("TR", 0.5, 0.5), ("MR", 0.5, 0.5))  # top loop
    draw_shu(t, ("TR", 0.3, 0.7), ("BR", 0.3, 0.7))                # right vertical
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_都.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
