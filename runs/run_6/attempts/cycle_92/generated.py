"""cycle_92 — 路 (lu), 13 strokes. Anchors from cycle_92_dataset.json."""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from _anchor import anchor_to_xy  # noqa: F401  (sanity import; primitives also import it)
from shu import draw_shu
from heng import draw_heng
from dian import draw_dian
from pie import draw_pie
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
    # 13 strokes for 路 from dataset anchors (one primitive call per MMH stroke).
    draw_shu(t, ('TL', 0.044, 0.732), ('ML', 0.284, 0.516))         # s1
    draw_heng(t, ('TL', 0.276, 0.752), ('ML', 0.8, 0.22))           # s2
    draw_shu(t, ('ML', 0.372, 0.444), ('C', 0.036, 0.32))           # s3
    draw_dian(t, ('ML', 0.504, 0.468), ('BL', 0.54, 0.536))         # s4
    draw_heng(t, ('ML', 0.748, 0.952), ('C', 0.132, 0.864))         # s5
    draw_pie(t, ('ML', -0.064, 0.904), ('BL', 0.104, 0.672))        # s6
    draw_dian(t, ('BL', -0.264, 0.868), ('BC', 0.064, 0.408))       # s7
    draw_pie(t, ('TC', 0.684, 0.26), ('C', 0.168, 0.588))           # s8
    draw_pie(t, ('TC', 0.736, 0.968), ('BL', 0.888, 0.796))         # s9
    draw_heng(t, ('C', 0.452, 0.372), ('MR', 1.3, 0.44))            # s10
    draw_shu(t, ('BC', 0.224, 0.664), ('BC', 0.5, 1.3))             # s11
    draw_heng_zhe(t, ('BC', 0.464, 0.684),
                  ('BR', 0.248, 0.684),
                  ('BR', 0.248, 1.18))                              # s12
    draw_heng(t, ('BC', 0.576, 1.3), ('BR', 0.504, 1.3))            # s13

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_路.png"))


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
