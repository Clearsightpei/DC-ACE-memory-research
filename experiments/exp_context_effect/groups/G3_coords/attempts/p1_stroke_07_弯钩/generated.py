"""
G3 (coord-bank) — p1_stroke_07_弯钩
Target: 弯钩 (wan gou) — a curved arc that ends in a small hook.
Format: coordinate-based (no 米字格 anchors, no joint specs).

Shape description:
  弯钩 typically starts near the top-center, curves gently down and to the
  right (the belly to the right), then near the bottom bends back left
  and terminates with a short hook flicking to the upper-left.
  Compare: 你/子/亅with-belly. The characteristic feature: single smooth
  curve + short leftward hook at bottom.

Canvas: 300x300, white background, black ink.
"""

import turtle
from PIL import Image
import io
import os

CANVAS = 300


def _quad_bezier(p0, p1, p2, steps=40):
    """Return list of points along a quadratic Bezier from p0 to p2 via p1."""
    pts = []
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        pts.append((x, y))
    return pts


def draw_wan_gou(t, ox=0, oy=0, scale=1.0):
    """
    Draw 弯钩 as a tapered curve + short hook.
    Coordinates are in turtle math coords (y up), origin at canvas center.

    Anatomy (numeric offsets, coord-bank style):
      start point:    ( +5,  +110 )   near top-center, slight right
      belly control:  ( +40,   +10 )   pulls arc to the right
      hook base:      ( -10,  -95  )  bottom of curve, slightly left of center
      hook tip:       ( -35,  -78  )  short flick up-left
      widths taper:   6px at start -> 9px mid -> 5px at hook base -> 3px tip
    """
    # Segment 1: main curved body via quadratic Bezier
    p_start = (ox + 5 * scale, oy + 110 * scale)
    p_ctrl = (ox + 40 * scale, oy + 10 * scale)
    p_end = (ox - 10 * scale, oy - 95 * scale)

    curve_pts = _quad_bezier(p_start, p_ctrl, p_end, steps=60)

    # Draw curve with variable width (taper: thicker in middle, thin at ends)
    t.penup()
    t.goto(curve_pts[0])
    t.pendown()
    n = len(curve_pts)
    for i, (x, y) in enumerate(curve_pts):
        u = i / (n - 1)
        # width profile: 6 at u=0, 10 at u=0.55, 5 at u=1
        if u < 0.55:
            w = 6 + (10 - 6) * (u / 0.55)
        else:
            w = 10 - (10 - 5) * ((u - 0.55) / 0.45)
        t.width(max(3, w * scale))
        t.goto(x, y)

    # Segment 2: hook — short flick from p_end up-left
    p_hook_tip = (ox - 38 * scale, oy - 75 * scale)
    # Slight curve on the hook
    p_hook_ctrl = (ox - 22 * scale, oy - 78 * scale)
    hook_pts = _quad_bezier(p_end, p_hook_ctrl, p_hook_tip, steps=20)

    t.penup()
    t.goto(hook_pts[0])
    t.pendown()
    m = len(hook_pts)
    for i, (x, y) in enumerate(hook_pts):
        u = i / (m - 1)
        w = 5 - (5 - 2) * u  # taper from 5 to 2
        t.width(max(2, w * scale))
        t.goto(x, y)

    t.penup()


def main():
    out_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "01_弯钩.png",
    )

    screen = turtle.Screen()
    screen.setup(width=CANVAS, height=CANVAS)
    screen.screensize(CANVAS, CANVAS)
    screen.bgcolor("white")
    screen.tracer(0, 0)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color("black")
    t.penup()

    draw_wan_gou(t, ox=0, oy=0, scale=1.0)

    screen.update()

    # Export via canvas PostScript -> PIL
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color",
                           x=-CANVAS // 2, y=-CANVAS // 2,
                           width=CANVAS, height=CANVAS)
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=2)
    img = img.convert("RGB")
    img = img.resize((CANVAS, CANVAS), Image.LANCZOS)
    img.save(out_path, "PNG")

    try:
        screen.bye()
    except Exception:
        pass

    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
