"""Cycle 3 — atomic stroke 撇 (pie). Single-phase brushwork.

Reuses brushed_bezier from the Success Bank's heng.py.
"""

import io
import os
import sys
import turtle

from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code'))
from heng import brushed_bezier  # noqa: E402


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
    t.pensize(3)
    t.penup()
    t.goto(0, 0)
    t.setheading(90)


def w_pie(s: float) -> float:
    """撇 width profile.

    s ∈ [0, 1] from head (upper-right) to tail (lower-left).
      - Head dunbi (0–12%): peak 18 → 14. A pronounced bulb (the
        canonical 起笔 press of 撇 is heavier than 横's entry — the
        brush plants firmly before sweeping down).
      - Shaft (12–88%): 14 → 11 (gentle thinning, stays visually solid).
      - Final taper (88–100%): 11 → 3 (rapid taper to fine point
        over the last ~12% — this is the longer of the two ranges
        the brief offered, gives a smoother visual taper).
    """
    if s < 0.12:
        return 18.0 - (s / 0.12) * 4.0
    if s < 0.88:
        return 14.0 - ((s - 0.12) / 0.76) * 3.0
    return 11.0 - ((s - 0.88) / 0.12) * 8.0


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0, 0)

    t = turtle.Turtle()
    reset_turtle(t)

    # ── Task 01 | 撇 | pie
    # Head at upper-right (+150, +200), tail at lower-left (-180, -180).
    # Control points place the centerline slightly above the straight
    # head-to-tail line → gentle concave-down arc (canonical 撇 curvature).
    P0 = (150.0, 200.0)
    P1 = (30.0, 130.0)
    P2 = (-90.0, -30.0)
    P3 = (-180.0, -180.0)
    brushed_bezier(t, P0, P1, P2, P3, w_pie, samples=240)

    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_撇.png"))


if __name__ == "__main__":
    main()
