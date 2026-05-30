"""
Cycle 8 — Drawer attempt
6 characters: 大, 入, 工, 王, 火, 中.
Each stroke: cubic-Bezier centerline sampled densely with per-sample pensize.
middle width >= 50% of peak (no narrow waist).
"""

import io
import os
import math
import turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))


# ──────────────────────────────────────────────────────────────────────
# Infrastructure
# ──────────────────────────────────────────────────────────────────────

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


# ──────────────────────────────────────────────────────────────────────
# Bezier with per-sample pen width
# ──────────────────────────────────────────────────────────────────────

def cubic_bezier(p0, p1, p2, p3, n=160):
    pts = []
    for i in range(n + 1):
        u = i / n
        x = ((1 - u) ** 3) * p0[0] + 3 * ((1 - u) ** 2) * u * p1[0] + 3 * (1 - u) * (u ** 2) * p2[0] + (u ** 3) * p3[0]
        y = ((1 - u) ** 3) * p0[1] + 3 * ((1 - u) ** 2) * u * p1[1] + 3 * (1 - u) * (u ** 2) * p2[1] + (u ** 3) * p3[1]
        pts.append((x, y))
    return pts


def width_profile(u, profile, peak, base_floor=0.55):
    """
    Return pensize at parameter u in [0,1].
    profile: a short string keying which family of width modulation to use.
        'heng'   : heavy both ends (entry bump + end press), shaft ≥ 0.6
        'shu'    : heavy both ends, shaft ≥ 0.6
        'pie'    : heavy start, fine end
        'na'     : thin start, heavy flat-kick plateau at end
        'ti'     : heavy start, fine end (like pie but rising)
        'dian'   : thin entry, weighted belly, tapered tail
        'apex'   : symmetric weighted center (for 大 apex stub)
    peak: maximum pensize.
    base_floor: minimum fraction of peak in middle (we use 0.55 minimum).
    """
    if profile == "heng":
        # entry bump 0..0.15, shaft 0.15..0.80, end press 0.80..1.0
        if u < 0.15:
            t = u / 0.15
            w = 0.85 + 0.15 * (1 - (1 - t) ** 2)  # 0.85 → 1.0
        elif u < 0.80:
            # shaft: stay around 0.70–0.78 (>= 0.55)
            t = (u - 0.15) / 0.65
            w = 0.78 - 0.10 * math.sin(t * math.pi) * 0.3  # tiny dip
            w = max(w, 0.66)
        else:
            t = (u - 0.80) / 0.20
            w = 0.78 + 0.22 * (t ** 1.2)  # → ~1.0
    elif profile == "shu":
        if u < 0.15:
            t = u / 0.15
            w = 0.88 + 0.12 * (1 - (1 - t) ** 2)
        elif u < 0.85:
            t = (u - 0.15) / 0.70
            w = 0.75 - 0.08 * math.sin(t * math.pi) * 0.4
            w = max(w, 0.65)
        else:
            t = (u - 0.85) / 0.15
            w = 0.75 + 0.25 * t
    elif profile == "pie":
        # heavy head, fine tail
        if u < 0.10:
            # blunt heavy head
            w = 1.0
        elif u < 0.70:
            t = (u - 0.10) / 0.60
            w = 1.0 - 0.35 * t  # 1.0 → 0.65
        else:
            t = (u - 0.70) / 0.30
            w = 0.65 * (1 - t) + 0.05 * (1 - t)
            w = max(w, 0.05)
    elif profile == "na":
        # thin start → broadening → heavy flat plateau at end
        if u < 0.20:
            t = u / 0.20
            w = 0.10 + 0.45 * t  # 0.10 → 0.55
        elif u < 0.75:
            t = (u - 0.20) / 0.55
            w = 0.55 + 0.40 * t  # 0.55 → 0.95
        elif u < 0.92:
            # plateau near peak
            w = 1.0
        else:
            t = (u - 0.92) / 0.08
            w = 1.0 - 0.6 * t  # quick taper for flat-kick exit tip
    elif profile == "ti":
        # heavy base start → fine flick end
        if u < 0.10:
            w = 1.0
        elif u < 0.75:
            t = (u - 0.10) / 0.65
            w = 1.0 - 0.40 * t
        else:
            t = (u - 0.75) / 0.25
            w = 0.60 * (1 - t)
            w = max(w, 0.08)
    elif profile == "dian":
        # thin entry, weighted belly, tapered tail
        if u < 0.30:
            t = u / 0.30
            w = 0.30 + 0.55 * t  # 0.30 → 0.85
        elif u < 0.65:
            w = 1.0
        else:
            t = (u - 0.65) / 0.35
            w = 1.0 - 0.85 * t  # → 0.15
            w = max(w, 0.10)
    elif profile == "apex":
        w = 0.5 + 0.5 * math.sin(math.pi * u)
        w = max(w, 0.55)
    else:
        w = 0.85

    w = max(w, 0.05)
    return w * peak


def stroke_bezier(t, p0, p1, p2, p3, peak=14, profile="heng",
                  corner_boost=None, samples=160):
    """
    Draw a Bezier centerline with per-sample pensize.
    corner_boost: optional dict {'u': 0.5, 'sigma': 0.08, 'factor': 1.55}
                  Gaussian bump at parameter u for compound strokes' 顿笔.
    """
    pts = cubic_bezier(p0, p1, p2, p3, n=samples)
    for i, (x, y) in enumerate(pts):
        u = i / samples
        w = width_profile(u, profile, peak)
        if corner_boost is not None:
            cu = corner_boost.get("u", 0.5)
            sigma = corner_boost.get("sigma", 0.08)
            factor = corner_boost.get("factor", 1.55)
            bump = (factor - 1.0) * math.exp(-((u - cu) ** 2) / (2 * sigma ** 2))
            w *= (1.0 + bump)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.pensize(max(w, 1))
        t.goto(x, y)
        # draw a tiny segment forward for a dot at this sample
        # Actually a single dot from goto won't render — use t.dot:
        t.dot(max(w, 1))
    t.penup()


def compound_stroke(t, segments, peak=14, profile_list=None,
                    corner_boost=None, samples_each=120):
    """
    Compound stroke: a list of cubic segments drawn as one continuous brush.
    Each segment is (p0,p1,p2,p3). corner_boost applies at the boundary
    between segments[i] and segments[i+1] (global u of that boundary).
    """
    n_seg = len(segments)
    all_pts = []
    seg_boundaries = []  # global u at boundaries
    for seg in segments:
        pts = cubic_bezier(*seg, n=samples_each)
        if all_pts:
            pts = pts[1:]  # drop dup start
        all_pts.extend(pts)
    total = len(all_pts)
    # compute boundary indices
    boundaries = []
    acc = 0
    for i, seg in enumerate(segments[:-1]):
        acc += samples_each + 1 if i == 0 else samples_each
        boundaries.append(acc / total)

    if profile_list is None:
        profile_list = ["heng"] * n_seg

    # For width: piecewise apply each segment's profile across its range
    # boundaries split total into n_seg pieces
    seg_ranges = []
    start = 0
    for i in range(n_seg):
        # end index of seg i
        if i == 0:
            end = samples_each
        else:
            end = start + samples_each
        seg_ranges.append((start, end))
        start = end

    for idx, (x, y) in enumerate(all_pts):
        # find which segment
        seg_i = 0
        for j, (s, e) in enumerate(seg_ranges):
            if idx <= e:
                seg_i = j
                break
        s, e = seg_ranges[seg_i]
        local_u = (idx - s) / max(1, (e - s))
        w = width_profile(local_u, profile_list[seg_i], peak)
        # apply corner boost(s)
        if corner_boost is not None:
            global_u = idx / (total - 1)
            for cb in (corner_boost if isinstance(corner_boost, list) else [corner_boost]):
                cu = cb.get("u", 0.5)
                sigma = cb.get("sigma", 0.05)
                factor = cb.get("factor", 1.55)
                bump = (factor - 1.0) * math.exp(-((global_u - cu) ** 2) / (2 * sigma ** 2))
                w *= (1.0 + bump)
        t.penup()
        t.goto(x, y)
        t.dot(max(w, 1))


# ──────────────────────────────────────────────────────────────────────
# Tasks
# ──────────────────────────────────────────────────────────────────────

# ── Task 01 | 大 | dà
def task_01(t, screen):
    """
    大 — apex at y=+200, heng at y=+50, limb tails at y=-200.
    Heng spans >= 2.0× the limb-crossing span.
    Strokes:
      1) heng (very long, ~700 wide)
      2) pie (apex top → lower-left tail)
      3) na  (apex top → lower-right tail with flat kick)
    """
    reset_turtle(t)

    # Heng at y=+50, from (-280,+50) to (+280,+50)  → width 560.
    # At heng height, pie & na cross at x ≈ ±100.  Limb-span ≈ 200.
    # Heng (560) / limb-span (200) = 2.8× ≥ 2.0. ✓
    stroke_bezier(
        t,
        p0=(-280, 45),
        p1=(-90, 55),
        p2=(90, 55),
        p3=(280, 50),
        peak=15, profile="heng", samples=180,
    )

    # Apex at (0, +210).  Limbs cross heng at (-100,+50) and (+100,+50).
    # Tails at (-260, -200) and (+260, -200).

    # 撇: from apex down-left.  Start heavy at top, taper.
    stroke_bezier(
        t,
        p0=(0, 210),
        p1=(-70, 130),
        p2=(-170, 20),
        p3=(-260, -200),
        peak=15, profile="pie", samples=180,
    )

    # 捺: from apex down-right.  Thin start, heavy flat-kick at tail.
    stroke_bezier(
        t,
        p0=(0, 210),
        p1=(70, 130),
        p2=(170, 20),
        p3=(280, -205),
        peak=16, profile="na", samples=180,
    )

    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_大.png"))


# ── Task 02 | 入 | rù
def task_02(t, screen):
    """
    入 — amplified asymmetry.
    撇 heavier+longer; junction at ~50% down 撇.
    捺 tail extends further to lower-right than 撇 tail extends lower-left.
    """
    reset_turtle(t)

    # 撇: top apex around (+40, +220), sweep down-left to (-280, -240).
    # The 撇 is the dominant stroke.
    pie_p0 = (40, 220)
    pie_p1 = (-20, 130)
    pie_p2 = (-150, 0)
    pie_p3 = (-280, -240)
    stroke_bezier(
        t,
        p0=pie_p0, p1=pie_p1, p2=pie_p2, p3=pie_p3,
        peak=17, profile="pie", samples=200,
    )

    # Find midpoint of 撇 (u=0.5) — that's the junction for 捺.
    # u=0.5 cubic point:
    def bez_pt(u, p0, p1, p2, p3):
        x = ((1 - u) ** 3) * p0[0] + 3 * ((1 - u) ** 2) * u * p1[0] + 3 * (1 - u) * (u ** 2) * p2[0] + (u ** 3) * p3[0]
        y = ((1 - u) ** 3) * p0[1] + 3 * ((1 - u) ** 2) * u * p1[1] + 3 * (1 - u) * (u ** 2) * p2[1] + (u ** 3) * p3[1]
        return (x, y)

    junction = bez_pt(0.5, pie_p0, pie_p1, pie_p2, pie_p3)
    # junction ~ (-72, 27).  Now 捺 starts at junction, ends at (+310, -250).
    stroke_bezier(
        t,
        p0=junction,
        p1=(20, -10),
        p2=(170, -120),
        p3=(310, -250),
        peak=18, profile="na", samples=200,
    )

    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "02_入.png"))


# ── Task 03 | 工 | gōng
def task_03(t, screen):
    """
    工 — top heng + center shu + bottom heng.
    Top heng slightly shorter than bottom; shu vertical between them.
    """
    reset_turtle(t)

    # Top heng: y=+180, x in [-180, +180]  (width 360)
    stroke_bezier(
        t,
        p0=(-180, 175),
        p1=(-60, 185),
        p2=(60, 185),
        p3=(180, 180),
        peak=14, profile="heng", samples=160,
    )

    # Bottom heng: y=-180, x in [-220, +220]  (width 440, widest)
    stroke_bezier(
        t,
        p0=(-220, -185),
        p1=(-70, -175),
        p2=(70, -175),
        p3=(220, -180),
        peak=15, profile="heng", samples=160,
    )

    # Center shu: vertical from (0,+170) to (0,-170)
    stroke_bezier(
        t,
        p0=(0, 170),
        p1=(2, 80),
        p2=(-2, -80),
        p3=(0, -170),
        peak=14, profile="shu", samples=160,
    )

    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "03_工.png"))


# ── Task 04 | 王 | wáng
def task_04(t, screen):
    """
    王 — top heng + middle heng (shortest) + bottom heng (widest)
         + center shu crossing all three.
    """
    reset_turtle(t)

    # Top heng: y=+200, width 380
    stroke_bezier(
        t,
        p0=(-190, 195),
        p1=(-60, 205),
        p2=(60, 205),
        p3=(190, 200),
        peak=14, profile="heng", samples=160,
    )

    # Middle heng (shortest): y=0, width 280
    stroke_bezier(
        t,
        p0=(-140, -5),
        p1=(-40, 5),
        p2=(40, 5),
        p3=(140, 0),
        peak=13, profile="heng", samples=160,
    )

    # Bottom heng (widest): y=-200, width 440
    stroke_bezier(
        t,
        p0=(-220, -205),
        p1=(-70, -195),
        p2=(70, -195),
        p3=(220, -200),
        peak=15, profile="heng", samples=160,
    )

    # Center shu crossing all three: from (0,+200) to (0,-200)
    stroke_bezier(
        t,
        p0=(0, 195),
        p1=(2, 80),
        p2=(-2, -80),
        p3=(0, -195),
        peak=14, profile="shu", samples=180,
    )

    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "04_王.png"))


# ── Task 05 | 火 | huǒ
def task_05(t, screen):
    """
    火 — left 点 (tilted) + right 点 (tilted other way)
         + 撇 (left of center, from center-top sweeping down-left)
         + 捺 (right of center, from center-top sweeping down-right with flat tail).
    """
    reset_turtle(t)

    # Left 点: top-left area, tilted from upper-right to lower-left
    stroke_bezier(
        t,
        p0=(-130, 230),
        p1=(-145, 200),
        p2=(-165, 170),
        p3=(-180, 140),
        peak=14, profile="dian", samples=120,
    )

    # Right 点: top-right area, tilted from upper-left to lower-right
    stroke_bezier(
        t,
        p0=(130, 230),
        p1=(145, 200),
        p2=(165, 170),
        p3=(180, 140),
        peak=14, profile="dian", samples=120,
    )

    # 撇: head near center-top (slightly left), sweep down-left
    stroke_bezier(
        t,
        p0=(-20, 100),
        p1=(-80, 30),
        p2=(-160, -80),
        p3=(-240, -220),
        peak=15, profile="pie", samples=180,
    )

    # 捺: head near center-top (slightly right of 撇 head), sweep down-right
    # with flat-kick tail.
    stroke_bezier(
        t,
        p0=(20, 100),
        p1=(80, 30),
        p2=(170, -80),
        p3=(260, -220),
        peak=16, profile="na", samples=180,
    )

    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "05_火.png"))


# ── Task 06 | 中 | zhōng
def task_06(t, screen):
    """
    中 — outer frame (3 strokes) + long center shu.
    Frame:
      - left shu (frame left edge)
      - 横折 (top edge + right edge) as ONE continuous compound stroke
        with 顿笔 thickening at upper-right corner
      - bottom heng (closes the frame)
    Then long center shu extending well above and below the frame.
    """
    reset_turtle(t)

    # Frame dimensions: x in [-130, +130], y in [-80, +120]
    LEFT_X = -130
    RIGHT_X = 130
    TOP_Y = 120
    BOT_Y = -80

    # Left shu: from (LEFT_X, TOP_Y) to (LEFT_X, BOT_Y).
    stroke_bezier(
        t,
        p0=(LEFT_X, TOP_Y),
        p1=(LEFT_X - 2, TOP_Y - 60),
        p2=(LEFT_X + 2, BOT_Y + 60),
        p3=(LEFT_X, BOT_Y),
        peak=14, profile="shu", samples=160,
    )

    # 横折 compound: top edge (heng) then right edge (shu).
    # As ONE continuous brushed path with 顿笔 at the upper-right corner.
    seg_top = (
        (LEFT_X, TOP_Y),
        (LEFT_X + 80, TOP_Y + 5),
        (RIGHT_X - 80, TOP_Y + 5),
        (RIGHT_X, TOP_Y),
    )
    seg_right = (
        (RIGHT_X, TOP_Y),
        (RIGHT_X + 2, TOP_Y - 60),
        (RIGHT_X - 2, BOT_Y + 60),
        (RIGHT_X, BOT_Y),
    )
    compound_stroke(
        t,
        segments=[seg_top, seg_right],
        peak=14,
        profile_list=["heng", "shu"],
        corner_boost={"u": 0.5, "sigma": 0.06, "factor": 1.55},
        samples_each=140,
    )

    # Bottom heng: closes the frame.
    stroke_bezier(
        t,
        p0=(LEFT_X, BOT_Y),
        p1=(LEFT_X + 80, BOT_Y - 4),
        p2=(RIGHT_X - 80, BOT_Y - 4),
        p3=(RIGHT_X, BOT_Y),
        peak=14, profile="heng", samples=160,
    )

    # Long center shu: extends well above AND below frame.
    # Frame spans y in [-80, +120]; shu spans y in [-240, +240].
    stroke_bezier(
        t,
        p0=(0, 240),
        p1=(2, 100),
        p2=(-2, -100),
        p3=(0, -240),
        peak=15, profile="shu", samples=220,
    )

    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "06_中.png"))


# ──────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────

def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0, 0)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pencolor("black")
    t.pensize(3)

    tasks = [task_01, task_02, task_03, task_04, task_05, task_06]
    for fn in tasks:
        fn(t, screen)

    # Do not call screen.bye() / turtle.done() / mainloop()


if __name__ == "__main__":
    main()
