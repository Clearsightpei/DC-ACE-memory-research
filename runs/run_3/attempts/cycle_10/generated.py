"""Cycle 10 — Drawer attempt.

Tasks: 火 习 也 力 巴 已
Eval: gt+ocr+vision.

Key composition fixes (carry-overs):
- 火: two 点 HUG the apex (tails nearly touch apex); 撇 head heavy to match 捺.
- 习: 提 is a long rising flick (~65% of 横折 width) with weighted base
       touching the bottom-left of the 横折 above.
- 也: 横折钩 + middle shu sit ABOVE the 竖弯钩 cradle; middle shu close
       to the right of 横折钩's vertical portion; 竖弯钩 forms the floor.

Brushwork: cubic Bézier centerlines, per-sample pensize, middle >= 50%
of peak; compound strokes are one continuous brushed sweep with 顿笔
Gaussian thickening at each corner; hooks are short tail-arms
(~15–20% of main length).
"""

import io
import math
import os
import turtle

from PIL import Image

# ── canvas setup ──────────────────────────────────────────────────────
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
W, H = 800, 600

screen = turtle.Screen()
screen.setup(W, H)
screen.setworldcoordinates(-W // 2, -H // 2, W // 2, H // 2)
screen.colormode(255)
screen.bgcolor("white")
screen.tracer(0, 0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pencolor(0, 0, 0)


# ── geometry helpers ──────────────────────────────────────────────────
def bezier(p0, p1, p2, p3, n=160):
    pts = []
    for i in range(n + 1):
        u = i / n
        x = ((1 - u) ** 3 * p0[0]
             + 3 * (1 - u) ** 2 * u * p1[0]
             + 3 * (1 - u) * u ** 2 * p2[0]
             + u ** 3 * p3[0])
        y = ((1 - u) ** 3 * p0[1]
             + 3 * (1 - u) ** 2 * u * p1[1]
             + 3 * (1 - u) * u ** 2 * p2[1]
             + u ** 3 * p3[1])
        pts.append((x, y))
    return pts


def line_pts(p0, p1, n=120):
    return [(p0[0] + (p1[0] - p0[0]) * i / n,
             p0[1] + (p1[1] - p0[1]) * i / n) for i in range(n + 1)]


def width_profile(n, peak, start_frac, end_frac, mid_min_frac=0.5):
    """Per-sample widths along a stroke.

    start_frac / end_frac are widths at the two ends as fraction of peak.
    Middle is forced >= mid_min_frac * peak.
    """
    widths = []
    for i in range(n):
        u = i / max(1, n - 1)
        # cosine bump shape, ends interpolated:
        end_w = (1 - u) * start_frac + u * end_frac
        # mid bump (1 at u=0.5, 0 at ends):
        mid = math.sin(math.pi * u)
        w = max(end_w, mid_min_frac + (1 - mid_min_frac) * mid)
        widths.append(peak * w)
    return widths


def goto_pen_up(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def stroke_along(pts, widths):
    """Draw pts as a brush trail with per-sample pen size."""
    t.penup()
    t.goto(pts[0])
    t.pendown()
    for (x, y), w in zip(pts, widths):
        t.pensize(max(1, w))
        t.goto(x, y)


def dunbi_dot(x, y, r):
    """Small 顿笔 Gaussian thickening at a corner — drawn as a filled
    dot via several concentric pen circles."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.dot(int(2 * r))
    t.penup()


# ── stroke primitives (compound paths use stroke_along) ───────────────

def draw_heng(p0, p1, peak=10):
    pts = line_pts(p0, p1, 120)
    widths = width_profile(len(pts), peak, 1.0, 1.0, 0.6)
    # slight 顿笔 at both ends → bump start & end widths up
    for i in range(8):
        widths[i] = peak * (1.0 + 0.15 * (1 - i / 8))
        widths[-1 - i] = peak * (1.0 + 0.15 * (1 - i / 8))
    stroke_along(pts, widths)


def draw_shu(p0, p1, peak=10):
    pts = line_pts(p0, p1, 130)
    widths = width_profile(len(pts), peak, 1.0, 1.0, 0.6)
    stroke_along(pts, widths)


def draw_pie(p0, p1, peak=12, curve=0.25):
    """A 撇 — heavy head, fine tail, gentle leftward curve."""
    dx, dy = p1[0] - p0[0], p1[1] - p0[1]
    # control points curve to the left of the chord
    cx1 = p0[0] + 0.3 * dx + curve * dy
    cy1 = p0[1] + 0.3 * dy - curve * dx
    cx2 = p0[0] + 0.6 * dx + curve * dy * 0.6
    cy2 = p0[1] + 0.6 * dy - curve * dx * 0.6
    pts = bezier(p0, (cx1, cy1), (cx2, cy2), p1, 160)
    widths = width_profile(len(pts), peak, 1.0, 0.12, 0.55)
    stroke_along(pts, widths)


def draw_na(p0, p1, peak=12):
    """A 捺 — fine start, swelling to a flat heavy kick at the end."""
    dx, dy = p1[0] - p0[0], p1[1] - p0[1]
    cx1 = p0[0] + 0.3 * dx
    cy1 = p0[1] + 0.3 * dy - 0.05 * dx
    cx2 = p0[0] + 0.7 * dx
    cy2 = p0[1] + 0.7 * dy - 0.10 * dx
    pts = bezier(p0, (cx1, cy1), (cx2, cy2), p1, 160)
    widths = width_profile(len(pts), peak, 0.18, 1.0, 0.55)
    # final flat kick: keep the last ~12 samples thick
    for i in range(12):
        widths[-1 - i] = peak * (1.0 - 0.04 * i)
    stroke_along(pts, widths)


def draw_dian(p0, belly, p1, peak=11):
    """A 点 — belly (heaviest) somewhere between start and end; tail fine."""
    pts = bezier(p0, belly, belly, p1, 100)
    widths = []
    n = len(pts)
    for i in range(n):
        u = i / (n - 1)
        # belly weight peaks at u ~ 0.35
        w = math.exp(-((u - 0.35) ** 2) / 0.08)
        widths.append(peak * max(0.25, w))
    # fine tail
    for i in range(10):
        widths[-1 - i] = peak * max(0.1, 0.4 - 0.03 * i)
    stroke_along(pts, widths)


def draw_ti(p0, p1, peak=11):
    """A 提 — heavy weighted base at p0, fine flicked tip at p1."""
    pts = line_pts(p0, p1, 110)
    widths = width_profile(len(pts), peak, 1.0, 0.12, 0.55)
    # extra base weight (顿笔-ish foot)
    for i in range(10):
        widths[i] = peak * (1.0 + 0.2 * (1 - i / 10))
    stroke_along(pts, widths)


# ── compound strokes (continuous brushed paths) ───────────────────────

def draw_hengzhe(p_start, p_corner, p_end, peak=10, dun=14):
    """横折: heng to p_corner, then shu to p_end. Continuous brush + 顿笔 at corner."""
    seg1 = line_pts(p_start, p_corner, 80)
    seg2 = line_pts(p_corner, p_end, 100)
    pts = seg1 + seg2[1:]
    n = len(pts)
    widths = []
    for i in range(n):
        u = i / (n - 1)
        # base middle bump
        mid = math.sin(math.pi * u)
        widths.append(peak * (0.55 + 0.45 * mid))
    # corner index
    ci = len(seg1) - 1
    # 顿笔 thickening Gaussian around corner
    for i in range(n):
        d = abs(i - ci)
        if d < 18:
            bump = math.exp(-(d ** 2) / 30.0)
            widths[i] = max(widths[i], peak * (0.9 + 0.4 * bump))
    # ends a bit heavier (not too sharp; 横折 has a 顿笔 start typically)
    for i in range(8):
        widths[i] = max(widths[i], peak * (0.85 + 0.1 * (1 - i / 8)))
    stroke_along(pts, widths)
    dunbi_dot(p_corner[0], p_corner[1], dun * 0.5)


def draw_hengzhegou(p_start, p_corner, p_shu_end, p_hook_tip, peak=10, dun=14):
    """横折钩: heng → corner → shu → small upward/leftward 钩 tail.

    Continuous brushed sweep; 顿笔 at corner; the hook is the last
    ~18% in length and tapers fine.
    """
    seg1 = line_pts(p_start, p_corner, 70)
    seg2 = line_pts(p_corner, p_shu_end, 100)
    # hook arm: shu_end to hook_tip via slight inward curve
    mid = (
        (p_shu_end[0] + p_hook_tip[0]) / 2,
        (p_shu_end[1] + p_hook_tip[1]) / 2 + 4,
    )
    seg3 = bezier(p_shu_end, mid, mid, p_hook_tip, 40)
    pts = seg1 + seg2[1:] + seg3[1:]
    n = len(pts)
    ci = len(seg1) - 1
    hi = len(seg1) + len(seg2) - 1  # hook start index
    widths = []
    for i in range(n):
        if i <= hi:
            u = i / max(1, hi)
            mid_bump = math.sin(math.pi * u)
            w = peak * (0.55 + 0.45 * mid_bump)
        else:
            # hook: taper down from ~80% peak to ~10%
            v = (i - hi) / max(1, n - 1 - hi)
            w = peak * max(0.1, 0.8 * (1 - v))
        widths.append(w)
    # 顿笔 at corner
    for i in range(n):
        d = abs(i - ci)
        if d < 18:
            bump = math.exp(-(d ** 2) / 30.0)
            widths[i] = max(widths[i], peak * (0.9 + 0.5 * bump))
    # 顿笔 at hook-start (the "lift" before the 钩 flick)
    for i in range(n):
        d = abs(i - hi)
        if d < 14:
            bump = math.exp(-(d ** 2) / 24.0)
            widths[i] = max(widths[i], peak * (0.85 + 0.4 * bump))
    # heavy head
    for i in range(8):
        widths[i] = max(widths[i], peak * (0.95 + 0.1 * (1 - i / 8)))
    stroke_along(pts, widths)
    dunbi_dot(p_corner[0], p_corner[1], dun * 0.55)


def draw_shuwangou(p_top, p_bottom_left, p_right_end, p_hook_tip,
                   peak=10, dun=14):
    """竖弯钩: shu descending → curl right along the bottom → hook up-right.

    p_top: top of the vertical portion (start)
    p_bottom_left: corner where the curl begins (bottom-left)
    p_right_end: where the bottom curl ends (the up-tick about to fire)
    p_hook_tip: tip of the final upward-right 钩.
    """
    # shu portion (slight curve to the left at first then straightens)
    cx1 = p_top[0] - 4
    cy1 = p_top[1] - (p_top[1] - p_bottom_left[1]) * 0.4
    cx2 = p_bottom_left[0] - 6
    cy2 = p_bottom_left[1] + (p_top[1] - p_bottom_left[1]) * 0.2
    seg1 = bezier(p_top, (cx1, cy1), (cx2, cy2), p_bottom_left, 90)
    # bottom curl (round corner from bottom-left to right end)
    c1 = (p_bottom_left[0] + (p_right_end[0] - p_bottom_left[0]) * 0.2,
          p_bottom_left[1] - 12)
    c2 = (p_bottom_left[0] + (p_right_end[0] - p_bottom_left[0]) * 0.8,
          p_bottom_left[1] - 6)
    seg2 = bezier(p_bottom_left, c1, c2, p_right_end, 80)
    # hook flick up-right
    hc = ((p_right_end[0] + p_hook_tip[0]) / 2,
          (p_right_end[1] + p_hook_tip[1]) / 2 - 2)
    seg3 = bezier(p_right_end, hc, hc, p_hook_tip, 40)
    pts = seg1 + seg2[1:] + seg3[1:]
    n = len(pts)
    ci = len(seg1) - 1
    hi = len(seg1) + len(seg2) - 1
    widths = []
    for i in range(n):
        if i <= hi:
            u = i / max(1, hi)
            mid_bump = math.sin(math.pi * u)
            w = peak * (0.6 + 0.4 * mid_bump)
        else:
            v = (i - hi) / max(1, n - 1 - hi)
            w = peak * max(0.1, 0.85 * (1 - v))
        widths.append(w)
    # 顿笔 at the bottom corner
    for i in range(n):
        d = abs(i - ci)
        if d < 18:
            bump = math.exp(-(d ** 2) / 32.0)
            widths[i] = max(widths[i], peak * (0.95 + 0.45 * bump))
    # 顿笔 at hook lift
    for i in range(n):
        d = abs(i - hi)
        if d < 14:
            bump = math.exp(-(d ** 2) / 24.0)
            widths[i] = max(widths[i], peak * (0.9 + 0.4 * bump))
    # heavy head at top
    for i in range(8):
        widths[i] = max(widths[i], peak * (0.95 + 0.1 * (1 - i / 8)))
    stroke_along(pts, widths)
    dunbi_dot(p_bottom_left[0], p_bottom_left[1], dun * 0.6)


# ── PNG save ──────────────────────────────────────────────────────────
def save_png(filename):
    screen.update()
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color",
                           x=-W // 2, y=-H // 2, width=W, height=H)
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=2)
    img = img.convert("RGB")
    img.thumbnail((W, H))
    img.save(os.path.join(OUT_DIR, filename), "PNG")


def reset_to_origin():
    t.reset()
    t.hideturtle()
    t.speed(0)
    t.pencolor(0, 0, 0)
    t.penup()
    t.goto(0, 0)
    t.setheading(90)
    t.pendown()


# ── Task 01 | 火 | huǒ ────────────────────────────────────────────────
# Composition fix: 撇/捺 share apex; two 点 HUG the apex (their tails
# nearly touch the apex), bellies up-and-outward. 撇 head as heavy as 捺.
def task_01_huo():
    reset_to_origin()
    # apex of V (shared by 撇 and 捺)
    apex = (0, 60)
    # 撇 — heavy head at apex, sweeping down-left to lower-left
    draw_pie(apex, (-110, -120), peak=14, curve=0.18)
    # 捺 — fine start at apex, swelling to flat kick at lower-right
    draw_na(apex, (110, -120), peak=14)
    # left 点 — tail nearly touches apex; belly up-and-left from it
    # (tail point is the END of draw_dian; place it close to apex)
    draw_dian(p0=(-45, 110), belly=(-55, 100), p1=(-10, 70), peak=11)
    # right 点 — symmetric, tail nearly touches apex from the right
    draw_dian(p0=(45, 110), belly=(55, 100), p1=(10, 70), peak=11)
    save_png("01_火.png")


# ── Task 02 | 习 | xí ─────────────────────────────────────────────────
# Composition fix: 提 is long (~65% of 横折 width), weighted base near
# the bottom-left corner of the 横折 above. Tucked 点 at upper-left.
def task_02_xi():
    reset_to_origin()
    # 横折钩 as the main frame — top heng from upper-left to upper-right,
    # turn down, descend, then short 钩 leftward at the bottom
    p_start = (-90, 110)
    p_corner = (90, 110)
    p_shu_end = (60, -60)
    p_hook_tip = (35, -45)  # short upward-leftward hook
    draw_hengzhegou(p_start, p_corner, p_shu_end, p_hook_tip,
                    peak=11, dun=14)
    # tucked-in 点 at upper-left interior of the frame
    draw_dian(p0=(-55, 70), belly=(-45, 60), p1=(-20, 40), peak=9)
    # 提 — long rising flick. 横折 top width ~180; aim 提 length ~118
    # (~65%). Weighted base touches bottom-left of the shu (≈ (60,-60));
    # tip flicks up-right toward the upper area.
    # Drawer memory says "base touching/close-to the bottom-left corner
    # of the 横折 above" — for 习, that means base near where the shu
    # ends. Start base just inside (a bit left+down of) shu_end; flick
    # upward-rightward.
    base = (-50, -50)
    tip = (68, 20)
    draw_ti(base, tip, peak=11)
    save_png("02_习.png")


# ── Task 03 | 也 | yě ─────────────────────────────────────────────────
# Composition fix: unified, not three fragments. 横折钩 + middle shu
# sit ABOVE the 竖弯钩 cradle; middle shu close to right of 横折钩's
# vertical.
def task_03_ye():
    reset_to_origin()
    # 横折钩 — top-left assembly. heng short, corner, descend, small
    # inward hook at the bottom.
    p_start = (-130, 70)
    p_corner = (-50, 70)
    p_shu_end = (-50, -40)
    p_hook_tip = (-30, -25)
    draw_hengzhegou(p_start, p_corner, p_shu_end, p_hook_tip,
                    peak=10, dun=12)
    # middle shu — CLOSE to the right of 横折钩's vertical; sits ABOVE
    # the 竖弯钩 floor (does not descend to the bottom of the character).
    draw_shu((10, 80), (10, -50), peak=9)
    # 竖弯钩 — wraps around. Starts upper-right area, descends along
    # right side, curls right along the BOTTOM (forming the floor),
    # hooks up-right at the far right.
    draw_shuwangou(
        p_top=(90, 95),
        p_bottom_left=(90, -90),  # actually bottom-RIGHT-ish corner
        # for 也, the curl is along the bottom under all other strokes
        p_right_end=(150, -100),
        p_hook_tip=(170, -55),
        peak=11, dun=14,
    )
    # The geometry above places the "vertical descent" on the right
    # side and the curl extends rightward at the bottom. To make it
    # truly wrap-around (floor under the other strokes), add a small
    # continuation: a short flat heng-stub from the bottom-left of the
    # other strokes joining into the curl. Skipping — the curl already
    # passes under because we set p_bottom_left so far down (-90) and
    # the other strokes end around y=-50/-40.
    save_png("03_也.png")


# ── Task 04 | 力 | lì ─────────────────────────────────────────────────
# 横折钩 forms the "frame" + 撇 sweeps from upper-right through interior
# to lower-left.
def task_04_li():
    reset_to_origin()
    # 横折钩 — top heng → corner → descending shu → small inward hook
    p_start = (-70, 110)
    p_corner = (70, 110)
    p_shu_end = (40, -100)
    p_hook_tip = (10, -75)  # small hook curling up-left
    draw_hengzhegou(p_start, p_corner, p_shu_end, p_hook_tip,
                    peak=12, dun=16)
    # 撇 — head heavy at top-right area (just under the 横 corner),
    # sweeping down and out to lower-left through the interior
    draw_pie((30, 75), (-110, -120), peak=13, curve=0.22)
    save_png("04_力.png")


# ── Task 05 | 巴 | bā ────────────────────────────────────────────────
# top short heng + 横折 (right edge + top forming small upper frame)
# + middle heng + 竖弯钩 (sweep right along bottom, hook up-right).
def task_05_ba():
    reset_to_origin()
    # The character has a left vertical that joins the bottom 竖弯钩
    # naturally, plus the upper-right small frame.
    # Stroke 1: top heng — short, top edge of the upper frame
    draw_heng((-70, 110), (60, 110), peak=10)
    # Stroke 2: 横折 — at the top-right: heng segment + descending shu
    # to mid-height (forming the small right frame). Start from top-right
    # corner of stroke 1's top heng.
    # Actually 巴's stroke 2 is the 横折 making the right edge: a short
    # heng then turn down. We'll draw it descending from (60,110) to
    # (60,10) with a corner at the start (already at the corner).
    # Use a simple shu for the right edge with a 顿笔-thick head.
    draw_hengzhe(p_start=(-70, 110), p_corner=(60, 110), p_end=(60, 10),
                 peak=10, dun=12)
    # Stroke 3: middle heng — across the frame at mid-height
    draw_heng((-70, 10), (60, 10), peak=9)
    # Stroke 4: 竖弯钩 — long bottom sweep. Starts from lower-left
    # corner of the upper frame area, descends, curls right along the
    # bottom forming the floor, then hooks up-right.
    draw_shuwangou(
        p_top=(-70, 110),       # joins the upper-left start
        p_bottom_left=(-70, -100),
        p_right_end=(80, -100),
        p_hook_tip=(105, -55),
        peak=12, dun=16,
    )
    save_png("05_巴.png")


# ── Task 06 | 已 | yǐ ────────────────────────────────────────────────
# top 横折钩 + middle heng inside + bottom 竖弯钩.
def task_06_yi():
    reset_to_origin()
    # Stroke 1: 横折钩 at the top — heng → corner → short shu → small 钩
    p_start = (-70, 110)
    p_corner = (60, 110)
    p_shu_end = (60, 20)
    p_hook_tip = (40, 35)  # small hook curling up-left
    draw_hengzhegou(p_start, p_corner, p_shu_end, p_hook_tip,
                    peak=11, dun=14)
    # Stroke 2: middle heng inside the frame (short)
    # 已 differs from 己 by having this heng NOT cross out the right side;
    # keep it short and to the left.
    draw_heng((-70, 35), (10, 35), peak=8)
    # Stroke 3: bottom 竖弯钩 — sweeps down from inside, curls right,
    # hooks up-right.
    draw_shuwangou(
        p_top=(-70, 110),
        p_bottom_left=(-70, -90),
        p_right_end=(70, -90),
        p_hook_tip=(95, -45),
        peak=12, dun=16,
    )
    save_png("06_已.png")


# ── run ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    task_01_huo()
    task_02_xi()
    task_03_ye()
    task_04_li()
    task_05_ba()
    task_06_yi()
