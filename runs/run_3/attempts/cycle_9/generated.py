"""Cycle 9 — frame family (口, 日) + 钩 family (子, 习, 也) + 火 apex-share fix.

Continuous brushed sweep (cubic Bézier centerline sampled with per-sample
pensize). Compound strokes are ONE continuous brushed path with a Gaussian
顿笔 bump at each corner. 钩 strokes append a short snappy flick (own taper)
to the main stroke's end — same continuous brush, length ~15% of main.
"""

import io
import math
import os
import turtle

from PIL import Image

# ---------- canvas ----------
SCREEN_W, SCREEN_H = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

screen = turtle.Screen()
screen.setup(SCREEN_W, SCREEN_H)
screen.screensize(SCREEN_W, SCREEN_H)
screen.bgcolor("white")
screen.tracer(0, 0)

t = turtle.Turtle(visible=False)
t.speed(0)
t.color("black")
t.pensize(1)


# ---------- bezier helpers ----------
def _cubic(p0, p1, p2, p3, ts):
    pts = []
    for s in ts:
        u = 1 - s
        x = u * u * u * p0[0] + 3 * u * u * s * p1[0] + 3 * u * s * s * p2[0] + s * s * s * p3[0]
        y = u * u * u * p0[1] + 3 * u * u * s * p1[1] + 3 * u * s * s * p2[1] + s * s * s * p3[1]
        pts.append((x, y))
    return pts


def _gauss_bump(s, mu, sigma, amp):
    return 1.0 + amp * math.exp(-((s - mu) ** 2) / (2 * sigma * sigma))


def _width_profile(s, kind="heng",
                   peak=10.0, middle_floor_ratio=0.55,
                   bumps=()):
    """Width as a function of arc-fraction s in [0,1].

    Middle held >= middle_floor_ratio * peak. Peak <= ~2x middle.
    bumps: list of (mu, sigma, amp) applied multiplicatively for 顿笔 corner thickenings.
    """
    mid = peak * middle_floor_ratio
    if kind == "heng":
        # both ends weighted, light middle dip
        end = peak
        # dip-shaped: heavy at 0 and 1, gentle valley around 0.5
        w = end - (end - mid) * math.sin(math.pi * s)
    elif kind == "shu":
        end = peak
        w = end - (end - mid) * math.sin(math.pi * s)
    elif kind == "pie":
        # heavy head at start, fine point at end
        # cubic decline from peak to ~0
        w = peak * (1 - s) ** 1.4 + 0.3
        w = max(w, 0.4)
    elif kind == "na":
        # thin entry, broaden, flat-kick plateau last 12%
        if s < 0.85:
            w = (mid * 0.55) + (peak - mid * 0.55) * (s / 0.85) ** 1.6
        else:
            w = peak  # plateau
    elif kind == "ti":
        # weighted base at start → fine flick at end
        w = peak * (1 - s) ** 1.5 + 0.3
        w = max(w, 0.4)
    elif kind == "dian":
        # thin entry → rounded belly ~0.55 → tapered tail
        w = peak * (math.sin(math.pi * (s ** 0.85)) ** 1.2) + 0.4
    elif kind == "gou_tail":
        # taper from heavy to a fine point
        w = peak * (1 - s) ** 1.3 + 0.3
    elif kind == "flat_mid":
        # for compound shafts when chained: just middle-floor with a soft swell
        w = mid + (peak - mid) * math.sin(math.pi * s) * 0.7
    else:
        w = mid + (peak - mid) * math.sin(math.pi * s)

    for (mu, sigma, amp) in bumps:
        w *= _gauss_bump(s, mu, sigma, amp)
    return max(0.4, w)


def _brushed_path(segments, kind="heng", peak=10.0,
                  middle_floor_ratio=0.55, bumps=(), samples_per_seg=60):
    """segments: list of (p0,p1,p2,p3) cubic Bézier control points.
    Renders ONE continuous brushed stroke across all segments.
    Per-sample pensize uses arc-fraction across the whole concatenated path.
    """
    # collect points with their global arc fraction
    all_pts = []
    n_segs = len(segments)
    for i, (p0, p1, p2, p3) in enumerate(segments):
        ts = [k / samples_per_seg for k in range(samples_per_seg + 1)]
        pts = _cubic(p0, p1, p2, p3, ts)
        # avoid duplicate endpoints between segments
        if i > 0:
            pts = pts[1:]
        for j, p in enumerate(pts):
            # global s mapped over total samples
            local = (j + (1 if i > 0 else 0)) / (samples_per_seg)
            seg_s = (i + local) / n_segs
            all_pts.append((p, seg_s))

    # draw
    t.penup()
    t.goto(all_pts[0][0])
    t.setheading(0)
    t.pendown()
    for (pt, s) in all_pts:
        w = _width_profile(s, kind=kind, peak=peak,
                           middle_floor_ratio=middle_floor_ratio, bumps=bumps)
        t.pensize(w)
        t.goto(pt)
    t.penup()


# ---------- atomic stroke painters (start, end + shape control) ----------
def stroke_heng(x0, y0, x1, y1, peak=11.0, arc=0.10):
    """Soft weighted entry/end heng; small upward bow."""
    dx = x1 - x0
    dy = y1 - y0
    # control points push up a touch for brushy arc
    nx, ny = -dy, dx
    norm = math.hypot(nx, ny) or 1
    nx, ny = nx / norm, ny / norm
    a = (x0 + dx * 0.33 + nx * arc * 10, y0 + dy * 0.33 + ny * arc * 10)
    b = (x0 + dx * 0.66 + nx * arc * 10, y0 + dy * 0.66 + ny * arc * 10)
    _brushed_path([((x0, y0), a, b, (x1, y1))], kind="heng", peak=peak)


def stroke_shu(x0, y0, x1, y1, peak=11.0):
    a = (x0, y0 + (y1 - y0) * 0.33)
    b = (x0, y0 + (y1 - y0) * 0.66)
    _brushed_path([((x0, y0), a, b, (x1, y1))], kind="shu", peak=peak)


def stroke_pie(x0, y0, x1, y1, peak=12.0, bow=0.18):
    """Heavy head, fine point at end. Slight bow."""
    dx, dy = x1 - x0, y1 - y0
    # bow control: push perpendicular
    nx, ny = -dy, dx
    norm = math.hypot(nx, ny) or 1
    nx, ny = nx / norm, ny / norm
    a = (x0 + dx * 0.33 + nx * bow * 30, y0 + dy * 0.33 + ny * bow * 30)
    b = (x0 + dx * 0.70 + nx * bow * 15, y0 + dy * 0.70 + ny * bow * 15)
    _brushed_path([((x0, y0), a, b, (x1, y1))], kind="pie", peak=peak)


def stroke_na(x0, y0, x1, y1, peak=13.0):
    dx, dy = x1 - x0, y1 - y0
    a = (x0 + dx * 0.30, y0 + dy * 0.30)
    b = (x0 + dx * 0.65, y0 + dy * 0.65)
    _brushed_path([((x0, y0), a, b, (x1, y1))], kind="na", peak=peak)


def stroke_ti(x0, y0, x1, y1, peak=10.0):
    dx, dy = x1 - x0, y1 - y0
    a = (x0 + dx * 0.33, y0 + dy * 0.33)
    b = (x0 + dx * 0.66, y0 + dy * 0.66)
    _brushed_path([((x0, y0), a, b, (x1, y1))], kind="ti", peak=peak)


def stroke_dian(x0, y0, x1, y1, peak=9.0):
    dx, dy = x1 - x0, y1 - y0
    # bow outward for a teardrop
    nx, ny = -dy, dx
    norm = math.hypot(nx, ny) or 1
    nx, ny = nx / norm, ny / norm
    a = (x0 + dx * 0.30 + nx * 4, y0 + dy * 0.30 + ny * 4)
    b = (x0 + dx * 0.65 + nx * 2, y0 + dy * 0.65 + ny * 2)
    _brushed_path([((x0, y0), a, b, (x1, y1))], kind="dian", peak=peak)


# ---------- compound stroke painters (continuous brushed sweep) ----------
def compound_hengzhe(x0, y0, corner_x, corner_y, x1, y1, peak=11.0):
    """横折: heng arm to corner, then shu/descending arm. ONE brushed path
    with a corner 顿笔 Gaussian bump."""
    # heng segment
    a1 = (x0 + (corner_x - x0) * 0.33, y0)
    b1 = (x0 + (corner_x - x0) * 0.66, y0)
    seg1 = ((x0, y0), a1, b1, (corner_x, corner_y))
    # shu/descending segment
    a2 = (corner_x, corner_y + (y1 - corner_y) * 0.33)
    b2 = (x1, corner_y + (y1 - corner_y) * 0.66)
    seg2 = ((corner_x, corner_y), a2, b2, (x1, y1))
    # corner sits at mu=0.5 (boundary between two equal segments)
    bumps = [(0.5, 0.05, 0.55)]
    _brushed_path([seg1, seg2], kind="flat_mid", peak=peak,
                  middle_floor_ratio=0.6, bumps=bumps)


def compound_hengpie(x0, y0, corner_x, corner_y, x1, y1, peak=11.0):
    """横撇: short heng top, 90° turn, 撇 tail down-left tapering."""
    a1 = (x0 + (corner_x - x0) * 0.33, y0)
    b1 = (x0 + (corner_x - x0) * 0.66, y0)
    seg1 = ((x0, y0), a1, b1, (corner_x, corner_y))
    # pie segment — bow slightly and taper toward fine end
    dx, dy = x1 - corner_x, y1 - corner_y
    a2 = (corner_x + dx * 0.33 - 6, corner_y + dy * 0.33)
    b2 = (corner_x + dx * 0.66 - 3, corner_y + dy * 0.66)
    seg2 = ((corner_x, corner_y), a2, b2, (x1, y1))
    # corner bump at 0.5, taper second half
    # custom: emulate by chaining via samples — use generic kind but post-process not trivial.
    # Use "flat_mid" with bumps for corner, then a second pass taper-tail on the pie.
    bumps = [(0.5, 0.05, 0.55), (0.95, 0.06, -0.45)]  # negative amp = thin tail
    _brushed_path([seg1, seg2], kind="flat_mid", peak=peak,
                  middle_floor_ratio=0.55, bumps=bumps)


def compound_shugou(x0, y0, x_bot, y_bot, hook_dx=-20, hook_dy=14, peak=11.5):
    """竖钩: shu descending, then small 钩 flick up-and-left.
    ONE continuous brushed sweep, hook tail tapers to fine point.
    """
    a1 = (x0, y0 + (y_bot - y0) * 0.33)
    b1 = (x0, y0 + (y_bot - y0) * 0.66)
    seg1 = ((x0, y0), a1, b1, (x_bot, y_bot))
    # hook: small curve from (x_bot,y_bot) ending up-and-left
    end_hook = (x_bot + hook_dx, y_bot + hook_dy)
    # control points curve out then up
    a2 = (x_bot - 3, y_bot - 2)
    b2 = (x_bot + hook_dx * 0.7, y_bot + hook_dy * 0.4)
    seg2 = ((x_bot, y_bot), a2, b2, end_hook)
    # corner 顿笔 at junction (s=0.5), and taper on hook tail
    bumps = [(0.5, 0.05, 0.55), (0.95, 0.06, -0.55)]
    _brushed_path([seg1, seg2], kind="flat_mid", peak=peak,
                  middle_floor_ratio=0.6, bumps=bumps)


def compound_hengzhegou(x0, y0, corner_x, corner_y, x_bot, y_bot,
                        hook_dx=-14, hook_dy=10, peak=11.0):
    """横折钩: heng → corner → short shu → small 钩 flick up-and-left.
    Three segments, one brushed sweep.
    """
    # heng
    a1 = (x0 + (corner_x - x0) * 0.33, y0)
    b1 = (x0 + (corner_x - x0) * 0.66, y0)
    seg1 = ((x0, y0), a1, b1, (corner_x, corner_y))
    # shu
    a2 = (corner_x, corner_y + (y_bot - corner_y) * 0.33)
    b2 = (x_bot, corner_y + (y_bot - corner_y) * 0.66)
    seg2 = ((corner_x, corner_y), a2, b2, (x_bot, y_bot))
    # hook
    end_hook = (x_bot + hook_dx, y_bot + hook_dy)
    a3 = (x_bot - 2, y_bot - 2)
    b3 = (x_bot + hook_dx * 0.6, y_bot + hook_dy * 0.5)
    seg3 = ((x_bot, y_bot), a3, b3, end_hook)
    # corners at boundaries: 1/3 and 2/3 of total path
    bumps = [(0.333, 0.045, 0.55), (0.667, 0.045, 0.45), (0.97, 0.05, -0.5)]
    _brushed_path([seg1, seg2, seg3], kind="flat_mid", peak=peak,
                  middle_floor_ratio=0.6, bumps=bumps)


def compound_shuwangou(x0, y0, x_curl, y_bot, x_end, y_endhook, peak=12.0):
    """竖弯钩: shu descending → bottom curl right → final 钩 flick up-right.
    Three segments brushed continuously; final taper.
    """
    # shu segment from (x0,y0) down to (x0,y_bot-30)
    mid_y = y_bot + 60  # transition zone above bottom
    a1 = (x0, y0 + (mid_y - y0) * 0.33)
    b1 = (x0, y0 + (mid_y - y0) * 0.66)
    seg1 = ((x0, y0), a1, b1, (x0, mid_y))
    # curl: from (x0,mid_y) sweeping right and down to (x_curl, y_bot)
    a2 = (x0, y_bot)  # pull down
    b2 = (x0 + (x_curl - x0) * 0.6, y_bot)
    seg2 = ((x0, mid_y), a2, b2, (x_curl, y_bot))
    # hook flick up-right from (x_curl, y_bot) to (x_end, y_endhook)
    a3 = (x_curl + 5, y_bot + 2)
    b3 = (x_curl + (x_end - x_curl) * 0.6, y_bot + (y_endhook - y_bot) * 0.5)
    seg3 = ((x_curl, y_bot), a3, b3, (x_end, y_endhook))
    # corner bumps + tail taper
    bumps = [(0.333, 0.05, 0.45), (0.667, 0.05, 0.50), (0.96, 0.05, -0.55)]
    _brushed_path([seg1, seg2, seg3], kind="flat_mid", peak=peak,
                  middle_floor_ratio=0.6, bumps=bumps)


# ---------- save ----------
def _save_png(path):
    screen.update()
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color",
                           width=SCREEN_W, height=SCREEN_H,
                           pagewidth=SCREEN_W - 1, pageheight=SCREEN_H - 1,
                           x=-SCREEN_W // 2, y=-SCREEN_H // 2)
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=2)
    img = img.convert("RGB")
    img.save(path, "PNG")


def _reset():
    t.reset()
    t.hideturtle()
    t.speed(0)
    t.color("black")
    t.pensize(1)
    t.penup()
    t.goto(0, 0)
    t.setheading(90)


# ── Task 01 | 火 | huǒ
def task_01_huo():
    _reset()
    # Apex shared by 撇 and 捺 at (0, 130). Strokes spread wide and low.
    apex = (0, 130)
    # 1) 撇: from apex down-left, heavy head at apex, fine tail at bottom-left.
    stroke_pie(apex[0], apex[1], -110, -110, peak=12.5, bow=0.20)
    # 2) 捺: from apex down-right, fine entry, heavy plateau tail bottom-right.
    stroke_na(apex[0], apex[1], 110, -110, peak=13.0)
    # 3) Left 点: just upper-left of apex, hugging it.
    stroke_dian(-40, 175, -20, 145, peak=9.0)
    # 4) Right 点: just upper-right of apex.
    stroke_dian(40, 175, 20, 145, peak=9.0)
    _save_png(os.path.join(OUT_DIR, "01_火.png"))


# ── Task 02 | 口 | kǒu
def task_02_kou():
    _reset()
    # Square-ish frame, shorter than 中's.
    L, R = -80, 80
    TOP, BOT = 90, -90
    # 1) left shu (left edge)
    stroke_shu(L, TOP, L, BOT, peak=11.5)
    # 2) 横折 (top + right edge): start top-left → corner top-right → down to bottom-right
    compound_hengzhe(L, TOP, R, TOP, R, BOT, peak=11.5)
    # 3) bottom heng (closes the frame)
    stroke_heng(L, BOT, R, BOT, peak=11.5, arc=0.05)
    _save_png(os.path.join(OUT_DIR, "02_口.png"))


# ── Task 03 | 子 | zǐ
def task_03_zi():
    _reset()
    # 子 family: 横撇 head + 竖钩 long center + middle heng.
    # 1) 横撇: short heng top, then tail down-left.
    #    Top heng small at upper area, then pie tail leftward and downward.
    compound_hengpie(-45, 130, 55, 130, -25, 80, peak=11.0)
    # 2) 竖钩: long vertical from just below the 横撇 down, with bottom hook
    #    flicking up-and-left.
    compound_shugou(15, 95, 15, -120, hook_dx=-25, hook_dy=18, peak=11.5)
    # 3) middle heng across waist
    stroke_heng(-75, 0, 75, 0, peak=11.0, arc=0.08)
    _save_png(os.path.join(OUT_DIR, "03_子.png"))


# ── Task 04 | 习 | xí
def task_04_xi():
    _reset()
    # 习: small top-left 点 + 横折 frame-top + 提 flick under it.
    # 1) 点 small dot at top-left
    stroke_dian(-75, 110, -55, 80, peak=9.0)
    # 2) 横折: heng top, then descending right portion (slight inward slant).
    compound_hengzhe(-50, 90, 70, 90, 50, -40, peak=11.0)
    # 3) 提: rising flick at bottom — weighted base at start (lower-left)
    #    rising up-right.
    stroke_ti(-60, -50, 40, -10, peak=10.0)
    _save_png(os.path.join(OUT_DIR, "04_习.png"))


# ── Task 05 | 也 | yě
def task_05_ye():
    _reset()
    # 也: 横折钩 (top-left L hook), middle shu, 竖弯钩 (signature sweep).
    # 1) 横折钩: heng → corner → short shu → small 钩 up-left at bottom.
    compound_hengzhegou(-100, 80, -10, 80, -10, -30,
                        hook_dx=-15, hook_dy=12, peak=11.0)
    # 2) middle shu (slight separation from first stroke), vertical
    stroke_shu(35, 60, 35, -50, peak=10.5)
    # 3) 竖弯钩: long sweeping signature — start upper area, descend, curl right,
    #    end with up-right hook.
    compound_shuwangou(80, 60,  # start (top of shu portion)
                       110, -90,  # x_curl, y_bot (rightmost-bottom point)
                       130, -55,  # x_end, y_endhook (up-right flick end)
                       peak=12.0)
    _save_png(os.path.join(OUT_DIR, "05_也.png"))


# ── Task 06 | 日 | rì
def task_06_ri():
    _reset()
    # 日: tall narrow rectangle with middle heng. Narrower than 口.
    L, R = -55, 55
    TOP, BOT = 120, -120
    MID = 5
    # 1) left shu
    stroke_shu(L, TOP, L, BOT, peak=11.0)
    # 2) 横折: top edge + right edge
    compound_hengzhe(L, TOP, R, TOP, R, BOT, peak=11.0)
    # 3) middle heng (inside frame, horizontal)
    stroke_heng(L, MID, R, MID, peak=10.5, arc=0.05)
    # 4) bottom heng closing frame
    stroke_heng(L, BOT, R, BOT, peak=11.0, arc=0.05)
    _save_png(os.path.join(OUT_DIR, "06_日.png"))


if __name__ == "__main__":
    task_01_huo()
    task_02_kou()
    task_03_zi()
    task_04_xi()
    task_05_ye()
    task_06_ri()
