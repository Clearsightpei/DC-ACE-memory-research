"""Cycle 85 — 部 (bù). 10 MMH strokes: 咅 (left, 7) + 阝 (right, 3).

Anchors are taken verbatim from task_briefs/cycle_85.md. No magic
numbers — every position resolves via _anchor.anchor_to_xy.
"""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from _anchor import anchor_to_xy  # noqa: F401  (kept for parity with brief)
from dian import draw_dian
from heng import draw_heng
from shu import draw_shu
from heng_zhe import draw_heng_zhe


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

    # 咅 (left half, 7 strokes)
    # 1. dian — top dot of 立
    draw_dian(t, ("TL", 0.784, 0.26), ("TC", 0.172, 0.56))
    # 2. heng — top horizontal of 立
    draw_heng(t, ("ML", 0.24, 0.024), ("TC", 0.452, 0.868))
    # 3. dian — left dot of 立
    draw_dian(t, ("ML", 0.404, 0.32), ("ML", 0.584, 0.596))
    # 4. shu — short vertical of 立's right dot
    draw_shu(t, ("C", 0.172, 0.084), ("C", 0.004, 0.708))
    # 5. heng — bottom horizontal of 立
    draw_heng(t, ("ML", -0.22, 0.968), ("C", 0.696, 0.732))
    # 6. shu — vertical of 口
    draw_shu(t, ("BL", 0.228, 0.336), ("BL", 0.492, 1.136))
    # 7. heng_zhe — top+right of 口
    draw_heng_zhe(t,
                  ("BL", 0.42, 0.34),
                  ("BC", 0.244, 0.34),
                  ("BC", 0.244, 0.724))
    # 8. heng — bottom of 口
    draw_heng(t, ("BL", 0.564, 0.992), ("BC", 0.308, 0.852))

    # 阝 (right half, 2 strokes — heng_zhe ear + shu tail)
    # 9. heng_zhe — the ear loop of 阝
    draw_heng_zhe(t,
                  ("TR", 0.104, 0.976),
                  ("MR", 0.28, 0.976),
                  ("BR", 0.28, 0.428))
    # 10. shu — long descending vertical of 阝
    draw_shu(t, ("TC", 0.788, 0.816), ("BC", 0.96, 1.3))

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_部.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
