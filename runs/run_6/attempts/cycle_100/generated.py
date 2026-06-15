"""cycle_100 — 福 (fu), 13 MMH strokes.

Strokes (per brief):
  s1  dian      (TL,0.528,0.284) → (TC,0.024,0.644)
  s2  shu       (ML,-0.224,0.452) → (BL,-0.300,0.784)
  s3  shu       (BL,0.528,0.064) → (BL,0.560,1.300)
  s4  pie       (ML,0.792,0.964) → (BL,0.996,0.204)
  s5  dian      (TC,0.568,0.588) → (TR,0.640,0.452)
  s6  heng      (C,0.448,0.072) → (C,0.708,0.764)
  s7  heng      (C,0.680,0.088) → (MR,0.360,0.436)
  s8  heng      (C,0.776,0.676) → (MR,0.600,0.564)
  s9  shu       (BC,0.180,0.028) → (BC,0.532,1.288)
  s10 heng_zhe  (BC,0.396,0.048) -corner-> (BR,0.744,0.048) → (BR,0.744,1.300)
  s11 heng      (BC,0.664,0.652) → (BR,0.504,0.536)
  s12 heng      (BC,0.984,0.136) → (BR,0.032,0.980)
  s13 heng      (BC,0.612,1.180) → (BR,0.536,1.020)

Exactly 13 turtle-primitive calls in task_01.
"""
import io
import os
import sys
import turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from _anchor import anchor_to_xy  # noqa: E402
from dian import draw_dian        # noqa: E402
from shu import draw_shu          # noqa: E402
from pie import draw_pie          # noqa: E402
from heng import draw_heng        # noqa: E402
from heng_zhe import draw_heng_zhe  # noqa: E402


def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1)
    img.convert("RGBA").save(path, "PNG")


def reset(t):
    t.reset()
    t.hideturtle()
    t.speed(0)
    t.pencolor("black")
    t.penup()
    t.goto(0, 0)
    t.setheading(90)


def task_01(t, screen):
    reset(t)

    # s1 — dian (top of 礻 radical)
    draw_dian(t, ('TL', 0.528, 0.284), ('TC', 0.024, 0.644))
    # s2 — short shu of 礻
    draw_shu(t, ('ML', -0.224, 0.452), ('BL', -0.300, 0.784))
    # s3 — long shu down the left of 礻
    draw_shu(t, ('BL', 0.528, 0.064), ('BL', 0.560, 1.300))
    # s4 — pie of 礻
    draw_pie(t, ('ML', 0.792, 0.964), ('BL', 0.996, 0.204))
    # s5 — bottom dian of 礻
    draw_dian(t, ('TC', 0.568, 0.588), ('TR', 0.640, 0.452))
    # s6 — top heng of 一 above 口 (right component)
    draw_heng(t, ('C', 0.448, 0.072), ('C', 0.708, 0.764))
    # s7 — heng of upper 口/口-like
    draw_heng(t, ('C', 0.680, 0.088), ('MR', 0.360, 0.436))
    # s8 — bottom heng of upper 口
    draw_heng(t, ('C', 0.776, 0.676), ('MR', 0.600, 0.564))
    # s9 — center shu separating upper 口 from 田
    draw_shu(t, ('BC', 0.180, 0.028), ('BC', 0.532, 1.288))
    # s10 — heng_zhe forming top + right of 田
    draw_heng_zhe(t,
                  ('BC', 0.396, 0.048),
                  ('BR', 0.744, 0.048),
                  ('BR', 0.744, 1.300))
    # s11 — short heng cross-bar inside 田 (upper)
    draw_heng(t, ('BC', 0.664, 0.652), ('BR', 0.504, 0.536))
    # s12 — long bottom heng of 田
    draw_heng(t, ('BC', 0.984, 0.136), ('BR', 0.032, 0.980))
    # s13 — small inside-bottom heng of 田
    draw_heng(t, ('BC', 0.612, 1.180), ('BR', 0.536, 1.020))

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_福.png"))


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
