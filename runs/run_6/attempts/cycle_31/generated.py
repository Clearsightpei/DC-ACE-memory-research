import io, os, sys, turtle
from PIL import Image
WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy
from heng import brushed_bezier


def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1); img.convert("RGBA").save(path, "PNG")


def reset(t):
    t.reset(); t.hideturtle(); t.speed(0); t.pencolor("black")
    t.penup(); t.goto(0, 0); t.setheading(0)


def w_heng_seg(s):
    if s < 0.10: return 14.0 - (s / 0.10) * 3.0
    if s < 0.85: return 11.0
    return 11.0 + ((s - 0.85) / 0.15) * 2.0


def w_zhe_seg(s):
    if s < 0.10: return 13.0
    if s < 0.85: return 11.0
    return 11.0 + ((s - 0.85) / 0.15) * 8.0  # ends at 19 — dunbi press


def w_ti_seg(s):
    if s < 0.15: return 19.0 - (s / 0.15) * 4.0  # starts thick at dunbi (19→15)
    return 15.0 - ((s - 0.15) / 0.85) * 12.0  # tapers to 3 tip


def draw_heng_zhe_ti(t, fa, c1a, c2a, ta):
    p0 = anchor_to_xy(fa)
    p1 = anchor_to_xy(c1a)
    p2 = anchor_to_xy(c2a)
    p3 = anchor_to_xy(ta)
    a1 = (p0[0] + (p1[0] - p0[0]) * 0.33, p0[1] + (p1[1] - p0[1]) * 0.33 + 4)
    a2 = (p0[0] + (p1[0] - p0[0]) * 0.67, p0[1] + (p1[1] - p0[1]) * 0.67 + 4)
    brushed_bezier(t, p0, a1, a2, p1, w_heng_seg, samples=160)
    b1 = (p1[0] + (p2[0] - p1[0]) * 0.33, p1[1] + (p2[1] - p1[1]) * 0.33)
    b2 = (p1[0] + (p2[0] - p1[0]) * 0.67, p1[1] + (p2[1] - p1[1]) * 0.67)
    brushed_bezier(t, p1, b1, b2, p2, w_zhe_seg, samples=160)
    c1 = (p2[0] + (p3[0] - p2[0]) * 0.33, p2[1] + (p3[1] - p2[1]) * 0.33)
    c2 = (p2[0] + (p3[0] - p2[0]) * 0.67, p2[1] + (p3[1] - p2[1]) * 0.67)
    brushed_bezier(t, p2, c1, c2, p3, w_ti_seg, samples=140)


def task_01(t, screen):
    reset(t)
    draw_heng_zhe_ti(t,
        ("TL", 0.3, 0.3),
        ("TC", 0.5, 0.3),
        ("C",  0.5, 0.9),
        ("TR", 0.9, 0.7))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_heng_zhe_ti.png"))


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
