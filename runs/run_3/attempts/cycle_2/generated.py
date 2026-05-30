"""
Cycle 2 — Drawer attempt (run_3).

Post-reflection confirmation of the six atomic strokes from cycle 1.
Judged by reference-free Claude-vision calligraphy rubric:
顿笔 (weighted pause), 弧度 (curvature), 粗细 (taper), proportion, overall.

Approach (carried over from cycle 1 memory — scored 9–10/10):
  - Centerline is a smooth Bézier-ish path sampled densely (many tiny
    segments). At each sample we set `pensize(...)` so width modulates
    along the stroke (the single biggest win — uniform pensize scores 3–4).
  - Every stroke has a weighted rounded 顿笔 at the start and a weighted
    pressed 顿笔 at the end (or a real taper to a fine point where the
    stroke is supposed to terminate fine: 撇 tail, 提 flick).
  - 弧度: 横/竖 stay near-straight (correct). 撇/提 get a *gentle* large-
    radius bow (cycle-1 弧度=1 → aim for richer curvature this cycle).
"""

import io
import os
import turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))


# ----------------------------------------------------------------------
# Infrastructure
# ----------------------------------------------------------------------

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


# ----------------------------------------------------------------------
# Brush helpers — vary pensize along a path to fake calligraphic width
# ----------------------------------------------------------------------

def _bezier_point(p0, p1, p2, p3, s):
    """Cubic Bezier at parameter s in [0,1]."""
    u = 1.0 - s
    x = (u * u * u * p0[0]
         + 3 * u * u * s * p1[0]
         + 3 * u * s * s * p2[0]
         + s * s * s * p3[0])
    y = (u * u * u * p0[1]
         + 3 * u * u * s * p1[1]
         + 3 * u * s * s * p2[1]
         + s * s * s * p3[1])
    return x, y


def stroke_along_bezier(t, p0, p1, p2, p3, width_fn, steps=140):
    """Walk a cubic Bezier and re-pensize at every sample.

    width_fn(s) -> pensize in points for parameter s in [0, 1].
    顿笔 is achieved by making width_fn fat & rounded at the ends; taper
    is achieved by making width_fn -> ~0 at the relevant end.
    """
    t.penup()
    x0, y0 = _bezier_point(p0, p1, p2, p3, 0.0)
    t.goto(x0, y0)
    t.pensize(max(1, width_fn(0.0)))
    t.pendown()
    for i in range(1, steps + 1):
        s = i / steps
        w = max(1, width_fn(s))
        t.pensize(w)
        x, y = _bezier_point(p0, p1, p2, p3, s)
        t.goto(x, y)
    t.penup()


def dot_blob(t, x, y, radius):
    """Round 顿笔 cap — draw a filled disc by stacking circles."""
    t.penup()
    t.goto(x, y - radius)
    t.setheading(0)
    t.pensize(1)
    t.fillcolor("black")
    t.begin_fill()
    t.pendown()
    t.circle(radius)
    t.end_fill()
    t.penup()


# ----------------------------------------------------------------------
# Width profiles
# ----------------------------------------------------------------------

def _smoothstep(s):
    """Hermite smoothstep, s in [0,1]."""
    s = max(0.0, min(1.0, s))
    return s * s * (3 - 2 * s)


def width_weighted_both_ends(s, w_start=22, w_mid=11, w_end=22):
    """顿笔 at both ends, thinner middle (横, 竖, 点 belly)."""
    # Two-lobe profile: weight at s=0 and s=1, thin around s=0.5.
    # Use a cosine-ish well.
    import math
    well = (1 - math.cos(2 * math.pi * s)) / 2.0  # 0 at ends, 1 in middle
    # Interpolate: at well=0 use end weights, at well=1 use w_mid.
    end_w = w_start + (w_end - w_start) * s
    return end_w * (1 - well) + w_mid * well


def width_taper_to_end(s, w_start=24, w_end=2):
    """Thick weighted head, smooth taper to a fine point (撇)."""
    # Slight belly: heavy near s=0, narrow ramp toward end.
    # Use eased curve so the head feels rounded, not a wedge.
    eased = _smoothstep(s)
    return w_start * (1 - eased) + w_end * eased


def width_taper_to_start(s, w_start=2, w_end=24):
    """Fine entry, weighted pressed end (提 reversed — actually 提 has
    weighted base then taper UP-out; we use this for the 捺 broadening
    and an inverse for 提)."""
    eased = _smoothstep(s)
    return w_start * (1 - eased) + w_end * eased


def width_na_profile(s):
    """捺: thin entry → broadening belly → flattened pressed tail (顿笔
    kick) at the very end. Three-segment: ramp, belly, end press."""
    if s < 0.55:
        # Ramp from very thin to thick belly.
        a = s / 0.55
        return 3 + 22 * _smoothstep(a)
    elif s < 0.85:
        # Belly stays heavy.
        return 25
    else:
        # Final pressed kick — slight extra weight then leveling.
        a = (s - 0.85) / 0.15
        return 25 + 6 * _smoothstep(a)


def width_ti_profile(s):
    """提: weighted rounded base → strong taper to a fine flicked point."""
    # Start heavy at s=0, taper smoothly to near zero by s=1.
    eased = _smoothstep(s)
    return 24 * (1 - eased) + 2 * eased


def width_dian_profile(s):
    """点 teardrop: thin entry broadening to weighted rounded belly,
    then slight reduction near the tail (compact)."""
    import math
    # Asymmetric: small at s=0, peak around s=0.7, slight drop at tail.
    peak = 1 - (s - 0.7) ** 2 / 0.5
    peak = max(0.0, peak)
    return 4 + 22 * peak


# ----------------------------------------------------------------------
# Tasks
# ----------------------------------------------------------------------

# ── Task 01 | 点 | dian
def task_01(t):
    """点 dian — short teardrop. Thin upper-left entry, broadens to a
    rounded weighted belly lower-right; slight gentle curve."""
    # A small diagonal stroke from upper-left to lower-right.
    p0 = (-35, 50)
    p1 = (-15, 40)
    p2 = (15, 0)
    p3 = (45, -30)
    stroke_along_bezier(t, p0, p1, p2, p3, width_dian_profile, steps=120)
    # Round off the weighted belly (顿笔) with a small filled disc.
    dot_blob(t, 38, -25, 13)


# ── Task 02 | 横 | heng
def task_02(t):
    """横 heng — horizontal. Weighted rounded entry left, thinner middle,
    weighted pressed end right. Faint upward tilt; near-straight (弧度
    intentionally low)."""
    p0 = (-220, -10)
    p1 = (-110, -2)   # very slight upward control
    p2 = (110, 6)
    p3 = (220, 12)    # faint upward tilt
    stroke_along_bezier(
        t,
        p0, p1, p2, p3,
        lambda s: width_weighted_both_ends(s, w_start=22, w_mid=10, w_end=24),
        steps=180,
    )
    # Rounded 顿笔 caps to make the heads truly rounded, not cropped.
    dot_blob(t, -220, -10, 11)
    dot_blob(t, 220, 12, 13)


# ── Task 03 | 竖 | shu
def task_03(t):
    """竖 shu — vertical. Weighted bulb at top and foot, thinner middle,
    straight true spine. Slight foot weight emphasizes the 顿笔."""
    p0 = (0, 200)
    p1 = (0, 80)
    p2 = (0, -80)
    p3 = (0, -200)
    stroke_along_bezier(
        t,
        p0, p1, p2, p3,
        lambda s: width_weighted_both_ends(s, w_start=22, w_mid=9, w_end=26),
        steps=180,
    )
    # Rounded caps for clean 顿笔 read.
    dot_blob(t, 0, 200, 11)
    dot_blob(t, 0, -200, 14)


# ── Task 04 | 撇 | pie
def task_04(t):
    """撇 pie — left-falling. Strong weighted head upper-right, smooth
    taper to a fine point lower-left. Add a *gentle* natural bow this
    cycle (curator note: 弧度 was only 1)."""
    # Path bows leftward in the middle — gentle large-radius arc, not
    # a tight curl. End really tapers to a fine point (no end blob).
    p0 = (140, 180)
    p1 = (60, 110)     # bow control — push slightly left of straight
    p2 = (-50, 20)     # bow control — continue gentle leftward curve
    p3 = (-180, -180)
    stroke_along_bezier(t, p0, p1, p2, p3, width_taper_to_end, steps=180)
    # Weighted rounded head 顿笔 at start.
    dot_blob(t, 140, 180, 13)


# ── Task 05 | 捺 | na
def task_05(t):
    """捺 na — right-falling. Thin entry upper-left, broadening belly,
    flattened pressed 顿笔 kick at lower-right."""
    p0 = (-160, 170)
    p1 = (-60, 90)
    p2 = (50, 0)
    p3 = (200, -150)
    stroke_along_bezier(t, p0, p1, p2, p3, width_na_profile, steps=200)
    # Pressed tail: a small horizontal flat at the end emphasises 捺's
    # signature kick. Done with a couple of overstrokes that extend
    # slightly past the bezier endpoint, leveling off horizontally.
    t.penup()
    t.goto(200, -150)
    t.setheading(0)  # head right (flat)
    t.pensize(28)
    t.pendown()
    t.forward(22)
    t.pensize(22)
    t.forward(10)
    t.pensize(14)
    t.forward(8)
    t.pensize(6)
    t.forward(6)
    t.penup()


# ── Task 06 | 提 | ti
def task_06(t):
    """提 ti — rising flick. Weighted rounded base lower-left, strong
    taper to a fine flicked point upper-right. Add a *gentle* natural
    rise-curve (curator note: 弧度 was only 1)."""
    # Path arcs upward gently — a large-radius rise, not a tight curl.
    p0 = (-150, -100)
    p1 = (-70, -70)    # slight droop early → emphasises base weight
    p2 = (40, 0)       # rises through middle
    p3 = (170, 110)    # flicks upper-right
    stroke_along_bezier(t, p0, p1, p2, p3, width_ti_profile, steps=180)
    # Weighted rounded base 顿笔.
    dot_blob(t, -150, -100, 13)


# ----------------------------------------------------------------------
# Driver
# ----------------------------------------------------------------------

TASKS = [
    ("01", "dian", task_01),
    ("02", "heng", task_02),
    ("03", "shu",  task_03),
    ("04", "pie",  task_04),
    ("05", "na",   task_05),
    ("06", "ti",   task_06),
]


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0, 0)

    t = turtle.Turtle()
    for idx, key, fn in TASKS:
        reset_turtle(t)
        fn(t)
        screen.update()
        out_path = os.path.join(OUT_DIR, f"{idx}_{key}.png")
        save_canvas_to_png(screen, out_path)


if __name__ == "__main__":
    main()
