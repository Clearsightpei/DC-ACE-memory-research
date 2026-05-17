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
    t.reset()
    t.hideturtle()
    t.speed(0)
    t.pencolor("black")
    t.pensize(3)
    t.penup()
    t.goto(0, 0)
    t.setheading(90)


def _filled_segment(t, pts):
    """Draw a filled polygon from a centerline-with-width point list.
    pts is a list of (x, y) outline points already ordered around the shape."""
    t.penup()
    t.goto(pts[0])
    t.pendown()
    t.begin_fill()
    for p in pts[1:]:
        t.goto(p)
    t.goto(pts[0])
    t.end_fill()
    t.penup()


def _tapered_stroke(t, spine, widths):
    """spine: list of (x,y) centerline points. widths: half-width at each point.
    Builds a tapered filled shape (one side then back along the other)."""
    n = len(spine)
    left = []
    right = []
    for i in range(n):
        x, y = spine[i]
        if i == 0:
            dx = spine[1][0] - spine[0][0]
            dy = spine[1][1] - spine[0][1]
        elif i == n - 1:
            dx = spine[-1][0] - spine[-2][0]
            dy = spine[-1][1] - spine[-2][1]
        else:
            dx = spine[i + 1][0] - spine[i - 1][0]
            dy = spine[i + 1][1] - spine[i - 1][1]
        L = math.hypot(dx, dy) or 1.0
        # unit normal
        nx, ny = -dy / L, dx / L
        w = widths[i]
        left.append((x + nx * w, y + ny * w))
        right.append((x - nx * w, y - ny * w))
    outline = left + right[::-1]
    _filled_segment(t, outline)


# ── Task 01 | 点 | dian
def task_01(t):
    # A small pressed tear-drop dot: thin at top, swelling to a rounded
    # belly at lower-right. Tiny — the smallest stroke.
    spine = [
        (-8, 40),
        (0, 28),
        (8, 14),
        (14, 2),
    ]
    widths = [2.0, 6.0, 9.0, 5.0]
    _tapered_stroke(t, spine, widths)
    # round the belly
    t.penup()
    t.goto(8, 2)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    t.circle(7)
    t.end_fill()
    t.penup()


# ── Task 02 | 横 | heng
def task_02(t):
    # Horizontal, left to right, faint upward tilt. Slight 顿笔 (pressed
    # entry and a heavier pause at the right end).
    spine = [
        (-220, -8),
        (-110, 2),
        (0, 8),
        (110, 14),
        (210, 18),
    ]
    widths = [7.0, 5.0, 4.5, 5.0, 4.0]
    _tapered_stroke(t, spine, widths)
    # entry dab (顿笔) on the left
    t.penup()
    t.goto(-220, -8)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    t.circle(7)
    t.end_fill()
    # closing pause weight on the right
    t.penup()
    t.goto(210, 14)
    t.pendown()
    t.begin_fill()
    t.circle(8)
    t.end_fill()
    t.penup()


# ── Task 03 | 竖 | shu
def task_03(t):
    # Straight vertical, top to bottom, no curve. Slight taper, with a
    # pressed entry at the top (顿笔).
    spine = [
        (0, 230),
        (0, 110),
        (0, -10),
        (0, -130),
        (0, -240),
    ]
    widths = [6.0, 5.5, 5.0, 4.5, 3.5]
    _tapered_stroke(t, spine, widths)
    # entry dab at top
    t.penup()
    t.goto(0, 222)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    t.circle(7)
    t.end_fill()
    t.penup()


# ── Task 04 | 撇 | pie
def task_04(t):
    # Sweeps from upper-right down to lower-left, curving gently and
    # tapering to a fine point at the bottom-left. Pressed start.
    spine = [
        (170, 230),
        (130, 150),
        (80, 70),
        (10, -20),
        (-90, -120),
        (-190, -210),
    ]
    widths = [8.0, 7.0, 6.0, 4.5, 2.5, 0.6]
    _tapered_stroke(t, spine, widths)
    # pressed entry head
    t.penup()
    t.goto(170, 222)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    t.circle(8)
    t.end_fill()
    t.penup()


# ── Task 05 | 捺 | na
def task_05(t):
    # From upper-left falling down to lower-right; thin at the start,
    # broadening through the body, then flattening into a long
    # outstretched tail.
    spine = [
        (-190, 220),
        (-130, 140),
        (-70, 50),
        (-10, -40),
        (60, -110),
        (140, -150),
        (220, -160),
    ]
    widths = [2.0, 4.0, 6.5, 9.0, 10.0, 6.0, 1.0]
    _tapered_stroke(t, spine, widths)
    # flattened tail tip
    t.penup()
    t.goto(220, -160)
    t.pendown()
    t.begin_fill()
    t.goto(180, -150)
    t.goto(160, -158)
    t.goto(220, -163)
    t.goto(220, -160)
    t.end_fill()
    t.penup()


# ── Task 06 | 提 | ti
def task_06(t):
    # Short stroke flicking upward from lower-left to upper-right,
    # rising as it goes; thick pressed start, tapering to a sharp point.
    spine = [
        (-150, -120),
        (-90, -70),
        (-20, -10),
        (60, 60),
        (160, 150),
    ]
    widths = [9.0, 7.0, 5.0, 3.0, 0.6]
    _tapered_stroke(t, spine, widths)
    # pressed start head
    t.penup()
    t.goto(-150, -120)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    t.circle(8)
    t.end_fill()
    t.penup()


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0, 0)
    t = turtle.Turtle()
    for idx, (key, fn) in enumerate([
        ("dian", task_01),
        ("heng", task_02),
        ("shu",  task_03),
        ("pie",  task_04),
        ("na",   task_05),
        ("ti",   task_06),
    ], start=1):
        reset_turtle(t)
        fn(t)
        screen.update()
        save_canvas_to_png(screen, os.path.join(OUT_DIR, f"{idx:02d}_{key}.png"))


if __name__ == "__main__":
    main()
