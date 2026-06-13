"""c35 横撇弯钩 (heng_pie_wan_gou): horizontal + pie + wan + hook.

Used in 阝 (left/right ear radical). Complex 4-segment compound:
1. Short horizontal heng going right.
2. Pie (撇) going down-left.
3. Wan curve continuing down then bending right.
4. Sharp hook curling up-left.

Five anchors: from, c1 (end of heng), c2 (bottom of pie / start of wan),
c3 (right-bottom of wan / start of hook), to (hook tip).
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


def w_pie(s):
    if s < 0.15: return 19.0 - (s / 0.15) * 4.0  # dunbi base
    return 15.0 - ((s - 0.15) / 0.85) * 3.0  # gentle taper to 12


def w_wan(s):
    if s < 0.10: return 12.0
    if s < 0.85: return 11.0
    return 11.0 + ((s - 0.85) / 0.15) * 4.0


def w_hook(s):
    return 15.0 - s * 12.0


def draw_heng_pie_wan_gou(t, fa, c1a, c2a, c3a, ta):
    p0 = anchor_to_xy(fa); p1 = anchor_to_xy(c1a)
    p2 = anchor_to_xy(c2a); p3 = anchor_to_xy(c3a)
    p4 = anchor_to_xy(ta)
    a1 = (p0[0] + (p1[0]-p0[0])*0.33, p0[1] + (p1[1]-p0[1])*0.33 + 4)
    a2 = (p0[0] + (p1[0]-p0[0])*0.67, p0[1] + (p1[1]-p0[1])*0.67 + 4)
    brushed_bezier(t, p0, a1, a2, p1, w_heng_to_dunbi, samples=140)
    # Pie: down-left, bezier with slight curve
    b1 = (p1[0] + (p2[0]-p1[0])*0.33, p1[1] + (p2[1]-p1[1])*0.33)
    b2 = (p1[0] + (p2[0]-p1[0])*0.67, p1[1] + (p2[1]-p1[1])*0.67)
    brushed_bezier(t, p1, b1, b2, p2, w_pie, samples=160)
    # Wan: curving from bottom of pie to right
    chord_dx = p3[0] - p2[0]; chord_dy = p3[1] - p2[1]
    c1 = (p2[0] + chord_dx*0.33 - 5, p2[1] + chord_dy*0.33 - 15)
    c2 = (p2[0] + chord_dx*0.67 + 10, p2[1] + chord_dy*0.67 - 5)
    brushed_bezier(t, p2, c1, c2, p3, w_wan, samples=160)
    # Hook up-left, tapered
    d1 = (p3[0] + (p4[0]-p3[0])*0.33, p3[1] + (p4[1]-p3[1])*0.33)
    d2 = (p3[0] + (p4[0]-p3[0])*0.67, p3[1] + (p4[1]-p3[1])*0.67)
    brushed_bezier(t, p3, d1, d2, p4, w_hook, samples=100)


def task_01(t, screen):
    reset(t)
    draw_heng_pie_wan_gou(t,
        ("TL", 0.5, 0.2),
        ("TC", 0.3, 0.2),
        ("BL", 0.95, 0.4),
        ("BC", 0.7, 0.8),
        ("BC", 0.3, 0.4))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_heng_pie_wan_gou.png"))


def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
