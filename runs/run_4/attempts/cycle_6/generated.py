"""
Cycle 6 — Drawer attempt for 点 (dian, 右点).

A short teardrop-shaped dot, tilted ~45° down-right.
  Entry (thin, ~3)   → upper-left (-25, +20)
  Belly (heavy, 14)  → at s ≈ 0.30
  Tail  (fine, ~3)   → lower-right (+30, -25)

Width profile (from the task brief):
  s < 0.30 : 3  + (s/0.30) * 11      # build up 3 → 14
  s ≥ 0.30 : 14 - ((s-0.30)/0.70) * 11  # taper 14 → 3

Reuses brushed_bezier from heng.py (which already enforces the
min-pensize-3 floor — run_3 c17 lesson).
"""

import io
import os
import sys
import turtle

from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# Pull in mastered atomic-stroke helpers from the Success Bank.
sys.path.insert(0, os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code'))
from heng import brushed_bezier  # noqa: E402


def save_canvas_to_png(screen, path: str) -> None:
    """Snapshot the turtle canvas to PNG via PostScript → PIL."""
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode='color')
    img = Image.open(io.BytesIO(ps.encode('utf-8')))
    img = img.convert('RGB')
    img.save(path, 'PNG')


def reset_turtle(t, screen) -> None:
    t.reset()
    t.hideturtle()
    t.speed(0)
    screen.tracer(0, 0)
    t.pencolor('black')
    t.pensize(3)


def _w_dian(s: float) -> float:
    """Teardrop width: 3 → 14 by s=0.30, then 14 → 3 by s=1.0."""
    if s < 0.30:
        return 3.0 + (s / 0.30) * 11.0
    return 14.0 - ((s - 0.30) / 0.70) * 11.0


# ── Task 01 | 点 | dian ──
def draw_dian(t, ox: float = 0.0, oy: float = 0.0, scale: float = 1.0) -> None:
    """Draw a single 右点 (right dot) as ONE brushed cubic Bézier.

    Endpoints (before transform):
        P0 = (-25, +20)   thin entry, upper-left
        P3 = (+30, -25)   fine tail, lower-right
    Controls placed along the entry→tail line so the segment is a
    nearly-straight teardrop (the swell comes from the width profile,
    not from arc curvature). A small downward bias on P2 gives the
    belly a slight gravity-toward-tail feel typical of 楷书 点.
    """
    P0 = (-25.0 * scale + ox, 20.0 * scale + oy)
    P3 = (30.0 * scale + ox, -25.0 * scale + oy)
    # Controls on the chord, P2 nudged a few px downward for natural sag.
    P1 = (-7.0 * scale + ox, 5.0 * scale + oy)
    P2 = (13.0 * scale + ox, -12.0 * scale + oy)
    brushed_bezier(t, P0, P1, P2, P3, _w_dian, samples=180)


def main() -> None:
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.colormode(255)
    t = turtle.Turtle()
    reset_turtle(t, screen)

    draw_dian(t)

    screen.update()
    out_path = os.path.join(OUT_DIR, '01_点.png')
    save_canvas_to_png(screen, out_path)
    print(f'wrote {out_path}')

    try:
        screen.bye()
    except turtle.Terminator:
        pass


if __name__ == '__main__':
    main()
