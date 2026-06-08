"""Cycle 23 — 力 brushwork (iter 1).

力 = 横折钩 (frame) + 撇 (cuts through heng from upper-middle, sweeping
down-left). Distinguished from 刀 by the 撇 head visibly extending
ABOVE the heng top (force the upper extension).

Composition (from brief):
  draw_heng_zhe_gou(t, ox=-15, oy=-25, scale=0.95)
    → heng spans (-110, +89) → (+80, +89); shu corner→(+80, -120);
       hook to (+32.5, -82). Matches skel heng (-90,+95)→(+85,+95)
       with slight scale-normalized shift.
  draw_pie(t, ox=-90, oy=-10, scale=0.6)
    → 撇 head (+150,+200)*0.6 + (-90,-10) = (0, +110);
      tail (-180,-180)*0.6 + (-90,-10) = (-198, -118).
    Head y=+110 sits ABOVE heng y=+89 → ~21px crossing — visible
    upper extension that distinguishes 力 from 刀.
"""

import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code'))
from heng_zhe_gou import draw as draw_heng_zhe_gou
from pie import draw as draw_pie


def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1)
    img.convert("RGBA").save(path, "PNG")


def reset_turtle(t):
    t.reset(); t.hideturtle(); t.speed(0)
    t.pencolor("black"); t.pensize(3)
    t.penup(); t.goto(0, 0); t.setheading(90)


# ── Task 01 | 力 | li
def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0)

    t = turtle.Turtle()
    reset_turtle(t)

    # 横折钩 frame (drawn first — establishes the L-with-hook).
    draw_heng_zhe_gou(t, ox=-15, oy=-25, scale=0.95)

    # 撇 cuts through the heng from upper-middle down-left.
    # Head at y=+110 > heng's y=+89 → visible upper extension.
    draw_pie(t, ox=-90, oy=-10, scale=0.6)

    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_力.png"))


if __name__ == "__main__":
    main()
