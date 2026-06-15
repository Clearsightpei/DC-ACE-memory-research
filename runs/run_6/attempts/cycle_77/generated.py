"""Cycle 77 — 看 (kàn). 9 strokes: 手 + 目 (aligned-corner box)."""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy  # noqa
from pie import draw_pie
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
    # 手 top — long sweeping pie + 3 hengs (4 strokes total for 手 = pie + heng + heng + heng_gou; here use pie+3hengs simplified)
    draw_pie(t, ("TR", 0.7, 0.2), ("ML", 0.1, 1.0))                 # long pie
    draw_heng(t, ("TC", 0.2, 0.5), ("TR", 0.7, 0.5))                # 手 top short heng
    draw_heng(t, ("TL", 0.4, 1.0), ("TR", 0.6, 1.0))                # 手 middle heng (long)
    draw_heng(t, ("ML", 0.3, 0.3), ("MR", 0.7, 0.3))                # 手 lower heng
    # 目 box (aligned corners, WIDER) bottom
    # TL=(C 0.3, 0.5)=(-20, 0), TR=(C 0.7, 0.5)=(+20, 0)
    # BL=(BC 0.3, 1.0)=(-20, -150), BR=(BC 0.7, 1.0)=(+20, -150)
    draw_shu(t, ("C", 0.3, 0.5), ("BC", 0.3, 1.0))                  # left wall
    draw_heng_zhe(t, ("C", 0.3, 0.5), ("C", 0.7, 0.5), ("BC", 0.7, 1.0))  # top + right wall
    draw_heng(t, ("BC", 0.3, 0.3), ("BC", 0.7, 0.3))                # internal upper heng
    draw_heng(t, ("BC", 0.3, 0.65), ("BC", 0.7, 0.65))              # internal lower heng
    draw_heng(t, ("BC", 0.3, 1.0), ("BC", 0.7, 1.0))                # closing bottom
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_看.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
