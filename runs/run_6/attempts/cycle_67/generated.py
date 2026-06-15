"""Cycle 67 — 个 (gè). 3 strokes: pie, na, shu.

Anchors taken verbatim from task_briefs/cycle_67.md (apex_share + shu_apex_lift
already baked in by the Teacher).
"""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from _anchor import anchor_to_xy  # noqa: E402
from pie import draw_pie  # noqa: E402
from na import draw_na  # noqa: E402
from shu import draw_shu  # noqa: E402


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
    # Stroke 1: 撇 — apex (TC, 0.364, 0.348) → BL (-0.084, 0.296)
    draw_pie(t, ('TC', 0.364, 0.348), ('BL', -0.084, 0.296))
    # Stroke 2: 捺 — apex (TC, 0.54, 0.348) → MR (1.3, 0.996)
    draw_na(t, ('TC', 0.54, 0.348), ('MR', 1.3, 0.996))
    # Stroke 3: 竖 — apex-lifted head (TC, 0.368, 0.248) → BC (0.512, 1.3)
    draw_shu(t, ('TC', 0.368, 0.248), ('BC', 0.512, 1.3))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_个.png"))


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
