import io, os, math, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))


def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1)
    img.convert("RGBA").save(path, "PNG")


def reset_turtle(t):
    t.reset(); t.hideturtle(); t.speed(0)
    t.pencolor("black"); t.pensize(3)
    t.penup(); t.goto(0, 0); t.setheading(90)


# ---- brush helpers ----------------------------------------------------------
# A brush stroke = a centerline traced as a sequence of points, with the
# pensize varied point-to-point to give taper / weight / 顿笔 (pause-press).
# We over-draw each segment with a round cap so width transitions are smooth.

def _round(t):
    t.pensize  # noop; turtle caps are round-ish at large sizes

def brush_path(t, pts, widths):
    """pts: list of (x,y) centerline. widths: matching pensize per point.
    Draws filled round dots at each point + connecting segments so the
    stroke reads as a continuous swelling/tapering brush mark."""
    t.penup()
    t.goto(pts[0])
    t.setheading(0)
    # stamp a blob at every point for smooth taper
    for (x, y), w in zip(pts, widths):
        t.penup(); t.goto(x, y)
        t.dot(max(1.0, w))
    # connect consecutive points with a segment at the average width
    for i in range(len(pts) - 1):
        w = max(1.0, (widths[i] + widths[i + 1]) / 2.0)
        t.pensize(w)
        t.penup(); t.goto(pts[i])
        t.pendown(); t.goto(pts[i + 1])
        t.penup()


def lerp(a, b, s):
    return a + (b - a) * s


def bezier(p0, p1, p2, p3, n):
    out = []
    for i in range(n + 1):
        s = i / n
        u = 1 - s
        x = (u**3) * p0[0] + 3 * (u**2) * s * p1[0] + 3 * u * (s**2) * p2[0] + (s**3) * p3[0]
        y = (u**3) * p0[1] + 3 * (u**2) * s * p1[1] + 3 * u * (s**2) * p2[1] + (s**3) * p3[1]
        out.append((x, y))
    return out


def width_profile(n, w_start, w_mid, w_end, mid=0.5):
    """thin->thick->thin style profile across n+1 points."""
    ws = []
    for i in range(n + 1):
        s = i / n
        if s <= mid:
            ws.append(lerp(w_start, w_mid, s / mid))
        else:
            ws.append(lerp(w_mid, w_end, (s - mid) / (1 - mid)))
    return ws


# ── Task 01 | 点 | dian
def task_01(t):
    # small pressed tear-drop: light tip top, swelling press to lower-right,
    # ending in a weighted 顿笔. Short, never a thin line.
    p0 = (-20, 70)
    p1 = (0, 50)
    p2 = (15, 25)
    p3 = (35, 5)
    pts = bezier(p0, p1, p2, p3, 22)
    ws = width_profile(22, 6, 26, 34, mid=0.45)  # grows, heavy 顿笔 at tail
    brush_path(t, pts, ws)
    # extra press blob at the end (顿笔)
    t.penup(); t.goto(p3); t.dot(36)


# ── Task 02 | 横 | heng
def task_02(t):
    # left->right, slight upward tilt. Weighted entry (起笔顿),
    # thinner middle, strong 顿笔 press at the right end.
    p0 = (-180, -10)
    p1 = (-60, 6)
    p2 = (60, 12)
    p3 = (185, 22)
    pts = bezier(p0, p1, p2, p3, 40)
    ws = []
    n = 40
    for i in range(n + 1):
        s = i / n
        if s < 0.10:                      # 起笔: weighted entry
            ws.append(lerp(24, 12, s / 0.10))
        elif s < 0.82:                    # body: lean, slight swell
            ws.append(lerp(12, 15, (s - 0.10) / 0.72))
        else:                             # 收笔: press down 顿笔
            ws.append(lerp(15, 30, (s - 0.82) / 0.18))
    brush_path(t, pts, ws)
    t.penup(); t.goto(p3); t.dot(32)      # final 顿笔
    t.penup(); t.goto(p0); t.dot(26)      # entry weight


# ── Task 03 | 竖 | shu
def task_03(t):
    # top->bottom strong straight spine. Weighted entry, firm body,
    # slight 顿笔 then a controlled finish (here a 垂露 round end).
    p0 = (0, 150)
    p1 = (3, 60)
    p2 = (-2, -40)
    p3 = (1, -150)
    pts = bezier(p0, p1, p2, p3, 40)
    ws = []
    n = 40
    for i in range(n + 1):
        s = i / n
        if s < 0.12:                      # 起笔顿: heavy top
            ws.append(lerp(30, 16, s / 0.12))
        elif s < 0.85:                    # straight spine, mild taper
            ws.append(lerp(16, 14, (s - 0.12) / 0.73))
        else:                             # 垂露: small press / round drop
            ws.append(lerp(14, 26, (s - 0.85) / 0.15))
    brush_path(t, pts, ws)
    t.penup(); t.goto(p0); t.dot(30)      # weighted entry
    t.penup(); t.goto(p3); t.dot(26)      # 垂露 round end


# ── Task 04 | 撇 | pie
def task_04(t):
    # upper-right -> lower-left, curving, tapering to a fine sharp point.
    p0 = (90, 150)
    p1 = (50, 80)
    p2 = (-30, 0)
    p3 = (-120, -120)
    pts = bezier(p0, p1, p2, p3, 44)
    ws = []
    n = 44
    for i in range(n + 1):
        s = i / n
        if s < 0.12:                      # weighted 起笔
            ws.append(lerp(28, 20, s / 0.12))
        else:                             # long taper to a fine point
            ws.append(lerp(20, 1.5, (s - 0.12) / 0.88))
    brush_path(t, pts, ws)
    t.penup(); t.goto(p0); t.dot(30)      # entry weight / 顿笔


# ── Task 05 | 捺 | na
def task_05(t):
    # upper-left -> lower-right, broadening, then a flattened pressed tail.
    p0 = (-110, 140)
    p1 = (-50, 70)
    p2 = (20, -5)
    p3 = (95, -70)
    pts = bezier(p0, p1, p2, p3, 38)
    ws = []
    n = 38
    for i in range(n + 1):
        s = i / n
        ws.append(lerp(6, 30, s))         # thin start -> broadening belly
    brush_path(t, pts, ws)
    # flattened pressed tail (捺脚): a short horizontal sweep that thins out
    tail = bezier((95, -70), (118, -72), (140, -70), (170, -66), 18)
    tw = []
    for i in range(19):
        s = i / 18
        tw.append(lerp(30, 2, s))         # press then sharpen out flat
    brush_path(t, tail, tw)
    t.penup(); t.goto(95, -70); t.dot(34)  # press point before the flick


# ── Task 06 | 提 | ti
def task_06(t):
    # lower-left -> upper-right, weighted press start, rising and
    # flicking out to a sharp fine point.
    p0 = (-110, -110)
    p1 = (-55, -55)
    p2 = (10, 0)
    p3 = (120, 90)
    pts = bezier(p0, p1, p2, p3, 40)
    ws = []
    n = 40
    for i in range(n + 1):
        s = i / n
        if s < 0.15:                      # heavy 起笔顿 (pressed start)
            ws.append(lerp(30, 22, s / 0.15))
        else:                             # rise then flick to sharp point
            ws.append(lerp(22, 1.5, (s - 0.15) / 0.85))
    brush_path(t, pts, ws)
    t.penup(); t.goto(p0); t.dot(32)      # pressed entry 顿笔


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT); screen.bgcolor("white")
    screen.tracer(0, 0)
    t = turtle.Turtle()
    for idx, (key, fn) in enumerate([
        ("dian", task_01), ("heng", task_02), ("shu", task_03),
        ("pie", task_04), ("na", task_05), ("ti", task_06),
    ], start=1):
        reset_turtle(t)
        fn(t)
        screen.update()
        save_canvas_to_png(screen, os.path.join(OUT_DIR, f"{idx:02d}_{key}.png"))


if __name__ == "__main__":
    main()
