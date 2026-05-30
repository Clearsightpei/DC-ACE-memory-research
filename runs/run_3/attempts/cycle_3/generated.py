"""
Cycle 3 — Phase-2 entry: simple character composition.

Each character is composed from brushed atomic-stroke primitives.
Each primitive renders the centerline as a cubic Bézier sampled at
~150 points with per-sample `pensize` for true width modulation, plus
filled discs at start/end (顿笔) and a fine taper where appropriate.

Coordinate convention: turtle screen with origin (0,0) at center.
Tasks all start at (0,0) heading 90°.
"""

import io, os, math, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))


# ─── canvas plumbing ──────────────────────────────────────────────────────

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


# ─── Bézier sampler ───────────────────────────────────────────────────────

def cubic_bezier(p0, p1, p2, p3, n=150):
    """Sample a cubic Bézier at n+1 evenly-spaced t."""
    pts = []
    for i in range(n + 1):
        u = i / n
        x = ((1 - u) ** 3) * p0[0] + 3 * ((1 - u) ** 2) * u * p1[0] \
            + 3 * (1 - u) * u * u * p2[0] + u ** 3 * p3[0]
        y = ((1 - u) ** 3) * p0[1] + 3 * ((1 - u) ** 2) * u * p1[1] \
            + 3 * (1 - u) * u * u * p2[1] + u ** 3 * p3[1]
        pts.append((x, y))
    return pts


def stamp_disc(t, x, y, radius):
    """Filled disc at (x,y) — used for 顿笔 weighted heads/feet."""
    t.penup(); t.goto(x, y - radius); t.setheading(0)
    t.pendown(); t.begin_fill(); t.circle(radius); t.end_fill()
    t.penup()


def draw_bezier_varwidth(t, p0, p1, p2, p3, widths, n=150):
    """
    Render Bézier with per-sample pensize. `widths` is a function
    (u in [0,1]) -> half-pen radius. We use `pensize` directly because
    turtle draws stroke-centered lines.
    """
    pts = cubic_bezier(p0, p1, p2, p3, n)
    t.penup(); t.goto(pts[0]); t.pendown()
    for i, (x, y) in enumerate(pts):
        u = i / n
        w = max(1, widths(u))
        t.pensize(w)
        t.goto(x, y)
    t.penup()


# ─── atomic-stroke recipes (per drawer_memory.md) ─────────────────────────

def stroke_heng(t, cx, cy, length, peak=14, tilt=0.04):
    """
    横 heng: weighted rounded entry → thinner middle → weighted end press,
    faint upward tilt (left low, right high).  cx,cy = midpoint.
    `peak` = max pen radius at the press regions.
    """
    half = length / 2
    # endpoints, slight upward tilt to the right
    x0, y0 = cx - half, cy - tilt * half
    x3, y3 = cx + half, cy + tilt * half
    # near-straight: control pts on the line, no curvature
    x1, y1 = cx - half * 0.4, cy - tilt * half * 0.4
    x2, y2 = cx + half * 0.4, cy + tilt * half * 0.4

    def widths(u):
        # weighted entry (~u<0.12), thin middle, weighted end (~u>0.85)
        if u < 0.12:
            return peak - (peak - peak * 0.55) * (u / 0.12)
        if u > 0.85:
            return peak * 0.55 + (peak - peak * 0.55) * ((u - 0.85) / 0.15)
        # middle: gently thin
        m = (u - 0.12) / 0.73
        return peak * 0.55 - peak * 0.10 * math.sin(math.pi * m)

    # 顿笔 caps
    stamp_disc(t, x0, y0, peak * 0.55)
    draw_bezier_varwidth(t, (x0, y0), (x1, y1), (x2, y2), (x3, y3), widths)
    stamp_disc(t, x3, y3, peak * 0.75)


def stroke_shu(t, cx, cy, length, peak=14):
    """
    竖 shu: weighted bulb top → thin middle → weighted foot. Spine straight.
    cx,cy = midpoint.
    """
    half = length / 2
    x0, y0 = cx, cy + half          # top
    x3, y3 = cx, cy - half          # bottom
    x1, y1 = cx, cy + half * 0.4
    x2, y2 = cx, cy - half * 0.4

    def widths(u):
        if u < 0.12:
            return peak - (peak - peak * 0.55) * (u / 0.12)
        if u > 0.85:
            return peak * 0.55 + (peak - peak * 0.55) * ((u - 0.85) / 0.15)
        m = (u - 0.12) / 0.73
        return peak * 0.55 - peak * 0.10 * math.sin(math.pi * m)

    stamp_disc(t, x0, y0, peak * 0.7)
    draw_bezier_varwidth(t, (x0, y0), (x1, y1), (x2, y2), (x3, y3), widths)
    stamp_disc(t, x3, y3, peak * 0.65)


def stroke_pie(t, x_start, y_start, x_end, y_end, peak=16):
    """
    撇 pie: weighted head upper-right → gentle bow → fine taper to a point
    at lower-left. Large-radius, small arc extent (NOT tight).
    """
    # control points: bias slightly to give a gentle bow (bulging down-right)
    dx, dy = x_end - x_start, y_end - y_start
    # perpendicular bow: small offset to the lower-right of the chord
    px, py = -dy, dx              # perpendicular vector
    norm = math.hypot(px, py) or 1
    bow = 0.08                     # gentle, large-radius bow
    bx, by = (px / norm) * bow * math.hypot(dx, dy), (py / norm) * bow * math.hypot(dx, dy)
    # Want bow toward lower-right (more positive x, less y) — adjust sign
    # so the control points pull the curve below-right of the chord.
    if bx < 0:
        bx, by = -bx, -by
    x1 = x_start + dx * 0.33 + bx * 0.6
    y1 = y_start + dy * 0.33 + by * 0.6
    x2 = x_start + dx * 0.66 + bx * 0.4
    y2 = y_start + dy * 0.66 + by * 0.4

    def widths(u):
        # weighted head, taper to a fine point at the tail
        if u < 0.10:
            return peak - (peak - peak * 0.78) * (u / 0.10)
        # smooth taper to ~1 by u=1
        return max(1, peak * 0.78 * (1 - ((u - 0.10) / 0.90) ** 1.4))

    stamp_disc(t, x_start, y_start, peak * 0.6)
    draw_bezier_varwidth(t, (x_start, y_start), (x1, y1), (x2, y2), (x_end, y_end), widths)
    # no foot disc — tail is fine


def stroke_na(t, x_start, y_start, x_end, y_end, peak=18):
    """
    捺 na: thin entry → broadening belly → flat pressed tail (顿笔 kick)
    at lower-right.  Slight downward bow.
    """
    dx, dy = x_end - x_start, y_end - y_start
    # bow toward lower-left (curve sags down)
    px, py = -dy, dx
    norm = math.hypot(px, py) or 1
    bow = 0.06
    bx, by = (px / norm) * bow * math.hypot(dx, dy), (py / norm) * bow * math.hypot(dx, dy)
    # we want curve to bow downward (below chord)
    if by > 0:
        bx, by = -bx, -by
    x1 = x_start + dx * 0.33 + bx * 0.5
    y1 = y_start + dy * 0.33 + by * 0.5
    x2 = x_start + dx * 0.66 + bx * 0.3
    y2 = y_start + dy * 0.66 + by * 0.3

    def widths(u):
        # thin entry, broadening, peak just before the tail
        if u < 0.15:
            return max(2, peak * (0.20 + 0.40 * (u / 0.15)))
        if u < 0.78:
            return peak * (0.60 + 0.40 * ((u - 0.15) / 0.63))
        # last 22%: hold peak then a small flat kick at the very end
        return peak * 1.0

    # thin entry — no big disc at start
    stamp_disc(t, x_start, y_start, peak * 0.18)
    draw_bezier_varwidth(t, (x_start, y_start), (x1, y1), (x2, y2), (x_end, y_end), widths)
    # flat pressed tail (kick to the right) — short horizontal extension
    # to produce the characteristic 捺 foot
    t.penup(); t.goto(x_end, y_end); t.setheading(0)
    kick_len = peak * 1.6
    t.pensize(peak)
    t.pendown(); t.forward(kick_len); t.penup()
    # cap the tail
    stamp_disc(t, x_end + kick_len, y_end, peak * 0.55)


# ─── task functions ───────────────────────────────────────────────────────

# ── Task 01 | 一 | yi
def task_01(t):
    # one heng centered, generous length
    stroke_heng(t, cx=0, cy=0, length=380, peak=16, tilt=0.04)


# ── Task 02 | 二 | er
def task_02(t):
    # two heng stacked; bottom longer than top
    # top heng (shorter), bottom heng (longer)
    stroke_heng(t, cx=0, cy=90,  length=240, peak=14, tilt=0.04)
    stroke_heng(t, cx=0, cy=-90, length=360, peak=16, tilt=0.04)


# ── Task 03 | 三 | san
def task_03(t):
    # three heng; bottom longest, middle shortest, top medium
    stroke_heng(t, cx=0, cy=140,  length=280, peak=14, tilt=0.04)  # top medium
    stroke_heng(t, cx=0, cy=0,    length=200, peak=13, tilt=0.04)  # middle shortest
    stroke_heng(t, cx=0, cy=-140, length=380, peak=16, tilt=0.04)  # bottom longest


# ── Task 04 | 十 | shi
def task_04(t):
    # heng + shu crossing at center; shu extends slightly more below
    stroke_heng(t, cx=0,  cy=0,   length=360, peak=15, tilt=0.04)
    # shu centered with offset: top y=+170, bottom y=-210 (more below)
    # use stroke_shu with cx=0, cy=-20, length=380 → top 170, bottom -210
    stroke_shu(t, cx=0, cy=-20, length=380, peak=16)


# ── Task 05 | 人 | ren
def task_05(t):
    # 撇 + 捺 sharing top apex; 撇 starts higher and is longer than 捺
    apex_x, apex_y = 0, 180
    # 撇: from apex going lower-left, longer
    pie_end_x, pie_end_y = -180, -200
    stroke_pie(t, apex_x, apex_y, pie_end_x, pie_end_y, peak=16)
    # 捺: from same apex going lower-right, shorter (starts slightly lower visually
    # is the rule; per memory '撇 starts higher AND is longer than 捺'.
    # We use a shorter chord; start at apex (shared) and end nearer.
    na_start_x, na_start_y = 0, 140      # slightly below apex (visually shorter)
    na_end_x, na_end_y = 130, -160
    stroke_na(t, na_start_x, na_start_y, na_end_x, na_end_y, peak=16)


# ── Task 06 | 八 | ba
def task_06(t):
    # 撇 + 捺 with a gap at the top (NO shared apex — unlike 人)
    # 撇 on the left
    stroke_pie(t, x_start=-50, y_start=140, x_end=-200, y_end=-180, peak=15)
    # 捺 on the right, starts at a separate point (gap at top)
    stroke_na(t, x_start=50, y_start=140, x_end=200, y_end=-160, peak=16)


# ─── main ─────────────────────────────────────────────────────────────────

TASKS = [
    ("01", "一", task_01),
    ("02", "二", task_02),
    ("03", "三", task_03),
    ("04", "十", task_04),
    ("05", "人", task_05),
    ("06", "八", task_06),
]


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0, 0)
    t = turtle.Turtle()

    for idx, ch, fn in TASKS:
        reset_turtle(t)
        fn(t)
        screen.update()
        out_path = os.path.join(OUT_DIR, f"{idx}_{ch}.png")
        save_canvas_to_png(screen, out_path)


if __name__ == "__main__":
    main()
