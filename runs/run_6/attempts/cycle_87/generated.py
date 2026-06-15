"""Cycle 87 — 谁 (shui), 10 strokes.

讠 left (2 strokes: dian, heng_zhe) + 隹 right (8 strokes: pie, shu, dian,
heng, shu, heng, heng, heng). All anchors copied verbatim from the brief.
"""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from _anchor import anchor_to_xy  # noqa: F401  (sanity import — primitives use it internally)
from dian import draw_dian
from heng_zhe import draw_heng_zhe
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng


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

    # 讠 left radical (2 strokes)
    # 1. dian — upper dot of speech radical
    draw_dian(t, ("TL", 0.452, 0.388), ("TL", 0.816, 0.712))
    # 2. heng_zhe — horizontal-turn-down forming the speech bracket
    # x_frac clamped to -0.3 (anchor extended-range floor); dataset's y_clamp override.
    draw_heng_zhe(t, ("ML", -0.3, 0.624), ("BL", 0.004, 0.624), ("BC", 0.004, 0.544))

    # 隹 right component (8 strokes)
    # 3. pie — top-left short slash of 亻
    draw_pie(t, ("TC", 0.616, 0.252), ("ML", 0.872, 0.84))
    # 4. shu — vertical stem of 亻 (extends below the 米字格)
    draw_shu(t, ("C", 0.3, 0.508), ("BC", 0.364, 1.3))
    # 5. dian — small dot atop 隹's right side
    draw_dian(t, ("TR", 0.028, 0.6), ("TR", 0.392, 0.92))
    # 6. heng — first short horizontal of the 隹 ladder (downward-slanted)
    draw_heng(t, ("C", 0.704, 0.416), ("MR", 0.832, 0.22))
    # 7. shu — vertical stem on the right of 隹
    draw_shu(t, ("BC", 0.808, 0.012), ("MR", 0.744, 0.876))
    # 8. heng — second short horizontal (mid)
    draw_heng(t, ("BC", 0.76, 0.46), ("BR", 0.808, 0.308))
    # 9. heng — third short horizontal (lower)
    draw_heng(t, ("MR", 0.108, 0.476), ("BR", 0.16, 0.792))
    # 10. heng — bottom long horizontal base of 隹
    draw_heng(t, ("BC", 0.52, 0.972), ("BR", 1.108, 0.864))

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_谁.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
