"""Cycle 8 — uniform-width 横 variant (pensize ~25) for 一/二/三.

Follows brief: define draw_heng_wide inline (constant pensize, Bezier
centerline same as heng.py). Reuses brushed_bezier from success_bank.
NO subprocess — single turtle process, t.reset() between tasks.
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
from heng import brushed_bezier  # per-sample-pensize Bezier walker


# Uniform width to match the GT band.
# Brief said ~25 but pixel-measuring the GT bands shows actual thickness ≈ 5 px
# (the GT was rasterized from raw centerlines, not brushed). Brief explicitly
# permits refining ("does the band width visually match the GT band? Refine
# if not"). Using width 6 to match GT's ~5 px after turtle anti-aliasing.
HENG_WIDTH = 5.0


def draw_heng_wide(t, ox=0.0, oy=0.0, scale=1.0, width=HENG_WIDTH):
    """Uniform-width 横 — constant pensize matching MMH-postscript-rasterized GT band.

    Same Bezier centerline as heng.py (P0=(-200,-3), P3=(+200,+3), thirds for P1/P2),
    but width is a constant rather than the calligraphic dunbi-shaft-shoubi profile.
    """
    P0 = (-200.0 * scale + ox, -3.0 * scale + oy)
    P3 = (200.0 * scale + ox, 3.0 * scale + oy)
    P1 = (P0[0] + (P3[0] - P0[0]) / 3.0, P0[1] + (P3[1] - P0[1]) / 3.0)
    P2 = (P0[0] + 2.0 * (P3[0] - P0[0]) / 3.0, P0[1] + 2.0 * (P3[1] - P0[1]) / 3.0)
    brushed_bezier(t, P0, P1, P2, P3, lambda s: width, samples=220)


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
    """一 — single heng, centered."""
    reset(t)
    draw_heng_wide(t, ox=6, oy=-47, scale=0.81)
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_一.png"))


def task_02(t, screen):
    """二 — short top heng, long bottom heng."""
    reset(t)
    draw_heng_wide(t, ox=3, oy=35, scale=0.45)
    draw_heng_wide(t, ox=6, oy=-115, scale=0.80)
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "02_二.png"))


def task_03(t, screen):
    """三 — three hengs: shortest top, short middle, longest bottom."""
    reset(t)
    draw_heng_wide(t, ox=5, oy=60, scale=0.42)
    draw_heng_wide(t, ox=4, oy=-38, scale=0.38)
    draw_heng_wide(t, ox=14, oy=-140, scale=0.84)
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "03_三.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen)
    task_02(t, screen)
    task_03(t, screen)


if __name__ == "__main__":
    main()
