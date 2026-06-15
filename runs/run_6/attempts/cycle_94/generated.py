"""cycle_94 — 楚 (chu), 13 MMH strokes.

Top forest 林: heng+shu+pie+dian on left tree, dian+pie+na on right tree.
Bottom 疋: shu, heng, shu, heng, pie, na.

All positions derived from anchor_to_xy(...). Override: y_clamp — some
y_fracs exceed 1.0 (s10=1.112, s12/s13=1.3) which _anchor.py admits via
its extended [-0.3, 1.3] range.
"""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from _anchor import anchor_to_xy  # noqa: F401  (sanity import)
from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
from dian import draw_dian
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
    # Stroke 1: heng (left tree's 横)
    draw_heng(t, ('ML', 0.3, 0.128), ('TC', 0.388, 0.96))
    # Stroke 2: shu (left tree's 竖)
    draw_shu(t, ('TL', 0.852, 0.32), ('ML', 0.976, 0.944))
    # Stroke 3: pie (left tree's 撇)
    draw_pie(t, ('ML', 0.884, 0.164), ('BL', 0.136, 0.024))
    # Stroke 4: dian (left tree's 点)
    draw_dian(t, ('C', 0.06, 0.328), ('C', 0.268, 0.548))
    # Stroke 5: dian (right tree's 点 — top-left of right 木)
    draw_dian(t, ('TC', 0.552, 0.936), ('TR', 0.728, 0.768))
    # Stroke 6: pie (right tree's 撇)
    draw_pie(t, ('TC', 0.984, 0.188), ('MR', 0.092, 0.708))
    # Stroke 7: na (right tree's 捺)
    draw_na(t, ('MR', 0.008, 0.016), ('C', 0.352, 0.708))
    # Stroke 8: shu (top of 疋 — short vertical)
    draw_shu(t, ('MR', 0.212, 0.112), ('MR', 0.712, 0.548))
    # Stroke 9: heng (横 of 疋)
    draw_heng(t, ('BL', 0.632, 0.152), ('BR', 0.004, 0.344))
    # Stroke 10: shu (竖 dropping down)
    draw_shu(t, ('BC', 0.376, 0.128), ('BC', 0.584, 1.112))
    # Stroke 11: heng (lower short 横)
    draw_heng(t, ('BC', 0.636, 0.704), ('BR', 0.18, 0.616))
    # Stroke 12: pie (下 撇)
    draw_pie(t, ('BL', 0.844, 0.492), ('BL', 0.168, 1.3))
    # Stroke 13: na (bottom 捺)
    draw_na(t, ('BL', 0.956, 0.9), ('BR', 1.072, 1.3))

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_楚.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
