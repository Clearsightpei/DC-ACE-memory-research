"""Cycle 77 — 朋 (peng). 8 strokes: 月+月 side-by-side.

Strokes verbatim from task_briefs/cycle_77.md:
  1. pie       (TL,0.272,0.612) → (BL,-0.2,1.3)        # left  月 撇
  2. heng_zhe_gou (TL,0.532,0.648) → (TL,0.676,0.648) → (BL,0.676,1.0)   # left  月 right wall
  3. heng      (ML,0.544,0.492) → (ML,0.88,0.412)       # left  月 inner heng 1
  4. heng      (BL,0.46,0.06)  → (ML,0.892,0.988)       # left  月 inner heng 2
  5. pie       (TC,0.696,0.552) → (BC,0.304,1.292)      # right 月 撇
  6. heng_zhe_gou (TC,0.952,0.584) → (TR,0.136,0.584) → (BR,0.136,1.08)  # right 月 right wall
  7. heng      (C,1.0,0.416)   → (MR,0.412,0.332)       # right 月 inner heng 1
  8. heng      (BC,0.924,0.036)→ (MR,0.424,0.956)       # right 月 inner heng 2
"""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from _anchor import anchor_to_xy  # noqa: F401
from pie import draw_pie
from heng import draw_heng
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
    # Left 月
    draw_pie(t,           ('TL', 0.272, 0.612), ('BL', -0.2, 1.3))
    draw_heng_zhe_gou(t,  ('TL', 0.532, 0.648), ('TL', 0.676, 0.648), ('BL', 0.676, 1.0))
    draw_heng(t,          ('ML', 0.544, 0.492), ('ML', 0.88, 0.412))
    draw_heng(t,          ('BL', 0.46, 0.06),   ('ML', 0.892, 0.988))
    # Right 月
    draw_pie(t,           ('TC', 0.696, 0.552), ('BC', 0.304, 1.292))
    draw_heng_zhe_gou(t,  ('TC', 0.952, 0.584), ('TR', 0.136, 0.584), ('BR', 0.136, 1.08))
    draw_heng(t,          ('C', 1.0, 0.416),    ('MR', 0.412, 0.332))
    draw_heng(t,          ('BC', 0.924, 0.036), ('MR', 0.424, 0.956))

    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_朋.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen)
    screen.update()


if __name__ == "__main__":
    main()
