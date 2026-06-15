"""Cycle 72 — 明 (míng). 8 MMH strokes. Direct main-thread render (fast-mode)."""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy  # noqa
from shu import draw_shu
from heng_zhe import draw_heng_zhe
from heng import draw_heng
from pie import draw_pie
from heng_zhe_gou import draw_heng_zhe_gou


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
    # 日 (left)
    draw_shu(t, ("TL", 0.06, 0.732), ("BL", 0.176, 0.468))
    draw_heng_zhe(t, ("TL", 0.256, 0.756), ("TL", 0.976, 0.756), ("BL", 0.976, 0.444))
    draw_heng(t, ("ML", 0.312, 0.544), ("ML", 0.716, 0.46))
    draw_heng(t, ("BL", 0.3, 0.232), ("BL", 0.836, 0.112))
    # 月 (right)
    draw_pie(t, ("TC", 0.596, 0.46), ("BL", 0.704, 1.3))
    draw_heng_zhe_gou(t, ("TC", 0.924, 0.628), ("TR", 0.148, 0.628), ("BR", 0.148, 1.116))
    draw_heng(t, ("C", 0.876, 0.316), ("MR", 0.428, 0.224))
    draw_heng(t, ("BC", 0.796, 0.048), ("MR", 0.444, 0.96))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_明.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
