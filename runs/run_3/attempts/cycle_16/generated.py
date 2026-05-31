"""Cycle 16 — Drawer attempts.

Tasks:
  01 也  (carry-over: smooth bezier, no dot-stamp artifacts)
  02 巴  (carry-over: TALLER frame, hook extends below)
  03 见  (carry-over: long 撇 leg, >180px diagonal)
  04 小  (carry-over: tilted teardrop 点s)
  05 寸  (new: heng + 竖钩 + 点)
  06 万  (new: heng + 撇 + 横折弯钩)

Rendering rule (c15 lesson):
  Use smooth CUBIC BÉZIER with continuous per-sample pensize.
  The brush is rendered as ONE continuous fluid line whose width
  varies smoothly point-by-point via t.pensize(w); t.goto(x,y).
  DO NOT render as a series of overlapping disc stamps (no
  for p in pts: t.dot(w,...) patterns) — that leaves "beads on
  a wire" joint artifacts.
"""

import os
import turtle
from PIL import Image

# ---------------------------------------------------------------------------
# Output dir
# ---------------------------------------------------------------------------
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# Turtle / canvas
# ---------------------------------------------------------------------------
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.tracer(0, 0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.color("black")


def _reset():
    """Reset turtle to (0,0) heading 90° (up), pen up, fresh canvas."""
    t.reset()
    t.hideturtle()
    t.speed(0)
    t.color("black")
    t.penup()
    t.goto(0, 0)
    t.setheading(90)


def _save_png(name):
    """Save the current canvas to a PNG via PostScript -> PIL."""
    canvas = screen.getcanvas()
    ps_path = os.path.join(OUT_DIR, name.replace(".png", ".ps"))
    png_path = os.path.join(OUT_DIR, name)
    canvas.postscript(file=ps_path, colormode="color")
    img = Image.open(ps_path)
    # Use a white background to ensure no alpha artifacts
    bg = Image.new("RGB", img.size, "white")
    bg.paste(img)
    bg.save(png_path, "PNG")
    try:
        os.remove(ps_path)
    except OSError:
        pass


# ---------------------------------------------------------------------------
# Bézier / brush primitives
# ---------------------------------------------------------------------------
def _cubic(p0, p1, p2, p3, n=160):
    """Sample a cubic Bézier from p0..p3 at n+1 points."""
    pts = []
    for i in range(n + 1):
        u = i / n
        v = 1 - u
        x = (v ** 3) * p0[0] + 3 * (v ** 2) * u * p1[0] + 3 * v * (u ** 2) * p2[0] + (u ** 3) * p3[0]
        y = (v ** 3) * p0[1] + 3 * (v ** 2) * u * p1[1] + 3 * v * (u ** 2) * p2[1] + (u ** 3) * p3[1]
        pts.append((x, y))
    return pts


def _width(u, w_start, w_mid, w_end):
    """Width profile: piecewise-linear start->mid->end so mid is the peak/valley.
    Used to keep middle >= 50% peak."""
    if u <= 0.5:
        a = u / 0.5
        return w_start * (1 - a) + w_mid * a
    a = (u - 0.5) / 0.5
    return w_mid * (1 - a) + w_end * a


def brush_bezier(p0, p1, p2, p3, w_start, w_mid, w_end, n=160):
    """Draw a brushed cubic Bézier as ONE continuous line whose pensize
    varies smoothly per sample. NO disc stamps."""
    pts = _cubic(p0, p1, p2, p3, n=n)
    # Move to start with pen up, then draw continuously.
    t.penup()
    t.goto(pts[0])
    t.pendown()
    for i, (x, y) in enumerate(pts):
        u = i / n
        w = _width(u, w_start, w_mid, w_end)
        t.pensize(max(1, w))
        t.goto(x, y)
    t.penup()


def brush_compound(segments):
    """Draw a compound stroke as ONE continuous path. `segments` is a list
    of dicts: {p0,p1,p2,p3, w_start, w_mid, w_end, n}. The path is
    continuous (each segment's p0 should match previous p3). The endpoint
    width of segment k must match the start width of segment k+1 — this
    creates a smooth 顿笔 thickening at corners rather than a disc.
    The pen is set down on the first segment and stays down throughout."""
    if not segments:
        return
    first = segments[0]
    pts0 = _cubic(first["p0"], first["p1"], first["p2"], first["p3"],
                  n=first.get("n", 160))
    t.penup()
    t.goto(pts0[0])
    t.pendown()
    for seg in segments:
        n = seg.get("n", 160)
        pts = _cubic(seg["p0"], seg["p1"], seg["p2"], seg["p3"], n=n)
        ws, wm, we = seg["w_start"], seg["w_mid"], seg["w_end"]
        for i, (x, y) in enumerate(pts):
            u = i / n
            w = _width(u, ws, wm, we)
            t.pensize(max(1, w))
            t.goto(x, y)
    t.penup()


# ---------------------------------------------------------------------------
# Stroke recipes (continuous per-sample pensize, no dots)
# ---------------------------------------------------------------------------
def stroke_heng(x0, y0, length, w=12):
    """横 — horizontal, both ends heavy."""
    x1 = x0 + length
    # Slight downward sag-then-rise to feel brushed
    p0 = (x0, y0)
    p1 = (x0 + length * 0.33, y0 - 1)
    p2 = (x0 + length * 0.66, y0 - 1)
    p3 = (x1, y0)
    brush_bezier(p0, p1, p2, p3, w, w * 0.78, w, n=140)


def stroke_shu(x0, y0, length, w=12):
    """竖 — vertical, both ends heavy."""
    y1 = y0 - length
    p0 = (x0, y0)
    p1 = (x0 + 1, y0 - length * 0.33)
    p2 = (x0 - 1, y0 - length * 0.66)
    p3 = (x0, y1)
    brush_bezier(p0, p1, p2, p3, w, w * 0.78, w, n=140)


def stroke_pie(x0, y0, dx, dy, w=14):
    """撇 — start heavy, end fine, sweeping curve."""
    p0 = (x0, y0)
    p1 = (x0 + dx * 0.25, y0 + dy * 0.15)
    p2 = (x0 + dx * 0.65, y0 + dy * 0.55)
    p3 = (x0 + dx, y0 + dy)
    brush_bezier(p0, p1, p2, p3, w, w * 0.62, max(2, w * 0.18), n=180)


def stroke_dian(x0, y0, dx, dy, w=12):
    """点 — teardrop. Heavy at the 'belly' (start side specified by sign of dx/dy),
    fine tail. Caller chooses orientation by (dx, dy)."""
    # Belly at start, tail at end
    p0 = (x0, y0)
    p1 = (x0 + dx * 0.35, y0 + dy * 0.25)
    p2 = (x0 + dx * 0.7, y0 + dy * 0.6)
    p3 = (x0 + dx, y0 + dy)
    brush_bezier(p0, p1, p2, p3, w, w * 0.75, max(2, w * 0.2), n=120)


# ---------------------------------------------------------------------------
# Task 01 — 也  (yě)
# ---------------------------------------------------------------------------
def task_01():
    """也 — 横折钩 (upper-left), 竖 (middle inside), 竖弯钩 (frame).
    Tight bbox; smooth bezier; no dot artifacts."""
    _reset()

    # Stroke 1: 横折钩  (top-left short, then drops down with hook left at the bottom-ish)
    # Path: heng from (-110, 80) -> (-30, 80), then turns down to (-30, -10), hook left.
    brush_compound([
        # heng (short)
        dict(p0=(-110, 80), p1=(-80, 80), p2=(-50, 80), p3=(-30, 80),
             w_start=11, w_mid=9, w_end=12, n=80),
        # corner -> shu down (corner thickened via matching widths = 顿笔)
        dict(p0=(-30, 80), p1=(-28, 60), p2=(-30, 30), p3=(-30, -10),
             w_start=12, w_mid=10, w_end=11, n=120),
        # hook tail (short kick left-up)
        dict(p0=(-30, -10), p1=(-38, -8), p2=(-46, -2), p3=(-52, 6),
             w_start=11, w_mid=7, w_end=2, n=60),
    ])

    # Stroke 2: middle 竖 inside the frame
    stroke_shu(20, 50, 110, w=11)

    # Stroke 3: 竖弯钩  (the dominant wraparound frame)
    # starts upper-left-ish (left of stroke1's heng), drops far down, curves right, hooks up
    brush_compound([
        # vertical drop on the LEFT side
        dict(p0=(-150, 60), p1=(-148, 20), p2=(-150, -20), p3=(-150, -90),
             w_start=13, w_mid=10, w_end=13, n=140),
        # curve along the bottom rightward
        dict(p0=(-150, -90), p1=(-130, -115), p2=(-80, -125), p3=(20, -125),
             w_start=13, w_mid=11, w_end=13, n=140),
        # continue rightward along bottom, gentle rise
        dict(p0=(20, -125), p1=(60, -125), p2=(100, -120), p3=(140, -110),
             w_start=13, w_mid=11, w_end=13, n=120),
        # hook upward at the right end
        dict(p0=(140, -110), p1=(146, -90), p2=(148, -60), p3=(148, -25),
             w_start=13, w_mid=9, w_end=3, n=100),
    ])

    screen.update()
    _save_png("01_也.png")


# ---------------------------------------------------------------------------
# Task 02 — 巴  (bā)
# ---------------------------------------------------------------------------
def task_02():
    """巴 — TALLER frame (h > w), tri-decker top, 竖弯钩 hook clearly BELOW rect."""
    _reset()

    # Frame: width ~180, height ~260  (taller)
    L, R = -90, 90
    TOP, BOT = 130, -130  # but the 竖弯钩 will dip below BOT for the hook tail

    # Stroke 1: 竖 (left vertical) — full height
    stroke_shu(L, TOP, TOP - BOT, w=12)

    # Stroke 2: 横折 (top heng + right shu down to BOT) — ONE compound
    brush_compound([
        # top heng
        dict(p0=(L, TOP), p1=(-30, TOP - 1), p2=(30, TOP - 1), p3=(R, TOP),
             w_start=12, w_mid=10, w_end=13, n=120),
        # right shu down — only to BOT (rectangle's bottom-right)
        dict(p0=(R, TOP), p1=(R + 1, 60), p2=(R - 1, -30), p3=(R, BOT),
             w_start=13, w_mid=10, w_end=12, n=140),
    ])

    # Stroke 3: middle heng (tri-decker top: inner horizontal that touches both sides)
    stroke_heng(L, 40, R - L, w=11)

    # Stroke 4: 竖弯钩 — starts at upper area inside the frame? No: 巴's third stroke
    # is the bottom 横 of the inner box AND the 竖弯钩 wrapping bottom. The classical
    # stroke order: 竖, 横折, 横 (middle), 竖弯钩 (final, wrapping bottom).
    # Compound: starts from the LEFT vertical's bottom, runs right along bottom,
    # then curves up at right end with a hook.  Crucially, the hook tail extends BELOW BOT.
    # To make hook clearly extend BELOW the rectangle, we keep curve along y=-130 then
    # dip down to ~y=-160 before hooking up.
    brush_compound([
        # bottom heng from L to near R (but a bit shy of R, so curve starts)
        dict(p0=(L, BOT), p1=(-30, BOT - 2), p2=(30, BOT - 4), p3=(60, BOT - 8),
             w_start=12, w_mid=10, w_end=12, n=120),
        # curve down-and-right, dipping BELOW BOT
        dict(p0=(60, BOT - 8), p1=(85, BOT - 18), p2=(100, BOT - 30), p3=(110, BOT - 40),
             w_start=12, w_mid=11, w_end=13, n=100),
        # hook upward (the tail goes up-left, clearly outside/below the rectangle)
        dict(p0=(110, BOT - 40), p1=(108, BOT - 25), p2=(102, BOT - 8), p3=(94, BOT + 12),
             w_start=13, w_mid=8, w_end=2, n=90),
    ])

    screen.update()
    _save_png("02_巴.png")


# ---------------------------------------------------------------------------
# Task 03 — 见  (jiàn)
# ---------------------------------------------------------------------------
def task_03():
    """见 — 月-like top frame with a LONG 撇 leg + 竖弯钩 right leg.
    The 撇 must be a long diagonal (>180 px) exiting the frame at bottom."""
    _reset()

    # Top frame (smaller box) — left shu, top heng+right shu (横折), two inner hengs
    L, R = -80, 80
    TOP, MID_BOT = 130, -20  # the frame box (compressed to leave room for legs)

    # Stroke 1: left 竖 of the frame
    stroke_shu(L, TOP, TOP - MID_BOT, w=12)

    # Stroke 2: 横折钩 (top heng + right shu with small hook). For 见 the right side
    # has a small hook at the bottom of the frame's right vertical.
    brush_compound([
        dict(p0=(L, TOP), p1=(-25, TOP - 1), p2=(25, TOP - 1), p3=(R, TOP),
             w_start=12, w_mid=10, w_end=13, n=120),
        dict(p0=(R, TOP), p1=(R + 1, 60), p2=(R - 1, 10), p3=(R, MID_BOT),
             w_start=13, w_mid=10, w_end=12, n=140),
        # small hook left
        dict(p0=(R, MID_BOT), p1=(R - 8, MID_BOT + 2), p2=(R - 16, MID_BOT + 6),
             p3=(R - 22, MID_BOT + 12),
             w_start=12, w_mid=7, w_end=2, n=50),
    ])

    # Stroke 3: inner 横 (single inner horizontal — 见 has one inner heng, not two)
    stroke_heng(L, 55, R - L, w=10)

    # Stroke 4: 撇 — LONG diagonal from upper-right area down to lower-left,
    # clearly exiting frame at bottom. Start at (R-10, MID_BOT) end at (-160, -180).
    # That's a diagonal of ~ sqrt(150^2 + 160^2) ≈ 220 px. Good.
    stroke_pie(R - 10, MID_BOT, dx=-150, dy=-160, w=14)

    # Stroke 5: 竖弯钩 — right leg. Compound: short vertical drop, curve right, hook up.
    brush_compound([
        # vertical from the bottom-right corner of the frame down
        dict(p0=(R - 4, MID_BOT - 4), p1=(R - 2, -60), p2=(R, -110), p3=(R + 10, -150),
             w_start=12, w_mid=10, w_end=12, n=120),
        # curve rightward along bottom
        dict(p0=(R + 10, -150), p1=(R + 35, -170), p2=(R + 70, -175), p3=(R + 100, -170),
             w_start=12, w_mid=11, w_end=13, n=100),
        # hook upward
        dict(p0=(R + 100, -170), p1=(R + 108, -150), p2=(R + 110, -120), p3=(R + 108, -90),
             w_start=13, w_mid=9, w_end=2, n=90),
    ])

    screen.update()
    _save_png("03_见.png")


# ---------------------------------------------------------------------------
# Task 04 — 小  (xiǎo)
# ---------------------------------------------------------------------------
def task_04():
    """小 — center 竖钩 + two tilted teardrop 点s.
    Left 点: tilted ~45°, belly OUTER (lower-left), tail toward shu (upper-right).
    Right 点: tilted ~45°, belly OUTER (lower-right), tail toward shu (upper-left).
    """
    _reset()

    # Stroke 1: center 竖钩 (vertical with small hook at bottom-left)
    brush_compound([
        dict(p0=(0, 110), p1=(2, 50), p2=(-2, -20), p3=(0, -90),
             w_start=14, w_mid=11, w_end=13, n=140),
        # small hook left-up
        dict(p0=(0, -90), p1=(-10, -88), p2=(-20, -82), p3=(-28, -72),
             w_start=13, w_mid=7, w_end=2, n=50),
    ])

    # Stroke 2: left 点 — tilted ~45°, teardrop.
    # Belly OUTER (away from center shu): place belly at lower-left, tail at upper-right
    # belly at (-95, -20), tail moves up-right toward shu, i.e. dx=+35, dy=+35
    stroke_dian(-95, -20, dx=35, dy=35, w=13)

    # Stroke 3: right 点 — tilted ~45°, teardrop.
    # Belly OUTER at lower-right (95, -30), tail up-left toward shu: dx=-35, dy=+35
    stroke_dian(95, -30, dx=-35, dy=35, w=13)

    screen.update()
    _save_png("04_小.png")


# ---------------------------------------------------------------------------
# Task 05 — 寸  (cùn)
# ---------------------------------------------------------------------------
def task_05():
    """寸 — heng (top), 竖钩 (vertical down center, small hook bottom-left),
    点 (small dot, upper-right)."""
    _reset()

    # Stroke 1: heng (medium, near top)
    stroke_heng(-100, 80, 200, w=13)

    # Stroke 2: 竖钩 from heng's center going down, hook at bottom-left
    brush_compound([
        # vertical down
        dict(p0=(0, 80), p1=(2, 30), p2=(-2, -30), p3=(0, -110),
             w_start=12, w_mid=10, w_end=13, n=140),
        # small hook bottom-left
        dict(p0=(0, -110), p1=(-10, -108), p2=(-20, -102), p3=(-28, -92),
             w_start=13, w_mid=7, w_end=2, n=50),
    ])

    # Stroke 3: 点 (small dot in upper-right area)
    # Position to the right of the heng's center, above mid. Tilt ~45°.
    # Belly at upper-left of dot, tail down-right? For a typical 寸 dot
    # it sits to the right of the 竖钩 around y~+30. Make a short teardrop
    # tilting down-right.
    stroke_dian(45, 35, dx=28, dy=-28, w=12)

    screen.update()
    _save_png("05_寸.png")


# ---------------------------------------------------------------------------
# Task 06 — 万  (wàn)
# ---------------------------------------------------------------------------
def task_06():
    """万 — heng (top, short), 撇 (long, head at heng's left, sweep down-left),
    横折弯钩 (compound: heng → corner → curve → hook)."""
    _reset()

    # Stroke 1: top heng (short)
    stroke_heng(-80, 100, 160, w=12)

    # Stroke 2: 撇 — long, head at heng's left, sweeping down-left
    # head at (-75, 95), end at (-160, -150). Diagonal ~ sqrt(85^2 + 245^2) > 250 px.
    # Actually a clean 万-撇 starts near the left end of the heng and exits at lower-left.
    stroke_pie(-75, 95, dx=-95, dy=-250, w=15)

    # Stroke 3: 横折弯钩 — ONE continuous compound.
    # Starts near right end of top heng (~+70, 95-ish, but typically slightly below heng),
    # drops down, curves rightward, hooks up.
    brush_compound([
        # initial heng (very short, continuing the visual line from top heng)
        # In 万 this third stroke's start "heng" is short, almost a tick before the drop.
        dict(p0=(-10, 60), p1=(20, 60), p2=(50, 60), p3=(75, 58),
             w_start=11, w_mid=9, w_end=12, n=80),
        # corner -> drop (顿笔 thickening at corner via matched widths)
        dict(p0=(75, 58), p1=(76, 30), p2=(72, -10), p3=(60, -60),
             w_start=12, w_mid=10, w_end=12, n=120),
        # curve rightward along bottom
        dict(p0=(60, -60), p1=(70, -100), p2=(90, -130), p3=(120, -140),
             w_start=12, w_mid=11, w_end=13, n=120),
        # hook upward at right
        dict(p0=(120, -140), p1=(128, -120), p2=(130, -90), p3=(128, -60),
             w_start=13, w_mid=9, w_end=2, n=90),
    ])

    screen.update()
    _save_png("06_万.png")


# ---------------------------------------------------------------------------
# Run all
# ---------------------------------------------------------------------------
# ── Task 01 | 也 | yě
task_01()
# ── Task 02 | 巴 | bā
task_02()
# ── Task 03 | 见 | jiàn
task_03()
# ── Task 04 | 小 | xiǎo
task_04()
# ── Task 05 | 寸 | cùn
task_05()
# ── Task 06 | 万 | wàn
task_06()
