import io, os, sys, turtle
from PIL import Image
WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy
from heng import brushed_bezier, draw_heng
from shu import draw_shu

def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1); img.convert("RGBA").save(path, "PNG")

def reset(t):
    t.reset(); t.hideturtle(); t.speed(0); t.pencolor("black")
    t.penup(); t.goto(0,0); t.setheading(90)

def w_main(s):
    if s < 0.10: return 14.0 - (s/0.10)*3.0
    if s < 0.85: return 11.0
    return 11.0 + ((s-0.85)/0.15)*2.0

def w_drop(s):
    if s < 0.10: return 13.0
    if s < 0.85: return 11.0
    return 11.0 + ((s-0.85)/0.15)*7.0

def draw_heng_zhe(t, fa, ca, ta):
    p0 = anchor_to_xy(fa); pc = anchor_to_xy(ca); p3 = anchor_to_xy(ta)
    a1 = (p0[0] + (pc[0]-p0[0])*0.33, p0[1] + (pc[1]-p0[1])*0.33 + 4)
    a2 = (p0[0] + (pc[0]-p0[0])*0.67, p0[1] + (pc[1]-p0[1])*0.67 + 4)
    brushed_bezier(t, p0, a1, a2, pc, w_main, samples=180)
    b1 = (pc[0] + (p3[0]-pc[0])*0.33, pc[1] + (p3[1]-pc[1])*0.33)
    b2 = (pc[0] + (p3[0]-pc[0])*0.67, pc[1] + (p3[1]-pc[1])*0.67)
    brushed_bezier(t, pc, b1, b2, p3, w_drop, samples=180)

def task_01(t, screen):
    reset(t)
    draw_shu(t, ("TL", 0.37, 0.71), ("BL", 0.84, 0.94))
    draw_heng_zhe(t, ("ML", 0.67, 0.77), ("MR", 0.94, 0.42), ("BR", 0.6, 0.96))
    draw_heng(t, ("BL", 0.93, 0.19), ("BR", 0.93, 0.15))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_口.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
