"""Cycle 88 — 谈 (tan) — 10 MMH strokes.

Structure: 讠 (left radical, 2 strokes) + 炎 (right, 火+火, 8 strokes).
Anchors taken verbatim from task_briefs/cycle_88.md.
"""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from _anchor import anchor_to_xy  # noqa: F401  (used implicitly by primitives)
from dian import draw_dian
from heng_zhe import draw_heng_zhe
from pie import draw_pie
from na import draw_na


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
    # 讠 (left radical)
    # 1. 点 (top dot of 讠)
    draw_dian(t, ("TL", 0.384, 0.412), ("TL", 0.852, 0.816))
    # 2. 横折提 rendered as heng_zhe (closest available compound)
    draw_heng_zhe(t, ("ML", -0.3, 0.708), ("BL", 0.068, 0.708), ("BC", 0.068, 0.564))

    # 炎 (right: upper 火)
    # 3. 点 (upper-left dot of upper 火)
    draw_dian(t, ("TC", 0.288, 0.932), ("C", 0.576, 0.236))
    # 4. 点/short pie (upper-right inner)
    draw_dian(t, ("TR", 0.732, 0.584), ("MR", 0.324, 0.1))
    # 5. 撇 (upper 火 left-leaning pie)
    draw_pie(t, ("TC", 0.872, 0.296), ("C", 0.264, 0.912))
    # 6. 点 (upper 火 right dot)
    draw_dian(t, ("MR", 0.08, 0.34), ("MR", 0.584, 0.68))

    # 炎 (right: lower 火)
    # 7. 点 (lower 火 left dot)
    draw_dian(t, ("BC", 0.212, 0.264), ("BC", 0.48, 0.548))
    # 8. 点 (lower 火 inner-right dot)
    draw_dian(t, ("MR", 0.668, 0.912), ("BR", 0.26, 0.428))
    # 9. 撇 (lower 火 pie)
    draw_pie(t, ("C", 0.836, 0.92), ("BL", 0.972, 1.3))
    # 10. 捺 (lower 火 na)
    draw_na(t, ("BR", 0.028, 0.548), ("BR", 1.3, 1.3))

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_谈.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
