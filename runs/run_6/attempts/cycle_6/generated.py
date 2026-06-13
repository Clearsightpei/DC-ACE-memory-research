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
    t.penup(); t.goto(0,0); t.setheading(90)

def w_shu_main(s):
    # vertical drop: 16 -> 11 -> 13 (press at corner)
    if s < 0.10: return 16.0 - (s/0.10) * 5.0
    if s < 0.85: return 11.0
    return 11.0 + ((s-0.85)/0.15) * 2.0

def w_hook(s):
    # hook taper: 13 -> 3
    return 13.0 - s * 10.0

def draw_shu_gou(t, from_anchor, corner_anchor, to_anchor):
    p0 = anchor_to_xy(from_anchor)
    pc = anchor_to_xy(corner_anchor)
    p3 = anchor_to_xy(to_anchor)
    # Segment A: head to corner (vertical drop)
    p1 = (p0[0] + (pc[0]-p0[0]) * 0.33, p0[1] + (pc[1]-p0[1]) * 0.33)
    p2 = (p0[0] + (pc[0]-p0[0]) * 0.67, p0[1] + (pc[1]-p0[1]) * 0.67)
    brushed_bezier(t, p0, p1, p2, pc, w_shu_main, samples=200)
    # Segment B: corner to tail (hook)
    # Tangential junction: control point near corner continues the inward direction
    p1b = (pc[0] + (p3[0]-pc[0]) * 0.5, pc[1] + (p3[1]-pc[1]) * 0.5 + 5)
    p2b = (pc[0] + (p3[0]-pc[0]) * 0.8, pc[1] + (p3[1]-pc[1]) * 0.8 + 3)
    brushed_bezier(t, pc, p1b, p2b, p3, w_hook, samples=80)

def task_01(t, screen):
    reset(t)
    draw_shu_gou(t, ("TC", 0.2, 0.37), ("BC", 0.4, 0.95), ("BL", 0.78, 1.17))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_亅.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
