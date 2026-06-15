"""Cycle 71 — 明 (míng). 8 strokes = 日 (left) + 月 (right).

Brief: runs/run_6/task_briefs/cycle_71.md
Override: pie_clamp (s5.to.y_frac 1.56 → 1.3) — already applied in anchors.
"""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from _anchor import anchor_to_xy
from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
from heng_zhe import draw_heng_zhe
from heng_zhe_gou import draw_heng_zhe_gou


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

    # 1. 日 left wall — shu
    draw_shu(t, ('TL', 0.06, 0.732), ('BL', 0.176, 0.468))

    # 2. 日 top+right wall — heng_zhe (TL→TL corner→BL tail)
    draw_heng_zhe(t,
                  ('TL', 0.256, 0.756),
                  ('TL', 0.976, 0.756),
                  ('BL', 0.976, 0.444))

    # 3. 日 internal heng (middle bar)
    draw_heng(t, ('ML', 0.312, 0.544), ('ML', 0.716, 0.46))

    # 4. 日 closing bottom heng
    draw_heng(t, ('BL', 0.3, 0.232), ('BL', 0.836, 0.112))

    # 5. 月 pie (with pie_clamp override already encoded: to.y_frac=1.3)
    draw_pie(t, ('TC', 0.596, 0.46), ('BL', 0.704, 1.3))

    # 6. 月 right wall — heng_zhe_gou (TC→TR corner→BR tail with hook)
    # Attempt 2: lift head + corner y_frac 0.628 → 0.46 to match pie head y,
    # closing 月's top (attempt 1 had 17px open-top gap).
    draw_heng_zhe_gou(t,
                      ('TC', 0.924, 0.46),
                      ('TR', 0.148, 0.46),
                      ('BR', 0.148, 1.116))

    # 7. 月 internal upper heng
    draw_heng(t, ('C', 0.876, 0.316), ('MR', 0.428, 0.224))

    # 8. 月 internal lower heng
    draw_heng(t, ('BC', 0.796, 0.048), ('MR', 0.444, 0.96))

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_明.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
