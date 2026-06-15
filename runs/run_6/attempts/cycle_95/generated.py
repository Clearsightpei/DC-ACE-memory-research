"""Cycle 95 — 感 (gan), 13 strokes.

Anchors taken verbatim from task_briefs/cycle_95_dataset.json. No magic
numbers — every (from, to) is an anchor tuple resolved via
_anchor.anchor_to_xy inside the primitives.
"""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from _anchor import anchor_to_xy  # noqa: F401  (imported per Drawer rule)
from heng import draw_heng
from pie import draw_pie
from shu import draw_shu
from na import draw_na
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

    # Stroke 1: 横 (top horizontal of 厂-radical)
    draw_heng(t, ('ML', 0.7, 0.02), ('TR', 0.24, 0.784))

    # Stroke 2: 撇 (left descending sweep of 厂-radical)
    draw_pie(t, ('TL', 0.404, 0.972), ('BL', -0.2, 0.804))

    # Stroke 3: 横 (top of inner 口)
    draw_heng(t, ('ML', 0.86, 0.512), ('C', 0.548, 0.368))

    # Stroke 4: 撇 (small inner stroke inside 厂)
    draw_pie(t, ('ML', 0.704, 0.836), ('BL', 0.892, 0.424))

    # Stroke 5: 竖 (long vertical of 戈-radical)
    draw_shu(t, ('ML', 0.884, 0.848), ('BC', 0.296, 0.1))

    # Stroke 6: 横 (bottom horizontal of inner 口)
    draw_heng(t, ('BL', 0.964, 0.34), ('BC', 0.5, 0.228))

    # Stroke 7: 捺 (long 戈 diagonal — right-down)
    draw_na(t, ('TC', 0.376, 0.188), ('MR', 1.028, 0.976))

    # Stroke 8: 撇 (inner small left sweep of 戈)
    draw_pie(t, ('MR', 0.344, 0.14), ('BC', 0.588, 0.428))

    # Stroke 9: 点 (upper-right 点 of 戈)
    draw_dian(t, ('TR', 0.048, 0.296), ('TR', 0.424, 0.584))

    # Stroke 10: 竖 (left vertical of 心 radical)
    draw_shu(t, ('BL', 0.536, 0.872), ('BL', 0.316, 1.3))

    # Stroke 11: 横 (curving bottom of 心)
    draw_heng(t, ('BL', 0.82, 0.784), ('BR', 0.096, 0.968))

    # Stroke 12: 点 (middle 点 of 心)
    draw_dian(t, ('BC', 0.34, 0.604), ('BC', 0.74, 0.888))

    # Stroke 13: 点 (right 点 of 心)
    draw_dian(t, ('BR', 0.304, 0.692), ('BR', 0.8, 1.112))

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_感.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen)
    screen.update()


if __name__ == "__main__":
    main()
