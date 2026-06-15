"""Cycle 75 — 京 (jīng). 8 strokes: 亠 + 口-middle + 小.

BOX-RENDERING FIX: middle 口 uses aligned corners.
- TL corner ≡ shu head ≡ heng_zhe head
- TR corner ≡ heng_zhe corner
- BL corner ≡ shu tail ≡ bottom-heng head
- BR corner ≡ heng_zhe tail ≡ bottom-heng tail
Shu walls share x; heng tops/bottoms share y.
"""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy  # noqa
from dian import draw_dian
from heng import draw_heng
from shu import draw_shu
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
    # 亠 top
    draw_dian(t, ("TC", 0.4, 0.0), ("TC", 0.5, 0.3))  # top dot
    draw_heng(t, ("TL", 0.4, 0.4), ("TR", 0.6, 0.4))  # 亠 horizontal
    # Middle 口 box — ALIGNED corners
    # TL=(ML 0.9, 0.3), TR=(MR 0.1, 0.3), BL=(ML 0.9, 0.9), BR=(MR 0.1, 0.9)
    draw_shu(t, ("ML", 0.9, 0.3), ("ML", 0.9, 0.9))                   # left wall (same x)
    draw_heng_zhe(t, ("ML", 0.9, 0.3), ("MR", 0.1, 0.3), ("MR", 0.1, 0.9))  # top + right (same y top, same x right)
    draw_heng(t, ("ML", 0.9, 0.9), ("MR", 0.1, 0.9))                  # bottom (same y)
    # 小 bottom
    draw_shu(t, ("BC", 0.5, 0.0), ("BC", 0.5, 1.0))  # center vertical
    draw_pie(t, ("BL", 0.7, 0.3), ("BL", 0.3, 1.0))  # left pie
    draw_na(t, ("BR", 0.0, 0.3), ("BR", 0.5, 1.0))   # right na
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_京.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
