"""
Cycle 15 — Drawer attempts.
6 tasks: 也, 巴, 见, 天, 了, 小.
Brushed Bézier with per-sample pensize; 顿笔 at corners; hooks as short
tail-arms. 800x600 white canvas. Each task at (0,0) heading 90°.
"""

import io
import os
import turtle
from PIL import Image

# ---------------------------------------------------------------------------
# Canvas setup
# ---------------------------------------------------------------------------

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
CANVAS_W, CANVAS_H = 800, 600

screen = turtle.Screen()
screen.setup(CANVAS_W, CANVAS_H)
screen.bgcolor("white")
screen.tracer(0, 0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.color("black")


# ---------------------------------------------------------------------------
# Bézier brush primitives
# ---------------------------------------------------------------------------

def bezier(p0, p1, p2, p3, n=160):
    """Cubic Bézier sampled n+1 points."""
    pts = []
    for i in range(n + 1):
        u = i / n
        x = (1 - u) ** 3 * p0[0] + 3 * (1 - u) ** 2 * u * p1[0] \
            + 3 * (1 - u) * u ** 2 * p2[0] + u ** 3 * p3[0]
        y = (1 - u) ** 3 * p0[1] + 3 * (1 - u) ** 2 * u * p1[1] \
            + 3 * (1 - u) * u ** 2 * p2[1] + u ** 3 * p3[1]
        pts.append((x, y))
    return pts


def width_profile(i, n, w_start, w_mid, w_end):
    """Triangular profile with mid as peak; floor at 50% of peak."""
    u = i / n
    if u < 0.5:
        w = w_start + (w_mid - w_start) * (u / 0.5)
    else:
        w = w_mid + (w_end - w_mid) * ((u - 0.5) / 0.5)
    floor = 0.5 * max(w_start, w_mid, w_end)
    return max(w, floor)


def stamp_dot(x, y, r):
    """Round dot via filled circle."""
    t.penup()
    t.goto(x, y - r)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.penup()


def brush_curve(pts, w_start, w_mid, w_end):
    """Stroke a Bézier sample list with per-sample pensize; round caps via dots."""
    n = len(pts) - 1
    if n <= 0:
        return
    # round cap at start
    stamp_dot(pts[0][0], pts[0][1], w_start / 2.0)
    t.penup()
    t.goto(pts[0])
    t.pendown()
    for i in range(1, n + 1):
        w = width_profile(i, n, w_start, w_mid, w_end)
        t.pensize(max(1, w))
        t.goto(pts[i])
    t.penup()
    # round cap at end
    stamp_dot(pts[-1][0], pts[-1][1], w_end / 2.0)


def brush_bez(p0, p1, p2, p3, w_start, w_mid, w_end, n=160):
    pts = bezier(p0, p1, p2, p3, n)
    brush_curve(pts, w_start, w_mid, w_end)


def diandun(x, y, r=8):
    """顿笔 lump: small filled circle to thicken a corner."""
    stamp_dot(x, y, r)


# ---------------------------------------------------------------------------
# Stroke primitives — atomic & compound
# ---------------------------------------------------------------------------

def heng(x0, y0, x1, y1, w=14):
    """Horizontal-ish stroke, heavy at both ends."""
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    brush_bez((x0, y0), (x0 * 0.7 + mx * 0.3, y0 * 0.7 + my * 0.3 - 2),
              (x1 * 0.7 + mx * 0.3, y1 * 0.7 + my * 0.3 - 2), (x1, y1),
              w, w * 0.75, w)


def shu(x0, y0, x1, y1, w=14):
    """Vertical-ish stroke, heavy both ends."""
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    brush_bez((x0, y0), (mx, y0 * 0.7 + my * 0.3),
              (mx, y1 * 0.7 + my * 0.3), (x1, y1),
              w, w * 0.75, w)


def pie(x0, y0, x1, y1, w_start=18, w_end=4):
    """撇: heavy → fine, curves outward."""
    # control: slight bow to the right-of-line
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    # perpendicular offset for bow
    dx, dy = x1 - x0, y1 - y0
    nx, ny = -dy, dx
    norm = (nx * nx + ny * ny) ** 0.5 or 1
    nx, ny = nx / norm, ny / norm
    bow = 30
    c1 = (x0 + dx * 0.33 + nx * bow * 0.4, y0 + dy * 0.33 + ny * bow * 0.4)
    c2 = (x0 + dx * 0.66 + nx * bow * 0.8, y0 + dy * 0.66 + ny * bow * 0.8)
    brush_bez((x0, y0), c1, c2, (x1, y1), w_start, (w_start + w_end) / 2, w_end)


def na(x0, y0, x1, y1, w_start=4, w_end=18):
    """捺: fine → heavy with flat kick at end."""
    dx, dy = x1 - x0, y1 - y0
    c1 = (x0 + dx * 0.33, y0 + dy * 0.33)
    c2 = (x0 + dx * 0.66, y0 + dy * 0.66 + 6)
    brush_bez((x0, y0), c1, c2, (x1, y1), w_start, (w_start + w_end) / 2, w_end)
    # flat tail kick (horizontal flick)
    tail_len = 26
    brush_bez((x1, y1), (x1 + tail_len * 0.4, y1 - 1),
              (x1 + tail_len * 0.7, y1 - 2), (x1 + tail_len, y1 - 3),
              w_end, w_end * 0.7, 3)


def dian(x_head, y_head, x_tail, y_tail, w_belly=16, w_tail=3):
    """点: belly heavy → tail fine; head is the upper end."""
    dx, dy = x_tail - x_head, y_tail - y_head
    c1 = (x_head + dx * 0.4, y_head + dy * 0.4)
    c2 = (x_head + dx * 0.75, y_head + dy * 0.75)
    brush_bez((x_head, y_head), c1, c2, (x_tail, y_tail),
              w_belly * 0.6, w_belly, w_tail)


# Compound strokes -----------------------------------------------------------

def heng_zhe(x0, y0, x_corner, y_corner, x1, y1, w=14):
    """横折: heng then drop. Corner has 顿笔."""
    heng(x0, y0, x_corner, y_corner, w)
    diandun(x_corner, y_corner, w * 0.6)
    shu(x_corner, y_corner, x1, y1, w)


def heng_zhe_gou(x0, y0, x_corner, y_corner, x1, y1, w=14, hook=18):
    """横折钩: 横折 with hook tail at the bottom pointing up-left."""
    heng_zhe(x0, y0, x_corner, y_corner, x1, y1, w)
    # hook arm
    brush_bez((x1, y1), (x1 - hook * 0.3, y1 + hook * 0.3),
              (x1 - hook * 0.6, y1 + hook * 0.7), (x1 - hook, y1 + hook),
              w, w * 0.6, 3)
    diandun(x1, y1, w * 0.55)


def shu_gou(x0, y0, x1, y1, w=14, hook=22):
    """竖钩: 竖 with hook tail at bottom pointing up-left."""
    shu(x0, y0, x1, y1, w)
    brush_bez((x1, y1), (x1 - hook * 0.3, y1 + hook * 0.3),
              (x1 - hook * 0.6, y1 + hook * 0.7), (x1 - hook, y1 + hook),
              w, w * 0.6, 3)
    diandun(x1, y1, w * 0.55)


def shu_wan_gou(x_top, y_top, x_corner, y_corner, x_right, y_right,
                w=14, hook=20):
    """
    竖弯钩: starts at top, drops down (shu), curves right at the bottom (wan),
    ends at the right with hook UP.
    """
    # vertical segment
    shu(x_top, y_top, x_corner + 4, y_corner + 8, w)
    # curving bend bottom-left → bottom-right
    brush_bez((x_corner + 4, y_corner + 8), (x_corner, y_corner),
              ((x_corner + x_right) / 2, y_corner - 2),
              (x_right, y_right), w, w * 0.75, w)
    # hook up
    brush_bez((x_right, y_right), (x_right + 2, y_right + hook * 0.35),
              (x_right - 2, y_right + hook * 0.7),
              (x_right - 6, y_right + hook), w, w * 0.6, 3)
    diandun(x_corner + 2, y_corner + 4, w * 0.6)
    diandun(x_right, y_right, w * 0.55)


# ---------------------------------------------------------------------------
# Save helper
# ---------------------------------------------------------------------------

def save_png(filename):
    screen.update()
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color",
                           width=CANVAS_W, height=CANVAS_H,
                           pagewidth=CANVAS_W, pageheight=CANVAS_H)
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img = img.convert("RGB")
    if img.size != (CANVAS_W, CANVAS_H):
        img = img.resize((CANVAS_W, CANVAS_H), Image.LANCZOS)
    img.save(os.path.join(OUT_DIR, filename))


def reset_for_next():
    t.reset()
    t.hideturtle()
    t.speed(0)
    t.color("black")
    t.penup()
    t.goto(0, 0)
    t.setheading(90)


# ---------------------------------------------------------------------------
# Task 01 — 也 (yě)
# ---------------------------------------------------------------------------
# Re-think: 竖弯钩 is the DOMINANT frame sweeping upper→down→right→hook-up.
# 横折钩 sits in the upper-left corner of that area. Middle shu drops
# inside. Tighter bounding box; strokes overlap into one body.

def task_01_ye():
    # ── Task 01 | 也 | yě
    # 1) 横折钩 in upper-left: short heng from x=-130 to x=-30 at y=80,
    #    then drop down to y=-50, hook up-left.
    heng_zhe_gou(-130, 80, -30, 80, -30, -50, w=14, hook=18)
    diandun(-130, 80, 7)
    diandun(-30, 80, 7)

    # 2) Middle shu drops inside the frame, from y=70 down to y=-30.
    shu(20, 70, 20, -30, w=12)

    # 3) 竖弯钩 as the dominant frame: starts upper-left area (x=-150,y=110)
    #    sweeps down, curves right along bottom, hook UP at right end.
    #    Tighter overlap with the upper strokes.
    shu_wan_gou(-150, 110, -150, -90, 150, -90, w=15, hook=22)


# ---------------------------------------------------------------------------
# Task 02 — 巴 (bā)
# ---------------------------------------------------------------------------
# Squarer aspect ratio: frame width ≈ total height. Break verticality.

def task_02_ba():
    # ── Task 02 | 巴 | bā
    # Frame is roughly square: width ~200, total height ~200 (-100..+100).
    # Top: 横折 — heng across the top, drop on the right.
    heng_zhe(-100, 100, 100, 100, 100, -20, w=14)
    diandun(-100, 100, 7)
    diandun(100, 100, 7)

    # Left vertical (竖) closing left side.
    shu(-100, 100, -100, -100, w=14)

    # Middle horizontal divider inside the frame.
    heng(-100, 20, 80, 20, w=13)

    # Bottom 竖弯钩 closes the square: drops from left-bottom corner of
    # upper frame, sweeps right, hook up.
    shu_wan_gou(-100, -100, -100, -100, 130, -100, w=15, hook=22)


# ---------------------------------------------------------------------------
# Task 03 — 见 (jiàn)
# ---------------------------------------------------------------------------
# Smaller closed top frame; shorter 撇 leg down-LEFT (~80-100px);
# 竖弯钩 = right edge of frame extended downward.

def task_03_jian():
    # ── Task 03 | 见 | jiàn
    # Top frame: smaller, clearly closed. width ~160 (-80..+80), height ~140.
    # Top heng + right drop (横折).
    heng_zhe(-80, 100, 80, 100, 80, -40, w=14)
    diandun(-80, 100, 7)
    diandun(80, 100, 7)

    # Left vertical of frame.
    shu(-80, 100, -80, -40, w=13)

    # Middle horizontal (inside the small frame).
    heng(-80, 20, 80, 20, w=12)

    # Bottom horizontal closing the frame.
    heng(-80, -40, 80, -40, w=13)

    # 撇 leg: starts at bottom-left of frame, sweeps DOWN-LEFT, length ~95.
    pie(-80, -40, -150, -120, w_start=14, w_end=4)

    # 竖弯钩: right edge of frame extended downward, then bend right with hook up.
    shu_wan_gou(80, -40, 80, -110, 160, -110, w=14, hook=20)


# ---------------------------------------------------------------------------
# Task 04 — 天 (tiān)
# ---------------------------------------------------------------------------
# Straighter 捺 (less curve), strong horizontal flat-tail kick at bottom-right.

def task_04_tian():
    # ── Task 04 | 天 | tiān
    # Top short heng.
    heng(-90, 110, 90, 110, w=14)
    diandun(-90, 110, 7)
    diandun(90, 110, 7)

    # Second (longer) heng below.
    heng(-130, 40, 130, 40, w=15)
    diandun(-130, 40, 7)
    diandun(130, 40, 7)

    # 撇 from apex (just below second heng) down-left.
    pie(0, 35, -150, -130, w_start=18, w_end=4)

    # 捺: straighter diagonal from apex down-right, ends with flat tail kick.
    # Use a near-linear Bézier (small bow).
    p0 = (0, 35)
    p1 = (60, -25)
    p2 = (130, -95)
    p3 = (170, -130)
    brush_bez(p0, p1, p2, p3, 5, 12, 20)
    # strong horizontal flat-tail kick at bottom-right
    brush_bez((170, -130), (200, -132), (225, -134), (250, -136), 20, 14, 4)


# ---------------------------------------------------------------------------
# Task 05 — 了 (le)
# ---------------------------------------------------------------------------
# Bottom stroke clearly CURVED — sweeps RIGHT then hooks LEFT at bottom
# (NOT a straight vertical-with-hook like 丁).

def task_05_le():
    # ── Task 05 | 了 | le
    # 1) Top 横撇: short heng then turn into a 撇 going down-left.
    heng(-110, 110, 80, 110, w=14)
    diandun(-110, 110, 7)
    diandun(80, 110, 8)
    # 撇 from the right corner sweeping down-left.
    pie(80, 110, -10, 30, w_start=16, w_end=4)

    # 2) Curved bottom stroke (弯钩): from upper center, sweeping out RIGHT,
    #    then curving DOWN and back LEFT, ending with hook to the upper-left.
    #    This is the key shape that distinguishes 了 from 丁.
    p0 = (0, 60)
    p1 = (60, 20)      # bows right
    p2 = (40, -80)     # curves down
    p3 = (-20, -130)   # ends down-left
    brush_bez(p0, p1, p2, p3, 14, 12, 14)
    # hook up-left at the tail
    brush_bez((-20, -130), (-40, -120), (-55, -110), (-70, -100), 14, 9, 3)
    diandun(-20, -130, 8)


# ---------------------------------------------------------------------------
# Task 06 — 小 (xiǎo)
# ---------------------------------------------------------------------------
# Center 竖钩 + left 点 + right 点 (mirror).

def task_06_xiao():
    # ── Task 06 | 小 | xiǎo
    # 1) center 竖钩: vertical through middle, small hook at bottom-left.
    shu_gou(0, 110, 0, -110, w=14, hook=22)

    # 2) left 点: tilted, head upper-LEFT, tail toward center.
    #    head at (-75, 70), tail at (-25, 20).
    dian(-75, 70, -25, 20, w_belly=15, w_tail=3)

    # 3) right 点: mirror — head upper-RIGHT, tail toward center.
    #    head at (75, 70), tail at (25, 20). Mirror = head upper-right
    #    means the BELLY is at the upper-right area sloping toward center.
    #    For a right 点 in 小, head is upper-right of the dot, but
    #    canonically the right 点 in 小 is drawn from upper-LEFT (near
    #    center) to lower-RIGHT. We follow the brief literally: mirror
    #    of left. Left went head(upper-left)→tail(toward center). Mirror:
    #    head(upper-right)→tail(toward center).
    dian(75, 70, 25, 20, w_belly=15, w_tail=3)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    tasks = [
        (task_01_ye,    "01_也.png"),
        (task_02_ba,    "02_巴.png"),
        (task_03_jian,  "03_见.png"),
        (task_04_tian,  "04_天.png"),
        (task_05_le,    "05_了.png"),
        (task_06_xiao,  "06_小.png"),
    ]
    for fn, name in tasks:
        reset_for_next()
        fn()
        save_png(name)


if __name__ == "__main__":
    main()
