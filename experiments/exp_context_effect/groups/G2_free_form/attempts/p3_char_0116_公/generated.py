"""
p3_char_0116_公 — G2 attempt (revision 1)
Decomposition: 公 = 八 (top, wide splay) + 厶 (bottom, small tucked-in)
  Stroke 1: 撇  wider/longer top-left flick
  Stroke 2: 捺  longer top-right diagonal with 顿 near end
  Stroke 3: 撇折 short 撇 into a flat rightward 折
  Stroke 4: 点  small dot closing the 厶 upper right

Revision notes vs first pass:
  - Widen 八 splay: 撇 endpoint further left+down, 捺 endpoint further right+down.
  - Remove heavy 顿-at-start dab that read as a floating dot.
  - Move 厶 lower and smaller so it sits under the 八 apex, not overlapping.
  - Rebalance overall composition — the GT is a wide, short character.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def bezier(p0, p1, p2, n=60):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


def stroke_quad(p0, p1, p2, r_start=5.0, r_end=1.6, press_at=None, press_extra=2.0, n=100):
    pts = bezier(p0, p1, p2, n)
    for i, (x, y) in enumerate(pts):
        t = i / n
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)
    if press_at is not None:
        idx = int(press_at * n)
        x, y = pts[idx]
        r = r_start + (r_end - r_start) * (idx / n) + press_extra
        dab(x, y, r)


def stroke_polyline_pts(pts, r_start=5.0, r_end=1.8):
    total = 0
    seg_lens = []
    for i in range(len(pts) - 1):
        dx = pts[i + 1][0] - pts[i][0]
        dy = pts[i + 1][1] - pts[i][1]
        L = (dx * dx + dy * dy) ** 0.5
        seg_lens.append(L)
        total += L
    if total == 0:
        return
    acc = 0
    step = 1.0
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        L = seg_lens[i]
        if L == 0:
            continue
        n = max(1, int(L / step))
        for k in range(n + 1):
            u = k / n
            x = x0 + (x1 - x0) * u
            y = y0 + (y1 - y0) * u
            t = (acc + u * L) / total
            r = r_start + (r_end - r_start) * t
            dab(x, y, r)
        acc += L


# ---- Stroke 1: 撇 (top-left, long splayed diagonal) ----
# Start near top-center (with clear GAP from 捺 start), sweep down-left.
# Ends at lower-left, roughly x=50, y=210.
stroke_quad(
    p0=(120, 80),
    p1=(95, 140),
    p2=(55, 215),
    r_start=5.0,
    r_end=1.4,
    n=110,
)

# ---- Stroke 2: 捺 (top-right, long diagonal with 顿 near foot) ----
# GAP at top (starts x=145, ~15 px right of 撇 start). Sweeps to lower-right.
# Ends around x=250, y=200. Slight downward curve, then a small 顿 near the end.
stroke_quad(
    p0=(145, 82),
    p1=(200, 130),
    p2=(255, 200),
    r_start=4.5,
    r_end=2.2,
    press_at=0.82,
    press_extra=2.2,
    n=120,
)

# ---- Stroke 3: 撇折 (厶's opening — small 撇 then rightward 折) ----
# 撇 portion: starts inside the 八 (x~130, y~155), sweeps down-left to x~100, y~235
撇_pts = bezier((132, 158), (115, 200), (95, 245), n=70)
stroke_polyline_pts(撇_pts, r_start=4.5, r_end=3.0)
# 顿 at 折 corner (small — not exceed segment radius by too much)
corner = 撇_pts[-1]
dab(corner[0], corner[1], 5.0)
# 折 portion: flat rightward with slight upward finish
折_pts = bezier(corner, (140, 252), (180, 245), n=60)
stroke_polyline_pts(折_pts, r_start=3.8, r_end=2.2)

# ---- Stroke 4: 点 (closing dot, upper-right of 厶) ----
# Small diagonal dot down-left, sits to the right of 撇折's tail end,
# tucked under the 捺 foot.
点_pts = bezier((190, 220), (183, 235), (175, 248), n=25)
stroke_polyline_pts(点_pts, r_start=4.5, r_end=1.8)


img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0116_公/01_公.png"
)
