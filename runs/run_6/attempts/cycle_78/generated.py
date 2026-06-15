"""Cycle 78 — 美 (měi). 9 strokes: 羊 + 大."""
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
    # 羊 top: 2 dots + 3 hengs + 1 shu
    draw_pie(t, ("TL", 0.6, 0.2), ("TC", 0.3, 0.6))                # left dot/pie
    draw_dian(t, ("TC", 0.7, 0.2), ("TC", 0.6, 0.6))               # right dot
    draw_heng(t, ("TL", 0.3, 0.8), ("TR", 0.7, 0.8))               # top heng
    draw_heng(t, ("ML", 0.3, 0.3), ("MR", 0.7, 0.3))               # middle heng
    draw_shu(t, ("TC", 0.5, 0.5), ("MR", 0.0, 1.0))                # vertical (羊 center)
    draw_heng(t, ("ML", 0.2, 0.8), ("MR", 0.8, 0.8))               # 羊 bottom heng
    # 大 bottom: heng + pie + na
    draw_heng(t, ("BL", 0.2, 0.2), ("BR", 0.8, 0.2))               # 大 top heng
    draw_pie(t, ("BC", 0.5, 0.2), ("BL", 0.0, 1.0))                # 大 pie
    draw_na(t, ("BC", 0.5, 0.2), ("BR", 1.0, 1.0))                 # 大 na
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_美.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
