"""
G3 attempt: p1_stroke_19_横斜钩 (héng xié gōu)
Stroke = horizontal + slant-down-right + upward hook.
Appears in characters like 飞, 风, 气.
Coordinate-only format (no anchors / no cells).
Canvas 300x300, white bg, black ink.
"""

import turtle
from PIL import Image
import io
import os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_PNG = os.path.join(OUT_DIR, "01_横斜钩.png")


def draw_heng_xie_gou(t, ox=0, oy=0, scale=1.0):
    # Segment 1: 横 (short horizontal, slight rise) — starts upper-left area.
    x0, y0 = ox + -110 * scale, oy + 70 * scale
    x1, y1 = ox + -30 * scale, oy + 75 * scale
    # Segment 2: 斜 (long slant down-right)
    x2, y2 = ox + 80 * scale, oy + -70 * scale
    # Segment 3: 钩 (short upward-left hook)
    x3, y3 = ox + 45 * scale, oy + -30 * scale

    # Stroke thickness taper: use multiple passes for a modest calligraphic feel.
    # Pass 1 — main body, medium thickness.
    t.penup()
    t.goto(x0, y0)
    t.pendown()
    t.pensize(int(9 * scale))
    t.goto(x1, y1)
    t.pensize(int(11 * scale))
    t.goto(x2, y2)
    # Hook: thinner + shorter
    t.pensize(int(9 * scale))
    t.goto(x3, y3)
    t.penup()


def main():
    screen = turtle.Screen()
    screen.setup(width=300, height=300)
    screen.screensize(300, 300)
    screen.bgcolor("white")
    screen.tracer(0, 0)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color("black")

    draw_heng_xie_gou(t, ox=0, oy=0, scale=1.0)

    screen.update()

    # Export canvas to PostScript, convert to 300x300 PNG via PIL.
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")

    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    # Force to 300x300 white background composited (in case of transparency).
    img = img.convert("RGB")
    if img.size != (300, 300):
        img = img.resize((300, 300), Image.LANCZOS)
    img.save(OUT_PNG, "PNG")

    try:
        screen.bye()
    except turtle.Terminator:
        pass


if __name__ == "__main__":
    main()
