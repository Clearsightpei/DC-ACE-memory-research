"""Cycle 76 — 春 (chūn). 9 strokes: 三 + 人 + 日."""
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
    # Three hengs (三-like top)
    draw_heng(t, ("TL", 0.72, 0.788), ("TR", 0.2, 0.62))
    draw_heng(t, ("ML", 0.66, 0.26), ("MR", 0.124, 0.1))
    draw_heng(t, ("ML", -0.072, 0.832), ("MR", 0.924, 0.608))
    # 人-like pie+na crossing
    draw_pie(t, ("TC", 0.272, 0.228), ("BL", -0.1, 0.864))
    draw_na(t, ("C", 0.716, 0.74), ("BR", 1.3, 0.544))
    # 日-box (4 strokes) at bottom
    draw_shu(t, ("BL", 0.8, 0.388), ("BL", 0.904, 1.3))
    draw_shu(t, ("BL", 0.98, 0.384), ("BC", 0.948, 1.3))
    draw_heng(t, ("BC", 0.04, 0.996), ("BC", 0.604, 0.916))
    draw_heng(t, ("BC", 0.012, 1.3), ("BC", 0.748, 1.3))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_春.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
