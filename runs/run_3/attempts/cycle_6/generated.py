"""Cycle 6 — Drawer output.

Three repairs applied:
1. 大 topology: 撇/捺 share an apex ABOVE the heng; heng cuts across both limbs.
2. 入 topology: 捺 starts on the 撇's spine, partway down (NOT at the apex).
3. Brushed width on every stroke and every primitive: middle width >= 50% peak,
   including short strokes (上 mid heng, 下 shu) and compound paths
   (七 竖弯, 山 竖折) — width modulation sweeps along ENTIRE path through turns.
"""

import io
import os
import math
import turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))


# ────────────────────────────────────────────────────────────────────────────
# Canvas helpers
# ────────────────────────────────────────────────────────────────────────────
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


# ────────────────────────────────────────────────────────────────────────────
# Core brushed-stroke engine
# ────────────────────────────────────────────────────────────────────────────
def cubic_bezier(p0, p1, p2, p3, n=160):
    """Return n+1 sampled points along a cubic Bezier from p0 to p3."""
    pts = []
    for i in range(n + 1):
        u = i / n
        b0 = (1 - u) ** 3
        b1 = 3 * (1 - u) ** 2 * u
        b2 = 3 * (1 - u) * u * u
        b3 = u ** 3
        x = b0 * p0[0] + b1 * p1[0] + b2 * p2[0] + b3 * p3[0]
        y = b0 * p0[1] + b1 * p1[1] + b2 * p2[1] + b3 * p3[1]
        pts.append((x, y))
    return pts


def width_profile(u, kind, peak=14.0):
    """Width at parameter u in [0,1] for a given stroke kind.

    Memory rules:
      - peak <= ~2 * middle, middle >= ~50% of peak.
      - Apply along entire path of every primitive.

    Returns a pensize value. We keep mid_floor >= 0.55 * peak to be safe.
    """
    mid_floor = 0.55 * peak  # >= 50% as memory demands
    cap = peak
    if kind == "heng":
        # weighted entry + shaft >= 50% + weighted end press.
        # Bell-ish with held middle plateau.
        if u < 0.12:
            w = cap - (cap - mid_floor) * (u / 0.12) * 0.4
        elif u > 0.88:
            w = cap - (cap - mid_floor) * ((1.0 - u) / 0.12) * 0.4
        else:
            # central plateau slightly under peak but >= mid_floor
            t = (u - 0.5) * 2.0  # -1..1
            w = cap - (cap - mid_floor) * 0.35 * (t * t)
        return max(mid_floor, w)
    if kind == "shu":
        # weighted bulb top + shaft >= 50% + weighted foot.
        if u < 0.12:
            w = cap - (cap - mid_floor) * (u / 0.12) * 0.35
        elif u > 0.88:
            w = cap - (cap - mid_floor) * ((1.0 - u) / 0.12) * 0.35
        else:
            t = (u - 0.5) * 2.0
            w = cap - (cap - mid_floor) * 0.30 * (t * t)
        return max(mid_floor, w)
    if kind == "pie":
        # HEAVY weighted head at START, gentle bow, fine point at END.
        # Width: ~peak at u=0 → mid_floor in middle → very thin tip at u=1.
        if u < 0.18:
            # near-peak head
            w = cap - (cap - mid_floor) * (u / 0.18) * 0.3
        elif u < 0.75:
            t = (u - 0.18) / (0.75 - 0.18)
            w = cap - (cap - mid_floor) * (0.3 + 0.4 * t)
            w = max(mid_floor, w)
        else:
            # taper down to fine tip
            t = (u - 0.75) / 0.25
            w = mid_floor * (1.0 - t) + 0.6 * (1 - t)  # tip ~0.6 px
        return max(0.6, w)
    if kind == "na":
        # thin entry → broadening body → HEAVY pressed tail with flat-kick
        # plateau (hold near-peak for last 10-15% then small horizontal kick).
        if u < 0.15:
            w = 0.8 + (mid_floor - 0.8) * (u / 0.15)
        elif u < 0.55:
            t = (u - 0.15) / 0.40
            w = mid_floor + (cap - mid_floor) * (0.4 + 0.5 * t)
        elif u < 0.88:
            # ramp to peak, hold near peak (plateau)
            t = (u - 0.55) / 0.33
            w = cap * (0.95 + 0.05 * t)
        else:
            # very small taper at the very end of the kick
            t = (u - 0.88) / 0.12
            w = cap * (1.0 - 0.35 * t)
        return max(0.8, w)
    if kind == "dian":
        # thin entry → rounded weighted belly → tapered tail.
        if u < 0.25:
            w = 0.8 + (cap - 0.8) * (u / 0.25)
        elif u < 0.65:
            w = cap
        else:
            t = (u - 0.65) / 0.35
            w = cap * (1.0 - 0.85 * t)
        return max(0.6, w)
    if kind == "ti":
        # weighted base at START → gentle rise → fine flick at END.
        if u < 0.18:
            w = cap - (cap - mid_floor) * (u / 0.18) * 0.3
        elif u < 0.7:
            t = (u - 0.18) / (0.7 - 0.18)
            w = cap - (cap - mid_floor) * (0.3 + 0.5 * t)
            w = max(mid_floor, w)
        else:
            t = (u - 0.7) / 0.3
            w = mid_floor * (1.0 - t) + 0.5 * (1 - t)
        return max(0.5, w)
    if kind == "compound":
        # Compound (折/弯/钩 families): brushed width across ENTIRE path,
        # including the corner. Mid floor held; slight thickening at corner
        # via the optional `corner_u` parameter is layered on by the caller.
        if u < 0.12:
            w = cap - (cap - mid_floor) * (u / 0.12) * 0.35
        elif u > 0.88:
            # weighted end (foot / flick base)
            w = cap - (cap - mid_floor) * ((1.0 - u) / 0.12) * 0.35
        else:
            t = (u - 0.5) * 2.0
            w = cap - (cap - mid_floor) * 0.25 * (t * t)
        return max(mid_floor, w)
    # fallback
    return mid_floor


def brushed_bezier(t, p0, p1, p2, p3, kind, peak=14.0, n=160,
                   corner_us=None, corner_boost=0.0):
    """Draw a cubic-Bezier centerline with per-sample pensize modulation.

    `corner_us`: optional list of u in [0,1] where a 顿笔 thickening sits
    (used by compound strokes — Gaussian-like bump added to width).
    """
    pts = cubic_bezier(p0, p1, p2, p3, n=n)
    t.penup()
    t.goto(pts[0])
    t.pendown()
    for i, (x, y) in enumerate(pts):
        u = i / n
        w = width_profile(u, kind, peak=peak)
        if corner_us and corner_boost > 0:
            for cu in corner_us:
                sigma = 0.05
                bump = corner_boost * math.exp(-((u - cu) ** 2) / (2 * sigma * sigma))
                w += bump
        t.pensize(max(0.5, w))
        t.goto(x, y)
    t.penup()


def brushed_path(t, ctrl_segments, kind, peak=14.0, n_per=120,
                 corner_us=None, corner_boost=0.0):
    """Draw a chain of cubic Bezier segments as ONE continuous brushed path.

    `ctrl_segments`: list of (p0,p1,p2,p3) tuples; consecutive segments
    should share endpoints. `corner_us` are global parameters (over the
    combined arclength 0..1) where 顿笔 thickenings sit.
    """
    # Build the global point list and global u list.
    all_pts = []
    for k, (p0, p1, p2, p3) in enumerate(ctrl_segments):
        seg = cubic_bezier(p0, p1, p2, p3, n=n_per)
        if k > 0:
            seg = seg[1:]  # avoid duplicate join point
        all_pts.extend(seg)
    N = len(all_pts) - 1
    t.penup()
    t.goto(all_pts[0])
    t.pendown()
    for i, (x, y) in enumerate(all_pts):
        u = i / N
        w = width_profile(u, kind, peak=peak)
        if corner_us and corner_boost > 0:
            for cu in corner_us:
                sigma = 0.04
                bump = corner_boost * math.exp(-((u - cu) ** 2) / (2 * sigma * sigma))
                w += bump
        t.pensize(max(0.5, w))
        t.goto(x, y)
    t.penup()


# ────────────────────────────────────────────────────────────────────────────
# Atomic stroke recipes (positions in screen coords; y up)
# ────────────────────────────────────────────────────────────────────────────
def stroke_heng(t, x0, y0, x1, y1, peak=14.0, tilt=4.0):
    """Horizontal stroke; faint upward tilt. Brushed width along entire path."""
    # Add slight upward tilt by raising the end a touch.
    y1t = y1 + tilt
    # Bezier with control points along the line for near-linear shape.
    dx = x1 - x0
    p0 = (x0, y0)
    p1 = (x0 + dx * 0.33, y0 + tilt * 0.3)
    p2 = (x0 + dx * 0.66, y1t - tilt * 0.3)
    p3 = (x1, y1t)
    brushed_bezier(t, p0, p1, p2, p3, "heng", peak=peak, n=140)


def stroke_shu(t, x0, y0, x1, y1, peak=14.0):
    """Vertical stroke. Brushed width."""
    dy = y1 - y0
    p0 = (x0, y0)
    p1 = (x0, y0 + dy * 0.33)
    p2 = (x1, y0 + dy * 0.66)
    p3 = (x1, y1)
    brushed_bezier(t, p0, p1, p2, p3, "shu", peak=peak, n=140)


def stroke_pie(t, x0, y0, x1, y1, peak=15.0, bow=20.0):
    """撇 — heavy head at start, gentle bow, fine tip at end."""
    dx = x1 - x0
    dy = y1 - y0
    # Bow outward to the right of the chord (i.e. slight bulge).
    # Perpendicular vector (normalized) to chord.
    L = math.hypot(dx, dy) or 1.0
    nx, ny = -dy / L, dx / L  # left-perpendicular
    # For 撇 going down-left, bow points to the right (positive perpendicular)
    p0 = (x0, y0)
    p1 = (x0 + dx * 0.33 + nx * bow * 0.6, y0 + dy * 0.33 + ny * bow * 0.6)
    p2 = (x0 + dx * 0.66 + nx * bow * 0.4, y0 + dy * 0.66 + ny * bow * 0.4)
    p3 = (x1, y1)
    brushed_bezier(t, p0, p1, p2, p3, "pie", peak=peak, n=160)


def stroke_na(t, x0, y0, x1, y1, peak=16.0, bow=18.0):
    """捺 — thin start, broadening, heavy pressed tail with flat kick."""
    dx = x1 - x0
    dy = y1 - y0
    L = math.hypot(dx, dy) or 1.0
    nx, ny = dy / L, -dx / L  # opposite-perpendicular for natural na bow
    # Add a small horizontal kick: drop end y slightly relative to a straight
    # chord so the last segment is more horizontal.
    p0 = (x0, y0)
    p1 = (x0 + dx * 0.33 + nx * bow * 0.4, y0 + dy * 0.33 + ny * bow * 0.4)
    p2 = (x0 + dx * 0.70 + nx * bow * 0.5, y0 + dy * 0.70 + ny * bow * 0.5)
    # Flat kick: extend the end slightly horizontally past x1.
    p3 = (x1 + 6, y1 + 2)
    brushed_bezier(t, p0, p1, p2, p3, "na", peak=peak, n=180)


def stroke_dian(t, x0, y0, x1, y1, peak=12.0):
    """点 — short droplet."""
    dx = x1 - x0
    dy = y1 - y0
    p0 = (x0, y0)
    p1 = (x0 + dx * 0.3, y0 + dy * 0.3)
    p2 = (x0 + dx * 0.6, y0 + dy * 0.6)
    p3 = (x1, y1)
    brushed_bezier(t, p0, p1, p2, p3, "dian", peak=peak, n=100)


# ────────────────────────────────────────────────────────────────────────────
# ── Task 01 | 大 | da
# ────────────────────────────────────────────────────────────────────────────
def task_01(screen, t):
    """大 — 撇 and 捺 share an apex ABOVE the heng; heng cuts across both
    limbs (~30–40% down from apex)."""
    reset_turtle(t)
    # Apex sits high.
    apex = (0, 150)
    # Pie tail at lower-left, far below and left of apex.
    pie_tail = (-160, -160)
    # Na tail at lower-right.
    na_tail = (160, -160)
    # Heng cuts across both limbs at ~35% from apex down.
    # 35% along pie chord: apex + 0.35 * (pie_tail - apex)
    fx = 0.35
    pie_cross = (apex[0] + fx * (pie_tail[0] - apex[0]),
                 apex[1] + fx * (pie_tail[1] - apex[1]))
    na_cross = (apex[0] + fx * (na_tail[0] - apex[0]),
                apex[1] + fx * (na_tail[1] - apex[1]))
    # Extend heng a bit beyond each limb for visibility.
    heng_x0 = pie_cross[0] - 30
    heng_y = (pie_cross[1] + na_cross[1]) / 2.0
    heng_x1 = na_cross[0] + 30

    # 1) Heng first (drawn UNDER the limbs visually; order doesn't matter for
    # turtle since we don't fill).
    stroke_heng(t, heng_x0, heng_y, heng_x1, heng_y, peak=14.0, tilt=4.0)
    # 2) Pie — from apex, through heng, to lower-left.
    stroke_pie(t, apex[0], apex[1], pie_tail[0], pie_tail[1],
               peak=15.0, bow=18.0)
    # 3) Na — from apex, through heng, to lower-right (flat kick at tail).
    stroke_na(t, apex[0], apex[1], na_tail[0], na_tail[1],
              peak=16.0, bow=16.0)

    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_大.png"))


# ────────────────────────────────────────────────────────────────────────────
# ── Task 02 | 入 | ru
# ────────────────────────────────────────────────────────────────────────────
def task_02(screen, t):
    """入 — only the 撇 has the apex. 捺 starts ON the 撇's spine ~35% from
    the head, sweeping to lower-right. Asymmetric."""
    reset_turtle(t)
    pie_head = (0, 160)
    pie_tail = (-150, -170)
    # Junction point on 撇's spine at 35% from head.
    f = 0.35
    junction_chord = (pie_head[0] + f * (pie_tail[0] - pie_head[0]),
                      pie_head[1] + f * (pie_tail[1] - pie_head[1]))
    # Offset slightly along the actual bowed spine (approximation OK).
    # 捺 starts from a touch right of the chord junction so it visibly meets
    # the 撇's spine.
    junction = (junction_chord[0] + 6, junction_chord[1] - 4)

    # 1) 撇 — heavy head at top apex.
    stroke_pie(t, pie_head[0], pie_head[1], pie_tail[0], pie_tail[1],
               peak=16.0, bow=22.0)
    # 2) 捺 — starts on the 撇's spine, sweeps to lower-right with flat kick.
    na_tail = (170, -170)
    stroke_na(t, junction[0], junction[1], na_tail[0], na_tail[1],
              peak=16.0, bow=18.0)

    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "02_入.png"))


# ────────────────────────────────────────────────────────────────────────────
# ── Task 03 | 上 | shang
# ────────────────────────────────────────────────────────────────────────────
def task_03(screen, t):
    """上 — shu (centered, rising above and below mid heng) +
    short mid heng (LEFT half, brushed >=50% middle width even though
    short) + bottom heng (longest)."""
    reset_turtle(t)
    # Vertical shu through center.
    shu_top = (0, 120)
    shu_bot = (0, -100)
    stroke_shu(t, shu_top[0], shu_top[1], shu_bot[0], shu_bot[1], peak=14.0)
    # Short mid heng on the right side of the shu (上's classic mid heng
    # extends to the right). Make it SHORT but enforce brushed width.
    mid_heng_y = 30
    stroke_heng(t, -5, mid_heng_y, 80, mid_heng_y, peak=12.0, tilt=2.0)
    # Bottom heng — longest.
    stroke_heng(t, -150, -110, 150, -110, peak=15.0, tilt=4.0)

    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "03_上.png"))


# ────────────────────────────────────────────────────────────────────────────
# ── Task 04 | 下 | xia
# ────────────────────────────────────────────────────────────────────────────
def task_04(screen, t):
    """下 — top heng (longest) + shu (centered, going down) + 点 (right of
    shu). Enforce >=50% middle width on the shu and weighted belly on 点."""
    reset_turtle(t)
    # Top heng — longest.
    stroke_heng(t, -150, 140, 150, 140, peak=15.0, tilt=4.0)
    # Shu through center.
    stroke_shu(t, 0, 135, 0, -150, peak=14.0)
    # 点 to the right of the shu, upper-right of shu's midpoint.
    stroke_dian(t, 30, 60, 70, 20, peak=13.0)

    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "04_下.png"))


# ────────────────────────────────────────────────────────────────────────────
# ── Task 05 | 七 | qi
# ────────────────────────────────────────────────────────────────────────────
def task_05(screen, t):
    """七 — heng (slight upward tilt) crossed by a 横折弯钩-like compound
    primitive (here a 竖弯 going down then sweeping right with flick).
    Brushed width along ENTIRE compound path including the corner."""
    reset_turtle(t)
    # Stroke 1: heng tilted up slightly, crossing the vertical at ~30% from
    # its head.
    stroke_heng(t, -150, 40, 150, 60, peak=14.0, tilt=2.0)
    # Stroke 2: 竖弯 starting from upper-middle (slightly right of center,
    # above the heng), descending, curling right at the bottom with a small
    # flick at the right end. Built as a chain of two Bezier segments so the
    # entire path has continuous brushed pensize.
    # Segment A: descend from upper-middle through the heng down to a knee
    # just before the corner (slightly left & above the actual corner).
    seg_a = ((20, 130),         # start: upper-middle, above heng
             (10, 60),           # ctrl 1: descending
             (-10, -40),         # ctrl 2: curving slightly left
             (-30, -100))        # end: pre-corner knee (lower-left of axis)
    # Segment B: curl into the corner and sweep right with a small flick at
    # the far right.
    seg_b = ((-30, -100),        # start: knee
             (-10, -140),        # ctrl 1: rounding the corner
             (60, -130),         # ctrl 2: along the bottom arm
             (140, -100))        # end: small upward flick at right end
    # The "corner" in the global u-parameter is at the join: ~50% of total.
    brushed_path(
        t,
        [seg_a, seg_b],
        kind="compound",
        peak=15.0,
        n_per=140,
        corner_us=[0.5],
        corner_boost=3.0,  # 顿笔 thickening at the turn
    )

    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "05_七.png"))


# ────────────────────────────────────────────────────────────────────────────
# ── Task 06 | 山 | shan
# ────────────────────────────────────────────────────────────────────────────
def task_06(screen, t):
    """山 — center shu + 竖折 (left descent + bottom arm + right ascent) +
    right shu. Apply brushed width across the ENTIRE 竖折 compound path
    including the 90° corner (顿笔 at the turn)."""
    reset_turtle(t)
    # Stroke 1: center shu (the tall vertical in the middle of 山, drawn
    # first by stroke order: actually 山's order is mid-shu then 竖折 then
    # right-shu — but the visual layout matters more than order here).
    stroke_shu(t, 0, 140, 0, -120, peak=14.0)
    # Stroke 2: 竖折 — left descent then horizontal bottom arm.
    # Built as two Bezier segments, drawn as ONE continuous brushed path.
    seg_a = ((-110, 60),        # start: left top
             (-110, 10),         # ctrl 1: straight down
             (-110, -50),        # ctrl 2: straight down
             (-110, -120))       # end: bottom-left corner
    seg_b = ((-110, -120),       # start: corner
             (-60, -120),        # ctrl 1: along bottom arm
             (60, -120),         # ctrl 2: along bottom arm
             (110, -120))        # end: bottom-right
    brushed_path(
        t,
        [seg_a, seg_b],
        kind="compound",
        peak=15.0,
        n_per=140,
        corner_us=[0.5],
        corner_boost=3.5,  # 顿笔 at the 90° turn
    )
    # Stroke 3: right shu — rises from the bottom-right end of the 竖折
    # upward (山's right vertical).
    stroke_shu(t, 110, 80, 110, -120, peak=14.0)

    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "06_山.png"))


# ────────────────────────────────────────────────────────────────────────────
# Main
# ────────────────────────────────────────────────────────────────────────────
def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0, 0)
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    task_01(screen, t)
    task_02(screen, t)
    task_03(screen, t)
    task_04(screen, t)
    task_05(screen, t)
    task_06(screen, t)


if __name__ == "__main__":
    main()
