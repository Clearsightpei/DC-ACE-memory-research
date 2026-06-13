"""c33 横斜钩 (heng_xie_gou): short horizontal + long slanted convex arc + small hook up-left.

Used in 风, 飞. Shape: ─ then a long diagonal curve going down-right
(slanted, convex bulging down), ending with a sharp hook curling up-left.

Four anchors: from (start of heng), c1 (end of heng / top of slant),
c2 (bottom of slant / start of hook), to (hook tip).

The slant is a curve, not a straight line. Bezier control points are
offset DOWN-LEFT from the chord to make the curve bulge that way.
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


def w_slant(s):
    if s < 0.15: return 19.0 - (s / 0.15) * 6.0
    if s < 0.85: return 11.0
    return 11.0 + ((s - 0.85) / 0.15) * 3.0


def w_hook(s):
    return 14.0 - s * 11.0  # taper to thin tip


def draw_heng_xie_gou(t, fa, c1a, c2a, ta):
    p0 = anchor_to_xy(fa); p1 = anchor_to_xy(c1a)
    p2 = anchor_to_xy(c2a); p3 = anchor_to_xy(ta)
    a1 = (p0[0] + (p1[0]-p0[0])*0.33, p0[1] + (p1[1]-p0[1])*0.33 + 4)
    a2 = (p0[0] + (p1[0]-p0[0])*0.67, p0[1] + (p1[1]-p0[1])*0.67 + 4)
    brushed_bezier(t, p0, a1, a2, p1, w_heng_to_dunbi, samples=160)
    # Slant curve bulging down-left (chord goes from c1 to c2 down-right)
    # Offset control points DOWN-LEFT of the chord midpoints for convex bow
    chord_dx = p2[0] - p1[0]; chord_dy = p2[1] - p1[1]
    b1 = (p1[0] + chord_dx*0.33 - 15, p1[1] + chord_dy*0.33 - 25)
    b2 = (p1[0] + chord_dx*0.67 - 8,  p1[1] + chord_dy*0.67 - 15)
    brushed_bezier(t, p1, b1, b2, p2, w_slant, samples=200)
    c1 = (p2[0] + (p3[0]-p2[0])*0.33, p2[1] + (p3[1]-p2[1])*0.33 + 8)
    c2 = (p2[0] + (p3[0]-p2[0])*0.67, p2[1] + (p3[1]-p2[1])*0.67 + 8)
    brushed_bezier(t, p2, c1, c2, p3, w_hook, samples=120)


def task_01(t, screen):
    reset(t)
    draw_heng_xie_gou(t,
        ("TL", 0.3, 0.3),
        ("TC", 0.6, 0.3),
        ("BR", 0.4, 0.4),
        ("BR", -0.1, -0.1))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_heng_xie_gou.png"))


def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
