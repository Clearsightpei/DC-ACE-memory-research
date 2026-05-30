"""Cycle 7 — Drawer attempt.

Carry-overs (with numeric fixes from drawer_memory.md):
  01 大 — heng length >= 1.4x the limb-crossing span; apex above heng.
  02 入 — 捺 starts at 45-55% down the 撇's spine.

New (撇+捺 family):
  03 又 — 横撇 (compound, one brushed path) + 捺 sweeping lower-right.
  04 个 — 撇+捺 sharing top apex + centered shu dropping from apex.
  05 不 — heng + long 撇 + centered shu + 点.
  06 木 — heng + centered shu (must extend BELOW heng) + 撇 + 捺.

Every stroke is a cubic-Bezier centerline sampled ~140-200 times with a
per-sample pensize. Middle of every stroke holds >= 50% of peak.
"""

import io
import os
import math
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
# Brush primitives — cubic Bezier centerline + per-sample width
# ---------------------------------------------------------------------------

def _bezier(p0, p1, p2, p3, n):
    pts = []
    for i in range(n + 1):
        u = i / n
        v = 1.0 - u
        x = (v ** 3) * p0[0] + 3 * (v ** 2) * u * p1[0] + 3 * v * (u ** 2) * p2[0] + (u ** 3) * p3[0]
        y = (v ** 3) * p0[1] + 3 * (v ** 2) * u * p1[1] + 3 * v * (u ** 2) * p2[1] + (u ** 3) * p3[1]
        pts.append((x, y))
    return pts


def _width_profile(n, peak, kind):
    """Per-sample width along [0..n].

    'middle >= 0.5*peak' is preserved for every kind.

    kind: 'heng', 'shu', 'pie', 'na', 'ti', 'dian'.
    """
    mid = max(0.55 * peak, 4.0)
    end_press = max(0.85 * peak, mid)
    head_press = max(0.9 * peak, mid)
    fine = max(0.18 * peak, 2.0)

    widths = []
    for i in range(n + 1):
        u = i / n  # 0 head -> 1 tail

        if kind == "heng":
            # Both ends heavy, shaft ~ mid. Slight belly.
            if u < 0.12:
                w = mid + (end_press - mid) * (1 - u / 0.12)
            elif u > 0.88:
                w = mid + (end_press - mid) * ((u - 0.88) / 0.12)
            else:
                # Soft sinusoidal belly between the two presses.
                t = (u - 0.12) / 0.76
                w = mid + 0.08 * peak * math.sin(math.pi * t)

        elif kind == "shu":
            if u < 0.10:
                w = mid + (head_press - mid) * (1 - u / 0.10)
            elif u > 0.90:
                w = mid + (end_press - mid) * ((u - 0.90) / 0.10)
            else:
                t = (u - 0.10) / 0.80
                w = mid + 0.06 * peak * math.sin(math.pi * t)

        elif kind == "pie":
            # Heavy head, fine tail. Shaft >= 50% of peak through middle.
            if u < 0.18:
                w = head_press - (head_press - mid) * (u / 0.18)
            elif u < 0.70:
                t = (u - 0.18) / 0.52
                w = mid - (mid - 0.55 * peak) * t * 0.4  # stays >= 50%
            else:
                t = (u - 0.70) / 0.30
                w = max(fine, mid * (1 - t) + fine * t)

        elif kind == "na":
            # Fine head, broadening, heavy pressed tail with flat-kick plateau
            # over last ~12% of arclength.
            if u < 0.18:
                w = fine + (mid - fine) * (u / 0.18)
            elif u < 0.65:
                t = (u - 0.18) / 0.47
                w = mid + (0.80 * peak - mid) * t
            elif u < 0.88:
                t = (u - 0.65) / 0.23
                w = 0.80 * peak + (peak - 0.80 * peak) * t
            else:
                # Flat-kick plateau, hold near-peak then a slight kick down.
                t = (u - 0.88) / 0.12
                w = peak - 0.15 * peak * t

        elif kind == "ti":
            if u < 0.15:
                w = head_press - (head_press - mid) * (u / 0.15)
            elif u < 0.70:
                w = mid
            else:
                t = (u - 0.70) / 0.30
                w = max(fine, mid * (1 - t) + fine * t)

        elif kind == "dian":
            # Thin entry, belly, tapered tail. Belly is the heavy region.
            if u < 0.25:
                w = fine + (peak - fine) * (u / 0.25)
            elif u < 0.55:
                w = peak
            else:
                t = (u - 0.55) / 0.45
                w = max(fine, peak * (1 - t) + fine * t)

        else:
            w = mid

        widths.append(max(w, 1.8))
    return widths


def brush_stroke(t, p0, p1, p2, p3, peak=18, kind="heng", samples=160):
    pts = _bezier(p0, p1, p2, p3, samples)
    widths = _width_profile(samples, peak, kind)
    t.penup()
    t.goto(pts[0])
    t.pendown()
    for (x, y), w in zip(pts[1:], widths[1:]):
        t.pensize(w)
        t.goto(x, y)
    t.penup()


def brush_compound(t, segments, peak=18, kind_per_segment=None,
                   dunbi_factor=1.35, samples_per_segment=120):
    """Continuous brushed path through several Bezier segments.

    Adds a 顿笔 (dunbi) thickening at each interior join.
    """
    # Build a flat sequence of points + widths so the corner pixel can be
    # bumped to make the 顿笔 read clearly (lift toward dunbi=2).
    all_pts = []
    all_w = []
    for seg_idx, (p0, p1, p2, p3) in enumerate(segments):
        seg_pts = _bezier(p0, p1, p2, p3, samples_per_segment)
        kind = kind_per_segment[seg_idx] if kind_per_segment else "heng"
        seg_w = _width_profile(samples_per_segment, peak, kind)
        if seg_idx > 0:
            # drop first sample to avoid duplicate at the join
            seg_pts = seg_pts[1:]
            seg_w = seg_w[1:]
        all_pts.extend(seg_pts)
        all_w.extend(seg_w)

    # Apply the dunbi thickening as a Gaussian-ish bump centered on every
    # interior join.
    join_indices = []
    cursor = 0
    for seg_idx, (p0, p1, p2, p3) in enumerate(segments[:-1]):
        cursor += samples_per_segment if seg_idx == 0 else samples_per_segment
        join_indices.append(cursor)

    bump_half_width = max(8, samples_per_segment // 8)
    for j in join_indices:
        for k in range(-bump_half_width, bump_half_width + 1):
            idx = j + k
            if 0 <= idx < len(all_w):
                falloff = math.exp(-(k * k) / (2 * (bump_half_width / 2) ** 2))
                bump_target = all_w[j] * dunbi_factor
                all_w[idx] = max(all_w[idx], all_w[idx] * (1 - falloff) + bump_target * falloff)

    t.penup()
    t.goto(all_pts[0])
    t.pendown()
    for (x, y), w in zip(all_pts[1:], all_w[1:]):
        t.pensize(w)
        t.goto(x, y)
    t.penup()


# ---------------------------------------------------------------------------
# Stroke helpers — one wrapper per atomic stroke
# ---------------------------------------------------------------------------

def heng(t, x0, y0, x1, y1, peak=18, bow=8):
    """Horizontal, slight upward tilt + tiny upward bow in the middle."""
    mx = (x0 + x1) / 2
    my = (y0 + y1) / 2
    # Faint upward bow (control points lifted by `bow`)
    c1 = (x0 + (x1 - x0) * 0.33, y0 + (y1 - y0) * 0.33 + bow)
    c2 = (x0 + (x1 - x0) * 0.66, y0 + (y1 - y0) * 0.66 + bow)
    brush_stroke(t, (x0, y0), c1, c2, (x1, y1), peak=peak, kind="heng", samples=170)


def shu(t, x0, y0, x1, y1, peak=18):
    c1 = (x0 + (x1 - x0) * 0.33, y0 + (y1 - y0) * 0.33)
    c2 = (x0 + (x1 - x0) * 0.66, y0 + (y1 - y0) * 0.66)
    brush_stroke(t, (x0, y0), c1, c2, (x1, y1), peak=peak, kind="shu", samples=170)


def pie(t, x0, y0, x1, y1, peak=20, curve=18):
    """撇: heavy head, bow outward to the right (concave-left)."""
    dx = x1 - x0
    dy = y1 - y0
    # Perpendicular to chord, rotated to bow rightward (for a down-left pie).
    length = math.hypot(dx, dy) or 1.0
    nx = -dy / length
    ny = dx / length
    # Sign so the bow goes to the right side of the head-to-tail line.
    if nx < 0:
        nx, ny = -nx, -ny
    c1 = (x0 + dx * 0.30 + nx * curve, y0 + dy * 0.30 + ny * curve)
    c2 = (x0 + dx * 0.65 + nx * (curve * 0.6), y0 + dy * 0.65 + ny * (curve * 0.6))
    brush_stroke(t, (x0, y0), c1, c2, (x1, y1), peak=peak, kind="pie", samples=180)


def na(t, x0, y0, x1, y1, peak=22, curve=14):
    """捺: fine head, broadens to heavy pressed tail with flat-kick plateau."""
    dx = x1 - x0
    dy = y1 - y0
    length = math.hypot(dx, dy) or 1.0
    nx = -dy / length
    ny = dx / length
    # Bow to the left side of head-to-tail (so a down-right na bows downward).
    if ny > 0:
        nx, ny = -nx, -ny
    c1 = (x0 + dx * 0.30 + nx * (curve * 0.6), y0 + dy * 0.30 + ny * (curve * 0.6))
    c2 = (x0 + dx * 0.65 + nx * curve, y0 + dy * 0.65 + ny * curve)
    brush_stroke(t, (x0, y0), c1, c2, (x1, y1), peak=peak, kind="na", samples=200)


def dian(t, x0, y0, x1, y1, peak=18):
    """点: short stroke, thin entry → belly → tapered tail."""
    dx = x1 - x0
    dy = y1 - y0
    c1 = (x0 + dx * 0.40, y0 + dy * 0.40)
    c2 = (x0 + dx * 0.70, y0 + dy * 0.70)
    brush_stroke(t, (x0, y0), c1, c2, (x1, y1), peak=peak, kind="dian", samples=120)


# ---------------------------------------------------------------------------
# Tasks
# ---------------------------------------------------------------------------

# ── Task 01 | 大 | dà
def task_01(screen, t):
    reset_turtle(t)
    # Apex of 撇/捺 well above the heng. Heng cuts through both limbs at
    # ~30-40% down from apex. Heng length >= 1.4x the limb-crossing span.
    apex_x, apex_y = 0, 170          # shared apex of 撇 and 捺
    # 撇 from apex sweeping down-left
    pie_tail = (-150, -180)
    # 捺 from apex sweeping down-right
    na_tail = (160, -180)

    # Heng crossing height — at ~35% down from apex to tail (y from 170 -> -180)
    cross_y = apex_y - 0.35 * (apex_y - pie_tail[1])  # ≈ 170 - 122 = 48
    # Where the 撇 line is at cross_y (interpolate linearly head->tail)
    frac_pie = (apex_y - cross_y) / (apex_y - pie_tail[1])
    pie_x_at_cross = apex_x + (pie_tail[0] - apex_x) * frac_pie
    frac_na = (apex_y - cross_y) / (apex_y - na_tail[1])
    na_x_at_cross = apex_x + (na_tail[0] - apex_x) * frac_na

    span = abs(na_x_at_cross - pie_x_at_cross)
    heng_half = 0.5 * 1.55 * span   # 1.55x the limb-crossing span
    heng_left = (-heng_half, cross_y)
    heng_right = (heng_half, cross_y)

    # Draw heng first (so limbs cross over it visually, but order doesn't change OCR)
    heng(t, heng_left[0], heng_left[1], heng_right[0], heng_right[1], peak=18, bow=4)
    pie(t, apex_x, apex_y, pie_tail[0], pie_tail[1], peak=22, curve=28)
    na(t, apex_x, apex_y, na_tail[0], na_tail[1], peak=24, curve=22)

    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_大.png"))


# ── Task 02 | 入 | rù
def task_02(screen, t):
    reset_turtle(t)
    # Only 撇 has the top apex. 捺 starts ON the 撇's spine at ~50% down.
    pie_head = (10, 180)
    pie_tail = (-160, -180)

    # Junction at 50% down the 撇's spine.
    frac = 0.50
    junction = (
        pie_head[0] + (pie_tail[0] - pie_head[0]) * frac,
        pie_head[1] + (pie_tail[1] - pie_head[1]) * frac,
    )
    # 捺 ends well below and to the right (dominates right extent).
    na_tail = (200, -200)

    pie(t, pie_head[0], pie_head[1], pie_tail[0], pie_tail[1], peak=22, curve=26)
    na(t, junction[0], junction[1], na_tail[0], na_tail[1], peak=24, curve=22)

    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "02_入.png"))


# ── Task 03 | 又 | yòu
def task_03(screen, t):
    reset_turtle(t)
    # 横撇 — compound, one continuous brushed path.
    # Short heng arm upper-left → corner 顿笔 → 撇 tail sweeping down-left.
    heng_start = (-120, 140)
    corner = (60, 160)          # short heng arm with faint upward tilt
    pie_end = (-110, -160)      # 撇 tail to lower-left

    # Bezier 1: short heng → corner
    seg1 = (
        heng_start,
        (heng_start[0] + 80, heng_start[1] + 6),
        (corner[0] - 50, corner[1] + 4),
        corner,
    )
    # Bezier 2: corner → 撇 tail (bows rightward like a 撇)
    cdx = pie_end[0] - corner[0]
    cdy = pie_end[1] - corner[1]
    length = math.hypot(cdx, cdy) or 1.0
    nx, ny = -cdy / length, cdx / length
    if nx < 0:
        nx, ny = -nx, -ny
    seg2 = (
        corner,
        (corner[0] + cdx * 0.30 + nx * 28, corner[1] + cdy * 0.30 + ny * 28),
        (corner[0] + cdx * 0.65 + nx * 16, corner[1] + cdy * 0.65 + ny * 16),
        pie_end,
    )
    brush_compound(
        t,
        [seg1, seg2],
        peak=22,
        kind_per_segment=["heng", "pie"],
        dunbi_factor=1.55,        # lift corner to dunbi=2
        samples_per_segment=140,
    )

    # 捺 crossing through: from upper-middle (just below the heng arm) sweeping
    # to lower-right.
    na_head = (-40, 70)
    na_tail = (170, -180)
    na(t, na_head[0], na_head[1], na_tail[0], na_tail[1], peak=24, curve=22)

    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "03_又.png"))


# ── Task 04 | 个 | gè
def task_04(screen, t):
    reset_turtle(t)
    # 撇 + 捺 sharing top apex (like 人), then a centered shu from apex down.
    apex = (0, 200)
    pie_tail = (-160, -60)
    na_tail = (160, -60)

    pie(t, apex[0], apex[1], pie_tail[0], pie_tail[1], peak=22, curve=28)
    na(t, apex[0], apex[1], na_tail[0], na_tail[1], peak=24, curve=22)

    # Centered shu dropping straight down from the apex through the middle.
    shu_top = (0, 100)            # start a bit below apex so the cap reads
    shu_bot = (0, -200)
    shu(t, shu_top[0], shu_top[1], shu_bot[0], shu_bot[1], peak=18)

    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "04_个.png"))


# ── Task 05 | 不 | bù
def task_05(screen, t):
    reset_turtle(t)
    # heng (top) wide, then 撇 (long, head on heng's left half, sweeping
    # down-left), shu (centered, below the heng), 点 (right of shu, midway).
    heng_left = (-200, 150)
    heng_right = (200, 150)
    heng(t, heng_left[0], heng_left[1], heng_right[0], heng_right[1], peak=18, bow=4)

    # 撇: head sits ON the heng, on its left half; tail goes down-left.
    pie_head = (-50, 150)
    pie_tail = (-200, -180)
    pie(t, pie_head[0], pie_head[1], pie_tail[0], pie_tail[1], peak=22, curve=24)

    # shu: centered, below the heng, dropping straight down.
    shu_top = (0, 145)            # touches heng just below the upper edge
    shu_bot = (0, -180)
    shu(t, shu_top[0], shu_top[1], shu_bot[0], shu_bot[1], peak=18)

    # 点: right of shu, midway down.
    dian_start = (75, 30)
    dian_end = (140, -40)
    dian(t, dian_start[0], dian_start[1], dian_end[0], dian_end[1], peak=18)

    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "05_不.png"))


# ── Task 06 | 木 | mù
def task_06(screen, t):
    reset_turtle(t)
    # heng (mid-upper), shu (centered, crossing through and BELOW the heng so
    # it doesn't read as 大), 撇 (from heng-shu intersection, down-left),
    # 捺 (from same intersection, down-right).
    heng_y = 100
    heng_left = (-220, heng_y)
    heng_right = (220, heng_y)
    heng(t, heng_left[0], heng_left[1], heng_right[0], heng_right[1], peak=18, bow=4)

    # shu: centered, must extend BELOW the heng — start above, end well below.
    shu_top = (0, 200)
    shu_bot = (0, -220)
    shu(t, shu_top[0], shu_top[1], shu_bot[0], shu_bot[1], peak=18)

    # 撇 + 捺 from the heng-shu intersection.
    inter = (0, heng_y)
    pie_tail = (-200, -120)
    na_tail = (200, -120)
    pie(t, inter[0], inter[1], pie_tail[0], pie_tail[1], peak=22, curve=24)
    na(t, inter[0], inter[1], na_tail[0], na_tail[1], peak=24, curve=18)

    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "06_木.png"))


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0, 0)
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    for task in (task_01, task_02, task_03, task_04, task_05, task_06):
        task(screen, t)


if __name__ == "__main__":
    main()
