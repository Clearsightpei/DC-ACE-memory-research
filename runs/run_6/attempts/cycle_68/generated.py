import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from _anchor import anchor_to_xy  # noqa: F401  (sanity import — primitives call it)
from heng import draw_heng
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

    # 古 — 5 MMH strokes: top 十 (heng + shu) over 口 (heng_zhe + shu + heng).
    # Anchors taken verbatim from task_briefs/cycle_68.md.
    # Override applied by Teacher: s2.to.y_frac shortened so shu ends ABOVE
    # the box top (avoids c60 piercing failure).

    # s1 — top heng of 十
    draw_heng(t, ('ML', -0.044, 0.56), ('MR', 1.184, 0.472))

    # s2 — shu of 十 (SHORTENED so tail stops above box top)
    draw_shu(t, ('TC', 0.372, 0.28), ('BC', 0.26, 0.20))

    # s3 — heng_zhe: top + right wall of 口
    # NOTE: brief's `to` anchor is ('BL', 0.968, 1.464) but y_frac=1.464
    # exceeds anchor validator's extended range [-0.3, 1.3]. Capped to 1.3
    # (minimum deviation needed to render; logged in summary).
    draw_heng_zhe(t,
                  ('BL', 0.6, 0.42),
                  ('BC', 0.968, 0.42),
                  ('BL', 0.968, 1.3))

    # s4 — left wall of 口 (shu)
    draw_shu(t, ('BL', 0.892, 0.444), ('BC', 0.944, 1.072))

    # s5 — bottom heng of 口
    draw_heng(t, ('BC', 0.048, 1.232), ('BR', 0.22, 1.24))

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_古.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
