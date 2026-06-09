"""
Cycle 9 — 八 / 人 / 入 via run_4 turtle 撇/捺 primitives.

八: 撇 + 捺 with VISIBLE GAP at top (heads separated).
人: 撇 + 捺 SHARED apex.
入: 捺 dominant (long); 撇 shorter, head attached BELOW 捺's apex.

Coordinates: turtle math-coords on an 800x600 canvas, origin center, y-up.
"""

import io
import os
import sys
import turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, "..", "..", "success_bank", "code")
sys.path.insert(0, SB)

from pie import draw as draw_pie  # noqa: E402
from na import draw as draw_na    # noqa: E402


def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1)
    img.convert("RGBA").save(path, "PNG")


def reset_turtle(t):
    t.reset()
    t.hideturtle()
    t.speed(0)
    t.pencolor("black")
    t.penup()
    t.goto(0, 0)
    t.setheading(90)


def draw_ba(t):
    """八 — visible gap at top.

    撇 (left): head near (-15, -20), tail near (-160, -150).
    捺 (right): head near (+55, +70), tail tip near (+240, -150).
    Heads are separated by ~70 px horizontally AND ~90 px vertically.
    """
    # 撇 — scale=0.5, ox=-82, oy=-120 -> head ~(-7, -20), tail ~(-172, -210)
    draw_pie(t, ox=-82, oy=-120, scale=0.5)
    # 捺 — scale=0.5, ox=+125, oy=-47 -> head ~(+50, +53), tail tip ~(+245, -133)
    draw_na(t, ox=125, oy=-47, scale=0.5)


def draw_ren(t):
    """人 — shared apex at top.

    Both strokes' heads should coincide near (0, 90).
    """
    # 撇 — scale=0.55, head canonical=(82.5, 110); want (0, 90) -> ox=-82.5, oy=-20
    draw_pie(t, ox=-82.5, oy=-20, scale=0.55)
    # 捺 — scale=0.55, head canonical=(-82.5, 110); want (0, 90) -> ox=+82.5, oy=-20
    draw_na(t, ox=82.5, oy=-20, scale=0.55)


def draw_ru(t):
    """入 — 撇 and 捺 both long, meet near the top; 捺 head sits just
    BELOW 撇's head (rather than coinciding as in 人). The two strokes
    diverge without crossing.

    Targets (turtle math-coords):
      撇 head ~ (+15, +95),  tail ~ (-150, -160)
      捺 head ~ (-10, +60),  tail tip ~ (+210, -150)
    """
    # 撇 — scale=0.55, head canonical=(82.5, 110); want (+15, +95)
    # -> ox=-67.5, oy=-15. tail becomes (-99-67.5, -99-15) = (-166, -114).
    # Centerline runs from (+15, +95) down-left to (-166, -114).
    draw_pie(t, ox=-67.5, oy=-15, scale=0.55)
    # 捺 — scale=0.60, head canonical=(-90, 120); want (-10, +60)
    # -> ox=+80, oy=-60. tail base=(102-... 170*0.6+80, -180*0.6-60)
    #    = (102+80, -108-60) = (182, -168); kick tip=(144+80, -103.2-60)=(224, -163).
    draw_na(t, ox=80, oy=-60, scale=0.60)


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0)

    t = turtle.Turtle()

    tasks = [
        ("01_八.png", draw_ba),
        ("02_人.png", draw_ren),
        ("03_入.png", draw_ru),
    ]

    for fname, fn in tasks:
        reset_turtle(t)
        fn(t)
        screen.update()
        save_canvas_to_png(screen, os.path.join(OUT_DIR, fname))

    try:
        turtle.bye()
    except turtle.Terminator:
        pass


if __name__ == "__main__":
    main()
