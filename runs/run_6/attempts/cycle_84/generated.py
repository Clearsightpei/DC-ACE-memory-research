"""Cycle 84 — 笑 (xiào). 10 strokes: ⺮ top + 夭 bottom.

Anchors copied verbatim from task_briefs/cycle_84.md (1-task-per-cycle).
"""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from _anchor import anchor_to_xy  # noqa: E402
from pie import draw_pie  # noqa: E402
from heng import draw_heng  # noqa: E402
from dian import draw_dian  # noqa: E402
from na import draw_na  # noqa: E402


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
    # ⺮ (bamboo radical, top) — strokes 1-6 (left half: pie+heng+dian; right half: pie+heng+dian)
    # Left bamboo half
    draw_pie(t,  ("TL", 0.704, 0.404), ("ML", 0.14,  0.472))   # 1
    draw_heng(t, ("TL", 0.768, 0.916), ("TC", 0.5,   0.768))   # 2
    draw_dian(t, ("ML", 0.844, 0.148), ("C",  0.08,  0.396))   # 3
    # Right bamboo half
    draw_pie(t,  ("TC", 0.832, 0.228), ("C",  0.444, 0.216))   # 4
    draw_heng(t, ("TC", 0.928, 0.748), ("TR", 0.768, 0.612))   # 5
    draw_dian(t, ("C",  0.952, 0.048), ("MR", 0.336, 0.344))   # 6
    # 夭 (bottom) — heng, heng, pie, na
    draw_heng(t, ("MR", 0.14,  0.624), ("ML", 0.836, 0.78))    # 7
    draw_heng(t, ("BL", 0.352, 0.472), ("BR", 0.74,  0.312))   # 8
    draw_pie(t,  ("C",  0.3,   0.868), ("BL", 0.204, 1.3))     # 9
    draw_na(t,   ("BC", 0.524, 0.456), ("BR", 1.216, 1.3))     # 10

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_笑.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
