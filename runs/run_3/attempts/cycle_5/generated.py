"""Cycle 5 — Phase 2 expansion.

Six characters: 大 入 上 下 七 山.

Drawer-side rendering: every stroke is a cubic-Bézier centerline
sampled densely with `pensize` varied per sample so width is
continuous (no barbell artifact). Width profile is keyed to STROKE
IDENTITY per the cheat sheet:

  横    both ends heavy, shaft ~55% peak
  竖    both ends heavy, shaft ~55% peak
  撇    head heavy at start (upper-right), taper to fine point
  捺    thin entry at start, broaden, HEAVY pressed tail at END,
        held near-peak width across last ~10-15% of arclength
        before a small horizontal kick-off taper (textbook flat kick)
  提    base heavy at start (lower-left), flick to fine point
  点    weighted belly, tapered tail

Compound strokes (七 stroke 2; 山 stroke 2) are drawn as a SINGLE
continuous brushed path: two Bézier segments stitched at the corner,
with a 顿笔 thickening at the corner (the 折 turn is one stroke).
"""

import io
import os
import turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))


# ---------------------------------------------------------------------------
# Canvas helpers
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# Bézier sampling + width-modulated stroke renderer
# ---------------------------------------------------------------------------

def bezier_point(p0, p1, p2, p3, u):
    """Cubic Bézier point at parameter u in [0,1]."""
    mu = 1.0 - u
    x = (mu ** 3) * p0[0] + 3 * (mu ** 2) * u * p1[0] + 3 * mu * (u ** 2) * p2[0] + (u ** 3) * p3[0]
    y = (mu ** 3) * p0[1] + 3 * (mu ** 2) * u * p1[1] + 3 * mu * (u ** 2) * p2[1] + (u ** 3) * p3[1]
    return (x, y)


def sample_bezier(p0, p1, p2, p3, n=160):
    return [bezier_point(p0, p1, p2, p3, i / float(n - 1)) for i in range(n)]


def draw_width_path(t, samples, widths):
    """Draw a polyline through `samples` setting pensize per segment.

    pensize for segment i is the average of widths[i] and widths[i+1];
    this guarantees continuous width modulation (no barbell).
    """
    t.penup()
    t.goto(samples[0])
    t.pendown()
    for i in range(1, len(samples)):
        w = 0.5 * (widths[i - 1] + widths[i])
        # clamp to a reasonable pen range
        if w < 1.0:
            w = 1.0
        t.pensize(w)
        t.goto(samples[i])
    t.penup()


# ---------------------------------------------------------------------------
# Width profiles, keyed to stroke identity
# ---------------------------------------------------------------------------

def width_heng(n, peak=11.0, shaft=6.5):
    """横: weighted entry + ~55% shaft + weighted end press."""
    ws = []
    for i in range(n):
        u = i / float(n - 1)
        if u < 0.10:
            # entry press: ease from peak*0.85 -> shaft
            f = u / 0.10
            w = peak * 0.92 - (peak * 0.92 - shaft) * f
        elif u > 0.90:
            # end press: ease from shaft -> peak
            f = (u - 0.90) / 0.10
            w = shaft + (peak - shaft) * f
        else:
            # gentle belly: a hair fatter in the middle
            v = (u - 0.5) / 0.4
            w = shaft + (shaft * 0.08) * (1.0 - v * v)
        ws.append(w)
    return ws


def width_shu(n, peak=11.0, shaft=6.5):
    """竖: weighted bulb top + ~55% shaft + weighted foot."""
    ws = []
    for i in range(n):
        u = i / float(n - 1)
        if u < 0.10:
            f = u / 0.10
            w = peak - (peak - shaft) * f
        elif u > 0.88:
            f = (u - 0.88) / 0.12
            w = shaft + (peak * 0.95 - shaft) * f
        else:
            v = (u - 0.5) / 0.4
            w = shaft + (shaft * 0.08) * (1.0 - v * v)
        ws.append(w)
    return ws


def width_pie(n, head=12.0, tip=1.5):
    """撇: weighted head at START → smooth taper to fine point at END."""
    ws = []
    for i in range(n):
        u = i / float(n - 1)
        # easeOutQuad from head -> tip
        w = head - (head - tip) * (u ** 1.4)
        ws.append(w)
    return ws


def width_na(n, entry=2.0, peak=13.0):
    """捺: THIN entry → broaden → HEAVY pressed tail at END.

    Critical refinement: hold near-peak width across the last ~12% of
    arclength before a small horizontal kick-off taper. The output is
    a textbook flat kick rather than a smooth taper-to-point.
    """
    ws = []
    hold_start = 0.78   # start of held near-peak plateau
    kick_start = 0.94   # last ~6% kicks off (small taper to a stubby flat tail)
    kick_end_w = peak * 0.78
    for i in range(n):
        u = i / float(n - 1)
        if u < hold_start:
            # broaden entry -> approach peak, easeInQuad
            f = u / hold_start
            w = entry + (peak - entry) * (f ** 1.3)
        elif u < kick_start:
            # held near-peak plateau (the flat kick proper)
            f = (u - hold_start) / (kick_start - hold_start)
            # bias slightly above peak in the middle of the hold, settle to peak
            w = peak * (1.0 + 0.03 * (1.0 - abs(2 * f - 1)))
        else:
            f = (u - kick_start) / (1.0 - kick_start)
            w = peak - (peak - kick_end_w) * f
        ws.append(w)
    return ws


def width_dian(n, belly=10.0, tail=1.5):
    """点: weighted belly → tapered tail."""
    ws = []
    for i in range(n):
        u = i / float(n - 1)
        if u < 0.45:
            f = u / 0.45
            w = tail + (belly - tail) * (f ** 0.9)
        else:
            f = (u - 0.45) / 0.55
            w = belly - (belly - tail) * (f ** 1.2)
        ws.append(w)
    return ws


# ---------------------------------------------------------------------------
# High-level stroke primitives (centerline geometry + width profile)
# ---------------------------------------------------------------------------

def stroke_heng(t, x0, y0, x1, y1, peak=11.0, shaft=6.5, n=160):
    """Slight upward tilt is the caller's job (set y1 > y0 a touch)."""
    # near-straight Bézier with tiny dipping control points
    mx = 0.5 * (x0 + x1)
    my = 0.5 * (y0 + y1)
    dx = x1 - x0
    # control points just above the chord to make a faint smile
    c1 = (x0 + 0.33 * dx, my + 2.0)
    c2 = (x0 + 0.66 * dx, my + 2.0)
    samples = sample_bezier((x0, y0), c1, c2, (x1, y1), n=n)
    widths = width_heng(n, peak=peak, shaft=shaft)
    draw_width_path(t, samples, widths)


def stroke_shu(t, x0, y0, x1, y1, peak=11.0, shaft=6.5, n=160):
    mx = 0.5 * (x0 + x1)
    my = 0.5 * (y0 + y1)
    # very slight rightward bow for organic shu, or none
    c1 = (mx + 1.0, y0 + 0.33 * (y1 - y0))
    c2 = (mx + 1.0, y0 + 0.66 * (y1 - y0))
    samples = sample_bezier((x0, y0), c1, c2, (x1, y1), n=n)
    widths = width_shu(n, peak=peak, shaft=shaft)
    draw_width_path(t, samples, widths)


def stroke_pie(t, x0, y0, x1, y1, head=12.0, tip=1.5, bow=22.0, n=160):
    """撇: start upper-right, end lower-left, head heavy → fine point."""
    # bow outward (to the upper-left) for the classic 撇 arc
    dx = x1 - x0
    dy = y1 - y0
    # perpendicular (left of chord travel direction): rotate (-dy, dx) and normalize
    import math
    L = math.hypot(dx, dy) or 1.0
    nx, ny = (-dy / L, dx / L)  # left of travel
    c1 = (x0 + 0.33 * dx + nx * bow * 0.6, y0 + 0.33 * dy + ny * bow * 0.6)
    c2 = (x0 + 0.66 * dx + nx * bow * 1.0, y0 + 0.66 * dy + ny * bow * 1.0)
    samples = sample_bezier((x0, y0), c1, c2, (x1, y1), n=n)
    widths = width_pie(n, head=head, tip=tip)
    draw_width_path(t, samples, widths)


def stroke_na(t, x0, y0, x1, y1, entry=2.0, peak=13.0, bow=18.0, n=180):
    """捺: start upper-left, end lower-right; thin → HEAVY at end with held plateau.

    The geometry curves so the last ~12% of the path is nearly
    horizontal (the flat kick) — we bias the second control point
    to pull the tail toward (x1, ~y1) horizontally.
    """
    import math
    dx = x1 - x0
    dy = y1 - y0
    L = math.hypot(dx, dy) or 1.0
    # perpendicular pointing to the LOWER-LEFT relative to travel
    nx, ny = (-dy / L, dx / L)  # left of travel; here that's lower-left-ish
    # First control: gentle outward bow making a 弧度
    c1 = (x0 + 0.30 * dx + nx * bow * 0.3, y0 + 0.30 * dy + ny * bow * 0.3)
    # Second control: pulled toward horizontal near the end so the tail
    # flattens (kick) — same y as the end, slightly inboard in x
    c2 = (x1 - 0.20 * dx, y1 + 2.0)
    samples = sample_bezier((x0, y0), c1, c2, (x1, y1), n=n)
    widths = width_na(n, entry=entry, peak=peak)
    draw_width_path(t, samples, widths)


def stroke_dian(t, x0, y0, x1, y1, belly=10.0, tail=1.5, n=80):
    """点: short rightward-arced dot, weighted belly → tapered tail."""
    dx = x1 - x0
    dy = y1 - y0
    c1 = (x0 + 0.40 * dx + 1.0, y0 + 0.40 * dy - 1.0)
    c2 = (x0 + 0.70 * dx + 1.5, y0 + 0.70 * dy - 1.0)
    samples = sample_bezier((x0, y0), c1, c2, (x1, y1), n=n)
    widths = width_dian(n, belly=belly, tail=tail)
    draw_width_path(t, samples, widths)


# ---------------------------------------------------------------------------
# COMPOUND STROKE PRIMITIVES — continuous-contact, one path
# ---------------------------------------------------------------------------

def stroke_shu_wan(t, x0, y0, corner, x2, y2, n_down=110, n_arc=90,
                   peak=11.0, shaft=6.5, hook_w=8.5):
    """竖弯 (七 stroke 2): vertical descent → smooth right turn → horizontal run.

    Drawn as a SINGLE continuous brushed path. We stitch two Bézier
    segments at the corner; pen contact is never lifted, and at the
    corner we layer a 顿笔 thickening.

    - (x0, y0): start (upper-middle)
    - corner: approximate inner corner where it turns right
    - (x2, y2): end of the rightward run (slight upward flick)
    """
    cx, cy = corner

    # Segment 1: vertical descent, easing into the corner.
    # Control points keep it mostly straight then curve into the turn.
    s1_p0 = (x0, y0)
    s1_p1 = (x0 + 1.0, y0 + 0.40 * (cy - y0))
    s1_p2 = (x0 + 4.0, cy + 0.25 * (y0 - cy))  # start curling toward corner
    s1_p3 = (cx, cy)
    seg1 = sample_bezier(s1_p0, s1_p1, s1_p2, s1_p3, n=n_down)

    # Width along segment 1: 竖-like (weighted top, ~55% shaft, slight
    # thickening as it approaches the corner — the 顿笔 buildup).
    w1 = []
    for i in range(n_down):
        u = i / float(n_down - 1)
        if u < 0.10:
            f = u / 0.10
            w = peak - (peak - shaft) * f
        elif u > 0.85:
            # approach corner: thicken (顿笔)
            f = (u - 0.85) / 0.15
            w = shaft + (peak * 1.05 - shaft) * f
        else:
            w = shaft + 0.5
        w1.append(w)

    # Segment 2: rightward run with a small upward flick at the end.
    s2_p0 = (cx, cy)
    s2_p1 = (cx + 0.30 * (x2 - cx), cy - 1.0)
    s2_p2 = (cx + 0.75 * (x2 - cx), cy + 6.0)
    s2_p3 = (x2, y2)
    seg2 = sample_bezier(s2_p0, s2_p1, s2_p2, s2_p3, n=n_arc)

    w2 = []
    for i in range(n_arc):
        u = i / float(n_arc - 1)
        if u < 0.15:
            # leaving corner: still thick (顿笔 spans the turn)
            f = u / 0.15
            w = peak * 1.05 - (peak * 1.05 - shaft) * f
        elif u > 0.80:
            # final flick (small hook taper)
            f = (u - 0.80) / 0.20
            w = shaft - (shaft - hook_w * 0.4) * f
        else:
            w = shaft + 0.3
        w2.append(w)

    # Draw seg1, then seg2 — without lifting (same endpoint).
    draw_width_path(t, seg1, w1)
    # Continue without lifting beyond the corner sample (already at cx,cy)
    t.penup()
    t.goto(seg2[0])
    t.pendown()
    for i in range(1, len(seg2)):
        w = 0.5 * (w2[i - 1] + w2[i])
        if w < 1.0:
            w = 1.0
        t.pensize(w)
        t.goto(seg2[i])
    t.penup()


def stroke_shu_zhe(t, x0, y0, corner, x2, y2, n_down=120, n_right=110,
                   peak=11.0, shaft=6.5):
    """竖折 (山 stroke 2): vertical down → 90° right at the bottom.

    Drawn as ONE continuous brushed path. The corner is a 顿笔
    (a thickening) — not two disconnected strokes. The geometry is
    nearly straight along each leg, with a brief curve at the corner
    so it reads as a turn rather than a join.

    - (x0, y0): top of the left vertical
    - corner: the bottom-left turn point
    - (x2, y2): right end of the bottom horizontal
    """
    cx, cy = corner

    # Segment 1: vertical descent into the corner.
    s1_p0 = (x0, y0)
    s1_p1 = (x0, y0 + 0.40 * (cy - y0))
    s1_p2 = (x0, y0 + 0.80 * (cy - y0))
    s1_p3 = (cx, cy)
    seg1 = sample_bezier(s1_p0, s1_p1, s1_p2, s1_p3, n=n_down)

    w1 = []
    for i in range(n_down):
        u = i / float(n_down - 1)
        if u < 0.10:
            f = u / 0.10
            w = peak - (peak - shaft) * f
        elif u > 0.82:
            # 顿笔 corner thickening (build up before the turn)
            f = (u - 0.82) / 0.18
            w = shaft + (peak * 1.10 - shaft) * f
        else:
            w = shaft + 0.4
        w1.append(w)

    # Segment 2: bottom horizontal leaving the corner.
    s2_p0 = (cx, cy)
    s2_p1 = (cx + 0.20 * (x2 - cx), cy + 1.0)
    s2_p2 = (cx + 0.70 * (x2 - cx), cy + 1.0)
    s2_p3 = (x2, y2)
    seg2 = sample_bezier(s2_p0, s2_p1, s2_p2, s2_p3, n=n_right)

    w2 = []
    for i in range(n_right):
        u = i / float(n_right - 1)
        if u < 0.18:
            # carry thickness out of the corner (the turn is one 顿笔)
            f = u / 0.18
            w = peak * 1.10 - (peak * 1.10 - shaft) * f
        elif u > 0.88:
            # weighted right end (the bottom heng has a press too)
            f = (u - 0.88) / 0.12
            w = shaft + (peak * 0.95 - shaft) * f
        else:
            w = shaft + 0.3
        w2.append(w)

    draw_width_path(t, seg1, w1)
    t.penup()
    t.goto(seg2[0])
    t.pendown()
    for i in range(1, len(seg2)):
        w = 0.5 * (w2[i - 1] + w2[i])
        if w < 1.0:
            w = 1.0
        t.pensize(w)
        t.goto(seg2[i])
    t.penup()


# ---------------------------------------------------------------------------
# Tasks
# ---------------------------------------------------------------------------

# ── Task 01 | 大 | da
def task_01(t, screen):
    reset_turtle(t)
    # 大 = heng (top) + 撇 + 捺. 撇/捺 share apex on the heng; 撇 longer.
    # Heng: roughly mid-upper, a touch wide.
    stroke_heng(t, -130, 90, 130, 100, peak=11.0, shaft=6.5)
    # 撇: starts at heng center (slightly right of center on heng for shared apex),
    # ends lower-left. 撇 is the longer of the two.
    stroke_pie(t, 10, 85, -170, -150, head=12.0, tip=1.5, bow=26.0)
    # 捺: starts at heng center (sharing apex), ends lower-right, with flat kick.
    stroke_na(t, 10, 85, 170, -140, entry=2.0, peak=13.5, bow=18.0)
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_大.png"))


# ── Task 02 | 入 | ru
def task_02(t, screen):
    reset_turtle(t)
    # 入 = 撇 + 捺. 撇 SHORTER than 人; 捺 starts ON the 撇 partway down
    # (not at top apex) and dominates the right side.
    # 撇 from upper-center down-left, shorter.
    stroke_pie(t, 20, 150, -130, -100, head=12.0, tip=1.5, bow=22.0)
    # 捺 begins ON the 撇 partway down (roughly 30-40% along it),
    # which numerically lands near the upper-center area.
    # 30% along 撇 from start (20,150) toward (-130,-100): (20-45, 150-75) = (-25, 75)
    stroke_na(t, -25, 75, 175, -130, entry=2.0, peak=13.5, bow=18.0)
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "02_入.png"))


# ── Task 03 | 上 | shang
def task_03(t, screen):
    reset_turtle(t)
    # 上 = shu (slightly left of center) + short mid-right heng + long bottom heng.
    # shu: vertical, slightly left of center; top above middle, bottom around bottom heng level.
    stroke_shu(t, -10, 130, -10, -100, peak=11.0, shaft=6.5)
    # mid-right short heng: meets shu around y=20 and extends rightward.
    stroke_heng(t, -10, 20, 110, 25, peak=10.0, shaft=6.0)
    # bottom heng: widest, sits at y=-100, centered.
    stroke_heng(t, -180, -105, 180, -98, peak=11.5, shaft=7.0)
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "03_上.png"))


# ── Task 04 | 下 | xia
def task_04(t, screen):
    reset_turtle(t)
    # 下 = long top heng + center shu + 点 (right of shu, midway down).
    # Top heng: long and high.
    stroke_heng(t, -180, 130, 180, 140, peak=11.5, shaft=7.0)
    # Center shu: starts on heng, descends to lower-mid; centered.
    stroke_shu(t, 0, 125, 0, -120, peak=11.0, shaft=6.5)
    # 点: right of shu, partway down (around y=20), short rightward dot.
    stroke_dian(t, 30, 40, 75, 5, belly=10.0, tail=1.5)
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "04_下.png"))


# ── Task 05 | 七 | qi
def task_05(t, screen):
    reset_turtle(t)
    # 七 = heng (slightly upward tilted, across middle) + compound 竖弯.
    # Heng across middle. Slight upward tilt: y1 > y0.
    stroke_heng(t, -150, 35, 150, 55, peak=11.0, shaft=6.5)
    # Compound stroke 2: starts upper-middle (above the heng), descends
    # through the heng (crossing it), turns RIGHT at the bottom with a
    # 顿笔 corner, ends with a small upward flick on the right.
    # start: upper-middle (above heng); corner at bottom-left of char;
    # end: right side, slightly higher than corner (flick).
    stroke_shu_wan(t,
                   x0=-30, y0=130,
                   corner=(-30, -110),
                   x2=140, y2=-85,
                   peak=11.0, shaft=6.5, hook_w=8.0)
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "05_七.png"))


# ── Task 06 | 山 | shan
def task_06(t, screen):
    reset_turtle(t)
    # 山 = center shu + left compound 竖折 + right shu (slightly shorter).
    # Three verticals connected by the bottom horizontal.
    # Layout: bottom horizontal at y = -120. Three verticals rise from it.
    # Center shu (tallest):
    stroke_shu(t, 0, 150, 0, -120, peak=11.0, shaft=6.5)
    # Left 竖折: left vertical + bottom horizontal as ONE continuous stroke.
    # Top of left vertical lower than center shu top.
    stroke_shu_zhe(t,
                   x0=-130, y0=60,
                   corner=(-130, -120),
                   x2=130, y2=-115,
                   peak=11.0, shaft=6.5)
    # Right shu (slightly shorter than center): top a bit lower; sits on the bottom.
    stroke_shu(t, 130, 80, 130, -110, peak=10.5, shaft=6.2)
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "06_山.png"))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0, 0)

    t = turtle.Turtle()

    for fn in (task_01, task_02, task_03, task_04, task_05, task_06):
        fn(t, screen)

    # Do NOT call screen.bye() or turtle.done() — leave it to the runner.


if __name__ == "__main__":
    main()
