"""Cycle 74 — 果 (guǒ, "fruit"), 8 strokes.

Structure: 田 (s1-s5) on top + 木 (s6 shu + s7 pie + s8 na) bottom.
- s1, s2: top corners (small slanted strokes — render via shu/heng_zhe as brief says)
- s3: 田's right wall (heng_zhe down)
- s4: 田's internal horizontal
- s5: 田's bottom heng
- s6: 木 vertical (long shu, clamped 1.66→1.3 already in brief)
- s7: 木 pie (sweeping to BL)
- s8: 木 na (sweeping to BR)

8 turtle calls (one per MMH stroke). All endpoints derived via anchor_to_xy.
"""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from _anchor import anchor_to_xy  # noqa: F401  (imported so we exercise it; primitives import it too)
from shu import draw_shu
from heng import draw_heng
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
    t.reset()
    t.hideturtle()
    t.speed(0)
    t.pencolor("black")
    t.penup()
    t.goto(0, 0)
    t.setheading(90)


def task_01(t, screen):
    reset(t)

    # s1: 田 top-left small slanted stroke — primitive shu
    draw_shu(t, ("TL", 0.48, 0.532), ("ML", 0.856, 0.632))

    # s2: 田 top heng_zhe (top edge + right wall corner)
    draw_heng_zhe(t, ("TL", 0.604, 0.508), ("TC", 0.9, 0.508), ("C", 0.9, 0.44))

    # s3: 田 right wall (rendered as heng per brief — long stroke)
    draw_heng(t, ("ML", 0.94, 0.056), ("TC", 0.784, 0.944))

    # s4: 田 internal horizontal
    draw_heng(t, ("ML", 0.936, 0.54), ("C", 0.856, 0.356))

    # s5: 田 bottom heng
    draw_heng(t, ("BL", 0.068, 0.076), ("MR", 0.808, 0.936))

    # s6: 木 vertical (long shu, clamp 1.66→1.3 already applied in to_anchor)
    draw_shu(t, ("TC", 0.316, 0.576), ("BC", 0.412, 1.3))

    # s7: 木 pie (sweeping down-left to BL)
    draw_pie(t, ("BC", 0.296, 0.064), ("BL", -0.032, 1.256))

    # s8: 木 na (sweeping down-right to BR)
    draw_na(t, ("BC", 0.536, 0.048), ("BR", 1.272, 1.188))

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_果.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen)
    screen.update()


if __name__ == "__main__":
    main()
