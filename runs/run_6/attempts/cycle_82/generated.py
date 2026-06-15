"""Cycle 82 — 真 (zhēn) — 10 MMH strokes.

Structure: 十 + 目 + 一 + 八 (4 components).
Anchors taken verbatim from task_briefs/cycle_82.md.
"""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from _anchor import anchor_to_xy  # noqa: F401  (used implicitly via primitives)
from heng import draw_heng
from shu import draw_shu
from heng_zhe import draw_heng_zhe
from dian import draw_dian


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
    # Stroke 1: heng — top of 十 (短横 above 目)
    draw_heng(t, ("TL", 0.556, 0.764), ("TR", 0.532, 0.596))
    # Stroke 2: shu — vertical of 十
    draw_shu(t, ("TC", 0.412, 0.196), ("C", 0.388, 0.2))
    # Stroke 3: shu — left vertical of 目
    draw_shu(t, ("ML", 0.828, 0.244), ("BL", 0.912, 0.66))
    # Stroke 4: heng_zhe — top + right vertical of 目
    draw_heng_zhe(t,
                  ("C", 0.012, 0.272),
                  ("C", 0.952, 0.272),
                  ("BC", 0.952, 0.552))
    # Stroke 5: heng — upper inner crossbar of 目
    draw_heng(t, ("C", 0.076, 0.728), ("C", 0.772, 0.64))
    # Stroke 6: heng — bottom of 目 (closing 横)
    draw_heng(t, ("BC", 0.092, 0.088), ("BC", 0.756, 0.008))
    # Stroke 7: heng — lower inner crossbar of 目
    draw_heng(t, ("BC", 0.08, 0.432), ("BC", 0.788, 0.348))
    # Stroke 8: heng — long 一 spanning under 目
    draw_heng(t, ("BL", -0.104, 0.812), ("BR", 1.128, 0.752))
    # Stroke 9: dian — left dot of 八
    draw_dian(t, ("BC", 0.224, 1.16), ("BL", 0.276, 1.3))
    # Stroke 10: dian — right dot of 八
    draw_dian(t, ("BC", 0.88, 1.008), ("BR", 0.492, 1.3))

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_真.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
