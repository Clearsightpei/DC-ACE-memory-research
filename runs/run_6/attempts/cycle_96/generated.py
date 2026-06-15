"""像 — cycle 96, 13 MMH strokes.

Brief anchors translated directly via _anchor.anchor_to_xy. One
primitive call per MMH stroke. No magic numbers.

Stroke list (from task_briefs/cycle_96_dataset.json):
  1  撇       (left-radical 亻 top diagonal)
  2  竖       (left-radical 亻 vertical)
  3  撇       (象 top diagonal)
  4  横折    (口-like box top)
  5  竖       (inner short vertical)
  6  横       (inner short horizontal)
  7  横       (inner short horizontal)
  8  撇       (small diagonal)
  9  竖       (lower vertical)
 10  撇       (lower-left diagonal)
 11  竖       (lower vertical)
 12  撇       (long lower 撇)
 13  捺       (final 捺 sweep)
"""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from _anchor import anchor_to_xy  # noqa: F401  (kept available)
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from heng_zhe import draw_heng_zhe
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

    # 1  撇  (亻 top diagonal)
    draw_pie(t, ('TL', 0.652, 0.412), ('BL', -0.26, 0.032))

    # 2  竖  (亻 vertical)
    draw_shu(t, ('ML', 0.396, 0.452), ('BL', 0.452, 1.3))

    # 3  撇  (象 top diagonal)
    draw_pie(t, ('TC', 0.612, 0.176), ('TC', 0.192, 0.912))

    # 4  横折  (top box)
    draw_heng_zhe(t,
                  ('TC', 0.644, 0.596),
                  ('TC', 0.86,  0.596),
                  ('TC', 0.86,  0.936))

    # 5  竖  (inner short vertical)
    draw_shu(t, ('C', 0.036, 0.084), ('C', 0.276, 0.7))

    # 6  横
    draw_heng(t, ('C', 0.192, 0.084), ('MR', 0.324, 0.6))

    # 7  横
    draw_heng(t, ('C', 0.34, 0.664), ('MR', 0.244, 0.504))

    # 8  撇  (small diagonal)
    draw_pie(t, ('C', 0.74, 0.092), ('BL', 0.964, 0.28))

    # 9  竖  (lower vertical — extends below grid, allowed by 1.3 cap)
    draw_shu(t, ('C', 0.572, 0.92), ('BC', 0.428, 1.3))

    # 10  撇
    draw_pie(t, ('BC', 0.652, 0.072), ('BL', 0.912, 0.72))

    # 11  竖
    draw_shu(t, ('BC', 0.844, 0.32), ('BL', 0.864, 1.252))

    # 12  撇  (long lower)
    draw_pie(t, ('MR', 0.388, 0.792), ('BR', 0.06, 0.288))

    # 13  捺  (final sweep)
    draw_na(t, ('BR', 0.088, 0.396), ('BR', 1.3, 0.928))

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_像.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen)
    screen.update()


if __name__ == "__main__":
    main()
