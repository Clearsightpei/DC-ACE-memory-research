"""演 — cycle 97, 14 MMH strokes.

Brief anchors translated directly via _anchor.anchor_to_xy. One
primitive call per MMH stroke. No magic numbers.

Stroke list (from task_briefs/cycle_97_dataset.json):
  1  dian        (氵 top dot)
  2  dian        (氵 middle dot)
  3  ti          (氵 bottom rising — rendered via draw_heng, no ti.py)
  4  dian        (宀 top dot)
  5  heng_zhe    (宀 horizontal-to-vertical roof)
  6  heng        (inner upper horizontal)
  7  heng        (inner short horizontal)
  8  heng_zhe    (inner box top + right vertical)
  9  heng        (inner box horizontal divider)
 10  heng        (inner lower horizontal)
 11  shu         (inner central vertical)
 12  heng        (inner short horizontal lower)
 13  pie         (bottom-left 撇)
 14  na          (bottom-right 捺)
"""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from _anchor import anchor_to_xy  # noqa: F401  (kept available)
from dian import draw_dian
from heng import draw_heng
from heng_zhe import draw_heng_zhe
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

    # 1  dian  (氵 top dot)
    draw_dian(t, ('TL', 0.28, 0.532), ('TL', 0.668, 0.856))

    # 2  dian  (氵 middle dot)
    draw_dian(t, ('ML', -0.016, 0.376), ('ML', 0.344, 0.676))

    # 3  ti  (氵 bottom rising — rendered as heng since no ti.py)
    draw_heng(t, ('BL', 0.204, 1.3), ('BL', 0.624, 0.032))

    # 4  dian  (宀 top dot)
    draw_dian(t, ('TC', 0.608, 0.176), ('TR', 0.036, 0.508))

    # 5  heng_zhe  (宀 roof)
    draw_heng_zhe(t,
                  ('TL', 0.984, 0.812),
                  ('ML', 0.84,  0.812),
                  ('ML', 0.84,  0.536))

    # 6  heng  (inner upper)
    draw_heng(t, ('C', 0.132, 0.04), ('MR', 0.592, 0.204))

    # 7  heng  (inner short)
    draw_heng(t, ('C', 0.388, 0.36), ('MR', 0.3, 0.256))

    # 8  heng_zhe  (inner box top + right vertical)
    draw_heng_zhe(t,
                  ('ML', 0.996, 0.828),
                  ('BC', 0.308, 0.828),
                  ('BC', 0.308, 0.724))

    # 9  heng  (inner divider)
    draw_heng(t, ('C', 0.188, 0.828), ('BR', 0.412, 0.672))

    # 10  heng  (inner lower)
    draw_heng(t, ('BC', 0.5, 0.208), ('BR', 0.232, 0.128))

    # 11  shu  (inner central vertical)
    draw_shu(t, ('C', 0.712, 0.472), ('BC', 0.776, 0.5))

    # 12  heng  (inner short lower)
    draw_heng(t, ('BC', 0.38, 0.676), ('BR', 0.224, 0.58))

    # 13  pie  (bottom-left 撇)
    draw_pie(t, ('BC', 0.592, 1.012), ('BL', 0.792, 1.3))

    # 14  na  (bottom-right 捺)
    draw_na(t, ('BR', 0.148, 0.94), ('BR', 0.752, 1.3))

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_演.png"))


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
