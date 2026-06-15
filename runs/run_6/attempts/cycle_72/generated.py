"""Cycle 72 — 京 (jīng). 8 strokes: 亠 + 口 + 小.

Decomposition (per task_briefs/cycle_72.md):
  s1 dian       — top dot of 亠
  s2 heng       — long top heng of 亠
  s3 shu        — 口 left vertical
  s4 heng_zhe   — 口 top + right (programmatic corner)
  s5 heng       — 口 bottom (and top of 小)
  s6 shu        — 小 central vertical
  s7 pie        — 小 left
  s8 na         — 小 right

All anchors are taken verbatim from the brief; no magic numbers.
"""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from _anchor import anchor_to_xy
from dian import draw_dian
from heng import draw_heng
from shu import draw_shu
from heng_zhe import draw_heng_zhe
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

    # s1: 亠 top dot
    draw_dian(t, ("TC", 0.224, 0.156), ("TC", 0.684, 0.492))

    # s2: 亠 long top heng
    draw_heng(t, ("ML", -0.036, 0.028), ("TR", 1.124, 0.844))

    # s3: 口 left vertical (shu)
    draw_shu(t, ("ML", 0.724, 0.432), ("BC", 0.064, 0.224))

    # s4: 口 top + right (heng_zhe, corner programmatic)
    draw_heng_zhe(t,
                  ("ML", 0.808, 0.408),
                  ("C", 0.91, 0.41),
                  ("C", 0.908, 0.884))

    # s5: 口 bottom heng (also top of 小)
    draw_heng(t, ("BC", 0.132, 0.144), ("BR", 0.128, 0.028))

    # s6: 小 central vertical
    draw_shu(t, ("BC", 0.392, 0.148), ("BC", 0.036, 1.284))

    # s7: 小 left pie
    draw_pie(t, ("BL", 0.668, 0.484), ("BL", 0.276, 1.176))

    # s8: 小 right na
    draw_na(t, ("BR", 0.044, 0.484), ("BR", 0.74, 1.192))

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_京.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
