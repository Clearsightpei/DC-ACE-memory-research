"""Cycle 1 — 3 tasks (一, 二, 三), mimicked from GT PNGs.

Strategy: each character is composed of one or more 横 (horizontal brushed
strokes). We define a single reusable `draw_heng(t, ox, oy, length, scale=1.0)`
following the §2.1 translate/scale interface and the §1.0 brushwork rule
(cubic Bézier centerline + per-sample pensize with a max(3, ...) floor).

A 横 in the GTs has:
  - small down-tilted entry tip (顿笔 at start)
  - gently arching body (slight dip in the middle, slight rise near the end)
  - small down-tilted exit tip (顿笔 at end)
We model this as a single cubic Bézier centerline with a width profile that
swells in the body and tapers near the tips, plus tiny straight feet drawn
at each end to capture the angled tips visible in the GT.
"""

import io
import os
import sys
import turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
if os.path.isdir(SB):
    sys.path.insert(0, SB)


# ---------- canvas helpers ----------

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


# ---------- §1.0 brushed Bézier ----------

def _bez(p0, p1, p2, p3, s):
    u = 1.0 - s
    x = (u * u * u * p0[0]
         + 3 * u * u * s * p1[0]
         + 3 * u * s * s * p2[0]
         + s * s * s * p3[0])
    y = (u * u * u * p0[1]
         + 3 * u * u * s * p1[1]
         + 3 * u * s * s * p2[1]
         + s * s * s * p3[1])
    return x, y


def brushed_bezier(t, P0, P1, P2, P3, w_profile, samples=220):
    t.penup()
    x0, y0 = _bez(P0, P1, P2, P3, 0.0)
    t.goto(x0, y0)
    t.pendown()
    for i in range(1, samples + 1):
        s = i / samples
        t.pensize(max(3, w_profile(s)))
        x, y = _bez(P0, P1, P2, P3, s)
        t.goto(x, y)
    t.penup()


# ---------- §2.1 reusable 横 primitive ----------

def draw_heng(t, ox=0.0, oy=0.0, length=300.0, scale=1.0):
    """Draw one 横 (horizontal brushed stroke) centered at (ox, oy).

    Length is the body span before scaling. The stroke has:
      - small down-angled entry foot at the left
      - a gently arching cubic Bézier body
      - small down-angled exit foot at the right

    Mimics the look of the MMH-rendered 横 in the cycle_1 GTs.
    """
    L = length * scale
    # body endpoints
    x0 = ox - L * 0.5
    x1 = ox + L * 0.5
    # gentle arch: dip slightly in mid-left, rise slightly on the right
    y_body_left = oy + 2.0 * scale
    y_body_right = oy + 6.0 * scale

    # control points: a flat-ish arch, slightly higher on the right
    P0 = (x0, y_body_left)
    P1 = (x0 + L * 0.30, oy - 4.0 * scale)
    P2 = (x0 + L * 0.70, oy + 4.0 * scale)
    P3 = (x1, y_body_right)

    # width profile: a swelling body, tapering toward the tips, floor at 3
    def w(s):
        # bell-ish profile peaking around 60% of stroke
        # ranges roughly 4 .. 9 (with the max(3, ...) floor in brushed_bezier)
        base = 4.0 + 5.0 * (1.0 - (s - 0.6) ** 2 / 0.36)
        return max(4.0, base) * scale

    # --- entry foot: short down-tilted segment at the left tip ---
    foot_len = 14.0 * scale
    t.penup()
    t.pensize(max(3, int(5 * scale)))
    t.goto(x0 - foot_len * 0.85, y_body_left - foot_len * 0.6)
    t.pendown()
    t.goto(x0, y_body_left)
    t.penup()

    # --- body: brushed Bézier ---
    brushed_bezier(t, P0, P1, P2, P3, w, samples=220)

    # --- exit foot: short down-tilted segment at the right tip ---
    t.penup()
    t.pensize(max(3, int(5 * scale)))
    t.goto(x1, y_body_right)
    t.pendown()
    t.goto(x1 + foot_len * 0.85, y_body_right - foot_len * 0.6)
    t.penup()


# ---------- tasks ----------

def task_01(t, screen):
    """一 — single horizontal stroke, centered slightly below middle."""
    reset_turtle(t)
    # From GT: stroke spans roughly x in [-150, +160], y around -50.
    draw_heng(t, ox=5.0, oy=-50.0, length=310.0, scale=1.0)
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_一.png"))


def task_02(t, screen):
    """二 — top short 横, bottom longer 横."""
    reset_turtle(t)
    # Top stroke: shorter, upper
    draw_heng(t, ox=-15.0, oy=+45.0, length=225.0, scale=1.0)
    # Bottom stroke: longer, lower
    draw_heng(t, ox=+5.0, oy=-80.0, length=315.0, scale=1.0)
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "02_二.png"))


def task_03(t, screen):
    """三 — three 横: top short, middle short, bottom long."""
    reset_turtle(t)
    # Top: short
    draw_heng(t, ox=-10.0, oy=+70.0, length=205.0, scale=1.0)
    # Middle: short (slightly shifted left)
    draw_heng(t, ox=-25.0, oy=-10.0, length=200.0, scale=1.0)
    # Bottom: longest
    draw_heng(t, ox=+10.0, oy=-105.0, length=330.0, scale=1.0)
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
