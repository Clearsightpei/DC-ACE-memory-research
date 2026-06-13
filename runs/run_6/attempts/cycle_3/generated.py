"""Cycle 3 — 丿 (pie) atomic stroke.

ONE brushed-Bezier diagonal stroke from TC (upper center) sweeping
down-left to BL. Tapered tail (width 11 → 3); heaviest at the head
(dunbi 18 → 14). This is the OPPOSITE of 横's profile.

Brief: cycle_3.md. Stroke count = 1 (matches MMH for 丿).
"""

import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from _anchor import anchor_to_xy
from heng import brushed_bezier


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


def w_pie(s):
    """丿 width profile.

    s ∈ [0, 1]. Head dunbi heaviest; tail tapers to ~3 (the min floor
    in brushed_bezier kicks in for the very tip).
      [0.00, 0.10] head dunbi: 18 → 14
      [0.10, 0.85] shaft:      14 → 11
      [0.85, 1.00] tail taper: 11 → 3 (fine tip)
    """
    if s < 0.10:
        return 18.0 - (s / 0.10) * 4.0
    if s < 0.85:
        return 14.0 - ((s - 0.10) / 0.75) * 3.0
    return 11.0 - ((s - 0.85) / 0.15) * 8.0


def draw_pie(t, from_anchor, to_anchor):
    """Draw a 丿 from `from_anchor` (head) to `to_anchor` (tapered tail).

    Control points sit at the 1/3 and 2/3 marks of the chord with a
    small +10 math-y offset, giving the 撇 a slight concave-down arc
    (peak above the chord — the canonical pie dips).
    """
    p0 = anchor_to_xy(from_anchor)
    p3 = anchor_to_xy(to_anchor)
    p1 = (p0[0] + (p3[0] - p0[0]) * 0.33,
          p0[1] + (p3[1] - p0[1]) * 0.33 + 10)
    p2 = (p0[0] + (p3[0] - p0[0]) * 0.67,
          p0[1] + (p3[1] - p0[1]) * 0.67 + 10)
    brushed_bezier(t, p0, p1, p2, p3, w_pie, samples=240)


def task_01(t, screen):
    reset(t)
    draw_pie(t, ("TC", 0.5, 0.5), ("BL", 0.0, 0.5))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_丿.png"))


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
