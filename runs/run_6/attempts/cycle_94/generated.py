"""Cycle 94 — 黑 (hēi). 12 strokes."""
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
    # 田 top (5 strokes: shu + heng_zhe + heng cross + heng cross + heng bottom)
    draw_shu(t, ("TL", 0.6, 0.4), ("ML", 0.6, 0.4))                # left wall
    draw_heng_zhe(t, ("TL", 0.6, 0.4), ("TR", 0.4, 0.4), ("MR", 0.4, 0.4))  # top + right
    draw_heng(t, ("TC", 0.4, 0.7), ("TC", 0.6, 0.7))               # internal heng top (mid)
    draw_shu(t, ("TC", 0.5, 0.4), ("ML", 0.5, 0.4))                # internal shu
    draw_heng(t, ("ML", 0.6, 0.4), ("MR", 0.4, 0.4))               # closing bottom
    # 土 middle (3 strokes)
    draw_heng(t, ("ML", 0.3, 0.8), ("MR", 0.7, 0.8))               # top heng
    draw_shu(t, ("C", 0.5, 0.5), ("BC", 0.5, 0.5))                 # vertical
    draw_heng(t, ("BL", 0.2, 0.2), ("BR", 0.8, 0.2))               # long bottom heng
    # 4 dots bottom (灬 simplified)
    draw_dian(t, ("BL", 0.4, 0.7), ("BL", 0.5, 1.0))
    draw_dian(t, ("BC", 0.3, 0.7), ("BC", 0.4, 1.0))
    draw_dian(t, ("BC", 0.7, 0.7), ("BC", 0.8, 1.0))
    draw_dian(t, ("BR", 0.5, 0.7), ("BR", 0.6, 1.0))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_黑.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
