"""Cycle 2 — atomic stroke 竖 (shu, 垂露 vertical).

Reuses the mastered brushed_bezier helper from success_bank/code/heng.py.
Single-phase per principle_bank §5.3 (atomic strokes).
"""

import io
import os
import sys
import turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code'))
from heng import brushed_bezier  # mastered helper (Bézier + per-sample pensize, floor=3)


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


# ── Task 01 | 竖 | shu
def w_shu(s: float) -> float:
    """垂露竖 width profile — symmetric barbell.

    s ∈ [0, 1] from top to bottom.
      - Entry press (top dunbi) 16 → 11 over first 10%.
      - Shaft ~11 over middle ~76%.
      - Closing press (bottom 收笔, 垂露 rounded) 11 → 18 over final 14%.
    """
    if s < 0.10:
        return 16.0 - (s / 0.10) * 5.0
    if s < 0.86:
        return 11.0
    return 11.0 + ((s - 0.86) / 0.14) * 7.0


def draw_shu(t, ox: float = 0.0, oy: float = 0.0, scale: float = 1.0):
    """Draw 竖 (垂露 variant). Top-to-bottom, essentially vertical."""
    # Top → bottom. Controls colinear so the centerline is straight.
    P0 = (0.0 * scale + ox, 200.0 * scale + oy)
    P3 = (0.0 * scale + ox, -200.0 * scale + oy)
    P1 = (P0[0] + (P3[0] - P0[0]) / 3.0, P0[1] + (P3[1] - P0[1]) / 3.0)
    P2 = (P0[0] + 2.0 * (P3[0] - P0[0]) / 3.0, P0[1] + 2.0 * (P3[1] - P0[1]) / 3.0)
    brushed_bezier(t, P0, P1, P2, P3, w_shu, samples=220)


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0)
    t = turtle.Turtle()
    reset_turtle(t)

    draw_shu(t)

    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_竖.png"))


if __name__ == "__main__":
    main()
