"""Cycle 75 — 京 (jīng). 8 strokes: 亠 + 口-middle + 小."""
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
    # s1: top dot
    draw_dian(t, ("TC", 0.224, 0.156), ("TC", 0.684, 0.492))
    # s2: long top heng (亠's heng)
    draw_heng(t, ("ML", -0.036, 0.028), ("TR", 1.124, 0.844))
    # s3: left side of middle 口 (heng_zhe stand-alone — top + left wall going down)
    draw_heng_zhe(t, ("ML", 0.724, 0.432), ("ML", 0.064, 0.432), ("BC", 0.064, 0.224))
    # s4: right vertical of middle box
    draw_shu(t, ("ML", 0.808, 0.408), ("C", 0.908, 0.884))
    # s5: bottom heng of middle box
    draw_heng(t, ("BC", 0.132, 0.144), ("BR", 0.128, 0.028))
    # s6: middle shu (vertical of 小)
    draw_shu(t, ("BC", 0.392, 0.148), ("BC", 0.036, 1.284))
    # s7: left pie of 小
    draw_pie(t, ("BL", 0.668, 0.484), ("BL", 0.276, 1.176))
    # s8: right na of 小
    draw_na(t, ("BR", 0.044, 0.484), ("BR", 0.74, 1.192))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_京.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
