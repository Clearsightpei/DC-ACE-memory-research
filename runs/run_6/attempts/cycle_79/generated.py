"""cycle_79 — 思 (sī, "think"). 9 MMH strokes: 田 (5) + 心 (4).

Anchors taken verbatim from task_briefs/cycle_79.md.
"""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from _anchor import anchor_to_xy  # noqa: F401  (used implicitly by primitives)
from shu import draw_shu
from heng_zhe import draw_heng_zhe
from heng import draw_heng
from shu_wan_gou import draw_shu_wan_gou
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

    # 田 (top component) — 5 strokes
    # s1: 竖 (left vertical of 田)
    draw_shu(t, ("TL", 0.364, 0.604), ("ML", 0.872, 0.972))
    # s2: 横折 (top + right vertical of 田)
    draw_heng_zhe(t, ("TL", 0.656, 0.66), ("TC", 0.976, 0.66), ("C", 0.976, 0.772))
    # s3: 横 (bottom edge of 田)
    draw_heng(t, ("C", 0.044, 0.26), ("C", 0.924, 0.144))
    # s4: 横 (interior short horizontal — left half)
    draw_heng(t, ("TC", 0.36, 0.668), ("C", 0.408, 0.672))
    # s5: 横 (interior short horizontal — right half)
    draw_heng(t, ("ML", 0.936, 0.896), ("C", 0.972, 0.704))

    # 心 (bottom component) — 4 strokes
    # s6: 竖弯钩 (the curving hook spine of 心)
    draw_shu_wan_gou(t, ("BL", 0.328, 0.344), ("BC", 0.076, 1.0), ("BL", 0.076, 1.104))
    # s7: 横 (left bottom inner — actually 卧钩's body region per brief)
    draw_heng(t, ("BL", 0.804, 0.452), ("BR", 0.316, 0.608))
    # s8: 点 (middle dot)
    draw_dian(t, ("BC", 0.372, 0.128), ("BC", 0.768, 0.464))
    # s9: 点 (right dot)
    draw_dian(t, ("MR", 0.524, 1.0), ("BR", 1.184, 0.46))

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_思.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
