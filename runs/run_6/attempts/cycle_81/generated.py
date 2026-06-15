"""cycle_81 — 高 (gāo), 10 MMH strokes.

Structure: 亠 (s1 dian + s2 heng) + small 口 (s3 heng_zhe + s4 heng tip + s5 heng base)
           + 冂 (s6 shu + s7 heng_zhe_gou) + inner 口 (s8 shu + s9 heng + s10 heng).

All anchors emitted verbatim from task_briefs/cycle_81.md.
"""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from _anchor import anchor_to_xy  # noqa: F401  (sanity)
from dian import draw_dian
from heng import draw_heng
from shu import draw_shu
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
    # 1. 点 — top dot of 亠
    draw_dian(t, ("TC", 0.192, 0.144), ("TC", 0.596, 0.42))
    # 2. 横 — long horizontal of 亠
    draw_heng(t, ("TL", 0.324, 0.86), ("TR", 0.7, 0.72))
    # 3. 横折 — small 口's heng_zhe (top + right side)
    draw_heng_zhe(t, ("ML", 0.868, 0.156), ("C", 0.1, 0.156), ("C", 0.1, 0.764))
    # 4. 横 — small 口's top-left tip stroke
    draw_heng(t, ("ML", 0.98, 0.136), ("C", 0.744, 0.456))
    # 5. 横 — small 口's bottom (closing)
    draw_heng(t, ("C", 0.18, 0.692), ("C", 0.976, 0.58))
    # 6. 竖 — 冂's left vertical
    draw_shu(t, ("BL", 0.22, 0.108), ("BL", 0.336, 1.3))
    # 7. 横折钩 — 冂's top + right with hook
    draw_heng_zhe_gou(t, ("BL", 0.472, 0.14), ("BR", 0.092, 0.14), ("BR", 0.092, 1.296))
    # 8. 竖 — inner 口's left
    draw_shu(t, ("BL", 0.86, 0.468), ("BC", 0.116, 1.136))
    # 9. 横 — inner 口's top
    draw_heng(t, ("BC", 0.064, 0.464), ("BC", 0.92, 0.824))
    # 10. 横 — inner 口's bottom
    draw_heng(t, ("BC", 0.184, 1.036), ("BC", 0.968, 0.956))

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_高.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
