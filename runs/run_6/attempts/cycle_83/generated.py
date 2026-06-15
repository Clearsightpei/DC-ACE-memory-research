"""都 (dū) — c83 attempt. 10 strokes: 者 (8) + 阝 (2).

Anchors are verbatim from task_briefs/cycle_83.md. No magic numbers.
"""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from _anchor import anchor_to_xy  # noqa: F401  (sanity import)
from dian import draw_dian
from heng import draw_heng
from pie import draw_pie
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
    # 者 (left, 8 strokes)
    # 1. dian (top dot of 耂)
    draw_dian(t, ("TL", 0.352, 0.904), ("TC", 0.364, 0.784))
    # 2. heng (short upper) — corrected order so we start at left, end at right
    draw_heng(t, ("TL", 0.748, 0.2), ("ML", 0.804, 0.424))
    # 3. heng (long crossbar of 耂)
    draw_heng(t, ("ML", -0.16, 0.636), ("C", 0.8, 0.376))
    # 4. pie (long down-left from 耂 top through to bottom-left)
    draw_pie(t, ("TC", 0.872, 0.664), ("BL", -0.3, 0.928))
    # 5. shu (left vertical of 日)
    draw_shu(t, ("BL", 0.52, 0.004), ("BL", 0.604, 1.196))
    # 6. heng_zhe (top + right side of 日)
    draw_heng_zhe(t,
                  ("BL", 0.732, 0.092),
                  ("BC", 0.404, 0.092),
                  ("BC", 0.404, 1.296))
    # 7. heng (middle stroke inside 日)
    draw_heng(t, ("BL", 0.744, 0.556), ("BC", 0.148, 0.48))
    # 8. heng (bottom stroke of 日)
    draw_heng(t, ("BL", 0.708, 1.072), ("BC", 0.176, 1.032))

    # 阝 (right, 2 strokes)
    # 9. heng_zhe (the ear loop)
    draw_heng_zhe(t,
                  ("TR", 0.272, 0.996),
                  ("MR", 0.272, 0.996),
                  ("BR", 0.452, 0.432))
    # 10. shu (long vertical tail of 阝)
    draw_shu(t, ("TC", 0.928, 0.86), ("BR", 0.088, 1.3))

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_都.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
