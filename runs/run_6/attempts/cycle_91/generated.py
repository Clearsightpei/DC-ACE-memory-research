import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from _anchor import anchor_to_xy
from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
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
    # 新 — 13 strokes, anchors verbatim from cycle_91 brief
    # 1. 立 top 点
    draw_dian(t, ("TL", 0.696, 0.224), ("TC", 0.112, 0.528))
    # 2. 立 top 横
    draw_heng(t, ("TL", 0.288, 0.936), ("TC", 0.548, 0.764))
    # 3. 立 left 点
    draw_dian(t, ("ML", 0.388, 0.172), ("ML", 0.6, 0.444))
    # 4. 立 right 撇/点
    draw_pie(t, ("TC", 0.188, 0.98), ("ML", 0.984, 0.56))
    # 5. 立 middle 横
    draw_heng(t, ("ML", -0.24, 0.836), ("C", 0.492, 0.592))
    # 6. 立 bottom 横
    draw_heng(t, ("BL", 0.02, 0.316), ("BC", 0.484, 0.084))
    # 7. 木 top short 竖/撇
    draw_shu(t, ("ML", 0.76, 0.784), ("BL", 0.46, 0.964))
    # 8. 木 horizontal
    draw_heng(t, ("BL", 0.284, 0.536), ("BL", 0.108, 1.104))
    # 9. 木 long 横
    draw_heng(t, ("BL", 0.996, 0.44), ("BC", 0.328, 0.656))
    # 10. 木 撇
    draw_pie(t, ("TR", 0.52, 0.52), ("C", 0.972, 0.072))
    # 11. 木 vertical (long 竖)
    draw_shu(t, ("C", 0.692, 0.024), ("BC", 0.32, 1.264))
    # 12. 斤 top 横
    draw_heng(t, ("C", 0.964, 0.732), ("MR", 1.2, 0.532))
    # 13. 斤 vertical 竖
    draw_shu(t, ("MR", 0.404, 0.748), ("BR", 0.552, 1.3))

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_新.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
