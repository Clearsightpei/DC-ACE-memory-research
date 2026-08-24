"""Render 了 (le) at 300x300, black on white. Retry #1.

Errata fix: 了 = 2 strokes only.
  1. 横撇 top: horizontal bar with a small down-flick 撇 at the right end.
  2. 竖钩 body: straight 竖 dropping from around the shoulder, terminal
     hook flicks up-and-left.

Prior attempt defects (retry_0):
  - Body was over-curved (bowed right then back left) instead of a
    mostly-straight 竖钩.
  - Strokes were too thin; GT reads as thick calligraphic ink.
  - Top bar tilted noticeably; GT is nearly flat.

Retry plan:
  - Thicker brush (r ~ 8 -> 7) matching GT ink weight.
  - Top 横 nearly flat (~y=95), spanning x=60..220.
  - Shoulder + 撇 flick down to ~(210, 130).
  - 竖钩 body: nearly straight 竖 from ~(175, 105) descending to
    ~(155, 245), then hook up-and-left to ~(105, 220).
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab(cx, cy, r):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")


def stroke(points, r_start, r_end, step=0.8):
    """Brush-dab along polyline points, tapering radius start->end."""
    seglens = []
    total = 0.0
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        L = math.hypot(x1 - x0, y1 - y0)
        seglens.append(L)
        total += L
    if total < 1e-6:
        dab(points[0][0], points[0][1], r_start)
        return
    n = max(2, int(total / step) + 1)
    for k in range(n + 1):
        t = k / n
        target = t * total
        acc = 0.0
        seg = 0
        while seg < len(seglens) and acc + seglens[seg] < target:
            acc += seglens[seg]
            seg += 1
        if seg >= len(seglens):
            x, y = points[-1]
        else:
            local = (target - acc) / seglens[seg]
            x0, y0 = points[seg]
            x1, y1 = points[seg + 1]
            x = x0 + local * (x1 - x0)
            y = y0 + local * (y1 - y0)
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def bezier(p0, p1, p2, p3, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u**3 * p0[0] + 3 * u**2 * t * p1[0] + 3 * u * t**2 * p2[0] + t**3 * p3[0]
        y = u**3 * p0[1] + 3 * u**2 * t * p1[1] + 3 * u * t**2 * p2[1] + t**3 * p3[1]
        pts.append((x, y))
    return pts


# ---- Stroke 1: 横撇 top ----
# Nearly-flat 横 with slight rise at the shoulder end (typical 顿笔).
# Wide horizontal spanning most of upper canvas width.
top_h = [
    (60, 100),
    (100, 97),
    (140, 94),
    (180, 92),
    (215, 92),
]
# 顿 at start
dab(60, 100, 9)
stroke(top_h, r_start=8.0, r_end=7.0, step=0.8)
# shoulder press (sharp corner turn)
dab(217, 92, 8.5)

# 撇 flick from shoulder going down-and-slightly-left
pie = bezier(
    (217, 94),
    (216, 108),
    (210, 122),
    (200, 138),
    n=30,
)
stroke(pie, r_start=8.0, r_end=1.8, step=0.8)

# ---- Stroke 2: 竖钩 (mostly-straight 竖 + terminal hook) ----
# Body starts just left of the top shoulder (around x=175, y=110) and
# drops nearly straight down, drifting slightly left. Terminal hook
# flicks up-and-left.
shu_start = (175, 108)
shu_end = (158, 248)

body = bezier(
    shu_start,
    (172, 155),   # gently to the left
    (162, 205),
    shu_end,
    n=80,
)
# 顿 at start
dab(shu_start[0], shu_start[1], 9)
stroke(body, r_start=8.0, r_end=7.0, step=0.8)

# Hook: short flick up and to the left
hook = bezier(
    shu_end,
    (145, 245),
    (125, 235),
    (105, 218),
    n=30,
)
stroke(hook, r_start=7.0, r_end=1.5, step=0.8)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0009_了__retry_1/01_了.png"
)
