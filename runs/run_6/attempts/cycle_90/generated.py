"""Cycle 90 — 等 (12 strokes: ⺮ bamboo top + 寺 below).

Anchors taken verbatim from task_briefs/cycle_90.md.
12 top-level primitive calls (= MMH stroke count).
"""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from _anchor import anchor_to_xy  # noqa
from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
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
    # ⺮ bamboo radical top (6 strokes) — left half then right half
    # 1. 撇 (left bamboo) — TL pie
    draw_pie(t, ("TL", 0.696, 0.212), ("ML", 0.212, 0.14))
    # 2. 横 (left bamboo) — TL→TC heng
    draw_heng(t, ("TL", 0.796, 0.628), ("TC", 0.476, 0.536))
    # 3. 点 (left bamboo) — TL→C dian
    draw_dian(t, ("TL", 0.848, 0.8), ("C", 0.056, 0.02))
    # 4. 撇 (right bamboo) — TC pie
    draw_pie(t, ("TC", 0.836, 0.1), ("TC", 0.524, 0.836))
    # 5. 横 (right bamboo) — TC→TR heng
    draw_heng(t, ("TC", 0.936, 0.5), ("TR", 0.716, 0.384))
    # 6. 点 (right bamboo) — TC→MR dian
    draw_dian(t, ("TC", 0.9, 0.752), ("MR", 0.26, 0.032))

    # 寺 (bottom — 土 over 寸, 6 strokes)
    # 7. 横 (top of 土) — ML→MR heng
    draw_heng(t, ("ML", 0.884, 0.364), ("MR", 0.156, 0.228))
    # 8. 竖 (vertical of 土) — TC→C shu
    draw_shu(t, ("TC", 0.368, 0.932), ("C", 0.432, 0.728))
    # 9. 横 (long horizontal — wide) — ML→MR heng
    draw_heng(t, ("ML", -0.088, 0.976), ("MR", 1.064, 0.756))
    # 10. 横 (lower horizontal of 寸) — BL→BR heng
    draw_heng(t, ("BL", 0.324, 0.492), ("BR", 0.616, 0.332))
    # 11. 竖 (vertical of 寸, hook-like tail extending below) — C→BC shu
    draw_shu(t, ("C", 0.656, 0.876), ("BC", 0.324, 1.3))
    # 12. 点 (dian inside 寸) — BL→BC dian
    draw_dian(t, ("BL", 0.84, 0.664), ("BC", 0.152, 1.048))

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_等.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
