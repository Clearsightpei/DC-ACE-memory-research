"""Cycle 12 — Drawer attempts.

All 6 are carry-overs with specific composition fixes (see brief).
Bézier centerline + per-sample pensize; middle >= 50% of peak;
compound strokes use single continuous path with corner thickening.
"""

import io
import os
import math
import turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))


# ---------- canvas helpers ----------

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


# ---------- bezier with per-sample pensize ----------

def cubic(p0, p1, p2, p3, n):
    pts = []
    for i in range(n + 1):
        u = i / n
        v = 1 - u
        x = (v ** 3) * p0[0] + 3 * (v ** 2) * u * p1[0] + 3 * v * (u ** 2) * p2[0] + (u ** 3) * p3[0]
        y = (v ** 3) * p0[1] + 3 * (v ** 2) * u * p1[1] + 3 * v * (u ** 2) * p2[1] + (u ** 3) * p3[1]
        pts.append((x, y))
    return pts


def thickness_profile(n, peak, mode):
    """Return list of per-sample pensize. middle >= 50% of peak.

    mode:
      'both'        — fine→peak→fine, symmetric (横/竖).
      'heavy_start' — peak at start, taper to fine end (撇/提).
      'heavy_end'   — fine start, peak at end (捺 — flat kick at tail).
      'belly'       — peak at ~40%, taper both sides (点).
      'flat'        — constant.
    """
    fine = max(2, peak * 0.35)
    mid_floor = peak * 0.5
    out = []
    for i in range(n + 1):
        u = i / n
        if mode == "both":
            # symmetric bell-ish: fine ends, mid >= 50%
            w = fine + (peak - fine) * math.sin(math.pi * u)
            w = max(w, mid_floor if 0.15 < u < 0.85 else fine)
        elif mode == "heavy_start":
            w = fine + (peak - fine) * (1 - u) ** 0.7
            w = max(w, mid_floor if u < 0.7 else fine * 0.9)
        elif mode == "heavy_end":
            w = fine + (peak - fine) * (u ** 0.7)
            w = max(w, mid_floor if u > 0.3 else fine * 0.9)
        elif mode == "belly":
            # peak near 0.4
            c = 0.4
            w = fine + (peak - fine) * math.exp(-((u - c) ** 2) / 0.06)
        else:  # flat
            w = peak
        out.append(max(2, w))
    return out


def draw_bezier(t, p0, p1, p2, p3, peak=14, mode="both", n=140):
    pts = cubic(p0, p1, p2, p3, n)
    widths = thickness_profile(n, peak, mode)
    t.penup()
    t.goto(*pts[0])
    t.pensize(widths[0])
    t.pendown()
    for i in range(1, len(pts)):
        t.pensize(widths[i])
        t.goto(*pts[i])
    t.penup()


# ---------- atomic strokes ----------

def heng(t, x0, y0, length, peak=14, dip=0.0):
    """Horizontal stroke. dip>0 makes a gentle V (middle dips down)."""
    x1 = x0 + length
    midx = (x0 + x1) / 2
    midy = y0 - dip
    p0 = (x0, y0)
    p1 = (x0 + length * 0.33, midy + (y0 - midy) * 0.3)
    p2 = (x0 + length * 0.66, midy + (y0 - midy) * 0.3)
    p3 = (x1, y0)
    # For a real dip, route control points through midy
    p1 = (midx - length * 0.18, midy + (y0 - midy) * 0.2)
    p2 = (midx + length * 0.18, midy + (y0 - midy) * 0.2)
    draw_bezier(t, p0, p1, p2, p3, peak=peak, mode="both")


def shu(t, x0, y0, length, peak=14):
    p0 = (x0, y0)
    p3 = (x0, y0 - length)
    p1 = (x0, y0 - length * 0.33)
    p2 = (x0, y0 - length * 0.66)
    draw_bezier(t, p0, p1, p2, p3, peak=peak, mode="both")


def pie(t, x0, y0, x1, y1, peak=14, curve=0.25):
    """Diagonal sweep down-and-left (or anywhere). heavy_start."""
    dx, dy = x1 - x0, y1 - y0
    # control points slightly bowed
    nx, ny = -dy, dx  # perpendicular
    nlen = math.hypot(nx, ny) or 1
    nx /= nlen
    ny /= nlen
    bow = curve * math.hypot(dx, dy)
    p0 = (x0, y0)
    p3 = (x1, y1)
    p1 = (x0 + dx * 0.33 + nx * bow * 0.6, y0 + dy * 0.33 + ny * bow * 0.6)
    p2 = (x0 + dx * 0.66 + nx * bow * 0.4, y0 + dy * 0.66 + ny * bow * 0.4)
    draw_bezier(t, p0, p1, p2, p3, peak=peak, mode="heavy_start")


def na(t, x0, y0, x1, y1, peak=18, curve=0.18):
    """Diagonal sweep down-and-right. heavy_end (flat kick at tail)."""
    dx, dy = x1 - x0, y1 - y0
    nx, ny = -dy, dx
    nlen = math.hypot(nx, ny) or 1
    nx /= nlen
    ny /= nlen
    bow = curve * math.hypot(dx, dy)
    # bow downward (negative side)
    p0 = (x0, y0)
    p3 = (x1, y1)
    p1 = (x0 + dx * 0.33 - nx * bow * 0.4, y0 + dy * 0.33 - ny * bow * 0.4)
    p2 = (x0 + dx * 0.66 - nx * bow * 0.7, y0 + dy * 0.66 - ny * bow * 0.7)
    draw_bezier(t, p0, p1, p2, p3, peak=peak, mode="heavy_end")


def dian(t, x0, y0, x1, y1, peak=14):
    """Dot: belly thickness, short stroke."""
    p0 = (x0, y0)
    p3 = (x1, y1)
    dx, dy = x1 - x0, y1 - y0
    p1 = (x0 + dx * 0.3, y0 + dy * 0.3)
    p2 = (x0 + dx * 0.7, y0 + dy * 0.7)
    draw_bezier(t, p0, p1, p2, p3, peak=peak, mode="belly", n=80)


# ---------- compound strokes ----------

def heng_zhe(t, x0, y0, h_len, v_len, peak=14):
    """横折: horizontal then turn down. Single continuous path,
    corner thickening (顿笔) via a brief belly dot on the corner."""
    heng(t, x0, y0, h_len, peak=peak)
    # corner thickening — small dot
    corner = (x0 + h_len, y0)
    t.penup()
    t.goto(*corner)
    t.pensize(peak * 1.15)
    t.dot(int(peak * 1.2))
    shu(t, x0 + h_len, y0, v_len, peak=peak)


def heng_zhe_gou(t, x0, y0, h_len, v_len, peak=14, hook=22):
    """横折钩: 横折 with a short up-left hook at bottom."""
    heng_zhe(t, x0, y0, h_len, v_len, peak=peak)
    # hook tail-arm: from (x0+h_len, y0-v_len) angle up-left
    bx, by = x0 + h_len, y0 - v_len
    hx, hy = bx - hook * 0.9, by + hook * 0.7
    p0 = (bx, by)
    p3 = (hx, hy)
    p1 = (bx - hook * 0.3, by + hook * 0.1)
    p2 = (bx - hook * 0.7, by + hook * 0.5)
    draw_bezier(t, p0, p1, p2, p3, peak=peak * 0.7, mode="heavy_start", n=60)


def shu_wan_gou(t, x0, y0, v_len, h_len, peak=14, hook=50):
    """竖弯钩: vertical down, curve right along floor, then sharp up-right hook.
    hook is LONG (~50px) per memory."""
    # vertical down
    shu(t, x0, y0, v_len, peak=peak)
    # curve right along bottom — bezier from (x0, y0-v_len) to (x0+h_len, y0-v_len)
    sx, sy = x0, y0 - v_len
    ex, ey = x0 + h_len, y0 - v_len + 5
    p0 = (sx, sy)
    p3 = (ex, ey)
    p1 = (sx + h_len * 0.1, sy - 25)
    p2 = (sx + h_len * 0.6, sy - 18)
    draw_bezier(t, p0, p1, p2, p3, peak=peak, mode="both", n=100)
    # corner thickening at curve endpoint
    t.penup()
    t.goto(ex, ey)
    t.dot(int(peak * 1.1))
    # hook — long, sharp, going up-right
    hx, hy = ex + hook * 0.55, ey + hook
    p0 = (ex, ey)
    p3 = (hx, hy)
    p1 = (ex + hook * 0.15, ey + hook * 0.35)
    p2 = (ex + hook * 0.35, ey + hook * 0.75)
    draw_bezier(t, p0, p1, p2, p3, peak=peak * 0.75, mode="heavy_start", n=70)


# ============================================================
#                       TASK FUNCTIONS
# ============================================================


# ── Task 01 | 大 | dà
def draw_da(t, screen):
    """大: wide limb tails (x ≈ ±260), short apex stub above heng,
    heng with slight V-dip."""
    reset_turtle(t)
    # Heng: y=+30, spans roughly x = -210 .. +210, slight V dip
    heng(t, -210, 30, 420, peak=15, dip=12)
    # Apex stub: very short — apex at (0, +130), then down to junction
    # Use a heng for the apex-to-junction? Actually use a small pie from apex
    # down to (0, +30) — short vertical sweep
    # Instead: draw the 撇 starting from apex (0, +130) down-left to (-260, -180)
    pie(t, 0, 130, -260, -180, peak=16, curve=0.18)
    # 捺: from apex (0, +130) down-right to (+260, -180)
    na(t, 0, 130, 260, -180, peak=19, curve=0.16)
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_大.png"))


# ── Task 02 | 入 | rù
def draw_ru(t, screen):
    """入: SHORTER 撇 (~280), LONGER dominant 捺 leaning further right.
    Junction at upper portion of 捺."""
    reset_turtle(t)
    # 捺 first as the dominant stroke: from apex (0, +180) down-right far
    # length large — endpoint at (+320, -200) so 捺 extends further right
    # than 撇 extends left
    na(t, 0, 180, 320, -200, peak=20, curve=0.18)
    # 撇 shorter (~280 length): from a junction point on the 捺's upper
    # portion (about 25% down: x≈+80, y≈+85) down-left to (-200, -90)
    # That gives 撇 horizontal extent ~280 (from +80 to -200)
    pie(t, 80, 85, -200, -90, peak=14, curve=0.18)
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "02_入.png"))


# ── Task 03 | 火 | huǒ
def draw_huo(t, screen):
    """火: two 点 OUTSIDE the apex's horizontal extent, at apex HEIGHT
    (not above). Apex at (0, +140). Left 点 belly at (-60, +140) slopes
    down-and-right; right 点 mirror."""
    reset_turtle(t)
    apex_y = 140
    # Center 撇 + 捺 first (the "head")
    # Apex at (0, +140); 撇 down-left to (-150, -180); 捺 down-right to (+150, -180)
    # A small 竖 stub from apex up a bit? Actually 火 has 撇+点+人.
    # Standard 火 strokes: 1) 点 (left dot), 2) 撇 (left small slant),
    # 3) 人-like 撇+捺. Simplify: draw center 撇 & 捺 as the human body,
    # then two 点 as ears.
    # Center 撇: from (0, +140) down to (-150, -200)
    pie(t, 0, apex_y, -150, -200, peak=15, curve=0.18)
    # Center 捺: from (0, +140) down to (+150, -200)
    na(t, 0, apex_y, 150, -200, peak=18, curve=0.18)
    # Left 点: belly at (-95, +140), slopes down-and-right toward apex.
    # Start near (-115, +160), end near (-60, +115). OUTSIDE apex (apex
    # has horizontal extent ~0 at apex_y).
    dian(t, -115, 165, -55, 110, peak=14)
    # Right 点: mirror — slopes down-and-left.
    dian(t, 115, 165, 55, 110, peak=14)
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "03_火.png"))


# ── Task 04 | 也 | yě
def draw_ye(t, screen):
    """也: 横折钩 frame + middle 竖 + 竖弯钩 (with LONG SHARP up-right hook).
    The long hook is the distinguishing feature vs 卫."""
    reset_turtle(t)
    # Stroke 1: 横折钩 — top heng + right 竖 + small hook at bottom-right.
    # heng from (-160, +160) to (+160, +160), then down to (+160, +20),
    # hook back up-left.
    heng_zhe_gou(t, -160, 160, 320, 140, peak=14, hook=22)
    # Stroke 2: middle 竖 — from (-20, +100) down to (-20, -20)
    shu(t, -20, 100, 120, peak=13)
    # Stroke 3: 竖弯钩 — left vertical, curve along floor, LONG SHARP up-right hook
    # Start at (-160, +100), down to (-160, -120), curve right to (+200, -120),
    # then SHARP UP-RIGHT hook of length ~50px.
    shu_wan_gou(t, -160, 100, 220, 360, peak=14, hook=55)
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "04_也.png"))


# ── Task 05 | 力 | lì
def draw_li(t, screen):
    """力: 横折钩 with top heng extending FAR LEFT of the corner
    (heng starts x≈-150, corner at x≈+80) + 撇 leg.
    Without the left-extending top, OCR reads 刀."""
    reset_turtle(t)
    # Stroke 1: 横折钩 — top heng starts (-150, +180) extends to (+80, +180),
    # then 竖 down to (+80, -80), then hook up-left.
    heng_zhe_gou(t, -150, 180, 230, 260, peak=15, hook=24)
    # Stroke 2: 撇 — from inside the frame top, swooping down-left out past frame.
    # Start at (-30, +120), end at (-180, -200).
    pie(t, -30, 120, -180, -200, peak=15, curve=0.22)
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "05_力.png"))


# ── Task 06 | 巴 | bā
def draw_ba(t, screen):
    """巴: TALL DOUBLE-DECKER upper rectangle (closed top + closed bottom +
    middle divider heng) + 竖弯钩 extending below.
    Distinguishes from 已's single-corner top."""
    reset_turtle(t)
    # Upper rectangle: top-left (-100, +200), top-right (+100, +200),
    # bottom-left (-100, +0), bottom-right (+100, +0).
    # Stroke 1: left 竖 — from (-100, +200) down to (-100, 0)
    shu(t, -100, 200, 200, peak=13)
    # Stroke 2: 横折 — top heng from (-100, +200) to (+100, +200) then
    # 竖 down to (+100, +0). This closes top and right.
    # Re-start at left-top:
    heng_zhe(t, -100, 200, 200, 200, peak=14)
    # Stroke 3: middle divider heng — at y = +100, from x=-100 to x=+100
    heng(t, -100, 100, 200, peak=13)
    # Stroke 4: bottom closing heng of upper rectangle — y = 0
    heng(t, -100, 0, 200, peak=13)
    # Stroke 5: 竖弯钩 extending below — start at (-100, 0), down to
    # (-100, -160), curve right to (+140, -160), hook up-right.
    shu_wan_gou(t, -100, 0, 160, 240, peak=14, hook=50)
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "06_巴.png"))


# ============================================================
#                          MAIN
# ============================================================

def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0, 0)
    t = turtle.Turtle()

    draw_da(t, screen)
    draw_ru(t, screen)
    draw_huo(t, screen)
    draw_ye(t, screen)
    draw_li(t, screen)
    draw_ba(t, screen)


if __name__ == "__main__":
    main()
