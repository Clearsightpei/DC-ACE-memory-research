"""Cycle 86 — 黄 (huang) — 11 MMH strokes.

廿 + 由 + 八 stacked. All anchors verbatim from task_briefs/cycle_86.md.
"""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from _anchor import anchor_to_xy  # noqa: F401
from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
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
    # 1. heng — top short bar of 廿
    draw_heng(t, ("TL", 0.508, 0.972), ("TR", 0.504, 0.832))
    # 2. pie — long horizontal sweep across 廿 (acts as the long upper 横 swept)
    draw_pie(t, ("TL", 0.884, 0.46), ("C", 0.088, 0.524))
    # 3. shu — left vertical of 廿
    draw_shu(t, ("TC", 0.856, 0.272), ("C", 0.736, 0.464))
    # 4. heng — long horizontal beneath 廿
    draw_heng(t, ("ML", -0.12, 0.732), ("MR", 1.116, 0.58))
    # 5. shu — left vertical of 由 box
    draw_shu(t, ("BL", 0.548, 0.036), ("BL", 0.888, 1.008))
    # 6. heng_zhe — top + right side of 由 box
    draw_heng_zhe(t,
                  ("BL", 0.788, 0.06),
                  ("BR", 0.056, 0.06),
                  ("BR", 0.056, 0.924))
    # 7. heng — middle bar inside 由
    draw_heng(t, ("BC", 0.036, 0.464), ("BC", 0.864, 0.396))
    # 8. shu — short central vertical inside 由
    draw_shu(t, ("C", 0.324, 0.712), ("BC", 0.392, 0.8))
    # 9. heng — bottom closing bar of 由
    draw_heng(t, ("BL", 0.964, 0.972), ("BC", 0.96, 0.804))
    # 10. dian — left foot (撇点)
    draw_dian(t, ("BC", 0.208, 1.252), ("BL", 0.252, 1.3))
    # 11. dian — right foot (捺点)
    draw_dian(t, ("BC", 0.844, 1.144), ("BR", 0.496, 1.3))

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_黄.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
