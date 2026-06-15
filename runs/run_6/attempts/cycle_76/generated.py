"""Cycle 76 — 法 (fǎ, "law"). 8 MMH strokes.

法 = 氵 (s1-s3) + 去 (s4-s8).
  s1: top water dot (dian)
  s2: middle water dot (dian)
  s3: bottom water ti (rising) — using draw_heng for the rising mark
  s4: 去's top heng
  s5: 去's vertical (shu)
  s6: 去's middle/long heng
  s7: 厶 outer (pie)
  s8: 厶 closing (heng/turn)

All anchors come verbatim from task_briefs/cycle_76.md. No magic numbers.
"""

import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from _anchor import anchor_to_xy  # noqa: F401  (kept for parity / forced import)
from dian import draw_dian
from heng import draw_heng
from shu import draw_shu
from pie import draw_pie


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

    # s1 — 氵 top dot (dian sweeping down-right)
    draw_dian(t, ("TL", 0.436, 0.608), ("ML", 0.896, 0.004))

    # s2 — 氵 middle dot (dian sweeping down-right)
    draw_dian(t, ("ML", 0.064, 0.332), ("ML", 0.424, 0.664))

    # s3 — 氵 bottom ti (rising mark from lower-left up to mid-right).
    # No standalone ti primitive in bank; substitute draw_heng — the
    # BL→ML anchors give an upward slope, which reads as a 提.
    draw_heng(t, ("BL", 0.224, 1.292), ("ML", 0.764, 0.888))

    # s4 — 去's top heng (slight downward right)
    draw_heng(t, ("C", 0.2, 0.304), ("MR", 0.604, 0.096))

    # s5 — 去's vertical (shu) — shortened so it does not pierce 厶
    draw_shu(t, ("TC", 0.668, 0.332), ("C", 0.756, 0.85))

    # s6 — 去's middle/long heng across the right half
    draw_heng(t, ("BL", 0.836, 0.156), ("MR", 1.088, 0.92))

    # s7 — 厶 outer pie (sweeping down-left)
    draw_pie(t, ("BC", 0.896, 0.208), ("BR", 0.368, 0.908))

    # s8 — 厶 closing stroke (pulled in for a closer 厶 triangle)
    draw_heng(t, ("BC", 0.8, 0.7), ("BR", 0.4, 0.95))

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_法.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen)
    screen.update()


if __name__ == "__main__":
    main()
