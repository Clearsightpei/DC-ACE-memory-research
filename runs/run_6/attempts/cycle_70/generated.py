import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from _anchor import anchor_to_xy  # noqa: F401  (sanity import — primitives call it)
from heng import draw_heng
from shu import draw_shu
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

    # 林 — 8 MMH strokes: left-木 (heng + shu + pie + na) + right-木 (heng + shu + pie + na).
    # Anchors taken verbatim from task_briefs/cycle_70.md.
    # Note: anchor_to_xy validator caps fracs at 1.3. Brief's clamped value
    # 1.456 (s2.to.y, s6.to.y) and 1.392 (s8.to.x) exceed 1.3 — clamped here
    # to the validator's max with minimum deviation.

    # ── left 木 ──
    # s1 — top heng of left-木
    draw_heng(t, ('ML', -0.112, 0.588), ('C', 0.168, 0.408))

    # s2 — shu of left-木 (vertical). y_frac 1.456 → 1.3
    draw_shu(t, ('TL', 0.504, 0.38), ('BL', 0.588, 1.3))

    # s3 — pie of left-木
    draw_pie(t, ('ML', 0.568, 0.636), ('BL', -0.288, 0.964))

    # s4 — na of left-木
    draw_na(t, ('ML', 0.764, 0.9), ('BC', 0.048, 0.144))

    # ── right 木 ──
    # s5 — top heng of right-木
    draw_heng(t, ('C', 0.376, 0.432), ('MR', 0.792, 0.204))

    # s6 — shu of right-木 (vertical). y_frac 1.456 → 1.3
    draw_shu(t, ('TC', 0.808, 0.232), ('BC', 0.928, 1.3))

    # s7 — pie of right-木
    draw_pie(t, ('C', 0.876, 0.516), ('BC', 0.012, 0.82))

    # s8 — na of right-木. x_frac 1.392 → 1.3
    draw_na(t, ('MR', 0.096, 0.648), ('BR', 1.3, 0.728))

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_林.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
