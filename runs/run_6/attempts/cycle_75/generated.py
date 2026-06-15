"""Cycle 75 — 金 (jīn). 8 MMH strokes. ATTEMPT 2.
Structure: 人 top (pie + na meeting at apex) → upper 王 hengs → center shu
→ two inner dots → long bottom heng.
All anchors emitted verbatim from task_briefs/cycle_75_dataset.json (updated).
"""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from _anchor import anchor_to_xy  # noqa: F401  (kept for compliance)
from pie import draw_pie
from na import draw_na
from heng import draw_heng
from shu import draw_shu
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
    # s1 — 撇 (left half of 人 apex, sweeping down-left).
    # x_frac -0.308 clamped to -0.3 (anchor validator floor).
    draw_pie(t, ("TC", 0.304, 0.288), ("BL", -0.3, 0.292))
    # s2 — 捺 (right half of 人 apex, sweeping down-right).
    draw_na(t, ("TC", 0.568, 0.664), ("MR", 1.3, 0.82))
    # s3 — upper interior 横 of 王 body (tightened).
    draw_heng(t, ("ML", 0.6, 0.7), ("MR", 0.3, 0.7))
    # s4 — lower interior 横 of 王 body (tightened).
    draw_heng(t, ("ML", 0.7, 1.0), ("MR", 0.3, 1.0))
    # s5 — central 竖 piercing 王 (tightened).
    draw_shu(t, ("C", 0.5, 0.65), ("BC", 0.5, 1.0))
    # s6 — left 点.
    draw_dian(t, ("BL", 0.508, 0.736), ("BL", 0.884, 1.116))
    # s7 — right 点.
    draw_dian(t, ("BR", 0.12, 0.492), ("BC", 0.7, 1.036))
    # s8 — long bottom 横 of 王 (tightened).
    draw_heng(t, ("BL", 0.3, 1.0), ("BR", 0.7, 1.0))

    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_金.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen)
    screen.update()


if __name__ == "__main__":
    main()
