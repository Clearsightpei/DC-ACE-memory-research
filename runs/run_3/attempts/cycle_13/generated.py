"""Cycle 13 — Drawer output (run_3).

Six tasks:
  01 火  (carry-over: 点 as inward-sloped 'ears' flanking apex)
  02 也  (carry-over: middle shu reaches 弯 floor; thick 横折钩)
  03 力  (carry-over: 撇 head crosses ABOVE top heng)
  04 巴  (carry-over: tri-decker upper frame to break 已 prior)
  05 见  (carry-over: 撇 leg diverges down-LEFT past frame)
  06 天  (new: two heng stacked; 撇/捺 hang BELOW lower heng)

All strokes are Bézier centerlines with per-sample pensize (middle
≥ 50% of peak), 顿笔 corners, fine hook tails. Each task starts
at (0,0), heading 90°. PNG via canvas.postscript → PIL.
"""

import io
import os
import turtle

from PIL import Image

# ---------------------------------------------------------------- canvas

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("white")
screen.tracer(0, 0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.color("black")


# ---------------------------------------------------------------- helpers

def _bez(p0, p1, p2, p3, n=160):
    """Sampled cubic Bézier — n points along the curve."""
    pts = []
    for i in range(n + 1):
        u = i / n
        v = 1.0 - u
        x = v*v*v*p0[0] + 3*v*v*u*p1[0] + 3*v*u*u*p2[0] + u*u*u*p3[0]
        y = v*v*v*p0[1] + 3*v*v*u*p1[1] + 3*v*u*u*p2[1] + u*u*u*p3[1]
        pts.append((x, y))
    return pts


def _width_profile(n_plus_1, start_w, mid_w, end_w):
    """Per-sample pensize, parabolic interpolation through (0, mid, end).

    Guarantees middle ≥ 50% of peak — caller supplies mid_w that satisfies it.
    """
    ws = []
    n = n_plus_1 - 1
    for i in range(n_plus_1):
        u = i / n
        # Quadratic Bézier on width: (1-u)^2 * start + 2(1-u)u * mid + u^2 * end
        w = (1 - u) ** 2 * start_w + 2 * (1 - u) * u * mid_w + u * u * end_w
        ws.append(max(1.0, w))
    return ws


def brush_bezier(p0, p1, p2, p3, start_w, mid_w, end_w, n=160):
    """Brushed cubic Bézier: per-sample pensize."""
    pts = _bez(p0, p1, p2, p3, n=n)
    ws = _width_profile(n + 1, start_w, mid_w, end_w)
    t.penup()
    t.goto(pts[0])
    t.pendown()
    for (x, y), w in zip(pts, ws):
        t.pensize(w)
        t.goto(x, y)
    t.penup()


def heng(x0, y, x1, peak=12):
    """Horizontal stroke, heavy at both ends, slight downward V-dip in middle."""
    dx = x1 - x0
    p0 = (x0, y)
    p1 = (x0 + dx * 0.30, y - 2)
    p2 = (x0 + dx * 0.70, y - 2)
    p3 = (x1, y)
    brush_bezier(p0, p1, p2, p3, start_w=peak, mid_w=peak * 0.6, end_w=peak, n=140)


def shu(x, y0, y1, peak=12):
    """Vertical stroke, heavy at both ends."""
    dy = y1 - y0
    p0 = (x, y0)
    p1 = (x, y0 + dy * 0.30)
    p2 = (x, y0 + dy * 0.70)
    p3 = (x, y1)
    brush_bezier(p0, p1, p2, p3, start_w=peak, mid_w=peak * 0.6, end_w=peak, n=140)


def pie(p0, p3, peak=14, bow=18):
    """撇 — heavy at start, tapers to fine point.

    bow controls how convex the curve is (positive = bowed outward).
    """
    mx = (p0[0] + p3[0]) / 2
    my = (p0[1] + p3[1]) / 2
    # Perpendicular bow direction (left-side of travel, so curve bows out-left).
    dx = p3[0] - p0[0]
    dy = p3[1] - p0[1]
    L = max(1.0, (dx * dx + dy * dy) ** 0.5)
    nx, ny = -dy / L, dx / L
    p1 = (p0[0] + dx * 0.30 + nx * bow * 0.4,
          p0[1] + dy * 0.30 + ny * bow * 0.4)
    p2 = (mx + nx * bow, my + ny * bow)
    brush_bezier(p0, p1, p2, p3, start_w=peak, mid_w=peak * 0.65, end_w=2, n=160)


def na(p0, p3, peak=14, bow=18):
    """捺 — fine at start, broadens to a heavy flat kick at end."""
    dx = p3[0] - p0[0]
    dy = p3[1] - p0[1]
    L = max(1.0, (dx * dx + dy * dy) ** 0.5)
    nx, ny = -dy / L, dx / L
    mx = (p0[0] + p3[0]) / 2
    my = (p0[1] + p3[1]) / 2
    p1 = (p0[0] + dx * 0.30 - nx * bow * 0.4,
          p0[1] + dy * 0.30 - ny * bow * 0.4)
    p2 = (mx - nx * bow, my - ny * bow)
    brush_bezier(p0, p1, p2, p3, start_w=2, mid_w=peak * 0.6, end_w=peak, n=160)


def dian(p0, p3, peak=12, bow=6):
    """点 — belly heavy, tail fine. p0 = belly, p3 = tail tip."""
    dx = p3[0] - p0[0]
    dy = p3[1] - p0[1]
    p1 = (p0[0] + dx * 0.30 + bow * 0.4,
          p0[1] + dy * 0.30)
    p2 = (p0[0] + dx * 0.60 + bow * 0.6,
          p0[1] + dy * 0.60)
    brush_bezier(p0, p1, p2, p3, start_w=peak, mid_w=peak * 0.6, end_w=2, n=120)


def save_png(name):
    """Save the current canvas to <OUT_DIR>/<name>."""
    screen.update()
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color",
                           width=WIDTH, height=HEIGHT,
                           pagewidth=WIDTH, pageheight=HEIGHT,
                           x=-WIDTH // 2, y=-HEIGHT // 2)
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=2)
    img = img.convert("RGB")
    img = img.resize((WIDTH, HEIGHT), Image.LANCZOS)
    img.save(os.path.join(OUT_DIR, name))


def start():
    """Reset turtle to (0,0) heading 90°."""
    t.reset()
    t.hideturtle()
    t.speed(0)
    t.color("black")
    t.penup()
    t.goto(0, 0)
    t.setheading(90)


# ── Task 01 | 火 | huǒ
def task_01_huo():
    start()
    # Apex (top of the 'head'): a short vertical stub from y=+80 to y=+130.
    # Apex top is at y = +130. 点 belly will sit at y = +90 (BELOW apex top).
    shu(0, 80, 130, peak=10)

    # Inner short 撇 from apex base sweeping down-left (head ridge).
    pie((-6, 70), (-50, -10), peak=11, bow=10)

    # Main 撇 — long left leg sweeping from upper-center down-left, wide tail.
    pie((-8, 50), (-180, -150), peak=14, bow=28)

    # Main 捺 — long right leg sweeping from upper-center down-right, wide tail.
    na((8, 50), (180, -150), peak=14, bow=28)

    # Left 点 — "ear" beside the apex. Belly at (-55, +90), tail toward apex
    # (slope INWARD: tail tip near apex, belly upper-left).
    # Belly y=+90 is BELOW apex top y=+130; clearly flanks the apex.
    dian((-55, 90), (-18, 60), peak=11, bow=4)

    # Right 点 — mirror. Belly at (+55, +90), tail toward apex.
    dian((55, 90), (18, 60), peak=11, bow=-4)

    save_png("01_火.png")


# ── Task 02 | 也 | yě
def task_02_ye():
    start()
    # 横折钩 (top-left assembly) — thickened so it dominates.
    # Horizontal segment from (-130, +90) to (-30, +90).
    heng(-130, 90, -30, peak=15)
    # Vertical drop from (-30, +90) to (-30, -40) — the 折 part.
    shu(-30, 90, -40, peak=15)
    # Hook tail-arm at bottom: short arc up-left with fine taper.
    brush_bezier((-30, -40), (-34, -55), (-50, -60), (-65, -50),
                 start_w=15, mid_w=10, end_w=2, n=100)

    # Middle 竖 (shu) — starts ABOVE the top heng level, foot lands on 弯 floor.
    # 弯 floor is at y = -120 (see 竖弯钩 below); middle shu bottom at y = -115.
    shu(40, 100, -115, peak=12)

    # 竖弯钩 — vertical drop, smooth curve into horizontal, then hook UP.
    # Vertical part: from (110, +90) down to (110, -90).
    shu(110, 90, -90, peak=13)
    # 弯 — corner curving from (110, -90) leftward & down to floor at (40, -120),
    # then continuing right to (160, -120), exiting upward as the hook.
    # Use two Béziers: first the curl, then the hook tail-arm.
    brush_bezier((110, -90), (110, -118), (130, -125), (160, -120),
                 start_w=13, mid_w=12, end_w=11, n=100)
    # The actual "floor" of 弯 — the segment from x≈40 to x≈160 at y≈-120.
    # Draw an explicit floor curve so middle shu can land on it.
    brush_bezier((40, -118), (75, -125), (120, -125), (160, -120),
                 start_w=11, mid_w=12, end_w=13, n=100)
    # Hook tail-arm: short arc up from the right tip.
    brush_bezier((160, -120), (170, -110), (170, -90), (160, -75),
                 start_w=13, mid_w=10, end_w=2, n=100)

    save_png("02_也.png")


# ── Task 03 | 力 | lì
def task_03_li():
    start()
    # Top 横折钩 — but here for 力 it's really a heng + 折 + hook combo.
    # Top heng from (-100, +90) to (+90, +90).
    heng(-100, 90, 90, peak=13)
    # 折 — short vertical drop from (+90, +90) to (+90, +30).
    shu(90, 90, 30, peak=13)
    # Hook tail-arm at (+90, +30): short curve up-left with fine taper.
    brush_bezier((90, 30), (84, 18), (70, 14), (55, 22),
                 start_w=13, mid_w=9, end_w=2, n=100)

    # 撇 — head must VISIBLY CROSS the top heng.
    # Head at (+30, +130) — well ABOVE the heng's y=+90.
    # Sweeps DOWN through the heng (passing through ~ (+10, +90)),
    # then out the lower-left to (-160, -130). Heavy at head.
    pie((30, 130), (-160, -130), peak=14, bow=32)

    save_png("03_力.png")


# ── Task 04 | 巴 | bā
def task_04_ba():
    start()
    # Upper rectangle frame — WIDE and TRI-DECKER (extra interior bar).
    # Left side (shu) from (-95, +130) down to (-95, -10).
    shu(-95, 130, -10, peak=12)
    # Top heng from (-95, +130) to (+95, +130).
    heng(-95, 130, 95, peak=12)
    # Right side: top heng's right end drops via 横折钩-style corner.
    # Right shu from (+95, +130) down to (+95, -10).
    shu(95, 130, -10, peak=12)
    # Bottom heng of upper frame from (-95, -10) to (+95, -10).
    heng(-95, -10, 95, peak=12)

    # Middle interior bar #1 — upper interior, at y = +80.
    heng(-95, 80, 95, peak=10)
    # Middle interior bar #2 — lower interior, at y = +35. (Tri-decker.)
    heng(-95, 35, 95, peak=10)

    # 竖弯钩 — the bottom "tail" that defines 巴 vs 已.
    # Starts from left side of bottom heng, drops, curves right, hook up.
    # Start at (-50, -10) and drop to (-50, -100).
    shu(-50, -10, -100, peak=12)
    # 弯: curve from (-50, -100) rightward to (+70, -120), narrower than upper frame.
    brush_bezier((-50, -100), (-50, -125), (10, -130), (70, -120),
                 start_w=12, mid_w=11, end_w=12, n=120)
    # Hook tail-arm: up from (+70, -120) with fine taper.
    brush_bezier((70, -120), (80, -105), (80, -85), (70, -70),
                 start_w=12, mid_w=9, end_w=2, n=100)

    save_png("04_巴.png")


# ── Task 05 | 见 | jiàn
def task_05_jian():
    start()
    # Frame — like 月/目 but with two interior heng.
    # Top heng from (-80, +130) to (+70, +130).
    heng(-80, 130, 70, peak=12)
    # Right side from (+70, +130) down to (+70, -50).
    shu(70, 130, -50, peak=12)
    # Left side (shu) — but this is going to become the 撇 leg at the bottom.
    # Draw the upper portion of left side as a normal shu from
    # (-80, +130) down to (-80, -50). The bottom will be the 撇 exit.
    shu(-80, 130, -50, peak=12)

    # Interior heng #1 at y = +70.
    heng(-80, 70, 70, peak=10)
    # Interior heng #2 at y = +10.
    heng(-80, 10, 70, peak=10)

    # Bottom heng connecting the two sides at y = -50.
    heng(-80, -50, 70, peak=12)

    # 竖弯钩 (right leg, the hook) — from (+70, -50) drops and hooks LEFT.
    shu(70, -50, -90, peak=11)
    brush_bezier((70, -90), (60, -110), (40, -115), (20, -105),
                 start_w=11, mid_w=8, end_w=2, n=100)

    # 撇 leg (left leg) — must visibly DIVERGE down-LEFT past the frame bottom.
    # Start at (-80, -50) and sweep down-LEFT to (-180, -140). Heavy at head.
    pie((-80, -50), (-180, -140), peak=13, bow=22)

    save_png("05_见.png")


# ── Task 06 | 天 | tiān
def task_06_tian():
    start()
    # Top heng — SHORT, near the top.
    # From (-50, +130) to (+50, +130).
    heng(-50, 130, 50, peak=12)

    # Second heng — LONGER, below the top heng (stacked like 二).
    # From (-110, +70) to (+110, +70).
    heng(-110, 70, 110, peak=13)

    # 撇 — from the lower heng's center, sweeping down-LEFT.
    # Critically: 撇 HEAD attaches AT the lower heng, NOT crossing through it.
    # Head at (-10, +70), tail at (-160, -140).
    pie((-10, 70), (-160, -140), peak=14, bow=26)

    # 捺 — from the lower heng's center, sweeping down-RIGHT.
    # Head at (+10, +70), tail at (+160, -140). Heavy flat kick at end.
    na((10, 70), (160, -140), peak=14, bow=26)

    save_png("06_天.png")


# ---------------------------------------------------------------- run all

if __name__ == "__main__":
    task_01_huo()
    task_02_ye()
    task_03_li()
    task_04_ba()
    task_05_jian()
    task_06_tian()
