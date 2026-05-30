"""
Cycle 11 — Drawer output (run_3)
Six tasks: 01_火, 02_也, 03_力, 04_巴, 05_月, 06_见

Standard skeleton:
  - Turtle on an 800x600 white canvas.
  - Each task draws strokes as cubic-Bezier centerlines, sampled densely,
    with per-sample pensize (middle >= 50% of peak) — "brushed" look.
  - Compound strokes (frames, hooks) are one continuous brushed sweep
    with a 顿笔 Gaussian thickening at each corner; hook is a short
    tail-arm (15-20% main length) with fine taper.
  - Each task starts at (0,0) heading 90° via t.reset().
  - PNG saved via canvas.postscript() -> PIL.
"""

import io
import math
import os
import turtle

from PIL import Image

OUT_DIR = os.path.dirname(os.path.abspath(__file__))


# ---------------------------------------------------------------------------
# Canvas setup
# ---------------------------------------------------------------------------
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.tracer(0, 0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pencolor("black")


# ---------------------------------------------------------------------------
# Bezier + brushed-stroke helpers
# ---------------------------------------------------------------------------
def cubic_bezier(p0, p1, p2, p3, n=160):
    """Sample a cubic Bezier from p0 -> p3 with control points p1, p2."""
    pts = []
    for i in range(n + 1):
        u = i / n
        mu = 1.0 - u
        x = (mu ** 3) * p0[0] + 3 * (mu ** 2) * u * p1[0] + 3 * mu * (u ** 2) * p2[0] + (u ** 3) * p3[0]
        y = (mu ** 3) * p0[1] + 3 * (mu ** 2) * u * p1[1] + 3 * mu * (u ** 2) * p2[1] + (u ** 3) * p3[1]
        pts.append((x, y))
    return pts


def width_profile(n, peak, w_start, w_end, belly=0.5, plateau=0.35):
    """
    Per-sample pensize profile.
    - peak: maximum pensize at the belly.
    - w_start / w_end: pensize at the two endpoints.
    - belly: location (0..1) of the peak.
    - plateau: half-width of the "middle" zone (>= 0.5 * peak guaranteed).
    Symmetric-ish: rises from w_start to peak, holds, falls to w_end.
    """
    widths = []
    for i in range(n):
        u = i / max(1, n - 1)
        if u < belly:
            # rising portion
            local = u / max(1e-6, belly)
            # cosine ease
            ramp = 0.5 - 0.5 * math.cos(math.pi * local)
            w = w_start + (peak - w_start) * ramp
        else:
            local = (u - belly) / max(1e-6, 1.0 - belly)
            ramp = 0.5 - 0.5 * math.cos(math.pi * local)
            w = peak + (w_end - peak) * ramp
        # enforce middle >= 50% peak
        if abs(u - belly) < plateau:
            w = max(w, 0.55 * peak)
        widths.append(max(1.0, w))
    return widths


def draw_brushed(pts, widths):
    """Draw a brushed stroke by stamping short segments with per-sample pensize."""
    if not pts:
        return
    t.penup()
    t.goto(pts[0])
    t.pendown()
    for i in range(1, len(pts)):
        t.pensize(widths[min(i, len(widths) - 1)])
        t.goto(pts[i])
    t.penup()


def brushed_bezier(p0, p1, p2, p3, peak=14, w_start=4, w_end=4,
                   belly=0.5, n=160):
    """Draw one Bezier stroke with a brushed (per-sample) width profile."""
    pts = cubic_bezier(p0, p1, p2, p3, n=n)
    widths = width_profile(len(pts), peak=peak, w_start=w_start,
                            w_end=w_end, belly=belly)
    draw_brushed(pts, widths)


def dunbi_dot(x, y, size=14):
    """Plant a 顿笔 (corner thickening) dot."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pensize(size)
    t.dot(size)
    t.penup()


def brushed_polyline(segments, peak=14, w_start=4, w_end=4, n=120,
                     dunbi_at_joins=True, dunbi_size=None):
    """
    Continuous brushed sweep through multiple Bezier segments.
    `segments` is a list of (p0, p1, p2, p3) tuples; consecutive segments
    should share endpoints. At each shared join, plant a 顿笔 dot.
    Width profile interpolates linearly between w_start (overall start)
    and w_end (overall end), with each segment's middle >= 0.55 * peak.
    """
    nseg = len(segments)
    if nseg == 0:
        return
    # per-segment endpoint widths (linear interp along the whole sweep)
    end_widths = []
    for i in range(nseg + 1):
        u = i / nseg
        end_widths.append(w_start + (w_end - w_start) * u)

    for i, (p0, p1, p2, p3) in enumerate(segments):
        ws = end_widths[i]
        we = end_widths[i + 1]
        pts = cubic_bezier(p0, p1, p2, p3, n=n)
        widths = width_profile(len(pts), peak=peak, w_start=ws,
                                w_end=we, belly=0.5)
        draw_brushed(pts, widths)

    if dunbi_at_joins:
        ds = dunbi_size if dunbi_size is not None else int(peak * 1.05)
        # plant dunbi at every internal join
        for i in range(nseg - 1):
            (_, _, _, p_end) = segments[i]
            dunbi_dot(p_end[0], p_end[1], size=ds)


# ---------------------------------------------------------------------------
# Atomic stroke recipes (centered, parameterized)
# ---------------------------------------------------------------------------
def stroke_heng(x0, y0, length, peak=14, curve=4):
    """横 — horizontal, heavy at both ends, slight downward sag rebound."""
    p0 = (x0, y0)
    p3 = (x0 + length, y0)
    p1 = (x0 + length * 0.30, y0 - curve)
    p2 = (x0 + length * 0.70, y0 - curve)
    brushed_bezier(p0, p1, p2, p3, peak=peak, w_start=peak * 0.95,
                   w_end=peak * 0.95, belly=0.5)


def stroke_shu(x0, y0, length, peak=14, curve=2):
    """竖 — vertical, heavy at both ends."""
    p0 = (x0, y0)
    p3 = (x0, y0 - length)
    p1 = (x0 + curve, y0 - length * 0.30)
    p2 = (x0 + curve, y0 - length * 0.70)
    brushed_bezier(p0, p1, p2, p3, peak=peak, w_start=peak * 0.95,
                   w_end=peak * 0.95, belly=0.5)


def stroke_pie(x_head, y_head, dx, dy, peak=14):
    """撇 — heavy at head (start), fine at tail (end). Curved sweep."""
    p0 = (x_head, y_head)
    p3 = (x_head + dx, y_head + dy)
    # bow the curve: control points pull leftward
    p1 = (x_head + dx * 0.30 + 6, y_head + dy * 0.25)
    p2 = (x_head + dx * 0.65 - 6, y_head + dy * 0.65)
    brushed_bezier(p0, p1, p2, p3, peak=peak, w_start=peak * 0.95,
                   w_end=peak * 0.18, belly=0.40)


def stroke_na(x_head, y_head, dx, dy, peak=14):
    """捺 — fine at start, heavy at end (flat kick)."""
    p0 = (x_head, y_head)
    p3 = (x_head + dx, y_head + dy)
    p1 = (x_head + dx * 0.30 - 4, y_head + dy * 0.25)
    p2 = (x_head + dx * 0.65 + 4, y_head + dy * 0.70)
    brushed_bezier(p0, p1, p2, p3, peak=peak, w_start=peak * 0.18,
                   w_end=peak * 0.95, belly=0.70)


def stroke_dian(x_head, y_head, dx, dy, peak=12):
    """点 — small dot stroke, belly heavy, fine tail."""
    p0 = (x_head, y_head)
    p3 = (x_head + dx, y_head + dy)
    p1 = (x_head + dx * 0.40, y_head + dy * 0.35)
    p2 = (x_head + dx * 0.70, y_head + dy * 0.70)
    brushed_bezier(p0, p1, p2, p3, peak=peak, w_start=peak * 0.30,
                   w_end=peak * 0.20, belly=0.55)


# ---------------------------------------------------------------------------
# Compound stroke recipes (one continuous brushed sweep + 顿笔 corners)
# ---------------------------------------------------------------------------
def compound_heng_zhe_gou(x_start, y_start, w, h, peak=14,
                           hook_len_frac=0.18):
    """
    横折钩 — heng (horizontal top), corner, shu (vertical down), hook (up-left).
    Starts at top-left (x_start, y_start), draws right by w, down by h.
    Hook tail-arm is hook_len_frac of the shu length, swung up-left.
    """
    top_left = (x_start, y_start)
    top_right = (x_start + w, y_start)
    bot_right = (x_start + w, y_start - h)

    # heng segment
    heng_seg = (
        top_left,
        (top_left[0] + w * 0.30, top_left[1] - 2),
        (top_right[0] - w * 0.30, top_right[1] - 2),
        top_right,
    )
    # shu segment (down from top_right to bot_right)
    shu_seg = (
        top_right,
        (top_right[0] + 2, top_right[1] - h * 0.30),
        (bot_right[0] + 2, bot_right[1] + h * 0.30),
        bot_right,
    )
    # hook tail-arm: from bot_right swing up-left
    hook_len = h * hook_len_frac
    hook_end = (bot_right[0] - hook_len * 0.85, bot_right[1] + hook_len * 0.55)
    hook_seg = (
        bot_right,
        (bot_right[0] - hook_len * 0.25, bot_right[1] + hook_len * 0.15),
        (bot_right[0] - hook_len * 0.60, bot_right[1] + hook_len * 0.40),
        hook_end,
    )
    segs = [heng_seg, shu_seg, hook_seg]
    brushed_polyline(segs, peak=peak, w_start=peak * 0.95,
                     w_end=peak * 0.20, n=120, dunbi_at_joins=True,
                     dunbi_size=int(peak * 1.15))


def compound_shu_wan_gou(x_start, y_start, h, w, peak=14,
                          hook_len_frac=0.20):
    """
    竖弯钩 — shu (vertical down), wan (curve through bottom), gou (hook up).
    Starts at (x_start, y_start) and forms a "J" shape:
    shu down by h, then sweeps right by w, then hooks UP at the end.
    """
    p_top = (x_start, y_start)
    p_corner = (x_start, y_start - h)  # bottom of the shu
    p_right = (x_start + w, y_start - h + w * 0.10)  # end of horizontal sweep

    # shu segment (down)
    shu_seg = (
        p_top,
        (p_top[0] - 2, p_top[1] - h * 0.30),
        (p_corner[0] - 2, p_corner[1] + h * 0.30),
        p_corner,
    )
    # wan segment — curve from p_corner through to p_right
    mid_curve = (p_corner[0] + w * 0.30, p_corner[1] - w * 0.18)
    wan_seg = (
        p_corner,
        (p_corner[0] + w * 0.10, p_corner[1] - w * 0.20),
        mid_curve,
        p_right,
    )
    # hook: from p_right, kick UP
    hook_len = w * hook_len_frac + 8
    hook_end = (p_right[0] - hook_len * 0.10, p_right[1] + hook_len)
    hook_seg = (
        p_right,
        (p_right[0] + hook_len * 0.10, p_right[1] + hook_len * 0.30),
        (p_right[0] + hook_len * 0.05, p_right[1] + hook_len * 0.70),
        hook_end,
    )
    segs = [shu_seg, wan_seg, hook_seg]
    brushed_polyline(segs, peak=peak, w_start=peak * 0.90,
                     w_end=peak * 0.25, n=130, dunbi_at_joins=True,
                     dunbi_size=int(peak * 1.10))


def compound_heng_zhe(x_start, y_start, w, h, peak=14):
    """
    横折 — heng then zhe (corner, then short vertical down). No hook.
    Used as the top-right of a frame.
    """
    top_left = (x_start, y_start)
    top_right = (x_start + w, y_start)
    bot_right = (x_start + w, y_start - h)
    heng_seg = (
        top_left,
        (top_left[0] + w * 0.30, top_left[1] - 2),
        (top_right[0] - w * 0.30, top_right[1] - 2),
        top_right,
    )
    shu_seg = (
        top_right,
        (top_right[0] + 2, top_right[1] - h * 0.30),
        (bot_right[0] + 2, bot_right[1] + h * 0.30),
        bot_right,
    )
    brushed_polyline([heng_seg, shu_seg], peak=peak,
                     w_start=peak * 0.95, w_end=peak * 0.95, n=120,
                     dunbi_at_joins=True, dunbi_size=int(peak * 1.15))


# ---------------------------------------------------------------------------
# PNG save helper
# ---------------------------------------------------------------------------
def save_png(filename):
    """Save current turtle canvas as PNG via PostScript -> PIL."""
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    # white background
    bg = Image.new("RGB", img.size, "white")
    bg.paste(img, mask=img.convert("RGBA").split()[-1] if img.mode == "RGBA" else None)
    bg.save(os.path.join(OUT_DIR, filename), "PNG")


# ============================================================================
# ── Task 01 | 火 | huǒ
# ============================================================================
# Final attempt: 4 strokes — left 点, right 点, 撇 (heavy head), 捺 (heavy end).
# Composition fix: BOTH 点 must literally HUG the apex (tails almost touching
# the apex point where 撇 and 捺 meet). 撇 head heavier (peak ~16 to match 捺).
# Maximize distinguishability from 八.
def draw_huo():
    t.reset()
    t.hideturtle()
    t.pencolor("black")

    APEX = (0, 120)  # the meeting point of 撇 and 捺 at top-center

    # 撇 (long, sweeping down-left from APEX). Heavy head (peak 16).
    # head AT the apex.
    stroke_pie(APEX[0], APEX[1], dx=-150, dy=-260, peak=16)

    # 捺 (long, sweeping down-right from APEX). Heavy end (flat kick).
    stroke_na(APEX[0], APEX[1], dx=150, dy=-260, peak=16)

    # Left 点 — tail HUGS the apex from the upper-left.
    # Place the point so its tail (end) lands within ~8px of APEX.
    # Tail (end) at approx (-12, APEX[1] + 8); head up-left.
    left_dian_head = (-46, APEX[1] + 50)
    left_dian_tail_dx = 34   # ends near (-12, ...)
    left_dian_tail_dy = -42  # ends near (..., APEX[1] + 8)
    stroke_dian(left_dian_head[0], left_dian_head[1],
                dx=left_dian_tail_dx, dy=left_dian_tail_dy, peak=14)

    # Right 点 — tail HUGS the apex from the upper-right.
    right_dian_head = (46, APEX[1] + 50)
    right_dian_tail_dx = -34
    right_dian_tail_dy = -42
    stroke_dian(right_dian_head[0], right_dian_head[1],
                dx=right_dian_tail_dx, dy=right_dian_tail_dy, peak=14)

    screen.update()
    save_png("01_火.png")


# ============================================================================
# ── Task 02 | 也 | yě
# ============================================================================
# 3 strokes occupying the SAME bounding rectangle:
#   - 横折钩 hangs from upper-left INTO the right wall of the 竖弯钩.
#   - middle 竖 drops straight through the center, FOOT landing on the
#     bottom curl of the 竖弯钩.
#   - 竖弯钩 forms the floor + right wall (wrap-around J).
# Bounding rect approx: x in [-130, 130], y in [-130, 140].
def draw_ye():
    t.reset()
    t.hideturtle()
    t.pencolor("black")

    # 1. 竖弯钩 — the "floor + right wall" wrap-around.
    # Start at upper-left of the body, drop down to floor, sweep right,
    # then hook UP at the bottom-right corner. We want the floor at y ~ -130
    # and the right wall going UP from floor to about y ~ 30.
    # Implement as: shu from (-100, 60) down to (-100, -110), then wan to
    # (130, -100), then hook up.
    # Reusing compound_shu_wan_gou: start = (-100, 60), h = 170, w = 230.
    compound_shu_wan_gou(x_start=-100, y_start=60, h=170, w=230, peak=14,
                         hook_len_frac=0.22)

    # 2. 横折钩 — upper-left "Γ-with-hook", hanging INTO the right wall.
    # Top heng from (-130, 130) to (60, 130), then descending shu to
    # (60, 10), with hook back left at the bottom. The bottom-right
    # corner of this 横折钩 lands inside the body (above the 竖弯钩 floor),
    # creating overlap with the right wall.
    compound_heng_zhe_gou(x_start=-130, y_start=130, w=190, h=120, peak=13,
                           hook_len_frac=0.22)

    # 3. Middle 竖 — drops STRAIGHT through the center, FOOT landing on
    # the bottom curl of the 竖弯钩 (which is around y = -110).
    # Start at top of the body (y ~ 110, inside the 横折钩 ceiling),
    # drop to y ~ -110.
    stroke_shu(x0=-15, y0=110, length=220, peak=13, curve=1)

    # 顿笔 at the foot (where shu lands on the 弯 floor)
    dunbi_dot(-15, -110, size=14)

    screen.update()
    save_png("02_也.png")


# ============================================================================
# ── Task 03 | 力 | lì
# ============================================================================
# 2 strokes — 横折钩 (frame) + 撇 PASSING THROUGH the interior of that frame.
# 撇 head starts at top of the frame near the heng's middle, sweeps
# down-left out through the frame and beyond. Visible interior overlap
# is essential.
def draw_li():
    t.reset()
    t.hideturtle()
    t.pencolor("black")

    # 1. 横折钩 — the frame. Top-left at (-90, 130), w = 180, h = 230.
    # Top heng spans x in [-90, 90]; right wall from y=130 to y=-100.
    compound_heng_zhe_gou(x_start=-90, y_start=130, w=180, h=230, peak=14,
                           hook_len_frac=0.20)

    # 2. 撇 — head AT THE TOP OF THE FRAME near the heng's middle.
    # Head at roughly (10, 125) — slightly right of the heng's midpoint,
    # ABOVE/AT the heng. Then sweep DOWN-LEFT across the interior of the
    # frame, exiting the bottom-left and continuing beyond.
    # End point at roughly (-150, -150) — well outside the frame.
    stroke_pie(10, 125, dx=-160, dy=-280, peak=15)

    screen.update()
    save_png("03_力.png")


# ============================================================================
# ── Task 04 | 巴 | bā
# ============================================================================
# Two-level frame. Top portion = small CLOSED rectangle with middle heng
# dividing it (double-decked). Below that, the 竖弯钩 extends down + right.
# Strokes (logical): 横折 (top frame top+right) + left shu (frame left edge) +
# middle heng inside top frame + 竖弯钩 (bottom). The closed upper rectangle
# is what distinguishes it from 已.
def draw_ba():
    t.reset()
    t.hideturtle()
    t.pencolor("black")

    # Upper rectangle: x in [-70, 70], y in [60, 140] (height 80).
    # Stroke A: left shu of the upper rectangle (from top-left down to
    # bottom-left of the upper rectangle, then continuing as the start of
    # the 竖弯钩 body below).
    # We'll split this conceptually: draw a left shu for the upper
    # rectangle, then a separate 竖弯钩 starting just below it.

    # 1. Top frame: 横折 (top + right side of upper rect)
    compound_heng_zhe(x_start=-70, y_start=140, w=140, h=80, peak=14)

    # 2. Left shu of the upper rect (closes the rectangle on the left)
    # Plus a 顿笔 at the bottom corner where it meets the bottom heng.
    stroke_shu(x0=-70, y0=140, length=80, peak=14, curve=0)

    # 3. Bottom heng of the upper rectangle (the "middle heng" that
    # divides the upper level — closing the small rectangle from below).
    stroke_heng(x0=-70, y0=60, length=140, peak=13, curve=2)

    # Add an interior dividing heng to make it visibly double-decked.
    # A thin middle heng halfway up the small rectangle.
    stroke_heng(x0=-55, y0=100, length=110, peak=10, curve=1)

    # 4. 竖弯钩 — extends DOWN from the bottom of the upper rectangle
    # (left side) and sweeps RIGHT and HOOKS UP. Start at (-70, 60),
    # drop to about y = -120, sweep right to x ~ 100, hook up.
    compound_shu_wan_gou(x_start=-70, y_start=60, h=180, w=170, peak=14,
                         hook_len_frac=0.20)

    screen.update()
    save_png("04_巴.png")


# ============================================================================
# ── Task 05 | 月 | yuè
# ============================================================================
# Tall rectangle frame (~140 wide, ~340 tall).
#   - left side: 撇 (gentle curve, head at top-left, sweeps slightly down-left)
#   - right side: 横折钩 (heng across top + descending shu + 钩 at bottom)
#   - two interior heng (upper and lower), parallel.
def draw_yue():
    t.reset()
    t.hideturtle()
    t.pencolor("black")

    # Frame x in [-70, 70], y in [-170, 170]. Width 140, height 340.

    # 1. Left side 撇 — gentle curve, head at top-left (-70, 170),
    # sweeps DOWN with a slight leftward bow, ending around (-90, -170).
    # Not a full diagonal — mostly vertical with a slight outward curve.
    p0 = (-70, 170)
    p3 = (-90, -170)
    p1 = (-72, 60)
    p2 = (-82, -80)
    brushed_bezier(p0, p1, p2, p3, peak=14, w_start=14 * 0.95,
                   w_end=14 * 0.22, belly=0.45, n=160)

    # 2. Right side 横折钩 — top-left of the frame is at (-70, 170);
    # the 横 goes RIGHT to (70, 170), then 折 down to (70, -170),
    # with a small hook UP-LEFT at the bottom.
    compound_heng_zhe_gou(x_start=-70, y_start=170, w=140, h=340, peak=14,
                           hook_len_frac=0.13)

    # 3. Interior heng (upper) — sits inside the frame, around y = 50.
    stroke_heng(x0=-60, y0=50, length=120, peak=10, curve=1)

    # 4. Interior heng (lower) — around y = -70.
    stroke_heng(x0=-60, y0=-70, length=120, peak=10, curve=1)

    screen.update()
    save_png("05_月.png")


# ============================================================================
# ── Task 06 | 见 | jiàn
# ============================================================================
# 4 strokes: small "目-like" frame on top + two angled bottom legs.
#   stroke 1: left shu of the top frame
#   stroke 2: 横折 (top + right edge of the top frame)
#   stroke 3: middle heng inside the top frame
#   stroke 4: 竖弯钩 attached to the bottom-right, sweeping right + hook up
# Plus we also need a left bottom leg (撇). To stay at 4 strokes we extend
# the left shu DOWN past the frame to act as the left leg / 撇 as well.
def draw_jian():
    t.reset()
    t.hideturtle()
    t.pencolor("black")

    # Top frame: x in [-70, 70], y in [40, 160]. Bottom legs extend below.

    # stroke 1: left shu — starts at top-left of frame and extends DOWN
    # past the bottom of the frame, curving slightly left to form the
    # 撇 leg. Implement as a single brushed Bezier.
    p0 = (-70, 160)
    p3 = (-110, -160)  # bottom-left, swept slightly outward
    p1 = (-70, 60)
    p2 = (-90, -60)
    brushed_bezier(p0, p1, p2, p3, peak=14, w_start=14 * 0.95,
                   w_end=14 * 0.25, belly=0.50, n=160)

    # stroke 2: 横折 — top edge + right edge of the top frame.
    # Top-left of frame at (-70, 160), width 140, descending to (70, 40).
    compound_heng_zhe(x_start=-70, y_start=160, w=140, h=120, peak=14)

    # stroke 3: middle heng inside the top frame (around y = 100).
    stroke_heng(x0=-60, y0=100, length=120, peak=10, curve=1)

    # stroke 4: 竖弯钩 — attached at the bottom-right of the top frame
    # (70, 40), descending and sweeping RIGHT, then hooking UP.
    # Start at (70, 40), drop h=150, sweep w=80 right, hook up.
    compound_shu_wan_gou(x_start=70, y_start=40, h=180, w=110, peak=14,
                         hook_len_frac=0.22)

    # Bottom heng to close the top frame (so it reads as a closed box).
    # Single thin heng connecting (-70, 40) to (70, 40).
    stroke_heng(x0=-70, y0=40, length=140, peak=11, curve=1)

    screen.update()
    save_png("06_见.png")


# ---------------------------------------------------------------------------
# Run all tasks
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    draw_huo()
    draw_ye()
    draw_li()
    draw_ba()
    draw_yue()
    draw_jian()
