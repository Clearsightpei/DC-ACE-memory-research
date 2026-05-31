"""Cycle 14 drawer — 6 tasks: 火, 也, 巴, 见, 天, 了.

Bezier-with-per-sample-pensize. Compound strokes = continuous brushed
sweep + corner 顿笔 + short hook tail-arms. Middle pensize >= 50% peak.
"""

import os
import turtle
from PIL import Image

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ── Turtle / screen setup ──────────────────────────────────────────
screen = turtle.Screen()
screen.setup(width=820, height=620)
screen.screensize(800, 600)
screen.bgcolor("white")
screen.tracer(0, 0)

canvas = screen.getcanvas()

t = turtle.RawTurtle(screen)
t.hideturtle()
t.speed(0)
t.penup()


# ── Helpers ────────────────────────────────────────────────────────
def cubic_bezier(p0, p1, p2, p3, n=160):
    pts = []
    for i in range(n + 1):
        u = i / n
        x = ((1 - u) ** 3) * p0[0] + 3 * ((1 - u) ** 2) * u * p1[0] + \
            3 * (1 - u) * (u ** 2) * p2[0] + (u ** 3) * p3[0]
        y = ((1 - u) ** 3) * p0[1] + 3 * ((1 - u) ** 2) * u * p1[1] + \
            3 * (1 - u) * (u ** 2) * p2[1] + (u ** 3) * p3[1]
        pts.append((x, y))
    return pts


def brushed_stroke(pts, w_start, w_mid, w_end, color="black"):
    """Draw a brushed stroke with per-sample pensize via dot-stamping.
    w_mid >= 50% of peak. Smooth piecewise-linear taper start→mid→end.
    """
    n = len(pts)
    if n < 2:
        return
    peak = max(w_start, w_mid, w_end)
    floor = 0.5 * peak
    w_mid = max(w_mid, floor)
    half = (n - 1) / 2.0
    for i, (x, y) in enumerate(pts):
        if i <= half:
            u = i / half if half else 0
            w = w_start + (w_mid - w_start) * u
        else:
            u = (i - half) / half if half else 0
            w = w_mid + (w_end - w_mid) * u
        w = max(1.5, w)
        t.penup()
        t.goto(x, y)
        t.dot(w, color)


def dot_blob(x, y, size, color="black"):
    t.penup()
    t.goto(x, y)
    t.dot(size, color)


def save_png(path):
    screen.update()
    ps_path = path.replace(".png", ".eps")
    canvas.postscript(file=ps_path, colormode="color",
                      width=820, height=620,
                      pagewidth=820, pageheight=620)
    img = Image.open(ps_path)
    img.load(scale=2)
    img = img.convert("RGB")
    # Resize down to a clean target size if very large
    w, h = img.size
    target_w = 800
    if w != target_w:
        ratio = target_w / w
        img = img.resize((target_w, int(h * ratio)), Image.LANCZOS)
    img.save(path, "PNG")
    try:
        os.remove(ps_path)
    except OSError:
        pass


# Atomic stroke helpers ----------------------------------------------
def heng(x0, y0, length, w_peak=22, curve=8):
    """Horizontal stroke, both ends heavy (slight 顿笔)."""
    x1 = x0 + length
    p0 = (x0, y0)
    p1 = (x0 + length * 0.33, y0 + curve)
    p2 = (x0 + length * 0.66, y0 + curve)
    p3 = (x1, y0)
    pts = cubic_bezier(p0, p1, p2, p3, n=140)
    brushed_stroke(pts, w_start=w_peak, w_mid=w_peak * 0.6,
                   w_end=w_peak, color="black")
    # corner 顿笔 dots
    dot_blob(x0, y0, w_peak * 1.05)
    dot_blob(x1, y0, w_peak * 1.05)


def shu(x0, y0, length, w_peak=22, curve=4):
    """Vertical stroke, both ends heavy."""
    y1 = y0 - length
    p0 = (x0, y0)
    p1 = (x0 - curve, y0 - length * 0.33)
    p2 = (x0 - curve, y0 - length * 0.66)
    p3 = (x0, y1)
    pts = cubic_bezier(p0, p1, p2, p3, n=140)
    brushed_stroke(pts, w_start=w_peak, w_mid=w_peak * 0.6,
                   w_end=w_peak, color="black")
    dot_blob(x0, y0, w_peak * 1.05)
    dot_blob(x0, y1, w_peak * 1.05)


def pie(x0, y0, dx, dy, w_peak=22):
    """撇 (left-falling): heavy start, fine end."""
    x1 = x0 + dx
    y1 = y0 + dy
    p0 = (x0, y0)
    p1 = (x0 + dx * 0.3, y0 + dy * 0.15)
    p2 = (x0 + dx * 0.6, y0 + dy * 0.55)
    p3 = (x1, y1)
    pts = cubic_bezier(p0, p1, p2, p3, n=160)
    brushed_stroke(pts, w_start=w_peak, w_mid=w_peak * 0.55,
                   w_end=w_peak * 0.18, color="black")
    dot_blob(x0, y0, w_peak * 1.1)


def na(x0, y0, dx, dy, w_peak=24):
    """捺 (right-falling): fine start, heavy near end, flat horizontal kick.
    Last ~15% of stroke is near-peak width and horizontal.
    """
    # Main body: from (x0,y0) sweeping to a 'kick point' before the tail.
    kick_in_x = x0 + dx * 0.85
    kick_in_y = y0 + dy * 0.92
    p0 = (x0, y0)
    p1 = (x0 + dx * 0.30, y0 + dy * 0.45)
    p2 = (x0 + dx * 0.65, y0 + dy * 0.80)
    p3 = (kick_in_x, kick_in_y)
    pts = cubic_bezier(p0, p1, p2, p3, n=140)
    brushed_stroke(pts, w_start=w_peak * 0.18, w_mid=w_peak * 0.55,
                   w_end=w_peak * 0.95, color="black")
    # Flat horizontal kick at tail (last 15%), near-peak width, horizontal.
    tail_len = abs(dx) * 0.18 + 14
    tail_pts = []
    n_tail = 40
    for i in range(n_tail + 1):
        u = i / n_tail
        x = kick_in_x + tail_len * u
        y = kick_in_y  # strictly horizontal
        tail_pts.append((x, y))
    brushed_stroke(tail_pts, w_start=w_peak * 0.95, w_mid=w_peak * 0.95,
                   w_end=w_peak * 0.55, color="black")


def dian(x0, y0, dx, dy, w_peak=20):
    """点: belly heavy, tail fine."""
    p0 = (x0, y0)
    p1 = (x0 + dx * 0.35, y0 + dy * 0.40)
    p2 = (x0 + dx * 0.70, y0 + dy * 0.75)
    p3 = (x0 + dx, y0 + dy)
    pts = cubic_bezier(p0, p1, p2, p3, n=120)
    brushed_stroke(pts, w_start=w_peak * 0.35, w_mid=w_peak,
                   w_end=w_peak * 0.18, color="black")


# Compound stroke helpers --------------------------------------------
def heng_zhe(x0, y0, hlen, vlen, w_peak=22):
    """横折: heng → corner 顿笔 → shu (no hook)."""
    # Heng portion
    p0 = (x0, y0)
    p1 = (x0 + hlen * 0.33, y0 + 6)
    p2 = (x0 + hlen * 0.66, y0 + 6)
    p3 = (x0 + hlen, y0)
    pts = cubic_bezier(p0, p1, p2, p3, n=120)
    brushed_stroke(pts, w_peak, w_peak * 0.6, w_peak * 1.1)
    # Corner 顿笔 (heavier dot)
    dot_blob(x0 + hlen, y0, w_peak * 1.3)
    # Shu portion
    sx = x0 + hlen
    p0 = (sx, y0)
    p1 = (sx - 4, y0 - vlen * 0.33)
    p2 = (sx - 4, y0 - vlen * 0.66)
    p3 = (sx, y0 - vlen)
    pts = cubic_bezier(p0, p1, p2, p3, n=120)
    brushed_stroke(pts, w_peak * 1.1, w_peak * 0.6, w_peak)
    dot_blob(x0, y0, w_peak * 1.05)
    dot_blob(sx, y0 - vlen, w_peak * 1.05)


def heng_zhe_gou(x0, y0, hlen, vlen, hook=24, w_peak=22):
    """横折钩: heng → corner 顿笔 → shu → small 钩 hooking up-left.
    For 也: hook at bottom-LEFT of vertical end (i.e., from (sx, y0-vlen)
    point we draw a short arm going left-and-up).
    """
    # Heng
    p0 = (x0, y0)
    p1 = (x0 + hlen * 0.33, y0 + 6)
    p2 = (x0 + hlen * 0.66, y0 + 6)
    p3 = (x0 + hlen, y0)
    pts = cubic_bezier(p0, p1, p2, p3, n=120)
    brushed_stroke(pts, w_peak, w_peak * 0.6, w_peak * 1.1)
    dot_blob(x0, y0, w_peak * 1.05)
    dot_blob(x0 + hlen, y0, w_peak * 1.3)  # corner 顿笔
    # Shu
    sx = x0 + hlen
    sy_end = y0 - vlen
    p0 = (sx, y0)
    p1 = (sx - 4, y0 - vlen * 0.33)
    p2 = (sx - 4, y0 - vlen * 0.66)
    p3 = (sx, sy_end)
    pts = cubic_bezier(p0, p1, p2, p3, n=120)
    brushed_stroke(pts, w_peak * 1.1, w_peak * 0.65, w_peak * 1.0)
    # Hook (short arm up-and-left from end)
    hp0 = (sx, sy_end)
    hp1 = (sx - hook * 0.4, sy_end + hook * 0.2)
    hp2 = (sx - hook * 0.8, sy_end + hook * 0.5)
    hp3 = (sx - hook, sy_end + hook * 0.8)
    pts = cubic_bezier(hp0, hp1, hp2, hp3, n=70)
    brushed_stroke(pts, w_peak * 1.0, w_peak * 0.55, w_peak * 0.18)


def shu_wan_gou(x0, y0, vlen, curve_len, w_peak=22, hook=22):
    """竖弯钩: shu → curve right → small upward hook.
    Returns end point of the curve before hook for composition use.
    """
    # Vertical portion
    p0 = (x0, y0)
    p1 = (x0 - 3, y0 - vlen * 0.4)
    p2 = (x0 - 3, y0 - vlen * 0.8)
    p3 = (x0, y0 - vlen)
    pts = cubic_bezier(p0, p1, p2, p3, n=120)
    brushed_stroke(pts, w_peak, w_peak * 0.6, w_peak * 0.9)
    dot_blob(x0, y0, w_peak * 1.05)
    # Curve right portion
    cx = x0
    cy = y0 - vlen
    cp0 = (cx, cy)
    cp1 = (cx + curve_len * 0.30, cy - 6)
    cp2 = (cx + curve_len * 0.70, cy + 6)
    cp3 = (cx + curve_len, cy + 18)
    pts = cubic_bezier(cp0, cp1, cp2, cp3, n=120)
    brushed_stroke(pts, w_peak * 0.9, w_peak * 0.6, w_peak * 1.0)
    # Hook (short arm going up)
    end_x = cx + curve_len
    end_y = cy + 18
    hp0 = (end_x, end_y)
    hp1 = (end_x + 3, end_y + hook * 0.35)
    hp2 = (end_x + 1, end_y + hook * 0.7)
    hp3 = (end_x - 4, end_y + hook)
    pts = cubic_bezier(hp0, hp1, hp2, hp3, n=70)
    brushed_stroke(pts, w_peak * 1.0, w_peak * 0.55, w_peak * 0.18)
    return end_x, end_y


def heng_gou(x0, y0, hlen, hook=22, w_peak=22):
    """横钩: short heng → small 钩 at right end, hooking down-and-left."""
    p0 = (x0, y0)
    p1 = (x0 + hlen * 0.33, y0 + 6)
    p2 = (x0 + hlen * 0.66, y0 + 6)
    p3 = (x0 + hlen, y0)
    pts = cubic_bezier(p0, p1, p2, p3, n=120)
    brushed_stroke(pts, w_peak, w_peak * 0.6, w_peak * 1.1)
    dot_blob(x0, y0, w_peak * 1.05)
    dot_blob(x0 + hlen, y0, w_peak * 1.3)  # corner 顿笔
    # Hook down-and-left
    hx0 = x0 + hlen
    hy0 = y0
    hp0 = (hx0, hy0)
    hp1 = (hx0 - hook * 0.2, hy0 - hook * 0.35)
    hp2 = (hx0 - hook * 0.55, hy0 - hook * 0.7)
    hp3 = (hx0 - hook, hy0 - hook)
    pts = cubic_bezier(hp0, hp1, hp2, hp3, n=70)
    brushed_stroke(pts, w_peak * 1.0, w_peak * 0.55, w_peak * 0.18)


# ── Task 01 | 火 | huǒ ─────────────────────────────────────────────
def draw_huo():
    t.reset()
    t.hideturtle()
    t.penup()
    screen.bgcolor("white")

    # Apex is just the meeting point of 撇/捺 — NO vertical stub above it.
    apex_x, apex_y = 0, 80

    # 撇 (main left-falling): from apex down-left to bottom-left.
    pie(apex_x, apex_y, dx=-150, dy=-260, w_peak=24)

    # 捺 (main right-falling): from apex down-right with flat tail.
    na(apex_x, apex_y, dx=160, dy=-260, w_peak=26)

    # Two 点 flanking the apex (left and right), at apex height, sloping inward.
    # Left 点: at x ~ -110, slopes inward (down-right toward apex).
    dian(-110, apex_y + 10, dx=22, dy=-40, w_peak=22)
    # Right 点: at x ~ +110, slopes inward (down-left toward apex).
    dian(110, apex_y + 10, dx=-22, dy=-40, w_peak=22)

    save_png(os.path.join(OUT_DIR, "01_火.png"))


# ── Task 02 | 也 | yě ──────────────────────────────────────────────
def draw_ye():
    t.reset()
    t.hideturtle()
    t.penup()
    screen.bgcolor("white")

    # Stroke 1: 横折钩 forming the top + left wraparound.
    # Long heng across top, then drop down with hook at bottom-LEFT end.
    # x from -160 to +140 along top, then drop to y = -120; hook left.
    heng_zhe_gou(x0=-160, y0=120, hlen=300, vlen=240, hook=30, w_peak=22)

    # Stroke 2: short middle vertical (thinner so 横折钩 dominates).
    # Inside the frame, centered roughly at x = -20, top around y = 80,
    # ending around y = -50. THINNER pensize.
    shu(x0=-20, y0=80, length=130, w_peak=14, curve=2)

    # Stroke 3: 竖弯钩 from upper-right area sweeping right then hooking up.
    # Starts at (+80, +60), drops, curves right, hooks up.
    shu_wan_gou(x0=80, y0=60, vlen=170, curve_len=130, w_peak=22, hook=24)

    save_png(os.path.join(OUT_DIR, "02_也.png"))


# ── Task 03 | 巴 | bā ──────────────────────────────────────────────
def draw_ba():
    t.reset()
    t.hideturtle()
    t.penup()
    screen.bgcolor("white")

    # Tri-decker top structure: wider upper frame dominating the silhouette.
    # Upper frame is wide (x: -130 to +130), narrower bottom (竖弯钩 goes right).

    # Stroke 1: left vertical (long shu, top to mid-bottom).
    shu(x0=-130, y0=160, length=270, w_peak=22, curve=2)

    # Stroke 2: top 横折 forming top + right side of upper box.
    # Heng from (-130, 160) to (+130, 160); then drop down to (130, 30).
    heng_zhe(x0=-130, y0=160, hlen=260, vlen=130, w_peak=22)

    # Stroke 3: middle 横 (the dividing line of tri-decker), at y = 30.
    heng(x0=-130, y0=30, length=260, w_peak=20, curve=4)

    # Stroke 4: small inner 横 in upper compartment (tri-decker), at y = 95.
    heng(x0=-130, y0=95, length=260, w_peak=18, curve=4)

    # Stroke 5: bottom 竖弯钩 — descends from left then curves right, hooks up.
    # Starts from where the left vertical bottom is (-130, -110) extending down
    # then sweeping right and hooking up. This is the 巴 differentiator.
    shu_wan_gou(x0=-130, y0=30, vlen=140, curve_len=240, w_peak=22, hook=24)

    save_png(os.path.join(OUT_DIR, "03_巴.png"))


# ── Task 04 | 见 | jiàn ────────────────────────────────────────────
def draw_jian():
    t.reset()
    t.hideturtle()
    t.penup()
    screen.bgcolor("white")

    # 见 = 冂-like top frame with inner heng + 撇 leg exiting bottom-left
    # + 竖弯钩 leg exiting bottom-right (the 儿 base).

    # Stroke 1: left vertical of the upper 冂 frame.
    shu(x0=-100, y0=160, length=260, w_peak=22, curve=2)

    # Stroke 2: top 横折 (heng across top, then right vertical down).
    heng_zhe(x0=-100, y0=160, hlen=200, vlen=260, w_peak=22)

    # Stroke 3: inner 横 (the eye-line of 见), at y = 30.
    heng(x0=-100, y0=30, length=200, w_peak=18, curve=4)

    # Stroke 4: 撇 leg — DISTINCT third stroke, head inside frame at
    # bottom-left corner, sweep length ≥ 150 px going down-LEFT at ~45°.
    # Head at (-90, -90) (inside frame bottom-left), exiting to (-190, -200).
    # That's dx=-110, dy=-110, ~45° down-left, length ~155.
    pie(x0=-90, y0=-90, dx=-110, dy=-115, w_peak=22)

    # Stroke 5: 竖弯钩 — from inside frame bottom area, sweeping right and up.
    # Starts at (0, -90), drops, curves right, hooks up.
    shu_wan_gou(x0=0, y0=-90, vlen=80, curve_len=140, w_peak=22, hook=24)

    save_png(os.path.join(OUT_DIR, "04_见.png"))


# ── Task 05 | 天 | tiān ───────────────────────────────────────────
def draw_tian():
    t.reset()
    t.hideturtle()
    t.penup()
    screen.bgcolor("white")

    # 天 = two heng stacked + 撇 + 捺 below.
    # Top heng (shorter), middle heng (longer), then 撇/捺 from middle heng.

    # Stroke 1: top heng (shorter), at y = 160.
    heng(x0=-90, y0=160, length=180, w_peak=20, curve=5)

    # Stroke 2: middle heng (longer), at y = 70.
    heng(x0=-150, y0=70, length=300, w_peak=22, curve=6)

    # Stroke 3: 撇 — from center of middle heng (0, 70) down-left.
    pie(x0=0, y0=70, dx=-130, dy=-220, w_peak=22)

    # Stroke 4: 捺 — from center of middle heng (0, 70) down-right,
    # with emphasized flat horizontal kick at the tail.
    na(x0=0, y0=70, dx=140, dy=-220, w_peak=26)

    save_png(os.path.join(OUT_DIR, "05_天.png"))


# ── Task 06 | 了 | le ──────────────────────────────────────────────
def draw_le():
    t.reset()
    t.hideturtle()
    t.penup()
    screen.bgcolor("white")

    # 了 = 横钩 (top) + 竖钩 / curving descending stroke (body).

    # Stroke 1: 横钩 — short horizontal at top, with small 钩 hooking
    # down-and-left at the right end.
    heng_gou(x0=-120, y0=140, hlen=240, hook=30, w_peak=22)

    # Stroke 2: curving descending stroke (竖钩) from middle of the 横钩,
    # dropping down with small leftward hook at the bottom.
    # Starts at (0, 140) (middle of the heng), curves down to ~(-10, -180),
    # then small hook left at bottom.
    start_x, start_y = 0, 140
    end_x, end_y = -20, -180
    p0 = (start_x, start_y)
    p1 = (start_x + 18, start_y - 100)   # initial bulge right
    p2 = (start_x - 20, start_y - 220)   # then curve left
    p3 = (end_x, end_y)
    pts = cubic_bezier(p0, p1, p2, p3, n=160)
    brushed_stroke(pts, w_start=22, w_mid=14, w_end=20)
    dot_blob(start_x, start_y, 24)

    # Bottom leftward hook
    hp0 = (end_x, end_y)
    hp1 = (end_x - 12, end_y + 6)
    hp2 = (end_x - 26, end_y + 14)
    hp3 = (end_x - 40, end_y + 22)
    pts = cubic_bezier(hp0, hp1, hp2, hp3, n=70)
    brushed_stroke(pts, w_start=20, w_mid=12, w_end=4)

    save_png(os.path.join(OUT_DIR, "06_了.png"))


# ── Run all tasks ───────────────────────────────────────────────────
if __name__ == "__main__":
    draw_huo()
    draw_ye()
    draw_ba()
    draw_jian()
    draw_tian()
    draw_le()
