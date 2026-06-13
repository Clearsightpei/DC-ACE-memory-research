"""c34 横折弯 (heng_zhe_wan): ─┐╮ horizontal + corner-down + smooth right curve, NO hook.

Like 横折弯钩 minus the final hook. Bowl-bottom shape: 横 segment,
sharp corner-down (dunbi), descend, smooth curve bending right.

Four anchors: from, c1 (top corner), c2 (start of wan curve where
descender ends), to (end of wan going right).
"""
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


def w_heng_to_dunbi(s):
    if s < 0.10: return 14.0 - (s / 0.10) * 3.0
    if s < 0.80: return 11.0
    return 11.0 + ((s - 0.80) / 0.20) * 8.0


def w_zhe_wan(s):
    if s < 0.15: return 19.0 - (s / 0.15) * 6.0
    if s < 0.85: return 11.0
    return 11.0 + ((s - 0.85) / 0.15) * 4.0  # ends slightly thicker


def draw_heng_zhe_wan(t, fa, c1a, c2a, ta):
    p0 = anchor_to_xy(fa); p1 = anchor_to_xy(c1a)
    p2 = anchor_to_xy(c2a); p3 = anchor_to_xy(ta)
    a1 = (p0[0] + (p1[0]-p0[0])*0.33, p0[1] + (p1[1]-p0[1])*0.33 + 4)
    a2 = (p0[0] + (p1[0]-p0[0])*0.67, p0[1] + (p1[1]-p0[1])*0.67 + 4)
    brushed_bezier(t, p0, a1, a2, p1, w_heng_to_dunbi, samples=160)
    # Zhe straight down (no curve)
    b1 = (p1[0] + (p2[0]-p1[0])*0.33, p1[1] + (p2[1]-p1[1])*0.33)
    b2 = (p1[0] + (p2[0]-p1[0])*0.67, p1[1] + (p2[1]-p1[1])*0.67)
    brushed_bezier(t, p1, b1, b2, p2, w_zhe_wan, samples=140)
    # Wan curving right — bezier with control points offset DOWN to bulge bottom
    chord_dx = p3[0] - p2[0]; chord_dy = p3[1] - p2[1]
    c1 = (p2[0] + chord_dx*0.33 - 5, p2[1] + chord_dy*0.33 - 20)
    c2 = (p2[0] + chord_dx*0.67 + 5, p2[1] + chord_dy*0.67 - 15)
    brushed_bezier(t, p2, c1, c2, p3, w_zhe_wan, samples=160)


def task_01(t, screen):
    reset(t)
    draw_heng_zhe_wan(t,
        ("TL", 0.3, 0.3),
        ("TC", 0.7, 0.3),
        ("C",  0.7, 1.0),
        ("MR", 1.0, 0.7))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_heng_zhe_wan.png"))


def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
